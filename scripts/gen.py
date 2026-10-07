# -*- coding: utf-8 -*-
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import longtail

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
        "hokkaido": {"name": "北海道", "en": "Hokkaido", "img": "img/region-hokkaido.jpg", "sub": "粉雪 · 7 個雪場", "desc": "全日本粉雪指標，從台灣直飛新千歲最順。", "resortIds": ["niseko", "rusutsu", "furano", "kiroro", "tomamu", "teine", "sahoro"]},
        "tohoku": {"name": "東北", "en": "Tohoku", "img": "img/region-tohoku.jpg", "sub": "樹冰 · 3 個雪場", "desc": "人較少、雪季長，樹冰與度假村型雪場。", "resortIds": ["zao", "appi", "bandai"]},
        "niigata": {"name": "新潟／越後", "en": "Niigata", "img": "img/region-niigata.jpg", "sub": "新幹線 · 8 個雪場", "desc": "東京最近的雪國。越後湯澤是樞紐，不是一座場。", "resortIds": ["gala-yuzawa", "ishiuchi", "yuzawa-kogen", "naeba", "kagura", "joetsu-kokusai", "myoko", "maiko"]},
        "nagano": {"name": "長野／北信", "en": "Nagano", "img": "img/region-nagano.jpg", "sub": "冬奧 · 6 個雪場", "desc": "白馬谷要先選山。輕井澤歸長野，適合東京當日。", "resortIds": ["happo-one", "tsugaike", "hakuba-goryu", "nozawa", "shiga-kogen", "karuizawa"]},
    },
    # 首頁「本週雪國」跑馬燈。排程 Agent 每週寫入，格式：
    # {"date": "YYYY-MM-DD", "resort_id": "gala-yuzawa", "text": "早鳥票開賣", "url": "https://..."}
    # 超過 60 天的項目由首頁自動忽略；空的時候首頁改顯示各場 season_delta。
    "news": [],
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
        L("二世谷滑雪全攻略 2026-27：雪場、交通、住宿", "SSW Board House", "https://sswboardhouse.com/niseko-ski-resort-guide-zh/", "overview"),
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
            L("RISONARE Tomamu 飯店開箱：北館樓下就是雪具租借與雪場出口", "娜塔蝦的滑雪食旅手記", "https://natasha-traveler.tw/risonare-tomamu/", "hotel"),
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
        "season_delta": "2026–27 預定 12/19 開季，南區停止營業；早割券 10/15 線上開賣。",
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
        "season_delta": "2026–27 官方公布 11/21 開季，預定營業到 5/6。",
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
        "season_delta": "2026–27 官網票價表營業期間 12/19–3/28，一日券 ¥7,800。",
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
        "pitfalls": ["18 區個性差很大，一頁講不完。", "交通與動線不直覺。", "餐飲評價兩極，偏貴。"],
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

# /go 第五題「幾月去」：early=11 月～12 月中、peak=12 月下旬～2 月、spring=3 月～閉季，各 1–5。
# 只依站內既有事實給分（season_note、SEASON 開閉季日、scores.powder、pitfalls）。
DATA["resorts"]["niseko"]["month_fit"] = {"early": 3, "peak": 5, "spring": 3}  # 11/28 開、5/5 關；粉雪 1–2 月最穩，3 月後變少
DATA["resorts"]["rusutsu"]["month_fit"] = {"early": 2, "peak": 5, "spring": 2}  # 標高較低，12 月初與 3 月下旬雪質打折，3/31 就關
DATA["resorts"]["furano"]["month_fit"] = {"early": 3, "peak": 5, "spring": 3}  # 11/28 開、5/5 關，乾粉雪旺季最好
DATA["resorts"]["kiroro"]["month_fit"] = {"early": 4, "peak": 5, "spring": 4}  # 季初季末雪量是北海道最強帶之一，11/28–5/5
DATA["resorts"]["tomamu"]["month_fit"] = {"early": 2, "peak": 4, "spring": 2}  # 12/1 才開、4/5 關
DATA["resorts"]["teine"]["month_fit"] = {"early": 4, "peak": 4, "spring": 2}  # 11/21 開，北海道最早一批；閉季未公布
DATA["resorts"]["sahoro"]["month_fit"] = {"early": 2, "peak": 4, "spring": 1}  # 12/1–3/31，春季最早關
DATA["resorts"]["zao"]["month_fit"] = {"early": 1, "peak": 5, "spring": 3}  # 12/12 才開；樹冰只在 1–2 月
DATA["resorts"]["appi"]["month_fit"] = {"early": 2, "peak": 4, "spring": 4}  # 例年 12 月開；北斜面，春滑可到很晚
DATA["resorts"]["bandai"]["month_fit"] = {"early": 3, "peak": 3, "spring": 4}  # 貓魔 11/28 開、5/9 關，季長
DATA["resorts"]["gala-yuzawa"]["month_fit"] = {"early": 1, "peak": 4, "spring": 3}  # 例年 12 月下旬才開、5 月初關
DATA["resorts"]["ishiuchi"]["month_fit"] = {"early": 1, "peak": 4, "spring": 2}  # 12/18–4/4
DATA["resorts"]["yuzawa-kogen"]["month_fit"] = {"early": 1, "peak": 3, "spring": 2}  # 12/18–4/4，雪質普通
DATA["resorts"]["naeba"]["month_fit"] = {"early": 1, "peak": 4, "spring": 2}  # 12/18–4/4
DATA["resorts"]["kagura"]["month_fit"] = {"early": 4, "peak": 4, "spring": 5}  # 11/28 開、5/16 關，本州最晚關之一
DATA["resorts"]["joetsu-kokusai"]["month_fit"] = {"early": 1, "peak": 4, "spring": 2}  # 12/12–4/4
DATA["resorts"]["myoko"]["month_fit"] = {"early": 1, "peak": 5, "spring": 3}  # 12/19 才開；雪量本州前段，5/5 關
DATA["resorts"]["maiko"]["month_fit"] = {"early": 1, "peak": 4, "spring": 1}  # 12/19–3/28，春季最早關
DATA["resorts"]["happo-one"]["month_fit"] = {"early": 2, "peak": 5, "spring": 4}  # 例年 12 月上旬開、5/5 關，旺季地形最好
DATA["resorts"]["tsugaike"]["month_fit"] = {"early": 3, "peak": 4, "spring": 4}  # 白馬谷季初較早開的之一，5/5 關
DATA["resorts"]["hakuba-goryu"]["month_fit"] = {"early": 2, "peak": 4, "spring": 3}  # 例年 12 月上旬開、5/6 關
DATA["resorts"]["nozawa"]["month_fit"] = {"early": 3, "peak": 5, "spring": 3}  # 例年 11 月底開、天然雪季長
DATA["resorts"]["shiga-kogen"]["month_fit"] = {"early": 2, "peak": 5, "spring": 5}  # 12/5 開；標高高，4 月仍常有好雪，5/5 關
DATA["resorts"]["karuizawa"]["month_fit"] = {"early": 5, "peak": 3, "spring": 2}  # 10/31 開，人造雪為主；旺季人多、春雪弱

