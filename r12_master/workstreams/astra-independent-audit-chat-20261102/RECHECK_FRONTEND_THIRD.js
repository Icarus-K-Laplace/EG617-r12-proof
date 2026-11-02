#!/usr/bin/env node
"use strict";

// Independent third integer transcription of the contextual frontend recurrence.
// Run from any directory: node RECHECK_FRONTEND_THIRD.js
// The frozen FRONTEND_REPLAY.json is read from the sibling integration workstream.
// No imports from recurrence_a.py, recurrence_b.py, or the root verifier.

const fs = require("fs");
const path = require("path");

const HERE = __dirname;
const REPLAY = path.resolve(
  HERE,
  "../astra-global-root-integration-chat-20261031/FRONTEND_REPLAY.json"
);
const OUTPUT = path.join(HERE, "FRONTEND_THIRD_REPLAY_RESULT.json");
const LIMIT = 145;
const EMPTY_AT = {1: 12, 2: 24, 3: 37, 4: 49};
const SEEDS = {
  "2,23": 131,
  "3,35": 210,
  "3,36": 234,
  "4,47": 284,
  "4,48": 308
};

function choose2(n) {
  return n * (n - 1) / 2;
}
function ceildiv(x, y) {
  return Math.floor((x + y - 1) / y);
}
function turan(a, n) {
  const q = Math.floor(n / a);
  const r = n % a;
  return a * choose2(q) + q * r;
}
function cap(n) {
  return choose2(n) - 11 * turan(12, n);
}
function equal(a, b) {
  return JSON.stringify(a) === JSON.stringify(b);
}

