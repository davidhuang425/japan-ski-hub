// /go 選場邏輯測資。用法：
//   node scripts/test_go.js            跑全部測資，任何一組失敗就 exit 1
//   node scripts/test_go.js --dump     印出每組的主選／備選／不要（存基準用）
//
// 規則來源：product-spec-s1.md 第 5 節。4 段答案（舊連結）視為 q5 = unsure。
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.join(__dirname, '..');
const ctx = {
  console,
  URL,
  URLSearchParams,
  document: { body: { getAttribute: () => '0' }, getElementById: () => null, querySelectorAll: () => [] },
  location: { hostname: 'localhost', href: 'http://localhost/go.html', origin: 'http://localhost', search: '', hash: '' },
  history: { replaceState() {} },
  navigator: {},
  addEventListener() {},
};
ctx.window = ctx;
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'data.js'), 'utf8').replace(/^var DATA/, 'DATA'), ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'app.js'), 'utf8'), ctx);
const Hub = ctx.Hub;
const R = ctx.DATA.resorts;

function run(code) {
  const a = Hub.decodeAnswers(code);
  if (!a) throw new Error('decode failed: ' + code);
  const p = Hub.pickResults(a);
  return { primary: p.primary, alt: p.alt, avoid: Hub.avoidFor(a, p.primary.concat(p.alt ? [p.alt] : [])).id };
}

const HOKKAIDO = Object.keys(R).filter((id) => R[id].region === 'hokkaido');
const any = (list, ids) => ids.some((id) => list.includes(id));
const none = (list, ids) => !ids.some((id) => list.includes(id));

// [名稱, 答案, 檢查函式]
const CASES = [
  ['東京當日新手', 'first.tokyo_day.skiers.access', (r) => any(r.primary, ['gala-yuzawa', 'karuizawa']) && none(r.primary, HOKKAIDO.concat(['happo-one']))],
  ['北海道粉雪', 'powder.hokkaido.skiers.powder', (r) => any(r.primary, ['niseko', 'rusutsu', 'kiroro']) && none(r.primary, ['gala-yuzawa', 'karuizawa'])],
  ['親子度假', 'green.hokkaido.kids.onsen', (r) => any(r.primary, ['rusutsu', 'tomamu']) && none(r.primary, ['happo-one'])],
  ['第一次本州', 'first.tokyo_transfer.mixed.coach', (r) => any(r.primary, ['naeba', 'gala-yuzawa', 'tsugaike']) && none(r.primary, ['happo-one', 'shiga-kogen'])],
  ['第一次別去八方', 'first.undecided.skiers.access', (r) => none(r.primary, ['happo-one'])],
  ['有人不滑', 'green.tokyo_transfer.non_skier.onsen', (r) => any(r.primary, ['nozawa', 'karuizawa', 'zao'])],
  ['預算可控', 'green.tokyo_transfer.skiers.budget', (r) => any(r.primary, ['gala-yuzawa', 'ishiuchi', 'yuzawa-kogen', 'naeba', 'appi']) && !(r.primary.length === 1 && r.primary[0] === 'niseko')],
  ['進階地形', 'red.tokyo_transfer.skiers.powder', (r) => any(r.primary, ['happo-one', 'kagura', 'shiga-kogen']) && none(r.primary, ['karuizawa'])],
];

// 第五題（幾月去）新增測資
const CASES_Q5 = [
  ['開季初期東京當日', 'first.tokyo_day.mixed.access.early', (r) => r.primary.includes('karuizawa') && none(r.primary, ['gala-yuzawa']) && r.avoid === 'gala-yuzawa'],
  ['春雪粉雪北海道', 'powder.hokkaido.skiers.powder.spring', (r) => (none(r.primary, ['niseko']) || r.avoid === 'niseko') && any(r.primary.concat([r.alt]), ['kiroro', 'niseko', 'furano'])],
  ['旺季有人不滑溫泉', 'green.tokyo_transfer.non_skier.onsen.peak', (r) => any(r.primary.concat([r.alt]), ['zao', 'nozawa'])],
  ['春雪第一次帶小孩', 'first.undecided.kids.coach.spring', (r) => r.primary.every((id) => (R[id].month_fit || {}).spring >= 2)],
];

// 舊 4 段連結在 q5 = unsure 下必須跟 5 段 unsure 完全一樣
const COMPAT = CASES.map(([n, c]) => [n + '（5 段 unsure）', c + '.unsure', null, c]);

const dump = process.argv.includes('--dump');
let fail = 0;
function check(name, code, fn) {
  let r;
  try { r = run(code); } catch (e) { console.log('ERROR ', name, code, e.message); fail++; return; }
  const ok = fn ? fn(r) : true;
  if (dump || !ok) console.log((ok ? 'ok    ' : 'FAIL  ') + name.padEnd(14) + ' ' + code.padEnd(42) + ' 主選=' + r.primary.join(',') + ' 備選=' + r.alt + ' 不要=' + r.avoid);
  if (!ok) fail++;
}
CASES.forEach(([n, c, f]) => check(n, c, f));
const hasQ5 = !!Hub.Q5_OPTS;
if (hasQ5) {
  CASES_Q5.forEach(([n, c, f]) => check(n, c, f));
  COMPAT.forEach(([n, c, _f, old]) => {
    const a = JSON.stringify(run(old)), b = JSON.stringify(run(c));
    if (a !== b) { console.log('FAIL  相容 ' + n + ' ' + a + ' vs ' + b); fail++; }
  });
}
console.log(fail ? fail + ' failed' : 'all passed (' + (CASES.length + (hasQ5 ? CASES_Q5.length + COMPAT.length : 0)) + ')');
process.exit(fail ? 1 : 0);
