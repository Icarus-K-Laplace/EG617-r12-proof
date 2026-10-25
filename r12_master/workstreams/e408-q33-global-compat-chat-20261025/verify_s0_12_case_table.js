#!/usr/bin/env node
"use strict";

/*
Arithmetic certificate for the S0=12 support-boundary case split.
This checks only the integer incidence table, not the graph-theoretic lemmas
or the K12 contradictions in R12_E408_Q33_S0_12_EXCLUSION.md.
*/

function assert(ok, message) {
  if (!ok) throw new Error(message);
}
function popcount(mask) {
  let n = 0;
  for (let x = mask; x; x &= x - 1) n++;
  return n;
}
function subsetsOfSize(n, k) {
  const out = [];
  for (let mask = 0; mask < (1 << n); mask++) {
    if (popcount(mask) === k) out.push(mask);
  }
  return out;
}
function minRequiredTExcess(n7, a, highMasks) {
  let total = 0;
  for (let t = 0; t < 7; t++) {
    let degreeFromW = n7 + a;
    for (const mask of highMasks) degreeFromW += (mask >>> t) & 1;
    total += Math.max(0, degreeFromW - 6);
  }
  return total;
}
function key(x) {
  return [x.n7, x.mode, x.b, x.a, x.epsT, x.m, x.A].join("|");
}

const found = [];
// N7=2: all remaining fourteen W vertices have q=8.
for (let a = 0; a <= 14; a++) {
  const epsT = 7 * 2 + 7 * a - 42;
  if (a > 6 - 2 || epsT < 0 || epsT > 4) continue;
  if (minRequiredTExcess(2, a, []) > epsT) continue;
  const m = 14 - a, A = a;
  assert(8 * m === 84 - epsT - A, "N7=2 incidence identity failed");
  found.push({ n7: 2, mode: "none", b: "-", a, epsT, m, A });
}

// N7=3: one q=9 vertex; b is its T-neighborhood size.
for (const b of [0, 1, 7]) {
  for (let a = 0; a <= 12; a++) {
    const epsT = 7 * 3 + 7 * a + b - 42;
    if (epsT < 0 || epsT > 4 || a > (b === 7 ? 2 : 3)) continue;
    for (const high of subsetsOfSize(7, b)) {
      if (minRequiredTExcess(3, a, [high]) > epsT) continue;
      const m = 12 - a, A = a + 9 - b;
      assert(8 * m === 84 - epsT - A, "N7=3 incidence identity failed");
      found.push({ n7: 3, mode: "one9", b, a, epsT, m, A });
      break;
    }
  }
}

// N7=4: either two q=9 vertices or one q=10 vertex.
for (const b1 of [0, 1, 7]) {
  for (const b2 of [0, 1, 7]) {
    for (let a = 0; a <= 10; a++) {
      const epsT = 7 * 4 + 7 * a + b1 + b2 - 42;
      if (epsT < 0 || epsT > 4 || a > 2) continue;
      let feasible = false;
      for (const H1 of subsetsOfSize(7, b1)) {
        for (const H2 of subsetsOfSize(7, b2)) {
          if (minRequiredTExcess(4, a, [H1, H2]) <= epsT) feasible = true;
        }
      }
      if (!feasible) continue;
      const m = 10 - a, A = a + 18 - b1 - b2;
      assert(8 * m === 84 - epsT - A, "N7=4 two-q9 incidence identity failed");
      found.push({ n7: 4, mode: "two9", b: [b1, b2].sort().join(","), a, epsT, m, A });
    }
  }
}
for (const b of [0, 1, 2, 7]) {
  for (let a = 0; a <= 11; a++) {
    const epsT = 7 * 4 + 7 * a + b - 42;
    if (epsT < 0 || epsT > 4 || a > 2) continue;
    for (const high of subsetsOfSize(7, b)) {
      if (minRequiredTExcess(4, a, [high]) > epsT) continue;
      const m = 11 - a, A = a + 10 - b;
      assert(8 * m === 84 - epsT - A, "N7=4 q10 incidence identity failed");
      found.push({ n7: 4, mode: "one10", b, a, epsT, m, A });
      break;
    }
  }
}

const normalized = [...new Map(found.map(x => [key(x), x])).values()]
  .sort((x, y) => key(x).localeCompare(key(y)));
const expected = [
  "2|none|-|4|0|10|4",
  "3|one9|0|3|0|9|12",
  "3|one9|1|3|1|9|11",
  "3|one9|7|2|0|10|4",
  "4|two9|0,0|2|0|8|20",
  "4|two9|0,1|2|1|8|19",
  "4|two9|1,1|2|2|8|18",
  "4|two9|0,7|1|0|9|12",
  "4|two9|1,7|1|1|9|11",
  "4|two9|7,7|0|0|10|4",
  "4|one10|0|2|0|9|12",
  "4|one10|1|2|1|9|11",
  "4|one10|2|2|2|9|10",
  "4|one10|7|1|0|10|4"
].sort();
const actual = normalized.map(key).sort();
assert(actual.length === expected.length, "unexpected number of incidence profiles: " + actual.length);
assert(actual.every((x, i) => x === expected[i]), "incidence profile table mismatch");
process.stdout.write(JSON.stringify({
  result: "PASS",
  profiles: normalized.length,
  table: normalized,
  scope: "integer incidence table only; graph-theoretic exclusions are proved in the Markdown proof"
}, null, 2) + "\n");