function recompute() {
  const B = Array.from({length: 13}, () => Array(LIMIT + 1).fill(null));
  const maxOrder = Array(13).fill(0);

  for (let n = 0; n <= LIMIT; n++) B[0][n] = n === 0 ? 0 : null;
  for (let n = 0; n <= 11; n++) B[1][n] = choose2(n);
  maxOrder[1] = 11;

  for (let a = 2; a <= 12; a++) {
    B[a][0] = 0;
    for (let n = 1; n <= LIMIT; n++) {
      if ((EMPTY_AT[a] !== undefined && n >= EMPTY_AT[a]) ||
          B[a][n - 1] === null) continue;

      const generic = Math.max(
        turan(a, n),
        n > 2 ? ceildiv(n * B[a][n - 1], n - 2) : 0,
        SEEDS[`${a},${n}`] || 0
      );
      let best = Infinity;

      for (let h = 0; h < n; h++) {
        const m = n - h - 1;
        const core = B[a - 1][m];
        if (core === null) continue;

        let q = Math.max(
          turan(10, h),
          choose2(h + 1) - cap(h + 1),
          choose2(h) - cap(h)
        );

        if (h >= 11) {
          const beta = Math.max(0, m - maxOrder[a - 2]);
          if (core + beta > cap(m + 2)) continue;

          const k = Math.max(
            ceildiv(h - 10, 2),
            1 + (h >= 12 ? 1 : 0) + (h >= 13 ? 1 : 0)
          );

          let common = Math.max(q, beta - 1);
          for (let t = 1; t <= k; t++) {
            common = Math.max(
              common,
              t * beta - choose2(2 * t) + turan(a, 2 * t)
            );
          }

          let triangleFree = common;
          for (let t = 1; t <= k; t++) {
            triangleFree = Math.max(triangleFree, t * beta - t * t);
          }

          let triangle = null;
          if (a >= 3) {
            const gamma = Math.max(0, m - maxOrder[a - 3]);
            if (core + gamma <= cap(m + 3)) {
              triangle = Math.max(common, gamma - 3);
            }
          }
          q = triangle === null ? triangleFree : Math.min(triangleFree, triangle);
        }

        const row = Math.max(
          ceildiv(n * h, 2),
          choose2(h + 1) + q + core
        );
        best = Math.min(best, row);
      }

      if (Number.isFinite(best)) {
        const value = Math.max(generic, best);
        if (value <= cap(n)) B[a][n] = value;
      }
    }

    const firstEmpty = B[a].findIndex((v, n) => n > 0 && v === null);
    maxOrder[a] = firstEmpty < 0 ? LIMIT : firstEmpty - 1;
  }

  const nodes = [];
  for (let a = 1; a <= 12; a++) {
    for (let n = 0; n <= LIMIT; n++) {
      nodes.push({a, n, bound: B[a][n]});
    }
  }

  const outerStops = [];
  for (let d = 0; d <= 11; d++) {
    for (let j = 0; j <= 11; j++) {
      const a = 11 - j;
      const n = 144 - d - 12 * j;
      const budget = 870 - choose2(d + 1) - 66 * j;
      const bound = n >= 0 ? B[a][n] : null;
      outerStops.push({
        d, j, a, n, budget, bound,
        survives: bound !== null && bound <= budget
      });
    }
  }

  const T61Rows = [];
  const a = 5, n = 61;
  for (let h = 0; h <= 60; h++) {
    const m = n - h - 1;
    const core = B[a - 1][m];
    if (core === null) {
      T61Rows.push({h, excluded: "empty core"});
      continue;
    }

    let q = Math.max(
      turan(10, h),
      choose2(h + 1) - cap(h + 1),
      choose2(h) - cap(h)
    );
    if (h >= 11) {
      const beta = Math.max(0, m - maxOrder[a - 2]);
      if (core + beta > cap(m + 2)) {
        T61Rows.push({h, excluded: "pair density"});
        continue;
      }
      const k = Math.max(
        ceildiv(h - 10, 2),
        1 + (h >= 12 ? 1 : 0) + (h >= 13 ? 1 : 0)
      );
      let common = Math.max(q, beta - 1);
      for (let t = 1; t <= k; t++) {
        common = Math.max(
          common,
          t * beta - choose2(2 * t) + turan(a, 2 * t)
        );
      }
      let triangleFree = common;
      for (let t = 1; t <= k; t++) {
        triangleFree = Math.max(triangleFree, t * beta - t * t);
      }
      const gamma = Math.max(0, m - maxOrder[a - 3]);
      const triangle = core + gamma <= cap(m + 3)
        ? Math.max(common, gamma - 3)
        : null;
      q = triangle === null ? triangleFree : Math.min(triangleFree, triangle);
    }
    T61Rows.push({
      h, core, q_floor: q,
      row_floor: Math.max(ceildiv(n * h, 2), choose2(h + 1) + q + core)
    });
  }

  return {
    nodes,
    max_orders: Object.fromEntries(maxOrder.map((v, i) => [String(i), v])),
    outer_stops: outerStops,
    T61_rows: T61Rows
  };
}

function main() {
  const source = JSON.parse(fs.readFileSync(REPLAY, "utf8"));
  const computed = recompute();
  const checks = {
    node_count: computed.nodes.length,
    nodes_exact: equal(computed.nodes, source.nodes),
    max_orders_exact: equal(computed.max_orders, source.max_orders),
    outer_stop_count: computed.outer_stops.length,
    outer_stops_exact: equal(computed.outer_stops, source.outer_stops),
    T61_row_count: computed.T61_rows.length,
    T61_rows_exact: equal(computed.T61_rows, source.T61_rows)
  };
  const survivors = computed.outer_stops.filter(x => x.survives);
  checks.survivor_count = survivors.length;
  checks.survivor = survivors;
  checks.T61_terminal_rows = computed.T61_rows.filter(
    x => x.h === 12 || x.h === 13 || x.h === 14
  );
  checks.status = Object.values(checks).some(v => v === false) ||
                  survivors.length !== 1 ||
                  survivors[0].d !== 11 || survivors[0].j !== 6
    ? "FAIL" : "PASS";

  fs.writeFileSync(OUTPUT, JSON.stringify({
    source_file: path.relative(HERE, REPLAY),
    source_git_blob_sha: "36c0d50ae20feb1ca4ab878cc256d700df77e8c5",
    independent_implementation: "RECHECK_FRONTEND_THIRD.js",
    checks
  }, null, 2) + "\n");
  console.log(JSON.stringify(checks, null, 2));
  if (checks.status !== "PASS") process.exitCode = 1;
}

main();
