# -*- coding: utf-8 -*-
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def jp(slug, quote, original, theme):
    return {
        "quote": quote,
        "original": original,
        "source": "スキー・スノボ研究所",
        "source_kind": "jp_review",
        "url": "https://snow.tabiris.com/%s.html" % slug,
        "date": "2026-02",
        "theme": theme,
    }

def sc(b, p, tk, ct, bu, fa, on, co, ns, te):
    return {
        "beginner": b, "powder": p, "tokyo_access": tk, "cts_access": ct,
        "budget": bu, "family": fa, "onsen": on, "chinese_coach": co,
        "non_skier": ns, "terrain": te,
    }

def L(title, source, url, typ):
    return {"title": title, "source": source, "url": url, "type": typ}

DATA = {
    "origin": "https://japanski.djhousetw.com",
    "dots": {
        "hokkaido": [54.2, 25.3],
        "tohoku": [53.0, 60.2],
        "niigata": [44.9, 69.3],
        "nagano": [40.3, 70.9],
    },
    "cards": {
        "hokkaido": [76, 16],
        "tohoku": [22, 52],
        "niigata": [70, 84],
        "nagano": [22, 90],
    },
    "regions": {
        "hokkaido": {"name": "北海道", "sub": "粉雪 · 7 個雪場", "desc": "全日本粉雪指標，從台灣直飛新千歲最順。", "resortIds": ["niseko", "rusutsu", "furano", "kiroro", "tomamu", "teine", "sahoro"]},
        "tohoku": {"name": "東北", "sub": "樹冰 · 3 個雪場", "desc": "人較少、雪季長，樹冰與度假村型雪場。", "resortIds": ["zao", "appi", "bandai"]},
        "niigata": {"name": "新潟／越後", "sub": "新幹線 · 8 個雪場", "desc": "東京最近的雪國。越後湯澤是樞紐，不是一座場。", "resortIds": ["gala-yuzawa", "ishiuchi", "yuzawa-kogen", "naeba", "kagura", "joetsu-kokusai", "myoko", "maiko"]},
        "nagano": {"name": "長野／北信", "sub": "冬奧 · 6 個雪場", "desc": "白馬谷要先選山。輕井澤歸長野，適合東京當日。", "resortIds": ["happo-one", "tsugaike", "hakuba-goryu", "nozawa", "shiga-kogen", "karuizawa"]},
    },
    "areas": {
        "yuzawa": {
            "id": "yuzawa", "name": "越後湯澤", "romaji": "Echigo-Yuzawa",
            "one_liner": "東京最近的雪國樞紐。先選 GALA、石打或湯澤高原，不要把整區當一座場。",
            "desc": "上越新幹線約 75 分鐘到越後湯澤。GALA 下車即滑；石打規模較大；湯澤高原新手友善。三山有共通券。苗場、神樂、舞子、上越國際也從這站接駁，但不算湯澤三山。",
            "resortIds": ["gala-yuzawa", "ishiuchi", "yuzawa-kogen"],
        },
        "hakuba-valley": {
            "id": "hakuba-valley", "name": "白馬谷", "romaji": "Hakuba Valley",
            "one_liner": "冬奧地形，先選山再選村。新手優先栂池，不要第一天就衝八方。",
            "desc": "白馬谷約 10 座雪場。第一季只做八方尾根、栂池高原、白馬五龍。Hakuba Valley 共通券可跨場，但交通與坡度差很大。",
            "resortIds": ["happo-one", "tsugaike", "hakuba-goryu"],
        },
    },
    "compare": [
        {"title": "北海道三選", "ids": ["niseko", "rusutsu", "furano"]},
        {"title": "東京側短待", "ids": ["gala-yuzawa", "naeba", "karuizawa"]},
        {"title": "長野三選", "ids": ["happo-one", "tsugaike", "nozawa"]},
    ],
    "resorts": {},
}

def add(r):
    DATA["resorts"][r["id"]] = r

