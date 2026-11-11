#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/lean"
export LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-2}"
mkdir -p logs
lean --version | tee logs/linux-lean-version.txt
grep -F 'version 4.35.0' logs/linux-lean-version.txt
grep -F 'eb6cafb7290e8bd5f2937522d8d804f58f02bafc' logs/linux-lean-version.txt
lake --version | tee logs/linux-lake-version.txt
sha256sum lean-toolchain lakefile.lean lake-manifest.json > logs/config-before.sha256
lake exe cache get Mathlib.Combinatorics.SimpleGraph.FiveWheelLike Mathlib.Combinatorics.SimpleGraph.DegreeSum Mathlib.Combinatorics.SimpleGraph.Extremal.Turan Mathlib.Tactic.IntervalCases Mathlib.Tactic.NormNum Mathlib.Algebra.Order.BigOperators.Group.Finset 2>&1 | tee logs/linux-cache.txt
sha256sum -c logs/config-before.sha256
node - <<'NODE'
const fs=require('fs'),cp=require('child_process');
const m=JSON.parse(fs.readFileSync('lake-manifest.json'));
if(m.packages.length!==9)throw Error('Expected nine pinned dependencies');
for(const p of m.packages){
  const actual=cp.execFileSync('git',['-C',`.lake/packages/${p.name}`,'rev-parse','HEAD'],{encoding:'utf8'}).trim();
  if(actual!==p.rev)throw Error(`Pin mismatch: ${p.name}`);
  console.log('PIN_PASS',p.name,actual);
}
NODE
lake clean eg617r12
result=0
for mod in EG617.Combinatorics.TuranArithmetic EG617.Frontend.EdgeCounting EG617.Frontend.TuranBounds EG617.Frontend.HereditaryCaps EG617.Core.Admissibility EG617.Core.R224; do
  if lake build "+$mod" 2>&1 | tee "logs/linux-$mod.txt"; then
    echo "MODULE_PASS $mod"
  else
    echo "MODULE_FAIL $mod"
    result=1
  fi
done
if [ "$result" != 0 ]; then exit "$result"; fi
lake build 2>&1 | tee logs/build.txt
node scripts/check-source.mjs
lake build +EG617.Audit.Axioms 2>&1 | tee logs/axioms.txt
node scripts/check-axioms.mjs
lake build +EG617.Audit.Statements 2>&1 | tee logs/statements.txt
node - <<'NODE'
const fs=require('fs'),crypto=require('crypto'),path=require('path');
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):e.name.endsWith('.lean')?[path.join(d,e.name)]:[])}
const files=['EG617.lean','lakefile.lean','lean-toolchain','lake-manifest.json',...walk('EG617')].sort();
for(const f of files)console.log('SOURCE_SHA256',crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex'),f);
NODE
echo 'KERNEL_AND_AXIOM_CHECKS_PASS; ORIGINAL_MAIN_THEOREM_NOT_PROVED'
