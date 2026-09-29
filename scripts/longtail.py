# -*- coding: utf-8 -*-
"""長尾決策頁：新手頁、交通頁、A vs B 比較頁。

全部從 gen.py 的 DATA / SEASON 產生，不另外寫內容。由 gen.py main() 呼叫 build()。
每頁都要有足夠的真實資料才產生，避免空殼頁。
"""
import json

DIMS = [
    ("beginner", "新手友善", "why_beginner"),
    ("powder", "粉雪", "why_powder"),
    ("terrain", "進階地形", None),
    ("family", "親子", "why_family"),
    ("budget", "預算可控", "why_budget"),
    ("onsen", "溫泉／度假感", "why_onsen"),
    ("chinese_coach", "中文教練", "why_coach"),
    ("tokyo_access", "東京出發", "why_tokyo"),
    ("cts_access", "直飛北海道", None),
    ("non_skier", "不滑雪的人", None),
]


def beginner_url(rid):
    return "resorts/%s-beginner.html" % rid


def access_url(rid):
    return "resorts/%s-access.html" % rid


def vs_slug(a, b):
    return "%s-vs-%s" % tuple(sorted((a, b)))


def vs_url(a, b):
    return "vs/%s.html" % vs_slug(a, b)


def compare_pairs(DATA):
    pairs = set()
    for rid, r in DATA["resorts"].items():
        for c in r.get("compare_with") or []:
            if c in DATA["resorts"] and c != rid:
                pairs.add(tuple(sorted((rid, c))))
    return sorted(pairs)


def go_link(prefix, r, first=True):
    q2 = "hokkaido" if r["region"] == "hokkaido" else "tokyo_transfer"
    return "%sgo.html?a=%s.%s.skiers.access" % (prefix, "first" if first else "green", q2)


def season_line(SEASON, md, rid, r):
    s = SEASON.get(rid) or {}
    if s.get("open"):
        line = "2026–27 季預定 %s 開季" % md(s["open"])
        if s.get("close"):
            line += "、%s 閉季" % md(s["close"])
        return line + "（官方公布）。"
    return (r.get("season_note") or "") + "（本季開季日待官方公布）"


def faq_ld(pairs):
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }, ensure_ascii=False)


def resort_links(r, prefix, DATA):
    """雪場頁底部的長尾內連。"""
    rid = r["id"]
    bits = [
        '<a class="card-link" href="%s%s">%s 適合新手嗎</a>' % (prefix, beginner_url(rid), r["name"]),
        '<a class="card-link" href="%s%s">%s 怎麼去</a>' % (prefix, access_url(rid), r["name"]),
    ]
    for c in r.get("compare_with") or []:
        o = DATA["resorts"].get(c)
        if o:
            bits.append('<a class="card-link" href="%s%s">%s 還是 %s</a>' % (prefix, vs_url(rid, c), r["name"], o["name"]))
    return '<div class="section"><h2>常見問題</h2><p class="longtail-links">%s</p></div>' % " · ".join(bits)


