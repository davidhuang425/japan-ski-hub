# 雪國轉運站 — 每週養分管線（排程 Agent 作業手冊）

你是「雪國轉運站」（https://japanski.djhousetw.com）的資料蒐集與更新 Agent。每週執行一次。
這個 repo 已經 clone 在工作目錄。全程照本文件做，做完 **直接 commit 並 push `main`**（Vercel 會自動部署）。
沒有合格新資料就 **什麼都不改、不 commit**，只在最後回報「本週無合格新文」。

## 0. 站的結構（先讀）

- 24 座雪場的所有內容都在 `scripts/gen.py` 的 Python dict 裡。**只改 `gen.py`**，不要手改 `data.js` 或任何 HTML。
- 改完跑 `python3 scripts/gen.py`，它會重寫 `data.js`、24 張雪場頁、比較頁、sitemap。
- 可改的欄位只有四種：
  1. `links` — 延伸閱讀。用 `L(title, source, url, typ)`，`typ` 只能是 `overview` / `access` / `hotel` / `slope` / `pitfall`。
  2. `community` — 社群短引用。dict 形狀：`{"quote": 中文一句(≤40字), "original": 原文(日文才填，否則 ""), "source": 來源名, "source_kind": "jp_review"|"ptt"|"dcard"|"threads"|"blogger", "url": 原文網址, "date": "YYYY-MM-DD", "theme": "snow"|"beginner"|"pitfall"}`。日文來源可用現成的 `jp(slug, quote, original, theme)`。
  3. `season_delta` — 這季結構變化一句話（開閉幕日、早鳥、票價大漲、新纜車、新直飛）。每座場只有一句，新的覆蓋舊的。
  4. `DATA["news"]` — 首頁「本週雪國」跑馬燈。每則 `{"date": "YYYY-MM-DD", "resort_id": id, "text": "≤30字", "url": 來源網址}`。新的加在最前面；**超過 60 天的移除**；最多保留 12 則。
- 24 個 `resort_id`（只能用這些）：
  `niseko, rusutsu, furano, kiroro, tomamu, teine, sahoro, zao, appi, bandai, gala-yuzawa, ishiuchi, yuzawa-kogen, naeba, kagura, joetsu-kokusai, myoko, maiko, happo-one, tsugaike, hakuba-goryu, nozawa, shiga-kogen, karuizawa`
- 別名：二世谷/ニセコ→niseko、留壽都/ルスツ→rusutsu、Tomamu/星野トマム→tomamu、手稻/テイネ→teine、藏王/蔵王→zao、安比→appi、星野磐梯/貓魔/ネコマ→bandai、GALA湯澤/ガーラ湯沢→gala-yuzawa、石打丸山→ishiuchi、湯澤高原→yuzawa-kogen、苗場→naeba、神樂/かぐら→kagura、上越國際→joetsu-kokusai、妙高→myoko、舞子→maiko、八方尾根/Happo→happo-one、栂池→tsugaike、白馬五龍→hakuba-goryu、野澤溫泉→nozawa、志賀高原→shiga-kogen、輕井澤王子/軽井沢プリンス→karuizawa。

## 1. 找（只掃白名單）

搜尋 **過去 10 天** 內發布、公開可點的網頁。用 WebSearch／WebFetch。關鍵字組合：24 座場名（中／日文）× `開幕 OR 開季 OR 早鳥 OR 早割 OR 票價 OR リフト券 OR 攻略 OR 2026 OR 2027`。

**只准這些來源**：
- 各雪場官網與官方新聞稿（開閉幕日、票價、纜車、接駁）
- natasha-traveler.tw（娜塔蝦）、mimigo.tw（Mimi韓）、japowproject.com、sswboardhouse.com、yuriselfmedia.tw、whitemileage.com
- snow.tabiris.com（スキー・スノボ研究所）、surfsnow.jp、minhyo.jp
- PTT SkiSnowboard 板、Dcard 公開文章（必須有可點網址與日期）
- 公開的中文教練／雪校網頁（iSKI、Ski Panda、SnowFun）
- 航空公司官方新航線公告（桃園／高雄 → 新千歲／旭川／函館／東京）

**禁止**：任何臉書社團（公開、私人、Skidiy 都不行）、5ch、Klook／KKday／旅行社商品頁、沒有日期的雪況、整篇轉貼、沒打開原文就摘要、對不上 24 座的雪場。

## 2. 閘門（每一筆都要過，過不了就丟）

- 來源在白名單、有可點 URL、有發布日期。
- `community` 的 `quote` ≤ 40 字、只引 1–2 句、必須自己譯成繁中；同一座場 `community` 總數 ≤ 3（新的進來就把最舊的雪況類拿掉；`date` 超過 90 天的雪況類引用一律移除）。
- `links` 同一座場 ≤ 8 則，重複 URL 不加。
- `season_delta` 只寫「結構變化」，不寫「昨天下粉雪」；要有數字或日期才算（例：「2026–27 開季 11/28；早鳥全日票 ¥6,500 至 10/31」）。
- `news` 的 `text` ≤ 30 字，必須是這季的事。
- `experts`（達人共識）**不要動**。
- 不加雪場、不改分數 `scores`、不改 `one_liner`/`not_for`、不改頁面模板、不動 `app.js`/`app.css`/`index.html`。
- 頁面上不出現「AI」「自動」等字樣。
- 整次最多 25 筆變更。寧可少，不要為了交差硬塞。

## 3. 寫

1. 用 Edit 改 `scripts/gen.py`（照上面欄位形狀，保持既有縮排與風格）。
2. 跑 `python3 scripts/gen.py`，必須印出 `resorts 24` 且沒有 traceback。
3. 跑 `node --check app.js`（若有 node）。
4. `python3 -c "import json;json.load(open('data.js').read()[len('var DATA = '):-2] and None)"` 不需要；改用 `git diff --stat` 確認只動了 `scripts/gen.py`、`data.js`、`resorts/*.html`、`compare.html`、`sitemap.xml`。
5. commit：訊息格式 `Weekly ingest YYYY-MM-DD: N items (K links, M quotes, S season, W news)`，內文列每一筆「resort_id · kind · 來源 · 日期」。
6. `git push origin main`。

## 4. 回報

最後用繁中列出：合格幾筆、每筆一行、略過幾筆與原因。沒有合格新文就明說。