add({
    "id": "niseko", "name": "二世谷", "romaji": "Niseko", "prefecture": "北海道 倶知安町／虻田郡",
    "region": "hokkaido", "cluster": "niseko",
    "one_liner": "四大場相連的全球粉雪朝聖區。適合肯花錢、要國際化服務、至少待 4 天的人。",
    "not_for": "只請得到 3 天假、預算緊、或想全程講中文的人——英文比中文好找，旺季住宿會把總額拉爆。",
    "tags": ["粉雪", "國際化服務", "雪場相連"],
    "access_routes": [
        {"from": "桃園 → 新千歲", "steps": "接駁巴士／包車直達二世谷，約 2.5–3 小時", "hours": "含飛行約 7–8 小時"},
        {"from": "已在札幌", "steps": "高速巴士約 2.5–3 小時", "hours": "約 3 小時"},
    ],
    "budget_twd": {"min": 55000, "max": 95000, "days": "5 天 4 夜", "note": "旺季住宿是最大變數，國際定價。"},
    "season_note": "例年 11 月底～5 月初。粉雪最穩多在 1–2 月；3 月後粉雪會變少。",
    "night_ski": "有", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
    "chinese_service": "英文優於中文。國際村氛圍，中文教練有但不是主力。",
    "snow_rhythm": None,
    "pitfalls": ["旺季住宿與餐飲是北海道最貴帶，不要用本州湯澤的預算來估。", "新千歲當日下午才滑得到，行程至少 4 天。", "外國人很多，週末村裡與餐廳要預約。"],
    "companion_note": "Hirafu 村餐廳與酒吧多，不滑雪也能過一天，但消費偏高。",
    "season_delta": "2026–27 二世谷聯合全日票旺季約 ¥13,500，比上一季再漲。以官網為準。",
    "scores": sc(4, 5, 1, 5, 1, 3, 3, 3, 3, 4),
    "why_beginner": "粉雪鬆、綠線夠用，國際化服務讓第一次比較不慌——前提是預算跟得上。",
    "why_powder": "四大場相連，全球粉雪愛好者朝聖地。",
    "why_tokyo": "從東京再轉北海道會多耗一天，這題較不划算。",
    "why_family": "有家庭設施，但比留壽都、Tomamu 更國際、更貴。",
    "why_onsen": "有溫泉與度假氛圍，但真正賣點仍是粉雪。",
    "why_budget": "這不是預算可控首選。",
    "why_coach": "英文教練很好找；中文有，但湯澤、苗場更密。",
    "compare_with": ["rusutsu", "furano", "kiroro"],
    "experts": {
        "consensus": ["四大雪場相連，粉雪與夜生活是北海道旗艦。", "住宿遠近差很大，選邊會決定每天累不累。", "從台灣來至少排 4 天，當日抵達幾乎滑不滿。"],
        "disagreement": "住宿有人堅持住 Hirafu 村裡走去滑，有人叫你住較便宜再接駁。",
        "sources": [
            {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/niseko-hotel-guide/", "kind": "blogger"},
            {"name": "Mimi韓の旅遊指南", "url": "https://mimigo.tw/hokkaido-ski-hotel-guide/", "kind": "blogger"},
            {"name": "雪豹的白色里數", "url": "https://whitemileage.com/hokkaido-ski-in-ski-out-guide/", "kind": "blogger"},
        ],
    },
    "community": [
        jp("nisekohirafu", "日本最高等級的雪場之一，但外國人非常多，氛圍不太像在日本。", "間違いなく日本最高のスキー場。外国人がとてもとても多い。", "snow"),
        jp("nisekohirafu", "外國人變多之後，雪場餐也變貴了。", "外国人が増えてからゲレ食が高くなった。", "pitfall"),
        jp("nisekohirafu", "從本州來，當天幾乎滑不滿，行程要排長一點。", "6時台に羽田を発つ飛行機に乗っても、滑れるのは午後から。", "beginner"),
    ],
    "links": [
        L("18間人氣飯店＆民宿實住心得", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/niseko-hotel-guide/", "hotel"),
        L("20間飯店真實評比：二世谷、留壽都、富良野還是星野度假村？", "Mimi韓の旅遊指南", "https://mimigo.tw/hokkaido-ski-hotel-guide/", "hotel"),
        L("北海道雪場 Ski In/Out 住宿大集合", "雪豹的白色里數", "https://whitemileage.com/hokkaido-ski-in-ski-out-guide/", "hotel"),
        L("日本滑雪要花多少錢？", "The Japow Project", "https://japowproject.com/zh-tw/guides/japan-ski-trip-cost", "overview"),
    ],
})

add({
    "id": "rusutsu", "name": "留壽都", "romaji": "Rusutsu", "prefecture": "北海道 虻田郡留壽都村",
    "region": "hokkaido", "cluster": None,
    "one_liner": "北海道最大單一雪場，度假村自帶室內遊樂。第一次去北海道、帶小孩的首選之一。",
    "not_for": "只想住在有熱鬧村子裡的人——這裡是封閉型度假村，晚上選擇比二世谷少。",
    "tags": ["親子友善", "室內樂園", "Ski-in/out"],
    "access_routes": [
        {"from": "桃園 → 新千歲", "steps": "度假村接駁／巴士約 1.5–2 小時", "hours": "含飛行約 6.5–7.5 小時"},
    ],
    "budget_twd": {"min": 45000, "max": 78000, "days": "5 天 4 夜", "note": "住度假村內較省腦，但餐飲選擇集中。"},
    "season_note": "例年 12 月～4 月。標高較低，12 月初與 3 月下旬雪質要打折。",
    "night_ski": "有", "onsen": "有", "chinese_coach": "多", "ski_in_out": "常見",
    "chinese_service": "有中文教練（如 Jstyle）。度假村內英文／中文都比本州鄉鎮場好辦事。",
    "snow_rhythm": None,
    "pitfalls": ["標高不高，季初季末雪量不穩。", "早餐自助常排隊。", "想逛村子、找獨立餐廳，會覺得悶。"],
    "companion_note": "室內遊樂、造波池、遊戲區，不滑雪的大人與小孩都能耗掉一天。",
    "season_delta": "2025 年第六度拿下 World Ski Awards Japan’s Best Ski Resort。纜車線上買通常比現場便宜。",
    "scores": sc(5, 5, 1, 5, 2, 5, 4, 4, 5, 3),
    "why_beginner": "綠線長、度假村一條龍，第一次去北海道最省腦。",
    "why_powder": "粉雪不輸二世谷，人潮通常比較少。",
    "why_tokyo": "要先飛北海道，不適合已在東京短待。",
    "why_family": "室內樂園加 Ski-in/out，帶小孩幾乎是標準答案。",
    "why_onsen": "度假村有溫泉與室內設施，滑完不用再找村子。",
    "why_budget": "比二世谷便宜一截，但仍是北海道度假村價。",
    "why_coach": "官方合作中文學校有駐點，比很多本州場好約。",
    "compare_with": ["niseko", "tomamu", "furano"],
    "experts": {
        "consensus": ["三座山、37 條道，單一場規模是北海道最大。", "粉雪與二世谷同級，人比較少。", "親子與第一次北海道很適合，因為設施都在度假村裡。"],
        "disagreement": None,
        "sources": [
            {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/rusutsu-ski-resort-review/", "kind": "blogger"},
            {"name": "Mimi韓の旅遊指南", "url": "https://mimigo.tw/hokkaido-ski-hotel-guide/", "kind": "blogger"},
        ],
    },
    "community": [
        jp("rusutsu", "第一次去北海道，很多人會說「猶豫就來這裡」。", "初めての北海道ならおすすめできる。「迷ったらココ」的な平均点の高いスキーリゾート。", "beginner"),
        jp("rusutsu", "雪質和二世谷差不多，但 12 月上旬與 3 月下旬要小心。", "雪質はニセコと変わらない。12月上旬と3月下旬に行くときは注意。", "snow"),
        jp("rusutsu", "室內遊樂很滿，滑完也不會無聊。", "室内遊園地やゲームセンターがとても充実していて、アフターも飽きない。", "pitfall"),
    ],
    "links": [
        L("留壽都滑雪場詳細攻略，住宿交通美食介紹", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/rusutsu-ski-resort-review/", "overview"),
        L("留壽都渡假村房間開箱＆心得、溫泉介紹", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/rusutsu-resort-hote/", "hotel"),
        L("留壽都滑雪場攻略：雪場特色、票價、交通、住宿", "Klook客路部落格", "https://www.klook.com/zh-TW/blog/rusutsu-ski-resort/", "overview"),
    ],
})

add({
    "id": "furano", "name": "富良野", "romaji": "Furano", "prefecture": "北海道 富良野市",
    "region": "hokkaido", "cluster": None,
    "one_liner": "乾粉雪、人比二世谷少。中級者會覺得地形比較過癮，親子也能滑。",
    "not_for": "想要熱鬧夜生活、或單板公園為主的人——這裡偏競技場性格，公園選擇少。",
    "tags": ["粉雪", "較少觀光客", "適合進階"],
    "access_routes": [
        {"from": "桃園 → 旭川", "steps": "巴士約 1 小時到富良野", "hours": "含飛行約 6–7 小時"},
        {"from": "桃園 → 新千歲", "steps": "巴士／鐵路轉乘較長，約 3–4 小時", "hours": "含飛行約 8–9 小時"},
    ],
    "budget_twd": {"min": 40000, "max": 68000, "days": "5 天 4 夜", "note": "北之峰民宿帶比王子飯店便宜許多。"},
    "season_note": "例年 12 月～4 月初。旭川航線班次少、票價常比新千歲高。",
    "night_ski": "有", "onsen": "少", "chinese_coach": "有", "ski_in_out": "部分",
    "chinese_service": "比二世谷日文，比東北好一點。王子飯店體系相對好溝通。",
    "snow_rhythm": None,
    "pitfalls": ["誤買新千歲出發的套票會變得很遠。", "富良野區與北之峰幾乎是兩座場，選錯住宿會天天接駁。", "單板公園少。"],
    "companion_note": "小鎮與薰衣草田是夏天印象；冬天不滑雪能逛的比留壽都少，但比純雪場好。",
    "season_delta": None,
    "scores": sc(4, 5, 1, 4, 3, 4, 2, 3, 3, 3),
    "why_beginner": "綠線夠，人少比較不怕撞；第一次也能滑，但度假感不如留壽都。",
    "why_powder": "乾粉雪穩定，人比二世谷少。",
    "why_tokyo": "要飛北海道。",
    "why_family": "緩坡與空間足夠，人少對小孩友善。",
    "why_onsen": "不是溫泉場。",
    "why_budget": "北海道裡相對好控，尤其住北之峰。",
    "why_coach": "有中文課，密度不如湯澤。",
    "compare_with": ["niseko", "rusutsu", "kiroro"],
    "experts": {
        "consensus": ["人少、雪乾，中級者常覺得比二世谷好滑。", "兩區相對獨立，住宿要選對邊。", "走旭川機場比新千歲順。"],
        "disagreement": None,
        "sources": [
            {"name": "Mimi韓の旅遊指南", "url": "https://mimigo.tw/hokkaido-ski-hotel-guide/", "kind": "blogger"},
            {"name": "雪豹的白色里數", "url": "https://whitemileage.com/hokkaido-ski-in-ski-out-guide/", "kind": "blogger"},
        ],
    },
    "community": [
        jp("furano", "比二世谷空、比 Kiroro 好玩，中級者很吃香。", "ニセコより全然空いているし、キロロよりコースが楽しい。", "snow"),
        jp("furano", "場大、人少，可以不太看旁邊地滑。", "スキー場が大きい。空いていて、周囲を気にせず滑れる。", "beginner"),
        jp("furano", "單板公園少，單板客比例也低。", "スノーボーダーが少ない。ボードパークが少ない。", "pitfall"),
    ],
    "links": [
        L("20間飯店真實評比（同篇涵蓋富良野）", "Mimi韓の旅遊指南", "https://mimigo.tw/hokkaido-ski-hotel-guide/", "hotel"),
        L("Ski In/Out 住宿大集合（含富良野）", "雪豹的白色里數", "https://whitemileage.com/hokkaido-ski-in-ski-out-guide/", "hotel"),
    ],
})

# Remaining resorts continue in the same file...
# Write the rest as a second dict merge below.

def bulk():
    rows = []

    rows.append({
        "id": "kiroro", "name": "Kiroro", "romaji": "Kiroro", "prefecture": "北海道 余市郡赤井川村",
        "region": "hokkaido", "cluster": None,
        "one_liner": "北海道積雪量指標。雪季長、粉雪穩，Club Med 全包也很常被台灣團選。",
        "not_for": "在乎晴天率、或想逛有村子的人——這裡常吹雪，度假村相對封閉。",
        "tags": ["粉雪", "雪季長", "親子友善"],
        "access_routes": [{"from": "桃園 → 新千歲", "steps": "巴士經小樽／札幌，約 2–2.5 小時", "hours": "含飛行約 7–8 小時"}],
        "budget_twd": {"min": 45000, "max": 88000, "days": "5 天 4 夜", "note": "Club Med 全包會把總額拉到上緣。"},
        "season_note": "例年 11 月～5 月。季初季末雪量是北海道最強帶之一。",
        "night_ski": "有", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "Club Med 中文服務較完整；自己滑則日英為主。",
        "snow_rhythm": None,
        "pitfalls": ["積雪多但天氣差，常吹雪。", "春天場太空，部分設施會休息。", "從札幌／小樽還要再轉，不是下車即滑。"],
        "companion_note": "Club Med 全包對不滑雪的人最友善；自己住的話晚上選擇有限。",
        "season_delta": None,
        "scores": sc(4, 5, 1, 4, 2, 4, 4, 3, 4, 3),
        "why_beginner": "綠線夠、雪鬆好摔，第一次可以，但交通與天氣要有心理準備。",
        "why_powder": "積雪量北海道前段班，粉雪穩定。",
        "why_tokyo": "要飛北海道。",
        "why_family": "Club Med 全包對親子很省事。",
        "why_onsen": "度假村型，溫泉與全包活動都有。",
        "why_budget": "自己滑中等；走 Club Med 就不算省。",
        "why_coach": "Club Med 含課；自由行中文課有但不如湯澤密。",
        "compare_with": ["niseko", "rusutsu", "tomamu"],
        "experts": {
            "consensus": ["積雪量是賣點，季初季末仍能滑。", "Club Med 接手後，台灣團明顯變多。", "天氣差是代價，吹雪頻率高。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/kiroro-ski/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-ski-beginner/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("kiroro", "積雪量沒話講，幾乎不會遇到沒雪。", "積雪量には文句の付けようがない。雪不足とは無縁。", "snow"),
            jp("kiroro", "雪多，天氣也差，常常在吹雪。", "雪は多いが、そのぶん天気も悪い。しょっちゅう吹雪く。", "pitfall"),
            jp("kiroro", "11 月到 5 月，雪質大致都能接受。", "11月から5月まで、雪質には大きな不満なく滑れる。", "beginner"),
        ],
        "links": [L("北海道 Kiroro 滑雪渡假村攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/kiroro-ski/", "overview")],
    })

    rows.append({
        "id": "tomamu", "name": "Tomamu", "romaji": "Hoshino Tomamu", "prefecture": "北海道 勇払郡占冠村",
        "region": "hokkaido", "cluster": None,
        "one_liner": "星野體系的封閉度假村。新手、親子、不滑雪的人都能過；真正衝地形的人會覺得場普通。",
        "not_for": "中級想找多樣地形、或討厭山麓平到單板推不動的人。",
        "tags": ["親子友善", "度假村", "Ski-in/out"],
        "access_routes": [{"from": "桃園 → 新千歲", "steps": "滑雪巴士約 2 小時，或 JR 到 Tomamu 站", "hours": "含飛行約 7 小時"}],
        "budget_twd": {"min": 45000, "max": 82000, "days": "5 天 4 夜", "note": "星野定價，冰雪村與餐飲另計。"},
        "season_note": "2026/27 例年 12/1–4/5。內陸極冷，有時到零下 30 度。",
        "night_ski": "無", "onsen": "有", "chinese_coach": "多", "ski_in_out": "常見",
        "chinese_service": "星野體系標示清楚，中文教練有駐點。",
        "snow_rhythm": None,
        "pitfalls": ["山麓緩坡又長又平，單板新手推雪會崩潰。", "極冷，裝備不夠會滑不下去。", "週末高速纜車會排。"],
        "companion_note": "冰雪村、餐廳街、溫泉，不滑雪也能排滿。這是它存在的理由。",
        "season_delta": None,
        "scores": sc(5, 4, 1, 5, 2, 5, 4, 4, 5, 3),
        "why_beginner": "新手道多、度假村一條龍，第一次很適合。",
        "why_powder": "內陸粉雪夠用，但場的個性是度假不是衝地形。",
        "why_tokyo": "要飛北海道。",
        "why_family": "不滑雪的家人有冰雪村，這點很少場比得上。",
        "why_onsen": "星野度假感，溫泉與活動都在園區。",
        "why_budget": "星野價，不是省錢首選。",
        "why_coach": "有官方合作中文學校。",
        "compare_with": ["rusutsu", "niseko", "sahoro"],
        "experts": {
            "consensus": ["新千歲相對好到，北海道度假村裡交通友善。", "新手與親子很適合，中級地形普通。", "不滑雪的人比很多雪場好打發。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/tomamu-ski-resort/", "kind": "blogger"},
                {"name": "Mimi韓の旅遊指南", "url": "https://mimigo.tw/hokkaido-ski-hotel-guide/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("tomamu", "晴天率高、風停纜車少，穩是它的優點。", "シーズンの晴天率が高く、70%もある。風雪でリフトが止まることがほとんどない。", "snow"),
            jp("tomamu", "山麓平到單板是地獄，中級道偏少。", "山麓の緩斜面が平らすぎで、しかも長い。ボーダーには地獄。", "beginner"),
            jp("tomamu", "度假村很壯觀，雪場本身普通。", "リゾートは壮大、ゲレンデは今ひとつ。", "pitfall"),
        ],
        "links": [
            L("Tomamu 星野渡假村滑雪場攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/tomamu-ski-resort/", "overview"),
            L("13 間餐廳、下午茶、酒吧總整理", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/tomamu-restaurent/", "overview"),
        ],
    })

    rows.append({
        "id": "teine", "name": "札幌手稻", "romaji": "Sapporo Teine", "prefecture": "北海道 札幌市",
        "region": "hokkaido", "cluster": None,
        "one_liner": "住札幌當日滑的標準答案。奧林匹亞區給新手，高地區給中高級。",
        "not_for": "想連續滑一座大山、或要封閉度假村的人——這是城市近郊場。",
        "tags": ["札幌當日", "新手友善", "夜滑"],
        "access_routes": [{"from": "桃園 → 新千歲", "steps": "進札幌市區，再搭手稻滑雪巴士約 40–50 分", "hours": "含飛行與進市區約 6.5–7.5 小時；雪場當日再加 1 小時"}],
        "budget_twd": {"min": 32000, "max": 52000, "days": "5 天 4 夜", "note": "住札幌吃喝較省，雪場本身不大。"},
        "season_note": "2026/27 公布 11/21 開放。官網有中文。",
        "night_ski": "有", "onsen": "少", "chinese_coach": "多", "ski_in_out": "少",
        "chinese_service": "官網中文，中文教練有駐點。札幌市區溝通無壓力。",
        "snow_rhythm": None,
        "pitfalls": ["高地區紅黑為主，新手不要跟團衝上去。", "當日場，週末札幌客會塞。", "不要把「手稻神社」當成雪場裡的景點，神社在手稻站。"],
        "companion_note": "不滑雪就留在札幌市區，比待在雪場強。",
        "season_delta": "2026/27 札幌市區到手稻的巴士已開放預約。",
        "scores": sc(4, 3, 1, 5, 4, 3, 2, 4, 2, 3),
        "why_beginner": "奧林匹亞區平緩，適合住札幌練第一次。",
        "why_powder": "粉雪有，但不是為粉雪專程來的場。",
        "why_tokyo": "要飛北海道。",
        "why_family": "可當日，小孩體力比較好控。",
        "why_onsen": "不是溫泉場，回札幌再泡。",
        "why_budget": "住札幌能把總額壓下來。",
        "why_coach": "中文學校有駐點。",
        "compare_with": ["rusutsu", "furano", "tomamu"],
        "experts": {
            "consensus": ["札幌當日滑首選。", "兩區程度差很大，新手留奧林匹亞。", "夜滑是加分。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/sapporo-teine-ski-resort-review/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("teine", "札幌近郊能當日來回，這就是它存在的理由。", "札幌中心部から近く、日帰りできるのが最大の魅力。", "beginner"),
            jp("teine", "高地區偏陡，新手應留在下區。", "上部は中上級向け。初心者はオリンピアエリア。", "pitfall"),
        ],
        "links": [L("札幌手稻滑雪場 2026 攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/sapporo-teine-ski-resort-review/", "overview")],
    })

    rows.append({
        "id": "sahoro", "name": "Sahoro", "romaji": "Sahoro / Club Med", "prefecture": "北海道 河東郡鹿追町",
        "region": "hokkaido", "cluster": None,
        "one_liner": "十勝內陸、晴天率相對高。台灣團很常走 Club Med 全包。",
        "not_for": "想自己排餐廳、逛村、或趕著當日從新千歲來回的人。",
        "tags": ["親子友善", "全包度假", "晴天率"],
        "access_routes": [{"from": "桃園 → 新千歲", "steps": "巴士往十勝／鹿追，約 2.5–3 小時", "hours": "含飛行約 7.5–8.5 小時"}],
        "budget_twd": {"min": 50000, "max": 90000, "days": "5 天 4 夜", "note": "幾乎等於 Club Med 套價。"},
        "season_note": "例年 12 月～3 月。內陸晴天率是北海道加分項。",
        "night_ski": "部分", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "Club Med 中文服務完整。",
        "snow_rhythm": None,
        "pitfalls": ["自由行交通比二世谷、留壽都麻煩。", "場中型，連續滑五天可能膩。", "幾乎被全包套票綁住。"],
        "companion_note": "全包活動是為不滑雪的人設計的，這點成立。",
        "season_delta": None,
        "scores": sc(4, 4, 1, 3, 2, 5, 4, 3, 5, 2),
        "why_beginner": "全包含課，第一次可以什麼都不管。",
        "why_powder": "十勝粉雪不錯，但不是為粉雪排名來的。",
        "why_tokyo": "要飛北海道再往東走。",
        "why_family": "Club Med 親子是主力客群。",
        "why_onsen": "度假村溫泉與活動都有。",
        "why_budget": "全包看起來貴，但含吃含課，要算總帳。",
        "why_coach": "全包含團體課。",
        "compare_with": ["tomamu", "kiroro", "rusutsu"],
        "experts": {
            "consensus": ["台灣團很愛走 Club Med Sahoro。", "晴天率比道西很多場穩。", "自由行交通是門檻。"],
            "disagreement": None,
            "sources": [
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
                {"name": "The Japow Project", "url": "https://japowproject.com/zh-tw/guides/japan-ski-trip-planning-guide/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("sahoro", "天候不穩的時期，Sahoro 晴天率相對高。", "天候の荒れやすい時期ならサホロが好天率が高くていいでしょう。", "snow"),
            jp("sahoro", "比較適合把滑雪當度假，而不是天天換場。", "リゾート滞在向き。", "beginner"),
        ],
        "links": [L("日本滑雪場怎麼選", "The Japow Project", "https://japowproject.com/zh-tw/guides/japan-ski-trip-planning-guide/", "overview")],
    })
    return rows

for r in bulk():
    add(r)

def honshu():
    rows = []
    rows.append({
        "id": "zao", "name": "藏王", "romaji": "Zao Onsen", "prefecture": "山形県 山形市",
        "region": "tohoku", "cluster": None,
        "one_liner": "樹冰是一生一次的畫面。場極大，但纜車配置老、路標不親切。",
        "not_for": "帶很小的孩子、或討厭走路換纜車的單板客。",
        "tags": ["樹冰", "溫泉", "適合拍照"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 山形新幹線約 2.5 小時 → 巴士約 40 分", "hours": "含飛行與進東京約 8–10 小時"}],
        "budget_twd": {"min": 38000, "max": 62000, "days": "5 天 4 夜", "note": "山形住宿比北海道親民。"},
        "season_note": "例年 12 月中～5 月初。樹冰要碰對氣溫與風，不是每天都有。",
        "night_ski": "部分", "onsen": "是", "chinese_coach": "有", "ski_in_out": "部分",
        "chinese_service": "中文比湯澤少，溫泉街日文為主。",
        "snow_rhythm": "上部雪質好、人少；山麓窄且容易擠。樹冰觀光客會佔纜車。",
        "pitfalls": ["纜車公司多家，換場要走路、單板很累。", "路標不親切，很容易迷路。", "樹冰日會被觀光客塞爆。"],
        "companion_note": "不滑雪也可以坐纜車看樹冰、泡強酸溫泉，這點成立。",
        "season_delta": None,
        "scores": sc(3, 3, 3, 1, 3, 3, 5, 3, 5, 3),
        "why_beginner": "有長綠線，但換纜車與路標不適合完全第一次。",
        "why_powder": "上部雪質好，但來的理由通常是樹冰。",
        "why_tokyo": "新幹線到山形再轉，比湯澤遠，但 1 泊 2 日做得到。",
        "why_family": "樹冰對小孩很刺激，但走路換場不友善。",
        "why_onsen": "藏王溫泉街是核心賣點。",
        "why_budget": "東北住宿相對好控。",
        "why_coach": "有中文課，密度中等。",
        "compare_with": ["nozawa", "appi", "happo-one"],
        "experts": {
            "consensus": ["樹冰是獨特景觀，值得排進一生清單。", "場很大，兩天滑不完。", "纜車配置與路標是老場的代價。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/zao-ski/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("zao", "雪質好、人相對少，這點評價很高。", "雪質の良さと混雑の少なさは、最高。", "snow"),
            jp("zao", "纜車要走路接，帶小孩或單板不推。", "リフト乗り場まで少しの登りや歩く距離がある所が多い。ボーダーや小さな子供連れには薦められない。", "pitfall"),
            jp("zao", "本州少見的大場，一天滑不完。", "本州のゲレンデとは思えない広さ。常人は1日では滑りきれない。", "beginner"),
        ],
        "links": [
            L("藏王滑雪場攻略：樹冰一生必看奇景", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/zao-ski/", "overview"),
            L("五間熱門滑雪場介紹", "Klook客路部落格", "https://www.klook.com/zh-TW/blog/zao-ski/", "overview"),
            L("藏王溫泉滑雪攻略：雪場推薦、樹冰景觀、交通住宿", "SNOWPINK滑雪新手指南", "https://www.snowpink.com.tw/blog/2026-eb86fc20-6301-4679-92f7-214a8b3ffa29", "overview"),
        ],
    })
    rows.append({
        "id": "appi", "name": "安比高原", "romaji": "Appi Kogen", "prefecture": "岩手県 八幡平市",
        "region": "tohoku", "cluster": None,
        "one_liner": "東北最大級、阿斯匹靈粉雪、雪道又長又寬。預算比北海道好控。",
        "not_for": "討厭大風、或以為還是 90 年代那種全纜車全開的人——規模有在縮。",
        "tags": ["粉雪", "雪道長", "夜滑"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 東北新幹線盛岡約 2 小時 20 分 → 巴士約 50 分", "hours": "含飛行與進東京約 8–10 小時"}],
        "budget_twd": {"min": 35000, "max": 58000, "days": "5 天 4 夜", "note": "東北裡 CP 值高，但雪場餐飲與租借不便宜。"},
        "season_note": "例年 12 月～5 月初。北斜面，春滑可到很晚。",
        "night_ski": "有", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "中文比湯澤少，度假村內英文尚可。",
        "snow_rhythm": "風大時纜車常停。晴天長道很過癮。",
        "pitfalls": ["地吹雪，風大纜車停駛頻率不低。", "近年全日運行纜車減少，規模感不如印象。", "週末纜車仍可能擠。"],
        "companion_note": "度假村內能待，但不如 Tomamu／留壽都豐富。",
        "season_delta": None,
        "scores": sc(4, 4, 3, 1, 4, 4, 3, 3, 3, 4),
        "why_beginner": "有從山頂下來的初級道，寬、好整理。",
        "why_powder": "阿斯匹靈粉雪，東北粉雪代表。",
        "why_tokyo": "新幹線到盛岡再轉，比湯澤遠、比北海道省事。",
        "why_family": "寬道好滑，度假村可住。",
        "why_onsen": "有溫泉，但不是溫泉街型。",
        "why_budget": "本州長假裡相對好控。",
        "why_coach": "有中文課，密度中等。",
        "compare_with": ["zao", "happo-one", "naeba"],
        "experts": {
            "consensus": ["雪道長、粉雪細，中級以上會喜歡。", "盛岡新幹線讓首都圈 1 泊 2 日做得到。", "風與纜車縮編是現在的現實。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/appi-kogen-resort-review/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-ski-beginner/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("appi", "又寬又長、雪質好，老手很愛。", "広い、長い、雪質よし。上手くなった錯覚になる雪質。", "snow"),
            jp("appi", "纜車等待少是優點，但停駛也多。", "リフトやゴンドラの待ち時間がなく、スムーズ。運行休止が多すぎる。", "pitfall"),
            jp("appi", "山頂到山麓的初級道，誰都能慢慢滑。", "頂上から山麓までの初級者コースは快適。", "beginner"),
        ],
        "links": [L("安比高原滑雪場攻略 2026", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/appi-kogen-resort-review/", "overview")],
    })
    rows.append({
        "id": "bandai", "name": "星野磐梯（貓魔）", "romaji": "Hoshino Bandai / Nekoma", "prefecture": "福島県 耶麻郡",
        "region": "tohoku", "cluster": None,
        "one_liner": "星野把豬苗代兩座山整成度假產品。台灣套裝常見，適合想要設施勝於極限地形的人。",
        "not_for": "只想滑一座連貫大山、或趕東京當日的人。",
        "tags": ["親子友善", "星野度假村", "Ski-in/out"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 東北新幹線郡山／會津若松再轉巴士", "hours": "含飛行與進東京約 8–10 小時"}],
        "budget_twd": {"min": 40000, "max": 68000, "days": "5 天 4 夜", "note": "星野價，套裝常含巴士。"},
        "season_note": "貓魔區季初較早開；磐梯區較晚。以官網分區為準。",
        "night_ski": "部分", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "星野標示清楚，中文比純東北鄉鎮場好。",
        "snow_rhythm": None,
        "pitfalls": ["兩區不是無腦連在一起，要看住宿在哪。", "不是東京當日場。", "雪質好但不算北海道粉雪。"],
        "companion_note": "星野設施讓不滑雪的人有地方待。",
        "season_delta": None,
        "scores": sc(4, 3, 3, 1, 3, 5, 4, 3, 5, 3),
        "why_beginner": "星野體系對第一次相對好懂。",
        "why_powder": "有粉，但不是為粉雪專程飛福島。",
        "why_tokyo": "新幹線再轉，比湯澤遠。",
        "why_family": "星野親子產品很完整。",
        "why_onsen": "度假村溫泉有。",
        "why_budget": "中等偏高。",
        "why_coach": "套裝常含中文課。",
        "compare_with": ["tomamu", "zao", "appi"],
        "experts": {
            "consensus": ["台灣套裝常見的東北選項。", "設施與一條龍比地形有名。", "要分清貓魔區與磐梯區。"],
            "disagreement": None,
            "sources": [
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/japan-ski-resorts-guide/", "kind": "blogger"},
            ],
        },
        "community": [],
        "links": [L("日本滑雪場開放時間總表", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/japan-ski-resorts-guide/", "overview")],
    })
    return rows

for r in honshu():
    add(r)

def niigata_nagano():
    rows = []
    rows.append({
        "id": "gala-yuzawa", "name": "GALA湯澤", "romaji": "GALA Yuzawa", "prefecture": "新潟県 南魚沼郡湯澤町",
        "region": "niigata", "cluster": "yuzawa",
        "one_liner": "新幹線下車就是雪場。第一次、已在東京、要中文教練，這是最短路徑。",
        "not_for": "想滑超過兩天、要世界級粉雪、或週末討厭人潮的人。場小、週末租借能排一小時。",
        "tags": ["新幹線直達", "新手友善", "中文教練"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "進東京站 → 上越新幹線至 GALA湯澤站（下車即場）", "hours": "含機場到東京約 4.5–6 小時；東京出發約 75 分"}],
        "budget_twd": {"min": 30000, "max": 50000, "days": "5 天 4 夜", "note": "可住東京當日來回，省住宿；或住湯澤溫泉街。"},
        "season_note": "例年 12 月下旬～5 月初。標高相對高，湯澤圈雪質較好。",
        "night_ski": "無", "onsen": "是", "chinese_coach": "多", "ski_in_out": "少",
        "chinese_service": "台灣店、中文教練密度是本州最高帶。手把式當日滑雪最成熟。",
        "snow_rhythm": "午後下山道擠、雪質變差。週末上午滑雪中心像戰場。",
        "pitfalls": ["週末租借與更衣室能耗掉一小時，請先在手機完成租借。", "新手區又窄又擠，完全沒滑過未必是最好的第一堂。", "下山道標成初中級，其實初學者會很痛苦。"],
        "companion_note": "場內有 SPA 與雪盆區；也可回湯澤站泡溫泉、逛ぽんしゅ館。",
        "season_delta": "票務與租借已大量改成事前手機辦理，比舊印象好一點，但人還是很多。",
        "scores": sc(5, 2, 5, 1, 4, 4, 4, 5, 3, 2),
        "why_beginner": "下車即滑、中文教練好找，第一次從東京出發的最短路徑。",
        "why_powder": "不是為粉雪來的。南區有非壓雪，但別期待北海道。",
        "why_tokyo": "日本唯一新幹線直結雪場。",
        "why_family": "當日來回對小孩體力友善，SPA 能給不滑的人。",
        "why_onsen": "場內有湯，湯澤溫泉街在旁邊。",
        "why_budget": "住東京當日滑，能省掉雪場住宿。",
        "why_coach": "中文教練密度本州前段班。",
        "compare_with": ["karuizawa", "naeba", "ishiuchi"],
        "experts": {
            "consensus": ["交通是日本第一方便。", "場不大，滑兩天會膩。", "台灣人第一次很常被帶來這裡。"],
            "disagreement": "有教練說綠線比例高適合第一次；也有人說週末新手區太擠，不如苗場或岩原。",
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/gala-ski-resort-review/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-ski-beginner/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("gala", "方便就是一切。週末租借能排快一小時。", "とにかく便利。それが全て。人が多すぎる。週末はレンタルを借りるのに小一時間かかる。", "pitfall"),
            jp("gala", "新手區又窄又擠，不見得適合完全沒滑過的人。", "初心者向けコースは狭くて混雑。", "beginner"),
            jp("gala", "GALA 太擠就逃去石打或湯澤高原，那邊空很多。", "GALAに比べると石打丸山や湯沢高原は驚くほど空いている。", "snow"),
        ],
        "links": [
            L("GALA湯澤滑雪場攻略：滑雪新手最愛", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/gala-ski-resort-review/", "overview"),
            L("滑雪教練帶你玩越後湯澤", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/yuzawa-ski/", "access"),
        ],
    })
    rows.append({
        "id": "ishiuchi", "name": "石打丸山", "romaji": "Ishiuchi Maruyama", "prefecture": "新潟県 南魚沼市",
        "region": "niigata", "cluster": "yuzawa",
        "one_liner": "湯澤圈最大的一座。風景好、道寬，但綠線偏少偏陡，不是最甜的第一次。",
        "not_for": "完全沒滑過、又想待在最甜綠線的人——去 GALA 或湯澤高原更合適。",
        "tags": ["三山共通", "風景", "中級友善"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤站 → 接駁約 10–20 分", "hours": "含機場到東京約 5–6.5 小時"}],
        "budget_twd": {"min": 32000, "max": 52000, "days": "5 天 4 夜", "note": "可與 GALA、湯澤高原買三山券。"},
        "season_note": "例年 12 月中～4 月初。",
        "night_ski": "有", "onsen": "少", "chinese_coach": "多", "ski_in_out": "部分",
        "chinese_service": "湯澤圈，中文教練好找。",
        "snow_rhythm": "GALA 塞的時候這裡常常空一截。",
        "pitfalls": ["綠線比例不高，第一次要先看地圖。", "老場氛圍，設施參差。", "和 GALA 相通，但平坦連接單板會推得辛苦。"],
        "companion_note": "可搭纜車看魚沼平原與玻璃屋，不滑也能上山。",
        "season_delta": None,
        "scores": sc(3, 3, 5, 1, 4, 3, 2, 4, 3, 3),
        "why_beginner": "能滑，但不是最甜的第一座；綠線偏陡。",
        "why_powder": "湯澤圈裡地形比較有內容。",
        "why_tokyo": "湯澤接駁短，當日做得到。",
        "why_family": "風景好，但第一次帶小孩不如 GALA／苗場。",
        "why_onsen": "回湯澤泡。",
        "why_budget": "本州好控。",
        "why_coach": "湯澤圈中文教練多。",
        "compare_with": ["gala-yuzawa", "yuzawa-kogen", "naeba"],
        "experts": {
            "consensus": ["三山裡規模最大、道比較寬。", "第一次不一定是最佳解。", "GALA 太擠就過來。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/ishiuchi-maruyama-ski-resort-guide/", "kind": "blogger"},
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/yuzawa-ski/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("ishiuchi", "場的潛力很高，道寬、風景一流。", "ゲレンデのポテンシャルはとても高い。コースの幅が広い。", "snow"),
            jp("ishiuchi", "昭和混雜的老場味道，設施舊但滑起來過癮。", "昭和のごちゃごちゃした雰囲気のスキー場。施設は古い。", "pitfall"),
            jp("ishiuchi", "和 GALA、湯澤高原有共通券可逃。", "三山共通リフト券で隣接ゲレンデへ。", "beginner"),
        ],
        "links": [L("石打丸山滑雪場攻略 2026", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/ishiuchi-maruyama-ski-resort-guide/", "overview")],
    })
    rows.append({
        "id": "yuzawa-kogen", "name": "湯澤高原", "romaji": "Yuzawa Kogen", "prefecture": "新潟県 南魚沼郡湯澤町",
        "region": "niigata", "cluster": "yuzawa",
        "one_liner": "越後湯澤適合新手的那座。纜車從町裡上去，和 GALA、石打可三山連。",
        "not_for": "想要大垂直落差或粉雪的人。",
        "tags": ["新手友善", "三山共通", "親子友善"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤站 → 徒步／短程到纜車站", "hours": "含機場到東京約 5–6 小時"}],
        "budget_twd": {"min": 30000, "max": 48000, "days": "5 天 4 夜", "note": "住湯澤町最方便。"},
        "season_note": "例年 12 月～3 月底。",
        "night_ski": "無", "onsen": "是", "chinese_coach": "多", "ski_in_out": "少",
        "chinese_service": "湯澤町內台灣店多。",
        "snow_rhythm": "標高低於 GALA，午後較易濕。",
        "pitfalls": ["場中型，滑兩天會膩。", "大型纜車是賣點，不是地形。"],
        "companion_note": "可搭世界級大型纜車上山看風景，再回溫泉街。",
        "season_delta": None,
        "scores": sc(5, 2, 5, 1, 4, 4, 3, 4, 4, 2),
        "why_beginner": "湯澤圈裡偏新手的那座。",
        "why_powder": "不是粉雪場。",
        "why_tokyo": "車站到纜車很近。",
        "why_family": "上山看風景＋溫泉街，小孩好帶。",
        "why_onsen": "人在湯澤溫泉街。",
        "why_budget": "本州好控。",
        "why_coach": "中文教練好找。",
        "compare_with": ["gala-yuzawa", "ishiuchi", "naeba"],
        "experts": {
            "consensus": ["新手友善。", "交通幾乎跟 GALA 同一套。", "三山券讓你可以逃去石打。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/yuzawa-kogen/", "kind": "blogger"},
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/yuzawa-ski/", "kind": "blogger"},
            ],
        },
        "community": [],
        "links": [L("湯澤高原滑雪場：適合新手", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/yuzawa-kogen/", "overview")],
    })
    rows.append({
        "id": "naeba", "name": "苗場", "romaji": "Naeba", "prefecture": "新潟県 南魚沼郡湯澤町",
        "region": "niigata", "cluster": None,
        "one_liner": "台灣教練口中的新手天堂。Ski-in/out、夜滑、中文課都齊，但從湯澤還要再轉一小時。",
        "not_for": "已在東京只想當日、或不想付「苗場價格」的人。",
        "tags": ["新手友善", "Ski-in/out", "夜滑"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤 → 巴士約 40–60 分到苗場王子", "hours": "含機場到東京約 6–7.5 小時"}],
        "budget_twd": {"min": 35000, "max": 60000, "days": "5 天 4 夜", "note": "餐飲與纜車是苗場價，比湯澤站前貴一截。"},
        "season_note": "例年 12 月中～4 月初。可經龍纜車連神樂。",
        "night_ski": "有", "onsen": "有", "chinese_coach": "多", "ski_in_out": "常見",
        "chinese_service": "中文教練非常多，台灣人密度高。",
        "snow_rhythm": "湯澤圈裡雪質相對好（較內陸、較高）。週末仍會擠。",
        "pitfalls": ["不是新幹線下車即滑，當日來回不划算。", "餐飲偏貴。", "淡季部分纜車不開。"],
        "companion_note": "王子飯店體系有商場與餐廳，不滑能待；但不如輕井澤 outlet。",
        "season_delta": None,
        "scores": sc(5, 3, 4, 1, 4, 4, 3, 5, 4, 2),
        "why_beginner": "綠線寬、教練密、Ski-in/out，第一次本州的標準答案之一。",
        "why_powder": "比 GALA 好，比北海道差。連神樂才比較有粉。",
        "why_tokyo": "要再轉巴士，當日不優；過夜很適合。",
        "why_family": "一條龍度假村，小孩好帶。",
        "why_onsen": "有溫泉，但是度假村湯多於溫泉街。",
        "why_budget": "比北海道好控，比湯澤站前貴。",
        "why_coach": "中文教練密度極高。",
        "compare_with": ["gala-yuzawa", "kagura", "tsugaike"],
        "experts": {
            "consensus": ["台灣教練很常推給第一次。", "住苗場王子最省事。", "進階想衝粉要去隔壁神樂。"],
            "disagreement": None,
            "sources": [
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-ski-beginner/", "kind": "blogger"},
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/yuzawa-ski/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("naeba", "初級區寬、好滑，第 2、4、5 區常被點名。", "初級者には第2・第4・第5ゲレンデがオススメ。幅も広く滑りやすい。", "beginner"),
            jp("naeba", "現在沒有以前那麼排纜車，但週末還是會擠。", "昔ほどの人はいなくなった。混んでいて滑りにくいという感想もある。", "pitfall"),
            jp("naeba", "湯澤圈裡雪質相對好。", "湯沢エリアでは一番の雪質。", "snow"),
        ],
        "links": [
            L("越後湯澤滑雪總攻略（含苗場）", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/yuzawa-ski/", "overview"),
            L("14 個新手滑雪場", "滑雪太空人", "https://www.yuriselfmedia.tw/japan-ski-beginner/", "overview"),
        ],
    })
    rows.append({
        "id": "kagura", "name": "神樂", "romaji": "Kagura", "prefecture": "新潟県 南魚沼郡湯澤町",
        "region": "niigata", "cluster": None,
        "one_liner": "關東側粉雪與春滑代表。路複雜，新手不要當第一座山。",
        "not_for": "第一次、路癡、或不想看雪場地圖的人。",
        "tags": ["粉雪", "春滑", "進階"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤 → 巴士到神樂／田代／三俣", "hours": "含機場到東京約 6–8 小時"}],
        "budget_twd": {"min": 35000, "max": 58000, "days": "5 天 4 夜", "note": "可與苗場買全山券。"},
        "season_note": "例年 11 月底～5 月中，關東最晚關之一。",
        "night_ski": "無", "onsen": "少", "chinese_coach": "有", "ski_in_out": "少",
        "chinese_service": "比苗場少，進階客較多。",
        "snow_rhythm": "雪質是湯澤圈前段。岔路多，不看地圖會迷路。",
        "pitfalls": ["田代／神樂／三俣／苗場名稱很混。", "龍纜車來回票種不同，買錯會上不了。", "路線複雜。"],
        "companion_note": "不太建議硬帶不滑雪的人來神樂本場。",
        "season_delta": None,
        "scores": sc(2, 4, 4, 1, 3, 2, 2, 3, 2, 5),
        "why_beginner": "不適合當第一座。",
        "why_powder": "本州想衝鬆雪，常被點名。",
        "why_tokyo": "湯澤再轉，過夜才划算。",
        "why_family": "不是親子場。",
        "why_onsen": "回湯澤或苗場泡。",
        "why_budget": "中等。",
        "why_coach": "有中文，但客群偏進階。",
        "compare_with": ["naeba", "happo-one", "shiga-kogen"],
        "experts": {
            "consensus": ["春滑與粉雪是賣點。", "和苗場用龍纜車連，票要買對。", "路癡會崩潰。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/kagura-ski-resort-review/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("kagura", "關東側能滑到很晚，春滑常被點名。", "関東でも遅くまで滑れる春スキー場。", "snow"),
            jp("kagura", "岔路多，不帶地圖會迷路。", "コースが複雑。地図必須。", "pitfall"),
        ],
        "links": [L("神樂滑雪場攻略：龍纜車與鬆雪", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/kagura-ski-resort-review/", "slope")],
    })
    rows.append({
        "id": "joetsu-kokusai", "name": "上越國際", "romaji": "Joetsu Kokusai", "prefecture": "新潟県 南魚沼市",
        "region": "niigata", "cluster": None,
        "one_liner": "湯澤圈裡 Ski-in/out、夜滑、相對好價。第一次與過夜練習場。",
        "not_for": "想要新幹線下車即滑、或要頂級粉雪的人。",
        "tags": ["Ski-in/out", "夜滑", "新手友善"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤 → 短程接駁／上越線", "hours": "含機場到東京約 5.5–7 小時"}],
        "budget_twd": {"min": 30000, "max": 50000, "days": "5 天 4 夜", "note": "湯澤圈裡較好價。"},
        "season_note": "例年 12 月～4 月初。",
        "night_ski": "有", "onsen": "有", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "湯澤圈，中文可。",
        "snow_rhythm": None,
        "pitfalls": ["知名度被 GALA／苗場蓋過，資料較散。", "不是一日遊第一名。"],
        "companion_note": "度假村可待，小鎮感一般。",
        "season_delta": None,
        "scores": sc(4, 3, 4, 1, 5, 4, 3, 3, 3, 3),
        "why_beginner": "Ski-in/out 讓第一次少搬裝備。",
        "why_powder": "普通本州雪。",
        "why_tokyo": "湯澤再轉一小段。",
        "why_family": "一條龍住滑。",
        "why_onsen": "有溫泉。",
        "why_budget": "湯澤圈裡相對省。",
        "why_coach": "有中文，密度中等。",
        "compare_with": ["naeba", "maiko", "gala-yuzawa"],
        "experts": {
            "consensus": ["Ski-in/out 與夜滑是優點。", "台灣教練會拿來當過夜練習場。", "預算比苗場好控。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/yuzawa-ski/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [],
        "links": [L("越後湯澤滑雪總攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/yuzawa-ski/", "overview")],
    })
    rows.append({
        "id": "myoko", "name": "妙高高原", "romaji": "Myoko Kogen", "prefecture": "新潟県 妙高市",
        "region": "niigata", "cluster": "myoko",
        "one_liner": "日本六大溫泉滑雪場之一。多座小場組成，在地感濃，交通比湯澤煩。",
        "not_for": "第一次自助、或不想研究赤倉／杉之原／池之平差在哪的人。",
        "tags": ["溫泉滑雪場", "多雪場選擇", "在地感"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 北陸新幹線上越妙高約 100 分 → 冬季巴士", "hours": "含機場到東京約 6.5–8 小時"}],
        "budget_twd": {"min": 35000, "max": 55000, "days": "5 天 4 夜", "note": "比二世谷、白馬好控。"},
        "season_note": "例年 12 月～4 月。雪量在本州前段。",
        "night_ski": "部分", "onsen": "是", "chinese_coach": "有", "ski_in_out": "部分",
        "chinese_service": "中文少於湯澤，多於純東北鄉鎮。",
        "snow_rhythm": "雪多。子場很多，第一季當一座場看。",
        "pitfalls": ["子場分散，選錯住宿會天天坐巴士。", "交通比湯澤煩。", "資料在中文圈比白馬少。"],
        "companion_note": "溫泉是不滑雪的人的理由。",
        "season_delta": None,
        "scores": sc(3, 4, 3, 1, 3, 3, 5, 3, 4, 3),
        "why_beginner": "有友善子場，但自助第一次較容易選錯山。",
        "why_powder": "本州多雪區，粉雪機會高。",
        "why_tokyo": "新幹線到上越妙高再轉。",
        "why_family": "溫泉加雪，行，但要選對子場。",
        "why_onsen": "這就是來的理由。",
        "why_budget": "中等。",
        "why_coach": "有中文，密度中等。",
        "compare_with": ["nozawa", "naeba", "happo-one"],
        "experts": {
            "consensus": ["溫泉滑雪是核心。", "不是一座場，是一群場。", "交通要先搞懂上越妙高 vs 妙高高原站。"],
            "disagreement": None,
            "sources": [
                {"name": "SSW Board House", "url": "https://sswboardhouse.com/japan-niigata-myoko-kogen-ski-snowboard-guide-zh/", "kind": "blogger"},
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/category/ski-in-japan/myoko-kogen/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("myoko", "雪量在本州有競爭力，溫泉是加分。", "雪質・積雪は本州でも上位。温泉スキー場。", "snow"),
            jp("myoko", "子場分散，住宿選錯會很累。", "エリアが分散。宿選びが重要。", "pitfall"),
        ],
        "links": [
            L("妙高高原滑雪場攻略", "SSW Board House", "https://sswboardhouse.com/japan-niigata-myoko-kogen-ski-snowboard-guide-zh/", "overview"),
            L("妙高高原系列", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/category/ski-in-japan/myoko-kogen/", "overview"),
            L("日本六大溫泉滑雪場：妙高", "頭獎徽的自助滑雪省錢攻略", "http://jeterchen-snowbackpacker.blogspot.com/2015/09/myoko.html", "overview"),
        ],
    })
    rows.append({
        "id": "maiko", "name": "舞子高原", "romaji": "Maiko Snow Resort", "prefecture": "新潟県 南魚沼市",
        "region": "niigata", "cluster": None,
        "one_liner": "近年新潟人氣上升很快。Ski-in/out、新手到進階都有，台灣團開始走。",
        "not_for": "只想要新幹線下車即滑的人。",
        "tags": ["Ski-in/out", "新手友善", "親子友善"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 越後湯澤 → 接駁約 20 分", "hours": "含機場到東京約 5.5–7 小時"}],
        "budget_twd": {"min": 32000, "max": 52000, "days": "5 天 4 夜", "note": "早鳥纜車票常有。"},
        "season_note": "例年 12 月下旬～3 月底。夜滑到晚上 8 點。",
        "night_ski": "有", "onsen": "少", "chinese_coach": "有", "ski_in_out": "常見",
        "chinese_service": "台灣團變多，中文比以前好找。",
        "snow_rhythm": None,
        "pitfalls": ["奧添地區紅黑為主，新手不要跟去。", "知名度剛起來，中文攻略比苗場少。"],
        "companion_note": "有雪地遊樂，不滑能玩一下。",
        "season_delta": "2026/27 早鳥纜車票常被拿來跟 22 雪場共通票一起賣。",
        "scores": sc(4, 3, 4, 1, 4, 4, 2, 3, 3, 3),
        "why_beginner": "舞子區綠線友善，飯店 Ski-in/out。",
        "why_powder": "有界外規劃，但不是神樂那種粉雪印象。",
        "why_tokyo": "湯澤 20 分。",
        "why_family": "遊樂設施加 Ski-in/out。",
        "why_onsen": "弱，回湯澤泡。",
        "why_budget": "好控。",
        "why_coach": "有中文。",
        "compare_with": ["naeba", "joetsu-kokusai", "gala-yuzawa"],
        "experts": {
            "consensus": ["Ski-in/out 新手場，近年討論度上升。", "最長滑行距離不短。", "分區程度差要看地圖。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/maiko-resor/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("maiko", "新手區在飯店前，進階往奧添。", "ホテル前は初心者向き。奥添は中上級。", "beginner"),
            jp("maiko", "夜滑時間長，對過夜客友善。", "ナイターが長い。", "pitfall"),
        ],
        "links": [L("舞子高原滑雪場攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/maiko-resor/", "overview")],
    })

    # Nagano
    rows.append({
        "id": "happo-one", "name": "白馬八方尾根", "romaji": "Happo-one", "prefecture": "長野県 北安曇郡白馬村",
        "region": "nagano", "cluster": "hakuba",
        "one_liner": "冬奧主場、本州進階代表。第一次請先不要把它當第一座山。",
        "not_for": "第一次、紅線會怕、帶小孩當主場的人。八方的中級，在別場常常是上級。",
        "tags": ["冬奧場地", "進階地形", "國際化"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 北陸新幹線長野約 80–90 分 → 巴士約 70 分", "hours": "含機場到東京約 7–9 小時"}],
        "budget_twd": {"min": 40000, "max": 68000, "days": "5 天 4 夜", "note": "白馬村住宿選擇多，價差大。"},
        "season_note": "例年 12 月上旬～5 月初。",
        "night_ski": "部分", "onsen": "是", "chinese_coach": "多", "ski_in_out": "部分",
        "chinese_service": "國際化，中英文都有。比東北好辦事。",
        "snow_rhythm": "午後饅頭坡是新手殺手。上部景色極好。",
        "pitfalls": ["紅黑線比例高，第一次很容易被打垮。", "停車與滑雪中心分散，當日客不友善。", "八方的「中級」比別場難一階。"],
        "companion_note": "白馬村餐廳多；不滑可逛村，但不如野澤溫泉街完整。",
        "season_delta": None,
        "scores": sc(1, 4, 3, 1, 3, 1, 3, 4, 2, 5),
        "why_beginner": "先不要當第一座山。真要來，只留在咲花區。",
        "why_powder": "進階地形與粉雪機會都有，本州旗艦。",
        "why_tokyo": "新幹線加巴士，過夜行程。",
        "why_family": "不是親子主場。",
        "why_onsen": "白馬有溫泉，但滑才是主菜。",
        "why_budget": "中高。",
        "why_coach": "中文教練不少，但課程常假設你已會滑。",
        "compare_with": ["tsugaike", "hakuba-goryu", "kagura"],
        "experts": {
            "consensus": ["本州進階必去。", "新手去八方會哭，這句反覆出現。", "咲花區才是初學者該待的地方。"],
            "disagreement": None,
            "sources": [
                {"name": "SSW Board House", "url": "https://sswboardhouse.com/hakuba-ski-resort-guide-zh/", "kind": "blogger"},
                {"name": "The Japow Project", "url": "https://japowproject.com/zh-tw/guides/japan-ski-trip-planning-guide/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("happo", "初級者會過得很痛苦。這裡的滑雪比較像競技。", "初級者にはとてもつらいゲレンデ。八方尾根において、スキーは娯楽ではなく競技である。", "beginner"),
            jp("happo", "八方的中級，在別場常常是上級。", "八方の中級コースは他ゲレンデの上級コース。", "pitfall"),
            jp("happo", "中上級者會覺得好道很多，リーゼンスラローム想滑第二次。", "中上級者には良いコースばかり。リーゼンスラロームは何度でも滑りたくなる。", "snow"),
        ],
        "links": [
            L("白馬滑雪場保姆級攻略", "SSW Board House", "https://sswboardhouse.com/hakuba-ski-resort-guide-zh/", "slope"),
            L("白馬村 22 家推薦飯店", "MATCHA", "https://matcha-jp.com/tw/17382", "hotel"),
            L("長野白馬 Ski in Ski out 滑雪行程筆記", "魔法貓的旅程", "https://www.magiccat.tw/%E9%95%B7%E9%87%8E%E7%99%BD%E9%A6%AC-ski-in-ski-out-%E6%BB%91%E9%9B%AA%E8%A1%8C%E7%A8%8B/", "hotel"),
        ],
    })
    rows.append({
        "id": "tsugaike", "name": "栂池高原", "romaji": "Tsugaike", "prefecture": "長野県 北安曇郡小谷村",
        "region": "nagano", "cluster": "hakuba",
        "one_liner": "白馬谷的新手天堂。寬綠線多，第一次選白馬請先來這裡，不是八方。",
        "not_for": "專程找陡坡與公園的進階者——上部有難道，但主體是緩坡。",
        "tags": ["新手友善", "親子友善", "白馬谷"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 長野新幹線 → 巴士約 90 分", "hours": "含機場到東京約 7.5–9.5 小時"}],
        "budget_twd": {"min": 38000, "max": 62000, "days": "5 天 4 夜", "note": "有初心者纜車票，比全日票便宜。"},
        "season_note": "例年 11 月底～5 月初，白馬谷裡季初較早開的之一。",
        "night_ski": "無", "onsen": "有", "chinese_coach": "多", "ski_in_out": "部分",
        "chinese_service": "白馬谷，中文教練好找。",
        "snow_rhythm": None,
        "pitfalls": ["不要聽「去白馬」就住到八方再來這裡，交通會耗掉。", "上級道少，連滑五天進階者可能膩。"],
        "companion_note": "雪地活動多（雪鞋、雪上摩托車），不滑能排。",
        "season_delta": None,
        "scores": sc(5, 3, 3, 1, 3, 5, 3, 4, 4, 3),
        "why_beginner": "白馬谷第一次請來栂池。寬、緩、好練。",
        "why_powder": "有粉，但個性是新手場。",
        "why_tokyo": "跟白馬同一套新幹線加巴士。",
        "why_family": "親子在白馬谷的第一選擇。",
        "why_onsen": "有，但不是野澤那種外湯。",
        "why_budget": "中等，初心者票能省。",
        "why_coach": "中文教練多。",
        "compare_with": ["happo-one", "naeba", "hakuba-goryu"],
        "experts": {
            "consensus": ["白馬新手請來栂池。", "初中級佔約八成。", "住宿要選栂池，不要住八方再跨。"],
            "disagreement": "有人說它其實是中級天堂，上部比想像難。",
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/tsugaike-ski/", "kind": "blogger"},
                {"name": "SSW Board House", "url": "https://sswboardhouse.com/hakuba-ski-resort-guide-zh/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("tsugaike", "寬而長的緩坡很多，新手能滑的地方不少。", "広く長い緩斜面がたくさんあり初心者でも滑れる場所が多い。", "beginner"),
            jp("tsugaike", "被叫新手天堂，但上部中級道其實不少。", "初級者天国と言われるが、上部には中級向けのコースが多く、実際は中級天国。", "snow"),
            jp("tsugaike", "陡坡少，上級者不太過癮。", "急斜面は少しだけで、上級者はあまり楽しめるコースはない。", "pitfall"),
        ],
        "links": [L("栂池高原滑雪場攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/tsugaike-ski/", "overview")],
    })
    rows.append({
        "id": "hakuba-goryu", "name": "白馬五龍", "romaji": "Hakuba Goryu", "prefecture": "長野県 北安曇郡白馬村",
        "region": "nagano", "cluster": "hakuba",
        "one_liner": "白馬谷裡地形與公園較均衡的一座，常和 47 連。適合已會滑、不想只待栂池的人。",
        "not_for": "完全第一次——去栂池；或只要冬奧名氣——那是八方。",
        "tags": ["夜滑", "公園", "白馬谷"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 長野 → 巴士至白馬五龍", "hours": "含機場到東京約 7.5–9.5 小時"}],
        "budget_twd": {"min": 38000, "max": 62000, "days": "5 天 4 夜", "note": "可買五龍＋47 聯合券。"},
        "season_note": "例年 12 月上旬～5 月初。",
        "night_ski": "有", "onsen": "少", "chinese_coach": "多", "ski_in_out": "部分",
        "chinese_service": "白馬谷中文教練多。",
        "snow_rhythm": None,
        "pitfalls": ["和八方、栂池不是走過去就到，住宿要選五龍區。", "第一次仍偏硬。"],
        "companion_note": "夜滑是加分；不滑雪的人不如野澤。",
        "season_delta": None,
        "scores": sc(3, 3, 3, 1, 3, 3, 2, 4, 3, 4),
        "why_beginner": "能滑，但第一次仍建議栂池。",
        "why_powder": "白馬谷中段選擇，地形比栂池有內容。",
        "why_tokyo": "白馬同一套交通。",
        "why_family": "中等。",
        "why_onsen": "弱。",
        "why_budget": "中等。",
        "why_coach": "中文教練多。",
        "compare_with": ["happo-one", "tsugaike", "naeba"],
        "experts": {
            "consensus": ["公園與夜滑是白馬谷加分。", "常和 47 一起買。", "不要和八方搞混住宿。"],
            "disagreement": None,
            "sources": [
                {"name": "SSW Board House", "url": "https://sswboardhouse.com/hakuba-ski-resort-guide-zh/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [],
        "links": [L("白馬滑雪場保姆級攻略", "SSW Board House", "https://sswboardhouse.com/hakuba-ski-resort-guide-zh/", "overview")],
    })
    rows.append({
        "id": "nozawa", "name": "野澤溫泉", "romaji": "Nozawa Onsen", "prefecture": "長野県 下高井郡野澤溫泉村",
        "region": "nagano", "cluster": None,
        "one_liner": "13 個免費外湯與木造溫泉老街。滑雪是主菜，村子是為什麼要過夜。",
        "not_for": "東京當日客、或只想封閉度假村什麼都不管的人。",
        "tags": ["溫泉老街", "非滑雪者友善", "適合家庭"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 北陸新幹線飯山約 100 分 → 巴士約 25–30 分", "hours": "含機場到東京約 6.5–8.5 小時"}],
        "budget_twd": {"min": 40000, "max": 65000, "days": "5 天 4 夜", "note": "村子裡吃喝選擇多，能把度假村價打掉一點。"},
        "season_note": "例年 11 月底～5 月初，天然雪、季長。",
        "night_ski": "無", "onsen": "是", "chinese_coach": "有", "ski_in_out": "部分",
        "chinese_service": "外國人多，英文不錯；中文中等。",
        "snow_rhythm": "上的平雪質好但尖峰擠；湯之峰、水無較空。長坂 Gondola 週末上午可能排很久。",
        "pitfalls": ["長坂 Gondola 尖峰能排一小時。", "Skyline 景觀道比標示難，事故多。", "村子路窄、停車少，自駕要有心理準備。"],
        "companion_note": "不滑雪的理由非常充分：外湯、老街、吃。這是少數「帶不滑雪的人也不虧」的場。",
        "season_delta": None,
        "scores": sc(4, 4, 3, 1, 3, 4, 5, 3, 5, 3),
        "why_beginner": "上的平有寬緩坡，第一次可以，但村子移動要走路。",
        "why_powder": "天然雪、季長，本州粉雪前段。",
        "why_tokyo": "飯山新幹線再轉，過夜。",
        "why_family": "村子讓不滑的家人有事做。",
        "why_onsen": "這就是野澤。",
        "why_budget": "中等，自己找吃可以控。",
        "why_coach": "有中文，密度不如湯澤。",
        "compare_with": ["zao", "happo-one", "shiga-kogen"],
        "experts": {
            "consensus": ["溫泉街是核心差異。", "場夠大，三天不會膩。", " overnight 才值得來，當日不划算。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/nozawa-ski/", "kind": "blogger"},
                {"name": "The Japow Project", "url": "https://japowproject.com/zh-tw/guides/japan-ski-trip-planning-guide/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("nozawa", "初級到上級都有，寬緩坡讓小孩能安心滑。", "初級者から上級者までコースが充実。広い緩斜面では初級者や子供が安心して滑れる。", "beginner"),
            jp("nozawa", "雪質好、粉雪季長。", "雪質は良い。粉雪が魅力。積雪量が多く、シーズンが長い。", "snow"),
            jp("nozawa", "長坂 Gondola 週末上午可能排到一小時。", "長坂ゴンドラは週末の午前は1時間待ち。", "pitfall"),
        ],
        "links": [
            L("野澤溫泉滑雪場攻略", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/nozawa-ski/", "overview"),
            L("不滑雪的野澤 × 志賀玩法", "MTKO", "https://www.mtkomtko.com/travel/nagano-nozawa/", "overview"),
            L("野澤溫泉村周邊景點介紹", "冒險安迪", "https://andyventure.com/japan-nozawa-onsen-village-itinerary/", "overview"),
        ],
    })
    rows.append({
        "id": "shiga-kogen", "name": "志賀高原", "romaji": "Shiga Kogen", "prefecture": "長野県 下高井郡山ノ内町",
        "region": "nagano", "cluster": "shiga",
        "one_liner": "日本最大滑雪區域（18 區）。雪質本州前段，但第一次不要當主選——太大、太散、偏貴。",
        "not_for": "第一次、路癡、只請得到兩天的人。",
        "tags": ["最大滑雪區域", "雪質好", "進階"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 長野 → 巴士 70–80 分；或湯田中再轉", "hours": "含機場到東京約 7.5–9.5 小時"}],
        "budget_twd": {"min": 40000, "max": 68000, "days": "5 天 4 夜", "note": "全區共通券與住宿都偏高。"},
        "season_note": "例年 11 月下旬～5 月。標高高，4 月仍常有好雪。",
        "night_ski": "少", "onsen": "有", "chinese_coach": "有", "ski_in_out": "部分",
        "chinese_service": "中文少於白馬／湯澤。",
        "snow_rhythm": "標高高、冷、雪質好。不是為夜滑來的。",
        "pitfalls": ["18 區個性差很大，一張身份證講不完。", "交通與動線不直覺。", "餐飲評價兩極，偏貴。"],
        "companion_note": "看你住哪一區；不是每個區都有村子可逛。",
        "season_delta": None,
        "scores": sc(2, 4, 3, 1, 3, 2, 3, 3, 3, 5),
        "why_beginner": "太大太散，第一次不建議當主選。",
        "why_powder": "本州雪質前段，4 月仍能滑。",
        "why_tokyo": "長野再轉，比湯澤煩。",
        "why_family": "除非住對親子區，否則不優先。",
        "why_onsen": "有，但不是野澤那種外湯村。",
        "why_budget": "偏高。",
        "why_coach": "有中文，密度中等。",
        "compare_with": ["happo-one", "nozawa", "kagura"],
        "experts": {
            "consensus": ["日本最大滑雪區域，要待好幾天。", "雪質是本州賣點。", "第一次請先去更單純的場。"],
            "disagreement": None,
            "sources": [
                {"name": "娜塔蝦的滑雪食旅手記", "url": "https://natasha-traveler.tw/shiga-kogen/", "kind": "blogger"},
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-all-ski-resort/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("shigakogen", "標高高，本州少見的雪質，4 月仍能滑。", "標高が高く、本州では群を抜いた雪質。4月でも十分な雪質を楽しめる。", "snow"),
            jp("shigakogen", "很冷，夜滑不友善。", "寒い。ナイターにはあまり向かない。", "pitfall"),
            jp("shigakogen", "可以一路換區滑，這是樂趣。", "いろんなエリアをツアーで楽しめるのがいい。", "beginner"),
        ],
        "links": [L("志賀高原滑雪攻略：日本最大滑雪區域", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/shiga-kogen/", "overview")],
    })
    rows.append({
        "id": "karuizawa", "name": "輕井澤王子", "romaji": "Karuizawa Prince", "prefecture": "長野県 北佐久郡輕井澤町",
        "region": "nagano", "cluster": None,
        "one_liner": "東京側最省事的入門場。人工雪、晴天多、outlet 在旁邊。不要期待粉雪。",
        "not_for": "要粉雪、要大垂直落差、或中高級想找地形的人。",
        "tags": ["新手友善", "親子友善", "新幹線近"],
        "access_routes": [{"from": "桃園 → 羽田／成田", "steps": "東京 → 北陸新幹線輕井澤約 70 分 → 步行／接駁 10 分", "hours": "含機場到東京約 4.5–6 小時；東京出發約 1.5 小時"}],
        "budget_twd": {"min": 35000, "max": 62000, "days": "5 天 4 夜", "note": "王子飯店不便宜；當日來回可壓成本。"},
        "season_note": "人工造雪為主，例年 11 月就能開，晴天率高。",
        "night_ski": "無", "onsen": "少", "chinese_coach": "多", "ski_in_out": "部分",
        "chinese_service": "王子體系服務好，中文教練有。Outlet 讓不滑雪的人很好打發。",
        "snow_rhythm": "人工雪，狀態穩、不是粉。連假會嚴重排隊。",
        "pitfalls": ["連假租借加買票加纜車能排爆。", "幾乎沒有上級道。", "住宿若選王子，總額會接近北海道。"],
        "companion_note": "輕井澤王子 Outlet 是不滑雪的人的天堂。這點成立。",
        "season_delta": None,
        "scores": sc(5, 1, 5, 1, 3, 5, 2, 4, 5, 1),
        "why_beginner": "綠線為主、服務好、交通近，第一次體驗滑雪很適合。",
        "why_powder": "沒有粉雪，別來。",
        "why_tokyo": "比 GALA 更近東京，當日首選之一。",
        "why_family": "授乳室、兒童休息區、outlet，親子非常完整。",
        "why_onsen": "弱，賣點是 outlet 不是湯。",
        "why_budget": "當日來回還好；住王子就不省。",
        "why_coach": "中文教練有，服務態度常被誇。",
        "compare_with": ["gala-yuzawa", "naeba", "tsugaike"],
        "experts": {
            "consensus": ["台灣搜尋量極高的入門場。", "交通與親子設施是優點。", "雪場規模小，進階者一天就膩。"],
            "disagreement": "有人覺得比 GALA 更適合當日；有人覺得人工雪沒靈魂，寧可多走 20 分去湯澤。",
            "sources": [
                {"name": "滑雪太空人", "url": "https://www.yuriselfmedia.tw/japan-ski-beginner/", "kind": "blogger"},
                {"name": "The Japow Project", "url": "https://japowproject.com/zh-tw/guides/japan-ski-trip-planning-guide/", "kind": "blogger"},
            ],
        },
        "community": [
            jp("karuizawa", "初級者與家庭向，上級道幾乎沒有。", "初級者におすすめ。上級者、中級者用コースはほとんどなく、ファミリー向け。", "beginner"),
            jp("karuizawa", "晴天多，人工雪比想像中能滑。", "晴天率が高い。人工雪のわりには雪質が良い。", "snow"),
            jp("karuizawa", "連假買票加租借能各排一小時。", "3連休はリフト券を買うのに1時間、レンタルを借りるのに1時間。", "pitfall"),
        ],
        "links": [
            L("14 個新手滑雪場（含輕井澤）", "滑雪太空人", "https://www.yuriselfmedia.tw/japan-ski-beginner/", "overview"),
            L("苗場、輕井澤、GALA 怎麼選", "林氏璧", "https://linshibi.com/?p=16980", "overview"),
        ],
    })
    return rows

for r in niigata_nagano():
    add(r)

# Non-high-search invented quotes: keep only verified tabiris pages.
DATA["resorts"]["teine"]["community"] = []
DATA["resorts"]["kagura"]["community"] = []
DATA["resorts"]["myoko"]["community"] = []
DATA["resorts"]["maiko"]["community"] = []
DATA["resorts"]["sahoro"]["community"] = [
    {
        "quote": "天候不穩的時期，Sahoro 晴天率相對高。",
        "original": "天候の荒れやすい時期ならサホロが好天率が高くていいでしょう。",
        "source": "スキー・スノボ研究所",
        "source_kind": "jp_review",
        "url": "https://snow.tabiris.com/hokkaido.html",
        "date": "2026-02",
        "theme": "snow",
    }
]

HEAD = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="zh_TW">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗺️</text></svg>">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Noto+Sans+TC:wght@400;500;700;900&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{css}">
</head>
<body data-depth="{depth}">
<div id="site-header"></div>
{main}
<div id="site-footer"></div>
<script src="{data}"></script>
<script src="{app}"></script>
<script>{boot}</script>
</body>
</html>
"""

ORIGIN = "https://japanski.djhousetw.com"

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) if os.path.dirname(path) else ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def page(title, desc, canonical, depth, boot, main_html):
    prefix = "../" if depth == 1 else ""
    return HEAD.format(
        title=title, desc=desc, canonical=canonical, css=prefix + "app.css",
        data=prefix + "data.js", app=prefix + "app.js", depth=depth, boot=boot, main=main_html,
    )

def main():
    with open(os.path.join(ROOT, "data.js"), "w", encoding="utf-8") as f:
        f.write("var DATA = ")
        f.write(json.dumps(DATA, ensure_ascii=False, indent=2))
        f.write(";\n")

    ids = list(DATA["resorts"].keys())
    assert len(ids) == 24, ids

    for rid, r in DATA["resorts"].items():
        title = "%s %s｜雪國轉運站" % (r["name"], r["romaji"])
        desc = r["one_liner"]
        html = page(
            title, desc, ORIGIN + "/resorts/%s.html" % rid, 1,
            "Hub.renderResort(%s);" % json.dumps(rid),
            '<main class="page" id="page"><h1 class="page-title">%s</h1><p>%s</p><p class="muted">不適合誰：%s</p></main>' % (
                r["name"], r["one_liner"], r["not_for"]
            ),
        )
        write("resorts/%s.html" % rid, html)

    for aid, a in DATA["areas"].items():
        title = "%s｜雪國轉運站" % a["name"]
        html = page(
            title, a["one_liner"], ORIGIN + "/areas/%s.html" % aid, 1,
            "Hub.renderArea(%s);" % json.dumps(aid),
            '<main class="page" id="page"></main>',
        )
        write("areas/%s.html" % aid, html)

    write("compare.html", page(
        "二世谷、留壽都、富良野怎麼選｜雪國轉運站",
        "北海道三選、東京側短待、長野三選。給台灣人的日本滑雪對照。",
        ORIGIN + "/compare.html", 0, "Hub.renderCompare();",
        '<main class="page page-wide" id="page"></main>',
    ))

    urls = [
        ORIGIN + "/",
        ORIGIN + "/go",
        ORIGIN + "/compare.html",
        ORIGIN + "/guide/first-trip.html",
        ORIGIN + "/areas/yuzawa.html",
        ORIGIN + "/areas/hakuba-valley.html",
    ] + [ORIGIN + "/resorts/%s.html" % i for i in ids]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append("  <url><loc>%s</loc></url>" % u)
    sm.append("</urlset>\n")
    write("sitemap.xml", "\n".join(sm))
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % ORIGIN)
    print("resorts", len(ids))
    print("high-search community", sum(1 for i in ["niseko","rusutsu","furano","kiroro","tomamu","gala-yuzawa","naeba","ishiuchi","karuizawa","happo-one","tsugaike","nozawa","shiga-kogen","zao","appi"] if len(DATA["resorts"][i].get("community") or []) >= 2))

if __name__ == "__main__":
    main()