def beginner_article(DATA, SEASON, hx, md, rid):
    prefix = "../"
    r = DATA["resorts"][rid]
    sc = r["scores"]
    b = sc["beginner"]
    if b >= 5:
        verdict = "很適合。第一次滑雪就去 %s 是穩的選擇。" % r["name"]
    elif b == 4:
        verdict = "適合，但有幾個坑要先知道。"
    elif b == 3:
        verdict = "可以，但不是第一座山的首選；會滑一點再來比較划算。"
    else:
        verdict = "不建議當第一座山。先去新手友善的場，會滑了再來。"
    region = DATA["regions"][r["region"]]
    better = sorted(
        (x for x in region["resortIds"] if x != rid and DATA["resorts"][x]["scores"]["beginner"] > b),
        key=lambda x: -DATA["resorts"][x]["scores"]["beginner"],
    )[:3]
    similar = sorted(
        (x for x in region["resortIds"] if x != rid and DATA["resorts"][x]["scores"]["beginner"] >= 4),
        key=lambda x: -DATA["resorts"][x]["scores"]["beginner"],
    )[:3]
    alt_ids = better or similar
    alt_title = "同區更適合新手的場" if better else "同區也適合新手的場"
    alts = "".join(
        '<li><a href="%s%s">%s</a>：%s</li>'
        % (prefix, beginner_url(x), hx(DATA["resorts"][x]["name"]), hx(DATA["resorts"][x].get("why_beginner") or DATA["resorts"][x]["one_liner"]))
        for x in alt_ids
    )
    pit = "".join("<li>%s</li>" % hx(p) for p in (r.get("pitfalls") or []))
    faq = [
        ("%s 適合新手嗎？" % r["name"], verdict + " " + (r.get("why_beginner") or "")),
        ("%s 有中文教練嗎？" % r["name"], "中文教練：%s。%s" % (r.get("chinese_coach") or "", r.get("chinese_service") or "")),
        ("%s 第一次去要注意什麼？" % r["name"], "；".join(r.get("pitfalls") or [])),
    ]
    html = (
        '<main class="page" id="page">'
        '<div class="crumb"><a href="%sindex.html">轉運站</a> · <a href="%sresorts/%s.html">%s</a> · 新手</div>'
        '<h1 class="page-title">%s 適合新手嗎？</h1>'
        '<div class="verdict"><p><strong>結論　</strong>%s</p><p>%s</p></div>'
        '<div class="grid-5" style="margin-top:14px">'
        '<div class="fact"><dt>新手友善</dt><dd>%s / 5</dd></div>'
        '<div class="fact"><dt>中文教練</dt><dd>%s</dd></div>'
        '<div class="fact"><dt>夜滑</dt><dd>%s</dd></div>'
        '<div class="fact"><dt>不滑雪的人</dt><dd>%s / 5</dd></div>'
        "</div>"
        '<div class="section"><h2>第一次去要知道的坑</h2><ul class="pitfalls">%s</ul></div>'
        '<div class="section"><h2>中文教練與中文服務</h2><p>%s</p><p class="muted">%s</p></div>'
        "%s"
        '<div class="section"><h2>什麼時候去</h2><p>%s</p></div>'
        '<div class="section"><h2>%s</h2><ul class="pitfalls">%s</ul></div>'
        '<p class="cta-row"><a class="btn" href="%s">第一次？30 秒選場</a> '
        '<a class="btn secondary" href="%s%s">%s 怎麼去</a></p>'
        '<p class="muted">完整介紹：<a class="card-link" href="%sresorts/%s.html">%s 適合誰、從台灣怎麼走</a></p>'
        "</main>"
    ) % (
        prefix, prefix, rid, hx(r["name"]),
        hx(r["name"]),
        hx(verdict), hx(r.get("why_beginner") or r["one_liner"]),
        b, hx(r.get("chinese_coach")), hx(r.get("night_ski")), sc.get("non_skier"),
        pit,
        hx(r.get("why_coach") or ""), hx(r.get("chinese_service") or ""),
        ('<div class="section"><h2>一天裡的雪況</h2><p>%s</p></div>' % hx(r["snow_rhythm"])) if r.get("snow_rhythm") else "",
        hx(season_line(SEASON, md, rid, r)),
        alt_title, alts or "<li>同區沒有更新手友善的場。</li>",
        go_link(prefix, r), prefix, access_url(rid), hx(r["name"]),
        prefix, rid, hx(r["name"]),
    )
    return html, faq