# 「接下來這三步」：/go 結果卡與雪場頁共用。只整理站內既有事實；不寫價格、不放訂房網站。
# url 只准雪場官網或白名單網域（main() 會檢查）；沒有就 None。
DATA["resorts"]["niseko"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，再搭接駁巴士或包車 2.5–3 小時。當天下午才滑得到，至少排 4 天。", "url": None},
    "stay": {"title": "住哪一區", "text": "四大場住宿遠近差很大，選邊決定每天累不累；第一次多住比羅夫（Hirafu）村，餐廳與酒吧集中。旺季要早訂。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文教練有但不是主力，英文課比中文好約。", "url": None},
}
DATA["resorts"]["rusutsu"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，度假村接駁或巴士 1.5–2 小時。", "url": None},
    "stay": {"title": "住哪一區", "text": "住度假村內最省腦，設施與室內遊樂都在裡面；想逛村子、找獨立餐廳的人會覺得悶。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "有官方合作的中文雪校駐點，比多數本州場好約。", "url": None},
}
DATA["resorts"]["furano"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛旭川最順，巴士約 1 小時；別買新千歲出發的套票，會多花 2–3 小時。", "url": None},
    "stay": {"title": "住哪一區", "text": "富良野區與北之峰幾乎是兩座場，先決定滑哪邊再訂房，否則天天接駁。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "有中文課，密度不如湯澤；王子飯店體系相對好溝通。", "url": None},
}
DATA["resorts"]["kiroro"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，巴士經小樽或札幌 2–2.5 小時。", "url": None},
    "stay": {"title": "住哪一區", "text": "雪場內住宿為主；自己住晚上選擇有限，Club Med 全包對不滑雪的人最友善。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "Club Med 中文服務較完整；自己約課以日英為主。", "url": None},
}
DATA["resorts"]["tomamu"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，滑雪巴士約 2 小時，或搭 JR 到 Tomamu 站。", "url": None},
    "stay": {"title": "住哪一區", "text": "住星野度假村內，冰雪村、餐廳街、溫泉都在，不滑雪的人也能排滿。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "星野體系有中文教練駐點，標示清楚。", "url": None},
}
DATA["resorts"]["teine"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，先進札幌市區，再搭手稻滑雪巴士 40–50 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住札幌市區當日往返，晚上吃喝都在市區，比住雪場方便。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "官網有中文，中文教練有駐點；新手留在奧林匹亞區上課。", "url": None},
}
DATA["resorts"]["sahoro"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "桃園直飛新千歲，巴士往十勝約 2.5–3 小時；自由行交通是門檻。", "url": None},
    "stay": {"title": "住哪一區", "text": "幾乎都是 Club Med 全包，住宿、餐、課一起訂。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "Club Med 中文服務完整，課程通常包在套裝裡。", "url": None},
}
DATA["resorts"]["zao"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京（羽田／成田），山形新幹線約 2.5 小時再轉巴士 40 分；別當東京當日場。", "url": None},
    "stay": {"title": "住哪一區", "text": "住藏王溫泉街，滑完泡湯；纜車公司多家，選離你要滑那區近的旅館。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文教練比湯澤少，溫泉街以日文為主，出發前先約好。", "url": None},
}
DATA["resorts"]["appi"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，東北新幹線到盛岡約 2 小時 20 分，再轉巴士 50 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住安比度假村內飯店，Ski-in/out 最省事。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文比湯澤少，度假村內英文尚可。", "url": None},
}
DATA["resorts"]["bandai"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，東北新幹線到郡山或會津若松再轉巴士；不是東京當日場。", "url": None},
    "stay": {"title": "住哪一區", "text": "貓魔區與磐梯區不是無腦相連，先確定要滑哪區再選星野的住宿。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "星野標示清楚，中文比純東北鄉鎮場好一點。", "url": None},
}
DATA["resorts"]["gala-yuzawa"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，東京站搭上越新幹線約 75 分，GALA湯澤站下車就是雪場。", "url": None},
    "stay": {"title": "住哪一區", "text": "可以住東京當日來回省住宿；想住就住越後湯澤溫泉街，走路到車站。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文教練與台灣店密度是本州最高帶；週末先在手機完成租借。", "url": None},
}
DATA["resorts"]["ishiuchi"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤站，再接駁 10–20 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住越後湯澤站周邊或石打山腳；和 GALA 相通，可以兩邊輪流滑。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "湯澤圈中文教練好找；綠線比例不高，第一次上課前先看地圖。", "url": None},
}
DATA["resorts"]["yuzawa-kogen"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤站，走路或短程到纜車站。", "url": None},
    "stay": {"title": "住哪一區", "text": "住越後湯澤溫泉街最方便，三山共通券可以逃去石打。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "湯澤町內台灣店多，中文教練好找。", "url": None},
}
DATA["resorts"]["naeba"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤，再搭巴士 40–60 分到苗場王子；當日來回不划算。", "url": None},
    "stay": {"title": "住哪一區", "text": "住苗場王子飯店最省事，出門就是雪場。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文教練非常多，台灣人密度高，第一次很常被推來這裡上課。", "url": None},
}
DATA["resorts"]["kagura"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤，再搭巴士到神樂／田代／三俣；三個入口名稱很混，先確認哪一個。", "url": None},
    "stay": {"title": "住哪一區", "text": "多數人住苗場王子或越後湯澤，經龍纜車進場；票種要買對。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文教練比苗場少，進階客較多；新手不建議把神樂當第一堂。", "url": None},
}
DATA["resorts"]["joetsu-kokusai"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤，再短程接駁或轉上越線。", "url": None},
    "stay": {"title": "住哪一區", "text": "住度假村內飯店，Ski-in/out 加夜滑，預算比苗場好控。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "湯澤圈，中文可；台灣教練會拿來當過夜練習場。", "url": None},
}
DATA["resorts"]["myoko"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到上越妙高約 100 分，再轉冬季巴士；先搞清楚上越妙高站和妙高高原站。", "url": None},
    "stay": {"title": "住哪一區", "text": "子場分散，先決定主要滑哪一場再訂附近的溫泉旅館，否則天天坐巴士。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文少於湯澤；出發前先確認授課語言。", "url": None},
}
DATA["resorts"]["maiko"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，新幹線到越後湯澤，再接駁約 20 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住雪場內的 Ski-in/out 飯店最省事；奧添區紅黑為主，住哪都別讓新手跟上去。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "台灣團變多，中文比以前好找。", "url": None},
}
DATA["resorts"]["happo-one"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到長野 80–90 分，再搭巴士約 70 分到白馬。", "url": None},
    "stay": {"title": "住哪一區", "text": "住白馬村八方一帶，餐廳多；新手同行就讓他們待咲花區或去栂池。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "國際化，中英文教練都有；但課程常假設你已會滑。", "url": None},
}
DATA["resorts"]["tsugaike"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到長野，再搭巴士約 90 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住栂池高原，不要住八方再跨過來，交通會耗掉一大段時間。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "白馬谷中文教練好找；初中級道佔約八成，適合第一次上課。", "url": None},
}
DATA["resorts"]["hakuba-goryu"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到長野，再搭巴士到白馬五龍。", "url": None},
    "stay": {"title": "住哪一區", "text": "住五龍區，和八方、栂池不是走得到的距離。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "白馬谷中文教練多；第一次仍偏硬，先上課再自己滑。", "url": None},
}
DATA["resorts"]["nozawa"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到飯山約 100 分，再搭巴士 25–30 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "住野澤溫泉村，外湯、老街、吃都在走路範圍；要過夜才值得來。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "外國人多、英文不錯，中文中等，出發前先約。", "url": None},
}
DATA["resorts"]["shiga-kogen"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到長野，再搭巴士 70–80 分，或到湯田中再轉。", "url": None},
    "stay": {"title": "住哪一區", "text": "18 區個性差很大，先決定主要滑哪幾區，再住那一區的飯店。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "中文少於白馬和湯澤；第一次請先去更單純的場。", "url": None},
}
DATA["resorts"]["karuizawa"]["next_steps"] = {
    "fly": {"title": "飛哪個機場", "text": "飛東京，北陸新幹線到輕井澤約 70 分，下車步行或接駁 10 分。", "url": None},
    "stay": {"title": "住哪一區", "text": "可以住東京當日來回；住王子飯店省事但總額會接近北海道。", "url": None},
    "learn": {"title": "教練怎麼約", "text": "王子體系服務好，中文教練有；連假先線上買票與租借。", "url": None},
}

# vs 比較頁的一句話差異。只產生「互相列為比較對象」且有 note 的組合；key = longtail.vs_slug(a, b)。
DATA["vs_notes"] = {
    "appi-vs-zao": "要長雪道和細粉雪選安比；要看樹冰、泡溫泉街選藏王。兩座都要從東京搭新幹線再轉車。",
    "furano-vs-niseko": "想要人少、乾雪、預算好控選富良野；要四場相連、國際村和夜生活選二世谷。",
    "furano-vs-rusutsu": "中級以上想要地形選富良野；帶小孩、第一次北海道、想住在度假村裡選留壽都。",
    "gala-yuzawa-vs-ishiuchi": "完全沒滑過、只滑一天選 GALA；已經會一點、嫌 GALA 擠，走到隔壁石打，道更寬。",
    "gala-yuzawa-vs-karuizawa": "要中文教練和真雪選 GALA；帶不滑雪的家人、想順便逛 outlet 選輕井澤。兩座都能東京當日來回。",
    "gala-yuzawa-vs-naeba": "只滑一天、東京當日來回選 GALA；要過夜、上課、夜滑選苗場，住苗場王子出門就是雪場。",
    "hakuba-goryu-vs-happo-one": "已會滑、想要公園和夜滑選五龍；想挑戰本州最硬的地形選八方。兩座都不適合第一天。",
    "hakuba-goryu-vs-tsugaike": "第一次來白馬選栂池；已會滑、想要多一點變化選五龍。兩座住宿不要混著選。",
    "happo-one-vs-kagura": "要冬奧地形與白馬村選八方；要粉雪、春雪、從東京比較近選神樂。新手兩座都別當第一座山。",
    "happo-one-vs-tsugaike": "第一次來白馬選栂池，寬綠線多；八方留給已經會滑的人。住宿要跟著選，不要住八方再跨去栂池。",
    "ishiuchi-vs-yuzawa-kogen": "第一次選湯澤高原，從溫泉街直接上纜車；已經會滑、要大場和寬道選石打。三山共通券可以兩邊滑。",
    "joetsu-kokusai-vs-maiko": "要 Ski-in/out 加夜滑、預算好控選上越國際；新手到進階都要照顧到選舞子，但新手別跟去奧添區。",
    "kagura-vs-naeba": "第一次、要中文課選苗場；已會滑、要粉雪和春雪選神樂。兩座用龍纜車連，票要買對。",
    "kagura-vs-shiga-kogen": "從東京近、要粉雪與春雪選神樂；要待好幾天、滑遍日本最大雪區選志賀。兩座都不適合第一次。",
    "kiroro-vs-niseko": "要雪量、季初季末也穩、Club Med 全包選 Kiroro；要國際村、夜生活、四場相連選二世谷。",
    "naeba-vs-tsugaike": "從東京走得快、中文課最多選苗場；想去白馬又是第一次，選栂池。",
    "niseko-vs-rusutsu": "粉雪同級。要村子、夜生活、預算充足選二世谷；帶小孩、第一次北海道、想省腦選留壽都。",
    "nozawa-vs-shiga-kogen": "要溫泉街、外湯和帶不滑雪的人選野澤；要雪區夠大、滑好幾天不重複選志賀。",
    "nozawa-vs-zao": "兩座都是溫泉加雪場。從東京交通較順、村子好逛選野澤；要看樹冰選藏王，1–2 月才有。",
    "rusutsu-vs-tomamu": "兩座都是親子友善的度假村。場大、地形多選留壽都；不滑雪的人多、要冰雪村活動選 Tomamu。",
    "sahoro-vs-tomamu": "想要 Club Med 全包、晴天率高選 Sahoro；要自由行好到、設施多選 Tomamu。",
}

# 雪場代表圖：站長決定（2026-09-30）全站使用電腦繪製示意圖，不下載官方照片。
# 之後若要每座場一張專屬示意圖，放在 img/resort-<id>.jpg 並填 hero_img；hero_credit 保持 None。
for _rid in DATA["resorts"]:
    DATA["resorts"][_rid].setdefault("hero_img", None)
    DATA["resorts"][_rid].setdefault("hero_credit", None)

# 中文雪校總表（/schools.html）。只收官網明寫有中文授課的學校；不寫價格。
# url／source／updated 必填；resort_ids 只能是 24 座；note ≤40 字、只寫事實。
DATA["schools"] = [
    {"id": "snow-and-flow", "name": "Snow and Flow（雪浪）", "resort_ids": ["niseko", "rusutsu", "kiroro", "teine"], "url": "https://www.snowandflow.com/", "booking_url": "https://snowandflow.bookfast.jp/public/booking/order02.jsf?vid=2c98902a63f906290163fc3bc56f1143&i18n=en", "lang": ["zh", "en"], "kids_min_age": None, "lesson_types": ["private"], "note": "港台教練組成，以二世谷比羅夫為主", "source": "https://www.snowandflow.com/", "updated": "2026-09-30"},
    {"id": "chase-for-snow", "name": "Chase for Snow", "resort_ids": ["niseko", "rusutsu", "kiroro", "teine", "zao"], "url": "https://chaseforsnow.com/en/", "booking_url": "https://chase4snow.bookfast.jp/", "lang": ["zh", "en"], "kids_min_age": 4, "lesson_types": ["private", "group", "kids"], "note": "普通話、粵語授課；藏王本季改新制，請先確認開課", "source": "https://chaseforsnow.com/en/", "updated": "2026-09-30"},
    {"id": "pinnacle-snowsports", "name": "Pinnacle Snowsports", "resort_ids": ["niseko", "rusutsu", "kiroro"], "url": "https://pinnaclesnow.com/", "booking_url": "https://pinnaclesnow.com/private", "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private"], "note": "二世谷、留壽都、Kiroro 中文私人課", "source": "https://pinnaclesnow.com/private", "updated": "2026-09-30"},
    {"id": "snowplus", "name": "SnowPlus", "resort_ids": ["niseko", "rusutsu", "kiroro"], "url": "https://snowplus.school/", "booking_url": "https://book.snowplus.school/", "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "二世谷比羅夫、安努普利、花園，也教留壽都", "source": "https://snowplus.school/", "updated": "2026-09-30"},
    {"id": "jd-niseko", "name": "JD 二世谷中文滑雪學校", "resort_ids": ["niseko"], "url": "https://www.jdnisekosss.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": [], "note": "二世谷的中文滑雪學校", "source": "https://www.jdnisekosss.com/", "updated": "2026-09-30"},
    {"id": "niseko-supreme", "name": "Niseko Supreme", "resort_ids": ["niseko"], "url": "https://nisekosupreme.com/", "booking_url": None, "lang": ["en", "zh"], "kids_min_age": 3, "lesson_types": ["private", "kids"], "note": "以英文課為主，可另外安排中文", "source": "https://nisekosupreme.com/ski-lessons/", "updated": "2026-09-30"},
    {"id": "konayuki-rusutsu", "name": "Konayuki Chinese Ski School", "resort_ids": ["rusutsu"], "url": "https://rusutsu.com/en/konayukitendo-ski-lessons/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private"], "note": "留壽都官網列名的中文滑雪學校", "source": "https://rusutsu.com/en/konayukitendo-ski-lessons/", "updated": "2026-09-30"},
    {"id": "kiroro-international-academy", "name": "Kiroro International Ski & Snowboard Academy", "resort_ids": ["kiroro"], "url": "https://www.kiroro.co.jp/ski_international_lesson/", "booking_url": "https://webstore.kiroro.co.jp/EN/", "lang": ["en", "zh"], "kids_min_age": None, "lesson_types": ["private"], "note": "Kiroro 自營；私人課預約時註明要中文", "source": "https://www.kiroro.co.jp/ski_international_lesson/", "updated": "2026-09-30"},
    {"id": "snoway-academy", "name": "Snoway Academy", "resort_ids": ["kiroro", "rusutsu", "teine"], "url": "https://snoway.club/en/hokkaido-kiroro-ski-snowboard-lesson/", "booking_url": None, "lang": ["en", "zh"], "kids_min_age": None, "lesson_types": ["private", "kids"], "note": "英文、普通話、粵語授課", "source": "https://snoway.club/en/hokkaido-kiroro-ski-snowboard-lesson/", "updated": "2026-09-30"},
    {"id": "tomamu-academy", "name": "Tomamu 滑雪學院", "resort_ids": ["tomamu"], "url": "https://www.snowtomamu.jp/winter/cn/ski/lesson/", "booking_url": "https://www.alts-system.jp/tomamuacademy/book/?lang=zh_tw", "lang": ["zh", "en", "ja"], "kids_min_age": 4, "lesson_types": ["private", "group", "kids"], "note": "星野 Tomamu 自營；中文只開雙板私人課", "source": "https://www.snowtomamu.jp/winter/cn/ski/lesson/", "updated": "2026-09-30"},
    {"id": "visnow", "name": "Visnow Ski School", "resort_ids": ["tomamu", "teine", "kiroro", "rusutsu"], "url": "https://www.visnow.jp/", "booking_url": None, "lang": ["zh", "en"], "kids_min_age": None, "lesson_types": ["private", "kids"], "note": "星野 Tomamu 認可的中文滑雪學校", "source": "https://www.visnow.jp/tomamu-ski-snowboard", "updated": "2026-09-30"},
    {"id": "snowmaps-hokkaido", "name": "SnowMAPS Hokkaido", "resort_ids": ["tomamu", "teine"], "url": "https://www.snowmapshokkaido.com/", "booking_url": None, "lang": ["zh", "en", "ja"], "kids_min_age": None, "lesson_types": ["private"], "note": "公司在富良野北之峰，也教 Tomamu、手稻", "source": "https://www.snowmapshokkaido.com/", "updated": "2026-09-30"},
    {"id": "snowi", "name": "Snowi 白龍滑雪學校", "resort_ids": ["tomamu", "furano", "sahoro", "teine", "kiroro", "rusutsu"], "url": "https://snowisnow.com/", "booking_url": None, "lang": ["zh", "en", "ja"], "kids_min_age": None, "lesson_types": ["private", "kids"], "note": "北海道多場授課，創辦人與多數教練中文授課", "source": "https://snowisnow.com/", "updated": "2026-09-30"},
    {"id": "snowland", "name": "SnowLand 滑雪學校", "resort_ids": ["tomamu", "rusutsu", "teine"], "url": "https://land110602.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "kids"], "note": "Tomamu、留壽都、手稻中文課", "source": "https://land110602.com/", "updated": "2026-09-30"},
    {"id": "pure-ski", "name": "PURE SKI 滑雪純愛組", "resort_ids": ["tomamu", "teine", "rusutsu"], "url": "https://www.pureski-school.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "group"], "note": "團體課只在手稻開班", "source": "https://www.pureski-school.com/tomamu/", "updated": "2026-09-30"},
    {"id": "jstyle-ski", "name": "Jstyle Ski 中文滑雪學校", "resort_ids": ["tomamu", "rusutsu"], "url": "https://www.jstyleski.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": [], "note": "北海道中文教練預約平台", "source": "https://www.jstyleski.com/", "updated": "2026-09-30"},
    {"id": "krt-snow-school", "name": "KRT 中文滑雪學校", "resort_ids": ["furano", "naeba"], "url": "https://www.krtsnowschool.com/", "booking_url": "https://lin.ee/tWJ8XJm", "lang": ["zh"], "kids_min_age": 7, "lesson_types": ["private", "group"], "note": "苗場、新富良野的王子飯店櫃台報到", "source": "https://www.krtsnowschool.com/en/furano", "updated": "2026-09-30"},
    {"id": "pandaruman-furano", "name": "PANDARUMAN Kids Ski School", "resort_ids": ["furano"], "url": "https://www.pandarumankidsschool.com/en/furano", "booking_url": "https://www.pandarumankidsschool.com/en/furano-panda", "lang": ["en", "zh", "ja"], "kids_min_age": 3, "lesson_types": ["kids"], "note": "新富良野王子飯店的兒童雙板學校，3–6 歲", "source": "https://www.pandarumankidsschool.com/en/furano", "updated": "2026-09-30"},
    {"id": "prince-chinese-ski-school", "name": "王子中文滑雪學校", "resort_ids": ["furano", "naeba", "kagura", "karuizawa", "myoko"], "url": "https://www.princeskischool.com/", "booking_url": "http://jp.mikecrm.com/UBh60Hw", "lang": ["zh", "ja", "en"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "王子飯店集團認證的中文學校，苗場、神樂、輕井澤、妙高、富良野", "source": "https://www.princeskischool.com/", "updated": "2026-09-30"},
    {"id": "teine-chinese-ski-school", "name": "手稻中文滑雪學校", "resort_ids": ["teine"], "url": "https://www.teineskischool.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": [], "note": "札幌手稻官網列名的中文學校", "source": "https://www.teineskischool.com/", "updated": "2026-09-30"},
    {"id": "iski", "name": "iSKI 滑雪學校", "resort_ids": ["teine", "rusutsu", "ishiuchi", "kagura", "gala-yuzawa", "naeba"], "url": "https://www.iski.com.tw/ski-school", "booking_url": "https://www.iski.com.tw/index.php?route=product/snowing_product&trail_class_id=102", "lang": ["zh"], "kids_min_age": 3, "lesson_types": ["private", "group", "kids"], "note": "台灣業者；湯澤圈以石打為主，北海道在手稻、留壽都", "source": "https://www.iski.com.tw/ski-school", "updated": "2026-09-30"},
    {"id": "snowlife", "name": "雪道 SnowLife", "resort_ids": ["rusutsu", "teine"], "url": "https://www.hokkaidosnowlife.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private"], "note": "北海道中文私人課", "source": "https://www.hokkaidosnowlife.com/", "updated": "2026-09-30"},
    {"id": "appi-ski-snowboard-school", "name": "Appi Ski & Snowboard School", "resort_ids": ["appi"], "url": "https://www.appi-ski-and-snowboard-school.com/", "booking_url": "https://www.appi-ski-and-snowboard-school.com/book-now", "lang": ["zh", "en", "ja"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "安比高原的滑雪學校；中文師資有限，請提早預約", "source": "https://www.appi-ski-and-snowboard-school.com/home-ch", "updated": "2026-09-30"},
    {"id": "sora-nekoma", "name": "SORA International Ski & Snowboard School", "resort_ids": ["bandai"], "url": "https://sorasnow.com/", "booking_url": "https://sorasnow.com/pages/book-now", "lang": ["zh", "en"], "kids_min_age": None, "lesson_types": ["private"], "note": "貓魔山的國際滑雪學校，雪場官網列為中英文授課", "source": "https://www.nekoma.co.jp/special-program/", "updated": "2026-09-30"},
    {"id": "snow-star", "name": "雪星球滑雪學校 SNOW STAR", "resort_ids": ["zao", "teine"], "url": "https://snowstar.com.tw/", "booking_url": None, "lang": ["zh"], "kids_min_age": 5, "lesson_types": ["private", "group"], "note": "台灣團隊，全中文教學；5–8 歲只收一對一", "source": "https://snowstar.com.tw/", "updated": "2026-09-30"},
    {"id": "outdoorland", "name": "凹豆郎 Outdoorland", "resort_ids": ["zao"], "url": "https://outdoorland.club/", "booking_url": "https://outdoorland.club/products/ski-snowboard-lesson-zao", "lang": ["zh"], "kids_min_age": 3, "lesson_types": ["private"], "note": "藏王中文課，3 或 5 小時，雙板單板都有", "source": "https://outdoorland.club/products/ski-snowboard-lesson-zao", "updated": "2026-09-30"},
    {"id": "naeba-ski-school", "name": "Naeba Ski School", "resort_ids": ["naeba"], "url": "https://zh.naebass.jp/", "booking_url": "https://reserva.be/naebaskischool", "lang": ["zh", "en", "ja"], "kids_min_age": 3, "lesson_types": ["private", "group", "kids"], "note": "苗場在地雪校；雙板 3 歲起、單板 6 歲起", "source": "https://zh.naebass.jp/", "updated": "2026-09-30"},
    {"id": "sherpa-naeba", "name": "Sherpa International Snow School Naeba", "resort_ids": ["naeba"], "url": "https://sherpasnow.com/", "booking_url": "https://www.trunktools.jp/_app/sherpasnow/#!/en", "lang": ["zh", "en"], "kids_min_age": None, "lesson_types": ["private"], "note": "苗場，雙板與單板私人課", "source": "https://sherpasnow.com/", "updated": "2026-09-30"},
    {"id": "kagura-ski-school", "name": "かぐらスキースクール", "resort_ids": ["kagura"], "url": "https://www.kagura-ss.jp/chinese_hantai/", "booking_url": None, "lang": ["zh", "ja"], "kids_min_age": 6, "lesson_types": ["private"], "note": "神樂三俣滑雪中心 2 樓；中文教練需事先預約", "source": "https://www.kagura-ss.jp/chinese_hantai/", "updated": "2026-09-30"},
    {"id": "canyons", "name": "Canyons Snow Sports School", "resort_ids": ["gala-yuzawa", "kagura", "naeba", "ishiuchi"], "url": "https://canyons.jp/en/winter-tours/chinese-ski-school", "booking_url": "https://canyons.active-manager.io/customers/book-now/start?area=3&location=4", "lang": ["zh", "en"], "kids_min_age": 4, "lesson_types": ["private"], "note": "GALA湯澤的國際雪校；也在神樂、苗場、石打開課", "source": "https://canyons.jp/en/winter-tours/gala-yuzawa-snow-resort/", "updated": "2026-09-30"},
    {"id": "giant-ski-school", "name": "巨人中文滑雪學校", "resort_ids": ["gala-yuzawa"], "url": "https://www.giantskischool.com/", "booking_url": "http://jp.mikecrm.com/3Tz7hh1", "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "GALA湯澤官網列名的中文學校", "source": "https://gala.co.jp/en/winter/school/", "updated": "2026-09-30"},
    {"id": "snow-country-instructors", "name": "雪國教練 Snow Country Instructors", "resort_ids": ["naeba", "gala-yuzawa", "ishiuchi", "joetsu-kokusai", "kagura", "maiko"], "url": "https://www.snowcountry-instructors.com/chn/", "booking_url": "https://www.snowcountry-instructors.com/chn/contact/#book", "lang": ["zh", "en", "ja"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "湯澤町據點，湯澤圈多場授課，國語或粵語", "source": "https://www.snowcountry-instructors.com/chn/", "updated": "2026-09-30"},
    {"id": "snowgame", "name": "SnowGame 雪遊中文滑雪學校", "resort_ids": ["kagura", "naeba", "ishiuchi", "maiko"], "url": "https://www.snowgame.school/", "booking_url": "https://booking.snowgame.school/", "lang": ["zh"], "kids_min_age": 4, "lesson_types": ["private", "kids"], "note": "越後湯澤，台灣教練；雙板 4 歲、單板 6 歲起", "source": "https://www.snowgame.school/", "updated": "2026-09-30"},
    {"id": "pod-snowsports", "name": "Pod Snowsports", "resort_ids": ["yuzawa-kogen", "naeba"], "url": "https://podsnowsports.com/", "booking_url": "https://podsnowsports.com/store/", "lang": ["zh", "en"], "kids_min_age": 4, "lesson_types": ["private", "group"], "note": "湯澤高原官網列名的英中文雪校，需事先預約", "source": "https://www.yuzawakogen.com/winter/school/", "updated": "2026-09-30"},
    {"id": "snowsenpai", "name": "Snow Senpai 雪長姐", "resort_ids": ["ishiuchi", "gala-yuzawa"], "url": "https://www.snowsenpai.com/", "booking_url": "https://www.snowsenpai.com/yuzawa/", "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "group"], "note": "越後湯澤多場授課，全程中文", "source": "https://www.snowsenpai.com/", "updated": "2026-09-30"},
    {"id": "crazy-snow", "name": "Crazy Snow 瘋雪滑雪學校", "resort_ids": ["gala-yuzawa", "kagura", "naeba", "ishiuchi"], "url": "https://tokyo.crazyforsnow.com/", "booking_url": None, "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private"], "note": "越後湯澤地區，GALA、神樂、苗場、石打等", "source": "https://tokyo.crazyforsnow.com/", "updated": "2026-09-30"},
    {"id": "snowfish-vic", "name": "維克養雪魚 Snowfish Vic", "resort_ids": ["ishiuchi", "maiko", "gala-yuzawa", "naeba", "kagura"], "url": "https://snowfish-vic.com/", "booking_url": "https://snowfish-vic.com/booking-process/", "lang": ["zh"], "kids_min_age": None, "lesson_types": [], "note": "越後湯澤的中文教練團隊，單板與雙板", "source": "https://snowfish-vic.com/", "updated": "2026-09-30"},
    {"id": "evergreen-hakuba", "name": "Evergreen International Ski School", "resort_ids": ["happo-one", "tsugaike"], "url": "https://www.evergreen-skischool.com/", "booking_url": "https://www.evergreen-skischool.com/cn/reservations/", "lang": ["zh", "en", "ja"], "kids_min_age": 3, "lesson_types": ["private", "group", "kids"], "note": "白馬的國際滑雪學校，八方與栂池都有據點", "source": "https://www.tsugaike.gr.jp/snow/school", "updated": "2026-09-30"},
    {"id": "tsugaike-ski-school", "name": "栂池スキー学校", "resort_ids": ["tsugaike"], "url": "https://www.tsugaike-ss.com/", "booking_url": "https://jski-outdoors.jp.mikecrm.com/A0OwB3V", "lang": ["zh", "ja"], "kids_min_age": None, "lesson_types": ["private", "group", "kids"], "note": "栂池的在地雪校，雪場官網另設中文課預約表單", "source": "https://www.tsugaike.gr.jp/snow/school", "updated": "2026-09-30"},
    {"id": "toomi-snow-school", "name": "TOOMI Snow School 遠見中文滑雪學校", "resort_ids": ["hakuba-goryu"], "url": "https://toomisnow.com/", "booking_url": "https://booking.toomisnow.com/", "lang": ["zh"], "kids_min_age": None, "lesson_types": ["private", "group"], "note": "全中文教學，白馬五龍官網列名", "source": "https://www.hakubaescal.com/winter-en/school/", "updated": "2026-09-30"},
    {"id": "chillyhill-snowsports", "name": "Chillyhill Snowsports", "resort_ids": ["tsugaike", "nozawa", "shiga-kogen"], "url": "https://www.chillyhill.jp/", "booking_url": "https://www.chillyhill.jp/booking", "lang": ["zh", "en"], "kids_min_age": None, "lesson_types": ["private", "kids"], "note": "中文、廣東話私人課；8 歲以下兒童限一對一", "source": "https://www.chillyhill.jp/", "updated": "2026-09-30"},
]

# 2026–27 季節總表（/season/2026-27.html）。每週排程 Agent 從官網補齊。
# 只填官方公布的事實；沒公布就保持 None，頁面會顯示例年季節並標「待公布」。
#   open / close: "YYYY-MM-DD"（官方預定開季／閉季日）
#   early_bird:   一句話，例：「早割全日券 ¥6,500，10/31 前線上」
#   lift_price:   一句話，例：「旺季全日券 ¥8,000」
#   source:       官方公告網址（open/close/early_bird/lift_price 任一有值就必填）
#   early_bird_source: 早鳥資訊若在另一個官方頁面，填這裡（選填）
#   updated:      "YYYY-MM-DD"（最後查證日）
SEASON_ID = "2026-27"
SEASON = {rid: {"open": None, "close": None, "early_bird": None, "lift_price": None, "source": None, "early_bird_source": None, "updated": None}
          for rid in DATA["resorts"]}
DATA["season"] = {"id": SEASON_ID, "resorts": SEASON}

# 2026-09-29 官網查證（gala-yuzawa 尚未公布開季日）
SEASON["niseko"].update({"open": "2026-11-28", "close": "2027-05-05", "lift_price": "全山券 旺季 ¥13,500／一般 ¥12,600", "source": "https://www.niseko.ne.jp/ja/lift/", "updated": "2026-09-29"})
SEASON["rusutsu"].update({"open": "2026-11-28", "close": "2027-03-31", "early_bird": "KWP 季票早割 ¥95,000，11/3 前", "early_bird_source": "https://rusutsu.com/winter-season-passes/", "lift_price": "全日券 線上 ¥13,200／窗口 ¥16,700", "source": "https://rusutsu.com/winter-lift-tickets/", "updated": "2026-09-29"})
SEASON["furano"].update({"open": "2026-11-28", "close": "2027-05-05", "lift_price": "全日券 ¥9,000（初滑／春季 ¥7,500）", "source": "https://www.princehotels.co.jp/ski/furano/winter/lift/", "updated": "2026-09-29"})
SEASON["kiroro"].update({"open": "2026-11-28", "close": "2027-05-05", "early_bird": "季票早割 ¥72,000，12/13 前網購", "early_bird_source": "https://www.kiroro.co.jp/ja/news/2026-27-seasonpasssaleseb/", "lift_price": "全日券 ¥9,200（季初／春季 ¥5,800）", "source": "https://www.kiroro.co.jp/ja/lift_price/", "updated": "2026-09-29"})
SEASON["tomamu"].update({"open": "2026-12-01", "close": "2027-04-05", "early_bird": "季票早割 ¥76,000，10/1–11/30", "lift_price": "全日券 ¥9,200", "source": "https://www.snowtomamu.jp/winter/ski/ticket/", "updated": "2026-09-29"})
SEASON["teine"].update({"open": "2026-11-21", "early_bird": "KWP 季票早割，11/3 前，最多省 ¥28,000", "early_bird_source": "https://sapporo-teine.com/snow/news/30497", "source": "https://sapporo-teine.com/snow/", "updated": "2026-09-29"})
SEASON["sahoro"].update({"open": "2026-12-01", "close": "2027-03-31", "source": "https://sahoro-resort.com/", "updated": "2026-09-29"})
SEASON["zao"].update({"open": "2026-12-12", "close": "2027-05-05", "early_bird": "早割季票 ¥88,000，11/1–17 官網限定", "lift_price": "全日券 ¥8,000（旺季 ¥9,000）", "source": "https://zaomountainresort.com/chrage/", "updated": "2026-10-07"})
SEASON["appi"].update({"early_bird": "季票 Final Sale ¥89,900，11/30 前", "source": "https://www.appi.co.jp/snow-mountain-resort/ticket/seasonpass.php", "updated": "2026-09-29"})
SEASON["bandai"].update({"open": "2026-11-28", "close": "2027-05-09", "source": "https://www.nekoma.co.jp/", "updated": "2026-09-29"})
SEASON["gala-yuzawa"].update({"open": "2026-12-19", "early_bird": "早割券 10/15 線上開賣；超早割 ¥4,300 已完售", "lift_price": "窗口全日券 ¥8,000", "source": "https://gala.co.jp/winter/information/liftticketearlysale20261015/", "updated": "2026-10-07"})
SEASON["ishiuchi"].update({"open": "2026-12-18", "close": "2027-04-04", "early_bird": "早割一日券 ¥5,800（原價 ¥8,500）", "early_bird_source": "https://ishiuchi.or.jp/winter/other/8304/", "lift_price": "一日券 ¥8,500", "source": "https://ishiuchi.or.jp/winter/seasonpass-1/", "updated": "2026-09-29"})
SEASON["yuzawa-kogen"].update({"open": "2026-12-18", "close": "2027-04-04", "source": "https://www.yuzawakogen.com/topics/2627_seasonpass_w/", "updated": "2026-09-29"})
SEASON["naeba"].update({"open": "2026-12-18", "close": "2027-04-04", "source": "https://www.princehotels.co.jp/ski/naeba/winter/", "updated": "2026-09-29"})
SEASON["kagura"].update({"open": "2026-11-28", "close": "2027-05-16", "source": "https://www.princehotels.co.jp/ski/kagura/winter/", "updated": "2026-09-29"})
SEASON["joetsu-kokusai"].update({"open": "2026-12-12", "close": "2027-04-04", "early_bird": "早割一日券 ¥3,900，10/31 前", "lift_price": "一日券 ¥5,500", "source": "https://jkokusai.co.jp/ski/lift/", "updated": "2026-09-29"})
SEASON["myoko"].update({"open": "2026-12-19", "close": "2027-05-05", "source": "https://akr-ski.com/slope", "updated": "2026-09-29"})
SEASON["maiko"].update({"open": "2026-12-19", "close": "2027-03-28", "early_bird": "早割季票 ¥45,000，9/30 前", "early_bird_source": "https://smile-resort.com/ticket/maiko/", "source": "https://www.maiko-resort.com/news/2027seasonticket.html", "updated": "2026-09-29"})
SEASON["happo-one"].update({"close": "2027-05-05", "early_bird": "早割季票 ¥90,000 起，10/1–11/15", "early_bird_source": "https://www.happo-one.jp/ticket/seasonpass/", "lift_price": "一日券 ¥9,800（高峰期）", "source": "https://www.happo-one.jp/ticket/", "updated": "2026-09-29"})
SEASON["tsugaike"].update({"close": "2027-05-05", "early_bird": "早割一日券 ¥6,500，11/30 前", "lift_price": "一日券 ¥9,800", "source": "https://www.tsugaike.gr.jp/price", "updated": "2026-09-29"})
SEASON["hakuba-goryu"].update({"open": "2026-11-21", "close": "2027-05-06", "lift_price": "一日券 ¥10,000（網購 ¥8,200）", "source": "https://www.hakubaescal.com/winter/information/2026/10/01/2026-27%e3%82%b7%e3%83%bc%e3%82%ba%e3%83%b3-%e3%82%aa%e3%83%bc%e3%83%97%e3%83%b3%e6%97%a5%e6%b1%ba%e5%ae%9a%e3%81%ae%e3%81%8a%e7%9f%a5%e3%82%89%e3%81%9b/", "updated": "2026-10-07"})
SEASON["nozawa"].update({"open": "2026-12-19", "close": "2027-03-28", "early_bird": "早割季票 9/30 截止", "early_bird_source": "https://nozawaski.com/report_summer/40933/?summer", "lift_price": "一日券 ¥7,800", "source": "https://nozawaski.com/winter/lift_price/", "updated": "2026-10-07"})
SEASON["shiga-kogen"].update({"open": "2026-12-05", "close": "2027-05-05", "lift_price": "全山一日券 ¥9,500（網購 ¥8,500）", "source": "https://shigakogen-ski.or.jp/2026/08/2026-2027.html", "updated": "2026-09-29"})
SEASON["karuizawa"].update({"open": "2026-10-31", "close": "2027-03-31", "source": "https://www.princehotels.co.jp/ski/karuizawa/winter/", "updated": "2026-10-07"})
DATA["news"][:0] = [
    {"date": "2026-10-02", "resort_id": "gala-yuzawa", "text": "12/19 開季；早割券 10/15 線上開賣", "url": "https://gala.co.jp/winter/information/liftticketearlysale20261015/"},
    {"date": "2026-10-01", "resort_id": "hakuba-goryu", "text": "官方公布 11/21 開季", "url": "https://www.hakubaescal.com/winter/information/2026/10/01/2026-27%e3%82%b7%e3%83%bc%e3%82%ba%e3%83%b3-%e3%82%aa%e3%83%bc%e3%83%97%e3%83%b3%e6%97%a5%e6%b1%ba%e5%ae%9a%e3%81%ae%e3%81%8a%e7%9f%a5%e3%82%89%e3%81%9b/"},
    {"date": "2026-09-25", "resort_id": "karuizawa", "text": "10/31 開季，10/3 起開始造雪", "url": "https://www.princehotels.co.jp/press/260925_03"},
    {"date": "2026-09-15", "resort_id": "gala-yuzawa", "text": "本季南區停止營業", "url": "https://gala.co.jp/winter/news/64209"},
]

ORIGIN = "https://japanski.djhousetw.com"

# 對外連結白名單（官網網域另外從 SEASON 的 source 自動加入）。與 INGEST_AGENT.md 白名單一致。
ALLOWED_DOMAINS = [
    "natasha-traveler.tw", "mimigo.tw", "japowproject.com", "sswboardhouse.com", "yuriselfmedia.tw",
    "whitemileage.com", "snow.tabiris.com", "surfsnow.jp", "minhyo.jp", "ptt.cc", "dcard.tw",
    "princehotels.co.jp", "snowtomamu.jp", "hoshinoresorts.com", "clubmed.com.tw", "clubmed.co.jp",
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
<meta property="og:image" content="{origin}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="zh_TW">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗺️</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@400;500;700;900&family=Noto+Sans+TC:wght@300;400;500;700&family=Zen+Kaku+Gothic+New:wght@300;400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{css}">
<!--JSONLD-->
</head>
<body data-depth="{depth}">
<div id="site-header">{header}</div>
{main}
<div id="site-footer">{footer}</div>
<script src="{data}"></script>
<script src="{app}"></script>
<script>{boot}</script>
</body>
</html>
"""

def footer(prefix=""):
    return (
        '<footer class="site-footer">'
        '<p class="footer-links"><a href="%sabout.html">關於本站</a> · <a href="%sabout.html#report">回報錯誤</a> · <a href="%sseason/2026-27.html">本季總表</a> · <a href="%sschools.html">中文雪校</a></p>'
        '<p>本站只做地區整理與外部連結導引，不代辦訂房或滑雪課程；延伸閱讀與引用的版權與內容都屬於原作者，點擊會開新分頁前往原文，請支持原創作者。預算與季節資訊為約略整理，以當季官網為準。</p>'
        '<p>雪場頁上的「看看社群怎麼說」是編輯引用公開來源，不是使用者留言板。</p>'
        '</footer>'
    ) % (prefix, prefix, prefix, prefix)


def hx(s):
    return ("" if s is None else str(s)).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def classify_tag(t):
    if any(k in t for k in ("親子", "新手", "友善")):
        return t, "family"
    if "溫泉" in t:
        return "♨ " + t, "onsen"
    return t, "default"


def chrome(prefix, active="map"):
    def item(href, key, label):
        cls = ' class="active"' if active == key else ""
        return '<a href="%s"%s>%s</a>' % (href, cls, label)
    return (
        '<header class="topbar">'
        '<a class="brand" href="%sindex.html">'
        '<div class="brand-cn">雪國轉運站</div>'
        '<div class="brand-en">Snow Country Transit</div></a>'
        '<nav class="nav">%s%s%s%s'
        '<a href="%sgo.html" class="nav-cta%s">30 秒選場</a></nav></header>'
    ) % (
        prefix,
        item(prefix + "index.html#regions", "map", "雪場"),
        item(prefix + "season/" + SEASON_ID + ".html", "season", "本季"),
        item(prefix + "compare.html", "compare", "比較"),
        item(prefix + "guide/first-trip.html", "guide", "第一次"),
        prefix, " active" if active == "quiz" else "",
    )


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) if os.path.dirname(path) else ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def page(title, desc, canonical, depth, boot, main_html, active="map", jsonld=""):
    prefix = "../" if depth == 1 else ""
    html = HEAD.format(
        title=hx(title), desc=hx(desc), canonical=canonical, origin=ORIGIN,
        css=prefix + "app.css", data=prefix + "data.js", app=prefix + "app.js",
        depth=depth, boot=boot, main=main_html,
        header=chrome(prefix, active), footer=footer(prefix),
    )
    return html.replace("<!--JSONLD-->", jsonld or "")


def tags_html(tags):
    bits = []
    for t in tags or []:
        text, cls = classify_tag(t)
        bits.append('<span class="tag %s">%s</span>' % (cls, hx(text)))
    return "".join(bits)


NEXT_ORDER = ("fly", "stay", "learn")


LANG_LABEL = {"zh": "中文", "en": "英文", "ja": "日文", "ko": "韓文"}
LESSON_LABEL = {"private": "私人課", "group": "團體課", "kids": "兒童課"}


def schools_for(rid):
    return [sc for sc in DATA["schools"] if rid in sc["resort_ids"]]


def school_list_html(rid, prefix):
    lst = schools_for(rid)
    if not lst:
        return '<p class="muted">尚未整理，<a class="card-link" href="%sabout.html#report">歡迎回報</a>。</p>' % prefix
    items = []
    for sc in lst:
        book = sc.get("booking_url") or sc["url"]
        age = ("；兒童課 %d 歲起" % sc["kids_min_age"]) if sc.get("kids_min_age") else ""
        items.append(
            '<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            '<span class="muted">%s%s</span>'
            ' <a class="card-link" href="%s" target="_blank" rel="noopener noreferrer">預約</a></li>'
            % (hx(sc["url"]), hx(sc["name"]), hx("、".join(LESSON_LABEL[t] for t in sc.get("lesson_types") or [])), age, hx(book))
        )
    return '<ul class="school-list">%s</ul><p class="muted"><a class="card-link" href="%sschools.html#%s">看全部中文雪校</a></p>' % ("".join(items), prefix, rid)


def next_steps_html(r, heading="接下來這三步"):
    ns = r.get("next_steps") or {}
    items = []
    for i, k in enumerate(NEXT_ORDER, 1):
        st = ns.get(k)
        if not st:
            continue
        link = (' <a class="card-link" href="%s" target="_blank" rel="noopener noreferrer">官方資訊</a>' % hx(st["url"])) if st.get("url") else ""
        if k == "learn" and schools_for(r["id"]):
            link += ' <a class="card-link" href="../schools.html#%s">中文雪校</a>' % r["id"]
        items.append('<li><span class="step-num">%d</span><div><strong>%s</strong><p>%s%s</p></div></li>' % (i, hx(st["title"]), hx(st["text"]), link))
    if not items:
        return ""
    return '<div class="section next-steps" id="next"><h2>%s</h2><ol>%s</ol></div>' % (hx(heading), "".join(items))


def banner_html(r, region, prefix):
    """雪場頁頂部照片：有官方授權的 hero_img 就用，否則退回地區示意圖。"""
    if r.get("hero_img"):
        credit = ('<p class="banner-credit muted">照片：%s</p>' % hx(r["hero_credit"])) if r.get("hero_credit") else ""
        return '<img class="resort-banner" src="%s%s" alt="%s">%s' % (prefix, r["hero_img"], hx(r["name"]), credit)
    if region.get("img"):
        return '<img class="resort-banner" src="%s%s" alt="%s">' % (prefix, region["img"], hx(region["name"]))
    return ""


def resort_article(r):
    prefix = "../"
    region = DATA["regions"][r["region"]]
    hub = ""
    if r.get("cluster") == "yuzawa":
        hub = ' · <a href="%sareas/yuzawa.html">越後湯澤樞紐</a>' % prefix
    if r.get("cluster") == "hakuba":
        hub = ' · <a href="%sareas/hakuba-valley.html">白馬谷樞紐</a>' % prefix
    routes = "<ul class=\"route-list\">" + "".join(
        "<li><div class=\"route-from\">%s　<span class=\"route-hours\">%s</span></div><div class=\"muted\">%s</div></li>"
        % (hx(rt["from"]), hx(rt["hours"]), hx(rt["steps"]))
        for rt in (r.get("access_routes") or [])
    ) + "</ul>"
    b = r.get("budget_twd") or {}
    budget = ""
    if b:
        budget = (
            '<div class="budget"><span class="budget-num">NT$%s–%s</span>'
            '<span class="muted">%s，%s</span></div>'
            % ("{:,}".format(b["min"]), "{:,}".format(b["max"]), hx(b.get("days", "")), hx(b.get("note", "")))
        )
    facts = "".join(
        '<div class="fact"><dt>%s</dt><dd>%s</dd></div>' % (hx(lab), hx(val))
        for lab, val in (
            ("夜滑", r.get("night_ski")),
            ("溫泉", r.get("onsen")),
            ("中文教練", r.get("chinese_coach")),
            ("Ski-in/out", r.get("ski_in_out")),
            ("中文辦事", r.get("chinese_service")),
        )
    )
    pitfalls = "".join("<li>%s</li>" % hx(p) for p in (r.get("pitfalls") or []))
    rhythm = ('<div class="section"><h2>一日雪質節奏</h2><p>%s</p></div>' % hx(r["snow_rhythm"])) if r.get("snow_rhythm") else ""
    companion = ('<div class="section"><h2>不滑雪的人</h2><p>%s</p></div>' % hx(r["companion_note"])) if r.get("companion_note") else ""
    delta = ('<div class="section"><h2>這季備註</h2><p>%s</p></div>' % hx(r["season_delta"])) if r.get("season_delta") else ""
    ex = r.get("experts") or {}
    experts = ""
    if ex.get("consensus"):
        cons = "<ol>" + "".join("<li>%s</li>" % hx(c) for c in ex["consensus"]) + "</ol>"
        dis = ('<div class="disagree">達人有分歧：%s</div>' % hx(ex["disagreement"])) if ex.get("disagreement") else ""
        chips = '<div class="source-chips">' + "".join(
            '<a href="%s" target="_blank" rel="noopener noreferrer">%s · %s ↗</a>'
            % (hx(s["url"]), hx(s["name"]), "教練" if s.get("kind") == "coach" else "部落客")
            for s in (ex.get("sources") or [])
        ) + "</div>"
        experts = '<div class="section"><h2>看看達人怎麼說</h2><p class="section-note">本站整理，請讀原文</p><div class="expert-card">' + cons + dis + chips + "</div></div>"
    comm = r.get("community") or []
    community = ""
    if comm:
        tw, jp_g = [], []
        for q in comm:
            card = (
                '<div class="quote-card"><blockquote>%s</blockquote>' % hx(q.get("quote"))
                + (('<div class="quote-orig">%s</div>' % hx(q["original"])) if q.get("original") else "")
                + '<div class="quote-meta">%s · %s · <a href="%s" target="_blank" rel="noopener noreferrer">原文</a></div></div>'
                % (hx(q.get("source")), hx(q.get("date")), hx(q.get("url")))
            )
            if q.get("source_kind") in ("threads", "public_fb", "ptt", "dcard"):
                tw.append(card)
            else:
                jp_g.append(card)
        blocks = ""
        if tw:
            blocks += '<div class="community-group"><h3>台灣雪友</h3>' + "".join(tw) + "</div>"
        if jp_g:
            blocks += '<div class="community-group"><h3>日本當地</h3>' + "".join(jp_g) + "</div>"
        community = '<div class="section"><h2>看看社群怎麼說</h2><p class="section-note">本站整理，請讀原文。雪況類引用有日期，不是即時雪況。</p>' + blocks + "</div>"
    compare = ""
    names = []
    for cid in (r.get("compare_with") or []):
        o = DATA["resorts"].get(cid)
        if o:
            names.append('<a class="card-link" href="%sresorts/%s.html">%s</a>' % (prefix, cid, hx(o["name"])))
    if names:
        compare = '<div class="section"><h2>不要和它搞混</h2><p>' + " · ".join(names) + "</p></div>"
    skip = set(s.get("url") for s in (ex.get("sources") or []))
    type_label = {"overview": "總覽", "access": "交通", "hotel": "住宿", "slope": "雪道", "pitfall": "避雷"}
    link_items = []
    for l in (r.get("links") or []):
        if l.get("url") in skip:
            continue
        link_items.append(
            '<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            '<span class="link-source muted">%s · %s</span></li>'
            % (hx(l["url"]), hx(l["title"]), hx(type_label.get(l.get("type"), l.get("type"))), hx(l.get("source")))
        )
    links = ('<div class="section"><h2>延伸閱讀</h2><ul class="link-list" style="list-style:none;margin:0;padding:0">' + "".join(link_items) + "</ul></div>") if link_items else ""
    return (
        '<main class="page" id="page">'
        '<div class="crumb"><a href="%sindex.html">轉運站</a> · '
        '<a href="%sindex.html#%s">%s</a>%s · <a href="%sgo.html">30 秒選場</a></div>'
        '%s'
        '<div class="resort-name-row"><h1 class="page-title">%s</h1><span class="resort-romaji">%s</span></div>'
        '<div class="muted">%s</div>'
        '<div class="tag-row">%s</div>'
        '<div class="verdict"><p><strong>本站怎麼判　</strong>%s</p><p class="not-for">不適合誰：%s</p></div>'
        '<p class="cta-row"><a class="btn" href="%sgo.html">不確定？30 秒選場</a></p>'
        '%s'
        '<div class="section"><h2>從台灣怎麼到</h2>%s</div>'
        '<div class="section"><h2>5 天預算帶</h2>%s</div>'
        '<div class="section"><h2>運行資訊</h2><div class="grid-5">%s</div>'
        '<p class="muted" style="margin-top:10px">%s</p></div>'
        '<div class="section" id="schools"><h2>中文雪校</h2>%s</div>'
        "%s"
        '<div class="section"><h2>現場坑</h2><ul class="pitfalls">%s</ul></div>'
        "%s%s%s%s%s%s"
        '<p class="report-line muted">這頁有錯？<a href="%sabout.html#report">告訴我們</a></p>'
        "</main>"
    ) % (
        prefix, prefix, r["region"], hx(region["name"]), hub, prefix,
        banner_html(r, region, prefix),
        hx(r["name"]), hx(r["romaji"]), hx(r["prefecture"]), tags_html(r.get("tags")),
        hx(r["one_liner"]), hx(r["not_for"]), prefix, next_steps_html(r), routes, budget, facts, hx(r.get("season_note")), school_list_html(r["id"], prefix),
        rhythm, pitfalls, companion, experts, community, delta, compare, links, prefix,
    )


def area_article(a):
    prefix = "../"
    cards = []
    for rid in a["resortIds"]:
        r = DATA["resorts"][rid]
        cards.append(
            '<div class="resort-card"><div class="resort-name-row"><span class="resort-name">%s</span>'
            '<span class="resort-romaji">%s</span></div><p class="why">%s</p>'
            '<p class="not-for">不適合誰：%s</p>'
            '<a class="card-link" href="%sresorts/%s.html">看介紹 ↗</a></div>'
            % (hx(r["name"]), hx(r["romaji"]), hx(r["one_liner"]), hx(r["not_for"]), prefix, rid)
        )
    return (
        '<main class="page" id="page"><div class="crumb"><a href="%sindex.html">轉運站</a> · '
        '<a href="%sgo.html">30 秒選場</a></div>'
        '<div class="resort-name-row"><h1 class="page-title">%s</h1><span class="resort-romaji">%s</span></div>'
        '<div class="verdict"><p>%s</p></div><p>%s</p>'
        '<div class="section"><h2>先選山再出發</h2><div class="resort-list">%s</div></div></main>'
    ) % (prefix, prefix, hx(a["name"]), hx(a["romaji"]), hx(a["one_liner"]), hx(a["desc"]), "".join(cards))


def compare_article():
    groups_html = []
    for g in DATA["compare"]:
        heads = "<th></th>" + "".join(
            '<th><a href="resorts/%s.html">%s</a><div class="resort-romaji">%s</div></th>'
            % (rid, hx(DATA["resorts"][rid]["name"]), hx(DATA["resorts"][rid]["romaji"]))
            for rid in g["ids"]
        )
        rows_spec = [
            ("適合誰", "one_liner"),
            ("不適合誰", "not_for"),
            ("從台灣怎麼到", "hours"),
            ("預算帶", "budget"),
            ("中文教練", "chinese_coach"),
            ("粉雪", "powder"),
            ("新手友善", "beginner"),
        ]
        body = []
        for label, key in rows_spec:
            cells = []
            for rid in g["ids"]:
                r = DATA["resorts"][rid]
                if key == "hours":
                    val = r["access_routes"][0]["hours"]
                elif key == "budget":
                    b = r["budget_twd"]
                    val = "NT$%s–%s" % ("{:,}".format(b["min"]), "{:,}".format(b["max"]))
                elif key == "powder":
                    val = "%s/5" % r["scores"]["powder"]
                elif key == "beginner":
                    val = "%s/5" % r["scores"]["beginner"]
                else:
                    val = r[key]
                cells.append("<td>%s</td>" % hx(val))
            body.append("<tr><th>%s</th>%s</tr>" % (hx(label), "".join(cells)))
        groups_html.append(
            '<div class="section"><h2>%s</h2><div style="overflow:auto"><table class="compare-table">'
            "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div>"
            % (hx(g["title"]), heads, "".join(body))
        )
    return (
        '<main class="page page-wide" id="page">'
        '<div class="crumb"><a href="index.html">轉運站</a> · <a href="go.html">30 秒選場</a></div>'
        '<h1 class="page-title" id="hokkaido">二世谷、留壽都、富良野怎麼選</h1>'
        '<p class="muted">北海道三選、東京側短待、長野三選。要「日本滑雪該去哪」請用 <a class="card-link" href="go.html">30 秒選場</a>。</p>'
        + "".join(groups_html) + "</main>"
    )


def md(date):
    """'2026-11-28' -> '11/28'"""
    if not date:
        return ""
    y, m, d = date.split("-")
    return "%d/%d" % (int(m), int(d))


def season_article():
    prefix = "../"
    rows_by_region = []
    announced = 0
    for reg_id, reg in DATA["regions"].items():
        rows = []
        for rid in reg["resortIds"]:
            r = DATA["resorts"][rid]
            s = SEASON[rid]
            if s.get("open"):
                announced += 1
                open_cell = '<span class="season-date" data-open="%s">%s</span>' % (s["open"], md(s["open"]))
                if s.get("close"):
                    open_cell += '<span class="muted">～%s</span>' % md(s["close"])
                status = '<span class="pill season-status" data-open="%s">已公布</span>' % s["open"]
            else:
                open_cell = '<span class="muted">待公布</span>' + (('<span class="muted">～%s</span>' % md(s["close"])) if s.get("close") else "")
                status = '<span class="pill season-status tbd">待公布</span>'
            price_bits = [x for x in (s.get("early_bird"), s.get("lift_price")) if x]
            price = "<br>".join(hx(x) for x in price_bits) if price_bits else '<span class="muted">—</span>'
            src = ('<a class="card-link" href="%s" target="_blank" rel="noopener noreferrer">官方公告</a>' % hx(s["source"])
                   + (('<div><a class="card-link" href="%s" target="_blank" rel="noopener noreferrer">早鳥公告</a></div>' % hx(s["early_bird_source"])) if s.get("early_bird_source") else "")
                   + ('<div class="muted">%s 查證</div>' % md(s["updated"]) if s.get("updated") else "")) if s.get("source") else '<span class="muted">—</span>'
            rows.append(
                "<tr>"
                '<th scope="row"><a href="%sresorts/%s.html">%s</a><div class="resort-romaji">%s</div></th>'
                "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"
                "</tr>"
                % (prefix, rid, hx(r["name"]), hx(r["romaji"]),
                   open_cell, status, price, hx(r.get("season_note")), src)
            )
        rows_by_region.append(
            '<div class="section season-region" id="%s"><h2>%s</h2>'
            '<div class="table-wrap"><table class="compare-table season-table">'
            "<thead><tr><th>雪場</th><th>本季開季</th><th>狀態</th><th>早鳥／票價</th><th>例年季節</th><th>來源</th></tr></thead>"
            "<tbody>%s</tbody></table></div></div>"
            % (reg_id, hx(reg["name"]), "".join(rows))
        )
    news = sorted(DATA.get("news") or [], key=lambda n: n.get("date", ""), reverse=True)[:8]
    news_html = ""
    if news:
        items = "".join(
            '<li><time>%s</time><a href="%sresorts/%s.html">%s</a> %s</li>'
            % (hx(n.get("date")), prefix, hx(n.get("resort_id")),
               hx(DATA["resorts"].get(n.get("resort_id"), {}).get("name", "")), hx(n.get("text")))
            for n in news
        )
        news_html = '<div class="section"><h2>最近更新</h2><ul class="season-news">%s</ul></div>' % items
    jump = " · ".join('<a href="#%s">%s</a>' % (k, hx(v["name"])) for k, v in DATA["regions"].items())
    return (
        '<main class="page page-wide" id="page">'
        '<div class="crumb"><a href="%sindex.html">轉運站</a> · <a href="%sgo.html">30 秒選場</a></div>'
        '<h1 class="page-title">2026–27 日本滑雪場開季日與早鳥票總表</h1>'
        '<p class="lead-copy">24 座台灣人最常去的日本雪場，本季開季日、閉季日、早鳥票與票價。只收官方公布的資訊，每週更新；還沒公布的標「待公布」，先參考例年季節。</p>'
        '<div class="season-summary">'
        '<div><b id="seasonAnnounced">%d</b><span>/ 24 座已公布開季日</span></div>'
        '<div><b id="seasonNext">—</b><span id="seasonNextLabel">最快開季</span></div>'
        '<div><b>每週一</b><span>更新</span></div>'
        "</div>"
        '<p class="muted">跳到：%s　·　還沒決定去哪？<a class="card-link" href="%sgo.html">30 秒選場</a></p>'
        "%s%s"
        '<p class="muted" style="margin-top:28px">開閉季日依雪況可能提前或延後，出發前請再看官網。票價以日圓計、未含稅差。</p>'
        "</main>"
    ) % (prefix, prefix, announced, jump, prefix, news_html, "".join(rows_by_region))


def schools_article():
    prefix = ""
    blocks = []
    for reg_id, reg in DATA["regions"].items():
        rows = []
        for rid in reg["resortIds"]:
            r = DATA["resorts"][rid]
            lst = schools_for(rid)
            if not lst:
                rows.append(
                    '<tr id="%s"><th scope="row"><a href="resorts/%s.html">%s</a></th>'
                    '<td colspan="5" class="muted">尚未整理，<a class="card-link" href="about.html#report">歡迎回報</a></td></tr>'
                    % (rid, rid, hx(r["name"])))
                continue
            for i, sc in enumerate(lst):
                rows.append(
                    '<tr%s><th scope="row">%s</th>'
                    '<td data-label="雪校"><a href="%s" target="_blank" rel="noopener noreferrer">%s</a><div class="muted">%s</div></td>'
                    '<td data-label="語言">%s</td><td data-label="課型">%s</td><td data-label="兒童">%s</td>'
                    '<td data-label="預約"><a class="card-link" href="%s" target="_blank" rel="noopener noreferrer">預約</a>'
                    '<div class="muted"><a href="%s" target="_blank" rel="noopener noreferrer">來源</a> %s 查證</div></td></tr>'
                    % (' id="%s"' % rid if i == 0 else "",
                       ('<a href="resorts/%s.html">%s</a>' % (rid, hx(r["name"]))) if i == 0 else "",
                       hx(sc["url"]), hx(sc["name"]), hx(sc.get("note") or ""),
                       hx("、".join(LANG_LABEL.get(l, l) for l in sc.get("lang") or [])),
                       hx("、".join(LESSON_LABEL[t] for t in sc.get("lesson_types") or [])) or "—",
                       ("%d 歲起" % sc["kids_min_age"]) if sc.get("kids_min_age") else "—",
                       hx(sc.get("booking_url") or sc["url"]), hx(sc["source"]), md(sc["updated"])))
        blocks.append(
            '<div class="section" id="region-%s"><h2>%s</h2><div class="table-wrap"><table class="compare-table school-table">'
            "<thead><tr><th>雪場</th><th>雪校</th><th>授課語言</th><th>課型</th><th>兒童</th><th>預約</th></tr></thead>"
            "<tbody>%s</tbody></table></div></div>" % (reg_id, hx(reg["name"]), "".join(rows)))
    covered = len(set(rid for sc in DATA["schools"] for rid in sc["resort_ids"]))
    return (
        '<main class="page page-wide" id="page">'
        '<div class="crumb"><a href="index.html">轉運站</a> · 中文雪校</div>'
        '<h1 class="page-title">日本滑雪中文教練與雪校總表</h1>'
        '<p class="lead-copy">24 座台灣人最常去的日本雪場，哪裡有中文授課的雪校、教哪些場、小孩幾歲收、去哪裡預約。只收官網明寫有中文授課的學校，不做評價；價格常變，請以各校官網為準。</p>'
        '<div class="season-summary"><div><b>%d</b><span>所雪校</span></div><div><b>%d</b><span>/ 24 座雪場已整理</span></div><div><b>官網</b><span>每筆都附來源與查證日</span></div></div>'
        '<p class="muted">還沒決定去哪？<a class="card-link" href="go.html">30 秒選場</a>　·　發現雪校資訊有誤：<a class="card-link" href="about.html#report">告訴我們</a></p>'
        "%s</main>"
    ) % (len(DATA["schools"]), covered, "".join(blocks))


def main():
    with open(os.path.join(ROOT, "data.js"), "w", encoding="utf-8") as f:
        f.write("var DATA = ")
        f.write(json.dumps(DATA, ensure_ascii=False, indent=2))
        f.write(";\n")

    ids = list(DATA["resorts"].keys())
    assert len(ids) == 24, ids

    # next_steps／schools 等對外連結只准雪場官網或白名單網域
    from urllib.parse import urlparse
    allowed = set(ALLOWED_DOMAINS)
    for sid, sv in SEASON.items():
        for k in ("source", "early_bird_source"):
            if sv.get(k):
                allowed.add(urlparse(sv[k]).hostname)
    def check_url(where, u):
        if not u:
            return
        h = urlparse(u).hostname or ""
        assert any(h == d or h.endswith("." + d) for d in allowed), "%s: %s 不在允許網域" % (where, u)
    for rid, r in DATA["resorts"].items():
        for k, st in (r.get("next_steps") or {}).items():
            check_url("%s.next_steps.%s" % (rid, k), st.get("url"))
    seen = set()
    for sc in DATA["schools"]:
        where = "schools.%s" % sc.get("id")
        assert sc.get("id") and sc["id"] not in seen, where + " id 重複或缺"
        seen.add(sc["id"])
        for k in ("name", "url", "source", "updated"):
            assert sc.get(k), "%s 缺 %s" % (where, k)
        assert sc.get("resort_ids") and all(x in DATA["resorts"] for x in sc["resort_ids"]), where + " resort_ids 不在 24 座"
        assert "zh" in (sc.get("lang") or []), where + " 沒有中文授課"
        assert set(sc.get("lesson_types") or []) <= set(LESSON_LABEL), where + " lesson_types 不合法"
        assert len(sc.get("note") or "") <= 40, where + " note 超過 40 字"
        for k in ("url", "booking_url", "source"):
            u = sc.get(k) or ""
            assert "facebook.com" not in u and "klook" not in u and "kkday" not in u, "%s.%s 不准用臉書或 OTA" % (where, k)

    for rid, r in DATA["resorts"].items():
        title = "%s 適合誰、從台灣怎麼走｜雪國轉運站" % r["name"]
        desc = "%s 不適合誰：%s" % (r["one_liner"], r["not_for"])
        ld = json.dumps({
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title,
            "description": desc,
            "url": ORIGIN + "/resorts/%s.html" % rid,
            "inLanguage": "zh-Hant",
        }, ensure_ascii=False)
        html = page(
            title, desc, ORIGIN + "/resorts/%s.html" % rid, 1,
            "Hub.renderResort(%s);" % json.dumps(rid),
            resort_article(r).replace("</main>", longtail.resort_links(r, "../", DATA) + "</main>"), active="map",
            jsonld='<script type="application/ld+json">%s</script>' % ld,
        )
        write("resorts/%s.html" % rid, html)

    for aid, a in DATA["areas"].items():
        html = page(
            "%s 怎麼選｜雪國轉運站" % a["name"], a["one_liner"],
            ORIGIN + "/areas/%s.html" % aid, 1,
            "Hub.renderArea(%s);" % json.dumps(aid),
            area_article(a),
        )
        write("areas/%s.html" % aid, html)

    write("compare.html", page(
        "二世谷、留壽都、富良野怎麼選｜雪國轉運站",
        "北海道三選、東京當日（GALA／苗場／輕井澤）、長野三選。給台灣人的日本滑雪對照。",
        ORIGIN + "/compare.html", 0, "Hub.renderCompare();",
        compare_article(), active="compare",
    ))

    for sid, s in SEASON.items():
        if any(s.get(k) for k in ("open", "close", "early_bird", "lift_price")):
            assert s.get("source"), "season.%s has data but no source URL" % sid
    write("season/%s.html" % SEASON_ID, page(
        "2026–27 日本滑雪場開季日與早鳥票總表｜雪國轉運站",
        "二世谷、留壽都、GALA湯澤、苗場、白馬等 24 座日本雪場 2026–27 開季日、閉季日、早鳥票與票價，只收官方公布資訊，每週更新。",
        ORIGIN + "/season/%s.html" % SEASON_ID, 1, "Hub.renderSeason();",
        season_article(), active="season",
    ))

    write("schools.html", page(
        "日本滑雪中文教練與雪校總表｜雪國轉運站",
        "二世谷、留壽都、GALA湯澤、苗場、白馬等 24 座日本雪場的中文授課雪校：教哪些場、兒童幾歲收、預約連結，只收官網明寫中文授課的學校。",
        ORIGIN + "/schools.html", 0, "Hub.mountChrome('schools');",
        schools_article(), active="schools",
    ))

    longtail_urls = longtail.build(DATA, SEASON, page, hx, md, write, ORIGIN, school_list=school_list_html)

    urls = [
        ORIGIN + "/",
        ORIGIN + "/go",
        ORIGIN + "/season/%s.html" % SEASON_ID,
        ORIGIN + "/about.html",
        ORIGIN + "/schools.html",
        ORIGIN + "/compare.html",
        ORIGIN + "/guide/first-trip.html",
        ORIGIN + "/areas/yuzawa.html",
        ORIGIN + "/areas/hakuba-valley.html",
    ] + [ORIGIN + "/resorts/%s.html" % i for i in ids] + longtail_urls
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append("  <url><loc>%s</loc></url>" % u)
    sm.append("</urlset>\n")
    write("sitemap.xml", "\n".join(sm))
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % ORIGIN)
    print("resorts", len(ids))
    print("longtail pages", len(longtail_urls))
    print("high-search community", sum(1 for i in ["niseko","rusutsu","furano","kiroro","tomamu","gala-yuzawa","naeba","ishiuchi","karuizawa","happo-one","tsugaike","nozawa","shiga-kogen","zao","appi"] if len(DATA["resorts"][i].get("community") or []) >= 2))

if __name__ == "__main__":
    main()





