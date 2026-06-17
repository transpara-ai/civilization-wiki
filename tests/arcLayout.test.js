const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const L = require('../compile/assets/civilizationArcLayout.js');

function loadData() {
  const code = fs.readFileSync(path.join(__dirname, '../compile/assets/civilizationArcData.js'), 'utf8');
  const w = {}; new Function('window', code)(w); return w.CIVILIZATION_ARC_DATA;
}

test('scaleX maps domain endpoints to the plot edges', () => {
  const sx = L.scaleX({ start: 0, end: 15 }, 100, 1000);
  assert.strictEqual(sx(0), 100);
  assert.strictEqual(sx(15), 1000);
});

test('buildLayout yields 3 tracks; gates expands into 4 family rows', () => {
  const lay = L.buildLayout(loadData(), { width: 1600 });
  assert.deepStrictEqual(lay.tracks.map(t => t.id), ['construction', 'gates', 'worklist']);
  assert.strictEqual(lay.tracks.find(t => t.id === 'gates').rows.length, 4);
});

test('every gate lands in exactly one family row (none dropped)', () => {
  const data = loadData();
  const lay = L.buildLayout(data, { width: 1600 });
  const placed = lay.tracks.find(t => t.id === 'gates').rows.reduce((n, r) => n + r.items.length, 0);
  assert.strictEqual(placed, data.items.filter(i => i.type === 'gate').length);
});

test('nowX === scaleX(deriveNow); frontier is 13.9', () => {
  const lay = L.buildLayout(loadData(), { width: 1600 });
  assert.ok(Math.abs(lay.nowSeq - 13.9) < 1e-9);
  assert.strictEqual(lay.nowX, lay.scaleX(lay.nowSeq));
});

test('collapsing the gates track reduces contentHeight', () => {
  const data = loadData();
  const full = L.buildLayout(data, { width: 1600 });
  const coll = L.buildLayout(data, { width: 1600, collapsed: { gates: true } });
  assert.ok(coll.contentHeight < full.contentHeight);
});

test('markers within a row are placed in non-decreasing seq order', () => {
  const xs = L.buildLayout(loadData(), { width: 1600 }).tracks[0].rows[0].items.map(p => p.x);
  for (let i = 1; i < xs.length; i++) assert.ok(xs[i] >= xs[i - 1]);
});