def access_article(DATA, SEASON, hx, md, rid):
    prefix = "../"
    r = DATA["resorts"][rid]
    sc = r["scores"]
    routes = "".join(
        '<li><div class="route-from">%s　<span class="route-hours">%s</span></div><div class="muted">%s</div></li>'
        % (hx(rt["from"]), hx(rt["hours"]), hx(rt["steps"]))
        for rt in (r.get("access_routes") or [])
    )
    tk, ct = sc.get("tokyo_access", 0), sc.get("cts_access", 0)
    if r["region"] == "hokkaido":
        summary = "從台灣直飛北海道最順。" + ("從東京再轉過去會多耗一天。" if tk <= 2 else "")
    elif tk >= 5:
        summary = "東京出發最方便的一群，可以當日來回。"
    elif tk >= 3:
        summary = "從東京搭新幹線加接駁，半天內到得了，建議住一晚以上。"
    else:
        summary = "從東京過去要花大半天，適合排整趟行程專程去。"
    b = r.get("budget_twd") or {}
    budget = ""
    if b:
        budget = '<div class="section"><h2>從台灣出發的預算</h2><div class="budget"><span class="budget-num">NT$%s–%s</span><span class="muted">%s，%s</span></div></div>' % (
            "{:,}".format(b["min"]), "{:,}".format(b["max"]), hx(b.get("days", "")), hx(b.get("note", "")))
    acc_links = [l for l in (r.get("links") or []) if l.get("type") == "access"]
    links = ""
    if acc_links:
        links = '<div class="section"><h2>交通攻略延伸閱讀</h2><ul class="link-list" style="list-style:none;margin:0;padding:0">%s</ul></div>' % "".join(
            '<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a><span class="link-source muted">%s</span></li>'
            % (hx(l["url"]), hx(l["title"]), hx(l.get("source"))) for l in acc_links)
    near = [x for x in DATA["regions"][r["region"]]["resortIds"] if x != rid]
    if r.get("cluster"):
        near = [x for x in near if DATA["resorts"][x].get("cluster") == r["cluster"]] or near
    near_html = " · ".join('<a class="card-link" href="%s%s">%s 怎麼去</a>' % (prefix, access_url(x), hx(DATA["resorts"][x]["name"])) for x in near[:5])
    faq = [("%s 怎麼去？" % r["name"], summary + " " + "；".join("%s：%s（%s）" % (rt["from"], rt["steps"], rt["hours"]) for rt in (r.get("access_routes") or [])))]
    if r.get("why_tokyo"):
        faq.append(("從東京去 %s 方便嗎？" % r["name"], r["why_tokyo"]))
    html = (
        '<main class="page" id="page">'
        '<div class="crumb"><a href="%sindex.html">轉運站</a> · <a href="%sresorts/%s.html">%s</a> · 交通</div>'
        '<h1 class="page-title">%s 怎麼去？</h1>'
        '<div class="verdict"><p><strong>結論　</strong>%s</p>%s</div>'
        '<div class="section"><h2>從台灣怎麼到</h2><ul class="route-list">%s</ul></div>'
        "%s"
        '<div class="section"><h2>什麼時候去</h2><p>%s</p></div>'
        "%s"
        '<div class="section"><h2>附近雪場怎麼去</h2><p>%s</p></div>'
        '<p class="cta-row"><a class="btn" href="%s">不確定去哪？30 秒選場</a> '
        '<a class="btn secondary" href="%s%s">%s 適合新手嗎</a></p>'
        '<p class="muted">完整介紹：<a class="card-link" href="%sresorts/%s.html">%s 適合誰、從台灣怎麼走</a></p>'
        "</main>"
    ) % (
        prefix, prefix, rid, hx(r["name"]),
        hx(r["name"]),
        hx(summary), ('<p>%s</p>' % hx(r["why_tokyo"])) if r.get("why_tokyo") else "",
        routes, budget, hx(season_line(SEASON, md, rid, r)), links, near_html,
        go_link(prefix, r), prefix, beginner_url(rid), hx(r["name"]),
        prefix, rid, hx(r["name"]),
    )
    return html, faq


