(function () {
  var MOUNTAIN_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 19h18L14.5 8.5 11 13l-2.5-3L3 19z"></path><circle cx="17.5" cy="6.5" r="1.8"></circle></svg>';
  var TOKYO_DAY_IDS = ['gala-yuzawa', 'karuizawa', 'ishiuchi', 'yuzawa-kogen'];
  var Q1_OPTS = [
    ['first', '第一次（沒滑過，或只玩過雪盆）'],
    ['green', '綠線沒問題，紅線會怕'],
    ['red', '紅線沒壓力，想找地形'],
    ['powder', '衝粉雪／林間']
  ];
  var Q2_OPTS = [
    ['hokkaido', '從台灣直奔北海道'],
    ['tokyo_transfer', '先到東京再轉進雪場'],
    ['tokyo_day', '已在東京，只想當日或 1–2 天'],
    ['undecided', '還沒定，聽建議']
  ];
  var Q3_OPTS = [
    ['skiers', '自己或雪友，大家都會滑'],
    ['mixed', '程度不一的朋友／情侶'],
    ['kids', '有 12 歲以下小孩'],
    ['non_skier', '有人完全不滑雪']
  ];
  var Q4_OPTS = [
    ['access', '交通最省事'],
    ['budget', '預算可控'],
    ['powder', '粉雪品質'],
    ['onsen', '溫泉／度假感'],
    ['coach', '中文教練好找']
  ];

  function rootPath() {
    return (document.body.getAttribute('data-depth') || '0') === '1' ? '../' : '';
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function classifyTag(t) {
    if (t.indexOf('親子') > -1 || t.indexOf('新手') > -1 || t.indexOf('友善') > -1) return { text: t, cls: 'family' };
    if (t.indexOf('溫泉') > -1) return { text: '♨ ' + t, cls: 'onsen' };
    return { text: t, cls: 'default' };
  }
  function tagsHtml(tags) {
    return (tags || []).map(classifyTag).map(function (t) {
      return '<span class="tag ' + t.cls + '">' + esc(t.text) + '</span>';
    }).join('');
  }
  function analytics() {
    if (window.va) return;
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    var s = document.createElement('script');
    s.defer = true;
    s.src = '/_vercel/insights/script.js';
    document.head.appendChild(s);
  }
  function headerHtml(active) {
    var r = rootPath();
    function item(href, key, label) {
      return '<a href="' + href + '"' + (active === key ? ' class="active"' : '') + '>' + label + '</a>';
    }
    return '<header class="topbar">' +
      '<a class="brand" href="' + r + 'index.html">' +
        '<div class="brand-cn">雪國轉運站</div>' +
        '<div class="brand-en">Snow Country Transit Hub</div>' +
      '</a>' +
      '<div class="subhead">台灣人的日本滑雪選場入口</div>' +
      '<nav class="nav">' +
        item(r + 'go.html', 'quiz', '選場') +
        item(r + 'index.html#map', 'map', '地圖') +
        item(r + 'compare.html', 'compare', '比較') +
        item(r + 'guide/first-trip.html', 'guide', '第一次') +
      '</nav></header>';
  }
  function footerHtml() {
    return '<footer class="site-footer">' +
      '<p>本站只做地區整理與外部連結導引，不代辦訂房或滑雪課程；延伸閱讀與引用的版權與內容都屬於原作者，點擊會開新分頁前往原文，請支持原創作者。預算與季節資訊為約略整理，以當季官網為準。</p>' +
      '<p>現場回報尚未開放。雪場頁上的「看看社群怎麼說」是編輯引用公開來源，不是使用者留言板。</p>' +
      '</footer>';
  }
  function mountChrome(active) {
    var h = document.getElementById('site-header');
    var f = document.getElementById('site-footer');
    if (h) h.innerHTML = headerHtml(active);
    if (f) f.innerHTML = footerHtml();
    analytics();
  }
  function resortUrl(id) { return rootPath() + 'resorts/' + id + '.html'; }
  function areaUrl(id) { return rootPath() + 'areas/' + id + '.html'; }
  function clusterOf(id) { return (DATA.resorts[id] && DATA.resorts[id].cluster) || id; }

  function vetoPrimary(id, a) {
    var r = DATA.resorts[id];
    if (!r) return true;
    if (a.q2 === 'tokyo_day' && TOKYO_DAY_IDS.indexOf(id) === -1) return true;
    if (a.q1 === 'first' && (id === 'happo-one' || id === 'shiga-kogen')) return true;
    if (a.q3 === 'kids' && id === 'happo-one') return true;
    return false;
  }
  function allowAlt(id, a) {
    var r = DATA.resorts[id];
    if (!r) return false;
    if (a.q2 === 'tokyo_day') return id === 'naeba' || TOKYO_DAY_IDS.indexOf(id) !== -1;
    if (a.q1 === 'first' && id === 'happo-one') return true;
    return true;
  }
  function scoreResort(id, a) {
    var sc = DATA.resorts[id].scores;
    var s = 0;
    if (a.q1 === 'first') s += sc.beginner * 3;
    else if (a.q1 === 'green') s += sc.beginner * 2;
    else if (a.q1 === 'red') s += sc.terrain * 2;
    else if (a.q1 === 'powder') s += sc.powder * 3;
    if (a.q2 === 'hokkaido') s += sc.cts_access * 3;
    else if (a.q2 === 'tokyo_transfer') s += sc.tokyo_access * 2;
    else if (a.q2 === 'tokyo_day') s += sc.tokyo_access * 3;
    else if (a.q2 === 'undecided') s += sc.tokyo_access + sc.cts_access;
    if (a.q3 === 'kids') s += sc.family * 3;
    else if (a.q3 === 'non_skier') s += sc.non_skier * 3;
    else if (a.q3 === 'mixed') s += sc.beginner + sc.family;
    if (a.q4 === 'access') s += (a.q2 === 'hokkaido' ? sc.cts_access : sc.tokyo_access) * 3;
    else if (a.q4 === 'budget') s += sc.budget * 3;
    else if (a.q4 === 'powder') s += sc.powder * 3;
    else if (a.q4 === 'onsen') s += sc.onsen * 3;
    else if (a.q4 === 'coach') s += sc.chinese_coach * 3;
    return s;
  }
  function whyFor(r, a, asAlt) {
    if (asAlt && r.id === 'happo-one' && a.q1 === 'first') {
      return '進階地形很強，但先不要當第一座山：紅黑線比例高，午後容易變饅頭坡。';
    }
    if (a.q1 === 'first' && r.why_beginner) return r.why_beginner;
    if (a.q4 === 'powder' && r.why_powder) return r.why_powder;
    if (a.q4 === 'onsen' && r.why_onsen) return r.why_onsen;
    if (a.q4 === 'budget' && r.why_budget) return r.why_budget;
    if (a.q4 === 'coach' && r.why_coach) return r.why_coach;
    if ((a.q2 === 'tokyo_day' || a.q4 === 'access') && r.why_tokyo) return r.why_tokyo;
    if (a.q3 === 'kids' && r.why_family) return r.why_family;
    if (a.q1 === 'powder' && r.why_powder) return r.why_powder;
    return r.one_liner;
  }
  function pickResults(a) {
    var ids = Object.keys(DATA.resorts);
    var ranked = ids.map(function (id) {
      return { id: id, score: scoreResort(id, a), coach: DATA.resorts[id].scores.chinese_coach, access: DATA.resorts[id].scores.tokyo_access + DATA.resorts[id].scores.cts_access, budget: DATA.resorts[id].scores.budget };
    }).sort(function (x, y) {
      if (y.score !== x.score) return y.score - x.score;
      if (y.coach !== x.coach) return y.coach - x.coach;
      if (y.access !== x.access) return y.access - x.access;
      return y.budget - x.budget;
    });
    var primary = [];
    var used = {};
    ranked.forEach(function (row) {
      if (primary.length >= 2) return;
      if (vetoPrimary(row.id, a)) return;
      var c = clusterOf(row.id);
      if (used[c]) return;
      primary.push(row.id);
      used[c] = true;
    });
    var alt = null;
    ranked.forEach(function (row) {
      if (alt) return;
      if (primary.indexOf(row.id) !== -1) return;
      if (!allowAlt(row.id, a)) return;
      var c = clusterOf(row.id);
      if (used[c] && a.q2 !== 'tokyo_day') return;
      alt = row.id;
    });
    return { primary: primary, alt: alt };
  }
  function hasOpt(opts, val) {
    return opts.some(function (o) { return o[0] === val; });
  }
  function encodeAnswers(a) {
    return [a.q1, a.q2, a.q3, a.q4].join('.');
  }
  function decodeAnswers(s) {
    var p = String(s || '').split('.');
    if (p.length !== 4) return null;
    var a = { q1: p[0], q2: p[1], q3: p[2], q4: p[3] };
    if (!hasOpt(Q1_OPTS, a.q1) || !hasOpt(Q2_OPTS, a.q2) || !hasOpt(Q3_OPTS, a.q3) || !hasOpt(Q4_OPTS, a.q4)) return null;
    return a;
  }
  function youLine(a) {
    var bits = [];
    if (a.q1 === 'first') bits.push('第一次');
    else if (a.q1 === 'green') bits.push('綠線沒問題');
    else if (a.q1 === 'red') bits.push('想找地形');
    else if (a.q1 === 'powder') bits.push('衝粉雪');
    if (a.q2 === 'hokkaido') bits.push('直奔北海道');
    else if (a.q2 === 'tokyo_transfer') bits.push('東京再轉');
    else if (a.q2 === 'tokyo_day') bits.push('已在東京');
    else if (a.q2 === 'undecided') bits.push('行程未定');
    if (a.q3 === 'kids') bits.push('有小孩');
    else if (a.q3 === 'non_skier') bits.push('有人不滑');
    return bits.join(' · ');
  }
  function avoidFor(a) {
    if (a.q2 === 'tokyo_day') return { id: 'niseko', line: '已在東京短待，北海道當天到不了' };
    if (a.q3 === 'kids') return { id: 'happo-one', line: '帶小孩不要以八方當主場' };
    if (a.q1 === 'first') return { id: 'happo-one', line: '第一次先別當第一座山' };
    if (a.q1 === 'powder' || a.q4 === 'powder') return { id: 'karuizawa', line: '不是為粉雪來的場' };
    return { id: 'happo-one', line: '第一次或帶小孩先別當主場' };
  }
  function goPageBase() {
    if (/japanski\.djhousetw\.com$/.test(location.hostname) || /\.vercel\.app$/.test(location.hostname)) return '/go';
    return rootPath() + 'go.html';
  }
  function localShareUrl(a) {
    var base = goPageBase();
    if (base.charAt(0) === '/') return location.origin + base + '?a=' + encodeAnswers(a);
    return new URL(base, location.href).href.split('?')[0] + '?a=' + encodeAnswers(a);
  }

  function renderIndex() {
    mountChrome('map');
    var selected = null;
    var mode = 'home';
    var answers = { q1: null, q2: null, q3: null, q4: null };
    var step = 1;
    var dotsEl = document.getElementById('dots');
    var cardsEl = document.getElementById('cards');
    var panelEl = document.getElementById('panel');

    function selectRegion(id) {
      selected = id;
      mode = 'region';
      draw();
    }
    function drawMap() {
      var dotsHtml = '';
      var cardsHtml = '';
      Object.keys(DATA.dots).forEach(function (id) {
        var d = DATA.dots[id];
        var active = selected === id ? ' active' : '';
        dotsHtml += '<div class="geo-dot' + active + '" style="left:' + d[0] + '%;top:' + d[1] + '%"></div>';
        var c = DATA.cards[id];
        var r = DATA.regions[id];
        cardsHtml += '<button class="region-card' + active + '" style="left:' + c[0] + '%;top:' + c[1] + '%" data-id="' + id + '">' +
          '<span class="region-icon">' + MOUNTAIN_SVG + '</span>' +
          '<span class="region-card-text"><span class="region-card-title">' + esc(r.name) + '</span><span class="region-card-sub">' + esc(r.sub) + '</span></span>' +
          '</button>';
      });
      dotsEl.innerHTML = dotsHtml;
      cardsEl.innerHTML = cardsHtml;
      document.querySelectorAll('.region-card').forEach(function (btn) {
        btn.addEventListener('click', function () {
          answers = { q1: null, q2: null, q3: null, q4: null };
          step = 1;
          selectRegion(btn.getAttribute('data-id'));
        });
      });
    }
    function homePanel() {
      var qp = Object.keys(DATA.regions).map(function (id) {
        return '<button class="quickpick" data-id="' + id + '">' + esc(DATA.regions[id].name) + '</button>';
      }).join('');
      panelEl.innerHTML = '<div class="empty-state">' +
        '<div class="season-chip">2026–27 雪季</div>' +
        '<div class="empty-lede">台灣人的日本滑雪轉運站</div>' +
        '<div class="empty-sub">先選場，再轉乘到最好的中文攻略。點左邊地圖看地區，或用 30 秒問卷告訴我們你是誰。</div>' +
        '<a class="btn" href="' + rootPath() + 'go.html">幫我選場（30 秒）</a>' +
        '<div class="muted">或點左邊地圖看地區</div>' +
        '<div class="quickpicks">' + qp + '</div></div>';
      panelEl.querySelectorAll('.quickpick').forEach(function (btn) {
        btn.addEventListener('click', function () { selectRegion(btn.getAttribute('data-id')); });
      });
    }
    function quizPanel() {
      var qMap = { 1: ['q1', '程度', Q1_OPTS], 2: ['q2', '這趟怎麼走', Q2_OPTS], 3: ['q3', '同行', Q3_OPTS], 4: ['q4', '這趟最在乎', Q4_OPTS] };
      var q = qMap[step];
      var choices = q[2].map(function (opt) {
        var sel = answers[q[0]] === opt[0] ? ' selected' : '';
        return '<button class="choice' + sel + '" data-val="' + opt[0] + '">' + esc(opt[1]) + '</button>';
      }).join('');
      panelEl.innerHTML = '<div class="quiz">' +
        '<div class="quiz-progress">選場 ' + step + ' / 4</div>' +
        '<div class="quiz-q">' + esc(q[1]) + '</div>' +
        '<div class="choice-row">' + choices + '</div>' +
        '<div class="quiz-actions">' +
          (step > 1 ? '<button class="btn ghost" id="quizBack">上一題</button>' : '') +
          '<button class="btn ghost" id="quizCancel">取消</button>' +
        '</div></div>';
      panelEl.querySelectorAll('.choice').forEach(function (btn) {
        btn.addEventListener('click', function () {
          answers[q[0]] = btn.getAttribute('data-val');
          if (step < 4) { step += 1; draw(); }
          else { mode = 'results'; draw(); }
        });
      });
      var back = document.getElementById('quizBack');
      if (back) back.addEventListener('click', function () { step -= 1; draw(); });
      document.getElementById('quizCancel').addEventListener('click', function () {
        mode = 'home'; selected = null; draw();
      });
    }
    function resultCard(id, label, asAlt) {
      var r = DATA.resorts[id];
      return '<div class="result-card' + (asAlt ? ' alt' : '') + '">' +
        '<div class="kicker">' + esc(label) + '</div>' +
        '<div class="resort-name-row"><span class="resort-name">' + esc(r.name) + '</span><span class="resort-romaji">' + esc(r.romaji) + '</span></div>' +
        '<div class="why">' + esc(whyFor(r, answers, asAlt)) + '</div>' +
        '<div class="not-for">不適合誰：' + esc(r.not_for) + '</div>' +
        '<div class="card-actions">' +
          '<a class="btn" href="' + resortUrl(id) + '">看介紹</a>' +
          '<button class="btn secondary mark-map" data-region="' + r.region + '">在地圖上標出</button>' +
        '</div></div>';
    }
    function resultsPanel() {
      var picked = pickResults(answers);
      var html = '<div class="panel-head"><div><div class="panel-title">你的轉乘建議</div><div class="panel-desc">2 個主選、1 個備選。點進去看從台灣怎麼到。</div></div>' +
        '<button class="close-btn" id="closeBtn" aria-label="關閉">✕</button></div><div class="result-list">';
      picked.primary.forEach(function (id, i) { html += resultCard(id, i === 0 ? '主選' : '主選 2', false); });
      if (picked.alt) html += resultCard(picked.alt, '備選', true);
      html += '</div>';
      panelEl.innerHTML = html;
      document.getElementById('closeBtn').addEventListener('click', function () { mode = 'home'; selected = null; draw(); });
      panelEl.querySelectorAll('.mark-map').forEach(function (btn) {
        btn.addEventListener('click', function () {
          selected = btn.getAttribute('data-region');
          drawMap();
        });
      });
    }
    function regionPanel() {
      var region = DATA.regions[selected];
      var cards = region.resortIds.map(function (id) {
        var r = DATA.resorts[id];
        var hours = r.access_routes && r.access_routes[0] ? r.access_routes[0].hours : '';
        return '<div class="resort-card">' +
          '<div class="resort-name-row"><span class="resort-name">' + esc(r.name) + '</span><span class="resort-romaji">' + esc(r.romaji) + '</span></div>' +
          '<div class="resort-meta">' + esc(r.one_liner) + '</div>' +
          '<div class="tag-row">' + tagsHtml((r.tags || []).slice(0, 3)) + '</div>' +
          (hours ? '<div class="access-row">從台灣　<span class="access-value">' + esc(hours) + '</span></div>' : '') +
          '<div class="card-actions"><a class="card-link" href="' + resortUrl(id) + '">看介紹 ↗</a></div>' +
          '</div>';
      }).join('');
      var hub = '';
      if (selected === 'niigata') hub = '<p class="muted">越後湯澤是樞紐，不是一座場。先看 <a class="card-link" href="' + areaUrl('yuzawa') + '">越後湯澤轉乘表</a>。</p>';
      if (selected === 'nagano') hub = '<p class="muted">白馬谷有三座山。先看 <a class="card-link" href="' + areaUrl('hakuba-valley') + '">白馬谷轉乘表</a>。</p>';
      panelEl.innerHTML = '<div class="panel-head"><div><div class="panel-title">' + esc(region.name) + '</div><div class="panel-desc">' + esc(region.desc) + '</div></div>' +
        '<button class="close-btn" id="closeBtn" aria-label="關閉">✕</button></div>' + hub +
        '<div class="resort-list">' + cards + '</div>';
      document.getElementById('closeBtn').addEventListener('click', function () { selected = null; mode = 'home'; draw(); });
    }
    function draw() {
      drawMap();
      if (mode === 'quiz') quizPanel();
      else if (mode === 'results') resultsPanel();
      else if (mode === 'region' && selected) regionPanel();
      else homePanel();
    }
    draw();
    if (location.hash === '#quiz') {
      location.replace(rootPath() + 'go.html');
      return;
    } else if (location.hash && DATA.regions[location.hash.slice(1)]) {
      selectRegion(location.hash.slice(1));
    }
    window.addEventListener('hashchange', function () {
      if (location.hash === '#quiz') { location.replace(rootPath() + 'go.html'); }
      if (location.hash === '#map') { mode = 'home'; selected = null; draw(); mountChrome('map'); }
    });
  }

  function renderGo() {
    mountChrome('quiz');
    var el = document.getElementById('go');
    var answers = { q1: null, q2: null, q3: null, q4: null };
    var step = 1;
    var mode = 'quiz';
    var params = new URLSearchParams(location.search);
    var decoded = decodeAnswers(params.get('a'));
    if (decoded) {
      answers = decoded;
      mode = 'results';
    }

    function syncUrl() {
      if (mode !== 'results') return;
      var next = goPageBase() + '?a=' + encodeAnswers(answers);
      if (location.pathname + location.search !== next && location.search !== '?a=' + encodeAnswers(answers)) {
        history.replaceState(null, '', next);
      }
    }
    function draw() {
      if (mode === 'results') {
        syncUrl();
        resultsView();
      } else quizView();
    }
    function quizView() {
      var qMap = { 1: ['q1', '程度', Q1_OPTS], 2: ['q2', '這趟怎麼走', Q2_OPTS], 3: ['q3', '同行', Q3_OPTS], 4: ['q4', '這趟最在乎', Q4_OPTS] };
      var q = qMap[step];
      var choices = q[2].map(function (opt) {
        var sel = answers[q[0]] === opt[0] ? ' selected' : '';
        return '<button class="choice' + sel + '" data-val="' + opt[0] + '">' + esc(opt[1]) + '</button>';
      }).join('');
      el.innerHTML = '<div class="quiz go-quiz">' +
        '<div class="season-chip">2026–27 雪季</div>' +
        '<div class="quiz-progress">選場 ' + step + ' / 4</div>' +
        '<div class="quiz-q">' + esc(q[1]) + '</div>' +
        '<div class="choice-row">' + choices + '</div>' +
        '<div class="quiz-actions">' +
          (step > 1 ? '<button class="btn ghost" id="quizBack">上一題</button>' : '') +
        '</div></div>';
      el.querySelectorAll('.choice').forEach(function (btn) {
        btn.addEventListener('click', function () {
          answers[q[0]] = btn.getAttribute('data-val');
          if (step < 4) { step += 1; draw(); }
          else { mode = 'results'; draw(); }
        });
      });
      var back = document.getElementById('quizBack');
      if (back) back.addEventListener('click', function () { step -= 1; draw(); });
    }
    function resultsView() {
      var picked = pickResults(answers);
      var avoid = avoidFor(answers);
      var primary = picked.primary.map(function (id) {
        var r = DATA.resorts[id];
        return '<div class="share-row pick"><span class="label">主選</span><div><div class="name">' + esc(r.name) + '</div><div class="why-line">' + esc(whyFor(r, answers, false)) + '</div></div></div>';
      }).join('');
      var avoidR = DATA.resorts[avoid.id];
      var avoidHtml = '<div class="share-row avoid"><span class="label">不要</span><div><div class="name">' + esc(avoidR.name) + '</div><div class="why-line">' + esc(avoid.line) + '</div></div></div>';
      var idBtns = picked.primary.map(function (id) {
        return '<a class="btn secondary" href="' + resortUrl(id) + '">看 ' + esc(DATA.resorts[id].name) + ' 介紹</a>';
      }).join('');
      el.innerHTML = '<div class="quiz">' +
        '<div class="share-card" id="shareCard">' +
          '<div class="share-kicker">雪國轉運站 · 2026–27</div>' +
          '<div class="share-you">你：' + esc(youLine(answers)) + '</div>' +
          primary + avoidHtml +
        '</div>' +
        '<div class="card-actions" style="margin-top:16px">' +
          '<button class="btn" id="copyLink">複製連結</button>' +
          '<span class="copy-ok" id="copyOk" hidden>已複製，可貼到社團</span>' +
        '</div>' +
        '<p class="muted">截圖上面這張卡丟回去最快。連結打開會是同一份建議。</p>' +
        '<div class="card-actions">' + idBtns + '</div>' +
        '<div class="quiz-actions"><button class="btn ghost" id="again">重填一輪</button></div>' +
        '</div>';
      document.getElementById('copyLink').addEventListener('click', function () {
        var url = localShareUrl(answers);
        function ok() {
          var n = document.getElementById('copyOk');
          n.hidden = false;
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(ok).catch(function () { window.prompt('複製這條連結', url); ok(); });
        } else {
          window.prompt('複製這條連結', url);
          ok();
        }
      });
      document.getElementById('again').addEventListener('click', function () {
        answers = { q1: null, q2: null, q3: null, q4: null };
        step = 1;
        mode = 'quiz';
        history.replaceState(null, '', goPageBase());
        draw();
      });
    }
    draw();
  }

  function fact(label, value) {
    return '<div class="fact"><dt>' + esc(label) + '</dt><dd>' + esc(value) + '</dd></div>';
  }
  function routesHtml(routes) {
    return '<ul class="route-list">' + (routes || []).map(function (rt) {
      return '<li><div class="route-from">' + esc(rt.from) + '　<span class="route-hours">' + esc(rt.hours) + '</span></div><div class="muted">' + esc(rt.steps) + '</div></li>';
    }).join('') + '</ul>';
  }
  function linksHtml(links, skipUrls) {
    skipUrls = skipUrls || {};
    var kept = (links || []).filter(function (l) { return !skipUrls[l.url]; });
    if (!kept.length) return '';
    var items = kept.map(function (l) {
      var typeLabel = { overview: '總覽', access: '交通', hotel: '住宿', slope: '雪道', pitfall: '避雷' }[l.type] || l.type;
      return '<li><a href="' + esc(l.url) + '" target="_blank" rel="noopener noreferrer"><span>' + esc(l.title) + '</span></a>' +
        '<span class="link-source muted">' + esc(typeLabel) + ' · ' + esc(l.source) + '</span></li>';
    }).join('');
    return '<div class="section"><h2>延伸閱讀</h2><ul class="link-list" style="list-style:none;margin:0;padding:0">' + items + '</ul></div>';
  }
  function expertsHtml(ex) {
    if (!ex || !ex.consensus) return '';
    var cons = '<ol>' + ex.consensus.map(function (c) { return '<li>' + esc(c) + '</li>'; }).join('') + '</ol>';
    var dis = ex.disagreement ? '<div class="disagree">達人有分歧：' + esc(ex.disagreement) + '</div>' : '';
    var chips = '<div class="source-chips">' + (ex.sources || []).map(function (s) {
      var k = s.kind === 'coach' ? '教練' : '部落客';
      return '<a href="' + esc(s.url) + '" target="_blank" rel="noopener noreferrer">' + esc(s.name) + ' · ' + k + ' ↗</a>';
    }).join('') + '</div>';
    return '<div class="section"><h2>看看達人怎麼說</h2><p class="section-note">本站整理，請讀原文</p><div class="expert-card">' + cons + dis + chips + '</div></div>';
  }
  function communityHtml(list) {
    if (!list || !list.length) return '';
    var groups = { threads: [], public_fb: [], jp_review: [] };
    list.forEach(function (q) { (groups[q.source_kind] || groups.jp_review).push(q); });
    function block(title, arr) {
      if (!arr.length) return '';
      var cards = arr.map(function (q) {
        var orig = q.original ? '<div class="quote-orig">' + esc(q.original) + '</div>' : '';
        var label = q.date + (q.theme === 'snow' ? ' · 上季／雪況' : '');
        return '<div class="quote-card"><blockquote>' + esc(q.quote) + '</blockquote>' + orig +
          '<div class="quote-meta">' + esc(q.source) + ' · ' + esc(label) + ' · <a href="' + esc(q.url) + '" target="_blank" rel="noopener noreferrer">原文</a></div></div>';
      }).join('');
      return '<div class="community-group"><h3>' + title + '</h3>' + cards + '</div>';
    }
    var tw = block('台灣雪友', groups.threads.concat(groups.public_fb));
    var jp = block('日本當地', groups.jp_review);
    return '<div class="section"><h2>看看社群怎麼說</h2><p class="section-note">本站整理，請讀原文。雪況類引用有日期，不是即時雪況。</p>' + tw + jp + '</div>';
  }

  function renderResort(id) {
    mountChrome('map');
    var r = DATA.resorts[id];
    var el = document.getElementById('page');
    if (!r || !el) return;
    var skip = {};
    (r.experts && r.experts.sources || []).forEach(function (s) { skip[s.url] = true; });
    var compare = (r.compare_with || []).map(function (cid) {
      var o = DATA.resorts[cid];
      return o ? '<a class="card-link" href="' + resortUrl(cid) + '">' + esc(o.name) + '</a>' : '';
    }).filter(Boolean).join(' · ');
    var pitfalls = (r.pitfalls || []).map(function (p) { return '<li>' + esc(p) + '</li>'; }).join('');
    var budget = r.budget_twd
      ? '<div class="budget"><span class="budget-num">NT$' + r.budget_twd.min.toLocaleString() + '–' + r.budget_twd.max.toLocaleString() + '</span><span class="muted">' + esc(r.budget_twd.days + ' 天自助約，' + r.budget_twd.note) + '</span></div>'
      : '';
    var rhythm = r.snow_rhythm ? '<div class="section"><h2>一日雪質節奏</h2><p>' + esc(r.snow_rhythm) + '</p></div>' : '';
    var companion = r.companion_note ? '<div class="section"><h2>不滑雪的人</h2><p>' + esc(r.companion_note) + '</p></div>' : '';
    var delta = r.season_delta ? '<div class="section"><h2>這季備註</h2><p>' + esc(r.season_delta) + '</p></div>' : '';
    var region = DATA.regions[r.region];
    var hubLink = '';
    if (r.cluster === 'yuzawa') hubLink = ' · <a href="' + areaUrl('yuzawa') + '">越後湯澤樞紐</a>';
    if (r.cluster === 'hakuba') hubLink = ' · <a href="' + areaUrl('hakuba-valley') + '">白馬谷樞紐</a>';
    el.innerHTML = '<div class="crumb"><a href="' + rootPath() + 'index.html">轉運站</a> · <a href="' + rootPath() + 'index.html#' + r.region + '">' + esc(region.name) + '</a>' + hubLink + '</div>' +
      '<div class="resort-name-row"><h1 class="page-title">' + esc(r.name) + '</h1><span class="resort-romaji">' + esc(r.romaji) + '</span></div>' +
      '<div class="muted">' + esc(r.prefecture) + '</div>' +
      '<div class="tag-row">' + tagsHtml(r.tags) + '</div>' +
      '<div class="verdict"><p><strong>本站怎麼判　</strong>' + esc(r.one_liner) + '</p><p class="not-for">不適合誰：' + esc(r.not_for) + '</p></div>' +
      '<div class="section"><h2>從台灣怎麼到</h2>' + routesHtml(r.access_routes) + '</div>' +
      '<div class="section"><h2>5 天預算帶</h2>' + budget + '</div>' +
      '<div class="section"><h2>運行資訊</h2><div class="grid-5">' +
        fact('夜滑', r.night_ski) + fact('溫泉', r.onsen) + fact('中文教練', r.chinese_coach) +
        fact('Ski-in/out', r.ski_in_out) + fact('中文辦事', r.chinese_service) +
      '</div><p class="muted" style="margin-top:10px">' + esc(r.season_note || '') + '</p></div>' +
      rhythm +
      '<div class="section"><h2>現場坑</h2><ul class="pitfalls">' + pitfalls + '</ul></div>' +
      companion +
      expertsHtml(r.experts) +
      communityHtml(r.community) +
      delta +
      (compare ? '<div class="section"><h2>不要和它搞混</h2><p>' + compare + '</p></div>' : '') +
      linksHtml(r.links, skip);
  }

  function renderArea(id) {
    mountChrome('map');
    var a = DATA.areas[id];
    var el = document.getElementById('page');
    if (!a || !el) return;
    var cards = a.resortIds.map(function (rid) {
      var r = DATA.resorts[rid];
      return '<div class="resort-card"><div class="resort-name-row"><span class="resort-name">' + esc(r.name) + '</span><span class="resort-romaji">' + esc(r.romaji) + '</span></div>' +
        '<p class="why">' + esc(r.one_liner) + '</p><p class="not-for">不適合誰：' + esc(r.not_for) + '</p>' +
        '<a class="card-link" href="' + resortUrl(rid) + '">看介紹 ↗</a></div>';
    }).join('');
    el.innerHTML = '<div class="crumb"><a href="' + rootPath() + 'index.html">轉運站</a></div>' +
      '<div class="resort-name-row"><h1 class="page-title">' + esc(a.name) + '</h1><span class="resort-romaji">' + esc(a.romaji) + '</span></div>' +
      '<div class="verdict"><p>' + esc(a.one_liner) + '</p></div>' +
      '<p>' + esc(a.desc) + '</p>' +
      '<div class="section"><h2>先選山再出發</h2><div class="resort-list">' + cards + '</div></div>';
  }

  function renderCompare() {
    mountChrome('compare');
    var el = document.getElementById('page');
    var groups = DATA.compare;
    el.innerHTML = '<div class="crumb"><a href="index.html">轉運站</a></div><h1 class="page-title" id="hokkaido">二世谷、留壽都、富良野怎麼選</h1><p class="muted">北海道三選、東京側短待、長野三選。要「該去哪」請用 <a class="card-link" href="go.html">30 秒選場</a>。</p>' +
      groups.map(function (g) {
        var heads = '<th></th>' + g.ids.map(function (id) {
          var r = DATA.resorts[id];
          return '<th><a href="' + resortUrl(id) + '">' + esc(r.name) + '</a><div class="resort-romaji">' + esc(r.romaji) + '</div></th>';
        }).join('');
        var rows = [
          ['適合誰', 'one_liner'],
          ['不適合誰', 'not_for'],
          ['從台灣怎麼到', 'hours'],
          ['預算帶', 'budget'],
          ['中文教練', 'chinese_coach'],
          ['粉雪', 'powder'],
          ['新手友善', 'beginner']
        ].map(function (row) {
          var cells = g.ids.map(function (id) {
            var r = DATA.resorts[id];
            var val = '';
            if (row[1] === 'hours') val = r.access_routes[0].hours;
            else if (row[1] === 'budget') val = 'NT$' + r.budget_twd.min.toLocaleString() + '–' + r.budget_twd.max.toLocaleString();
            else if (row[1] === 'powder') val = r.scores.powder + '/5';
            else if (row[1] === 'beginner') val = r.scores.beginner + '/5';
            else val = r[row[1]];
            return '<td>' + esc(val) + '</td>';
          }).join('');
          return '<tr><th>' + esc(row[0]) + '</th>' + cells + '</tr>';
        }).join('');
        return '<div class="section"><h2>' + esc(g.title) + '</h2><div style="overflow:auto"><table class="compare-table"><thead><tr>' + heads + '</tr></thead><tbody>' + rows + '</tbody></table></div></div>';
      }).join('');
  }

  window.Hub = {
    mountChrome: mountChrome,
    renderIndex: renderIndex,
    renderGo: renderGo,
    renderResort: renderResort,
    renderArea: renderArea,
    renderCompare: renderCompare,
    pickResults: pickResults,
    scoreResort: scoreResort,
    vetoPrimary: vetoPrimary
  };
})();