def vs_article(DATA, SEASON, hx, md, a, b):
    prefix = "../"
    A, B = DATA["resorts"][a], DATA["resorts"][b]
    rows = []
    a_wins, b_wins = [], []
    for key, label, why in DIMS:
        x, y = A["scores"].get(key, 0), B["scores"].get(key, 0)
        mark_a = ' class="win"' if x > y else ""
        mark_b = ' class="win"' if y > x else ""
        rows.append('<tr><th scope="row">%s</th><td%s>%s / 5</td><td%s>%s / 5</td></tr>' % (label, mark_a, x, mark_b, y))
        if x - y >= 1:
            a_wins.append((x - y, label, why))
        elif y - x >= 1:
            b_wins.append((y - x, label, why))
    a_wins.sort(key=lambda t: -t[0])
    b_wins.sort(key=lambda t: -t[0])

    def reasons(R, wins):
        out = []
        for _, label, why in wins[:4]:
            txt = R.get(why) if why else ""
            out.append("<li><strong>%s</strong>%s</li>" % (label, ("：" + hx(txt)) if txt else ""))
        return "".join(out) or "<li>各項分數與另一座差不多，看交通與預算決定。</li>"

    def budget(R):
        bb = R.get("budget_twd") or {}
        return "NT$%s–%s" % ("{:,}".format(bb["min"]), "{:,}".format(bb["max"])) if bb else "—"

    def hours(R):
        rt = (R.get("access_routes") or [{}])[0]
        return "%s（%s）" % (rt.get("from", ""), rt.get("hours", "")) if rt else "—"

    top_a = a_wins[0][1] if a_wins else None
    top_b = b_wins[0][1] if b_wins else None
    if top_a and top_b:
        lead = "要%s選 %s；要%s選 %s。" % (top_a, A["name"], top_b, B["name"])
    elif top_a:
        lead = "多數項目 %s 較強，尤其是%s。" % (A["name"], top_a)
    elif top_b:
        lead = "多數項目 %s 較強，尤其是%s。" % (B["name"], top_b)
    else:
        lead = "兩座條件很接近，看交通與預算決定。"
    faq = [("%s 還是 %s？" % (A["name"], B["name"]), lead + " " + A["one_liner"] + " " + B["one_liner"])]
    html = (
        '<main class="page page-wide" id="page">'
        '<div class="crumb"><a href="%sindex.html">轉運站</a> · <a href="%scompare.html">比較</a></div>'
        '<h1 class="page-title">%s 還是 %s？</h1>'
        '<div class="verdict"><p><strong>結論　</strong>%s</p></div>'
        '<div class="vs-grid">'
        '<div class="vs-col"><h2><a href="%sresorts/%s.html">%s</a></h2><p>%s</p><p class="not-for">不適合：%s</p>'
        '<h3>選 %s，如果你在乎</h3><ul class="pitfalls">%s</ul></div>'
        '<div class="vs-col"><h2><a href="%sresorts/%s.html">%s</a></h2><p>%s</p><p class="not-for">不適合：%s</p>'
        '<h3>選 %s，如果你在乎</h3><ul class="pitfalls">%s</ul></div>'
        "</div>"
        '<div class="section"><h2>逐項比較</h2><div class="table-wrap"><table class="compare-table vs-table">'
        "<thead><tr><th></th><th>%s</th><th>%s</th></tr></thead><tbody>%s"
        '<tr><th scope="row">從台灣怎麼到</th><td>%s</td><td>%s</td></tr>'
        '<tr><th scope="row">5 天預算帶</th><td>%s</td><td>%s</td></tr>'
        '<tr><th scope="row">本季</th><td>%s</td><td>%s</td></tr>'
        "</tbody></table></div></div>"
        '<p class="cta-row"><a class="btn" href="%sgo.html">還是不確定？30 秒選場</a></p>'
        "</main>"
    ) % (
        prefix, prefix, hx(A["name"]), hx(B["name"]), hx(lead),
        prefix, a, hx(A["name"]), hx(A["one_liner"]), hx(A["not_for"]), hx(A["name"]), reasons(A, a_wins),
        prefix, b, hx(B["name"]), hx(B["one_liner"]), hx(B["not_for"]), hx(B["name"]), reasons(B, b_wins),
        hx(A["name"]), hx(B["name"]), "".join(rows),
        hx(hours(A)), hx(hours(B)), budget(A), budget(B),
        hx(season_line(SEASON, md, a, A)), hx(season_line(SEASON, md, b, B)),
        prefix,
    )
    return html, faq


def build(DATA, SEASON, page, hx, md, write, ORIGIN):
    """產生全部長尾頁，回傳 sitemap 用的網址清單。"""
    urls = []
    for rid, r in DATA["resorts"].items():
        html, faq = beginner_article(DATA, SEASON, hx, md, rid)
        path = beginner_url(rid)
        write(path, page(
            "%s 適合新手嗎？第一次滑雪要知道的事｜雪國轉運站" % r["name"],
            "%s 適合新手嗎：%s 中文教練、新手坑、同區替代選擇。" % (r["name"], r.get("why_beginner") or r["one_liner"]),
            ORIGIN + "/" + path, 1, "Hub.mountChrome('map');", html, active="map", jsonld=faq_ld(faq),
        ))
        urls.append(ORIGIN + "/" + path)

        html, faq = access_article(DATA, SEASON, hx, md, rid)
        path = access_url(rid)
        first = (r.get("access_routes") or [{}])[0]
        write(path, page(
            "%s 怎麼去？從台灣、東京交通方式與時間｜雪國轉運站" % r["name"],
            "%s 怎麼去：%s %s，%s" % (r["name"], first.get("from", ""), first.get("steps", ""), first.get("hours", "")),
            ORIGIN + "/" + path, 1, "Hub.mountChrome('map');", html, active="map", jsonld=faq_ld(faq),
        ))
        urls.append(ORIGIN + "/" + path)

    for a, b in compare_pairs(DATA):
        html, faq = vs_article(DATA, SEASON, hx, md, a, b)
        A, B = DATA["resorts"][a], DATA["resorts"][b]
        path = vs_url(a, b)
        write(path, page(
            "%s 還是 %s？差在哪、怎麼選｜雪國轉運站" % (A["name"], B["name"]),
            "%s 還是 %s：新手、粉雪、交通、預算逐項比較。%s" % (A["name"], B["name"], faq[0][1][:60]),
            ORIGIN + "/" + path, 1, "Hub.mountChrome('compare');", html, active="compare", jsonld=faq_ld(faq),
        ))
        urls.append(ORIGIN + "/" + path)
    return urls
