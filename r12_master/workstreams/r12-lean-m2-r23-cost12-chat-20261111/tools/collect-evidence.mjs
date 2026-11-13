import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const lean=path.join(root,'lean'), digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const scan=JSON.parse(fs.readFileSync(path.join(lean,'logs/source-scan.json'),'utf8'));
let doc='# Exact Lean declaration statements\n\nVerbatim source signatures. Consult CI_STATUS.json for actual verification.\nAll definitions and proof bodies are retained in the standard .lean files.\n\n';
for(const d of scan.declarations){
  const f=d.file.replaceAll('\\','/'),source=fs.readFileSync(path.join(lean,f),'utf8');
  const m=new RegExp('^(?:noncomputable )?(?:theorem|lemma|def|abbrev) '+d.name+'\\b','m').exec(source);
  if(!m)throw Error('Cannot locate '+d.name);
  let depth=0,stop=-1;
  for(let i=m.index;i<source.length;i++){
    if('([{'.includes(source[i]))depth++;
    if(')]}'.includes(source[i]))depth--;
    if(depth===0&&source.slice(i,i+2)===':='){stop=i;break;}
  }
  if(stop<0)throw Error('Missing body '+d.name);
  doc+='## EG617.'+d.name+'\n\nSource: '+f+'\n\n```lean\n'+source.slice(m.index,stop).trim()+'\n```\n\n';
}
fs.writeFileSync(path.join(root,'DECLARATION_STATEMENTS.md'),doc);
const repo=path.resolve(root,'../../..'),oldScope='r12_master/workstreams/r12-lean-m1-m2-chat-20261109/lean/';
const baseline='7b39c1aa90e8685dd7ec34f2c7f02c9c7ccdc871';
const files=execFileSync('git',['-C',repo,'ls-tree','-r','--name-only',baseline,'--',oldScope],{encoding:'utf8'}).trim().split('\n');
const comparison=[];
for(const f of files){
  const rel=f.slice(oldScope.length);
  if(!rel.endsWith('.lean')||rel==='EG617.lean'||rel.startsWith('EG617/Audit/'))continue;
  const before=execFileSync('git',['-C',repo,'show',baseline+':'+f]),after=fs.readFileSync(path.join(lean,rel));
  comparison.push({file:rel,before:digest(before),after:digest(after),unchanged:before.equals(after)});
}
if(comparison.some(r=>!r.unchanged))throw Error('Baseline mathematical source changed');
fs.writeFileSync(path.join(root,'logs/baseline-source-preservation.json'),JSON.stringify({baseline,status:'PASS',comparison},null,2)+'\n');
const [run,sha]=process.argv.slice(2);
if(!run||!sha){console.log('Statements and baseline comparison generated; no new kernel audit claimed.');process.exit(0);}
const raw=fs.readFileSync(path.join(root,'logs',`linux-${run}-full.txt`),'utf8');
const log=raw.replace(/^\d{4}-\d\d-\d\dT\S+Z /gm,'');
if(!log.includes('KERNEL_AND_AXIOM_CHECKS_PASS; ORIGINAL_MAIN_THEOREM_NOT_PROVED'))throw Error('No complete audit marker');
const expected=scan.declarations.map(d=>'EG617.'+d.name), reports=new Map();
for(const m of log.matchAll(/'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])/g)){
  if(expected.includes(m[1]))reports.set(m[1],(m[2]||'').split(',').map(s=>s.trim()).filter(Boolean));
}
const allowed=new Set(['propext','Classical.choice','Quot.sound']);
if(expected.some(n=>!reports.has(n)))throw Error('Incomplete axiom output');
for(const [n,ax] of reports)for(const a of ax)if(!allowed.has(a))throw Error(n+' uses '+a);
const hashes=[];
for(const m of log.matchAll(/^SOURCE_SHA256 ([a-f0-9]{64}) (.+)$/gm)){
  const f=m[2].trim(),actual=digest(fs.readFileSync(path.join(lean,f)));
  if(actual!==m[1])throw Error('CI/local hash mismatch '+f);
  hashes.push({file:f,sha256:actual});
}
if(hashes.length<scan.files.length+2)throw Error('Incomplete source/config hashes');
const pins=[...log.matchAll(/^PIN_PASS (\S+) ([a-f0-9]{40})$/gm)].map(m=>({name:m[1],rev:m[2]}));
const manifest=JSON.parse(fs.readFileSync(path.join(lean,'lake-manifest.json'),'utf8'));
if(pins.length!==9||manifest.packages.some(p=>!pins.some(q=>q.name===p.name&&q.rev===p.rev)))throw Error('Dependency pin mismatch');
const status={date:'2026-11-13',sha,run:Number(run),url:`https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/${run}`,
  cleanLinuxBuild:'PASS',fullAxiomAudit:'PASS',statementInspection:'PASS',localMatchesCISHA256:'PASS',
  declarations:expected.length,theorems:scan.declarations.filter(d=>['theorem','lemma'].includes(d.kind)).length,
  originalMathematicalSourcesUnchanged:true,pins,hashes,Gate47:'FORMALIZATION_GAP',MainTheorem:'ABSENT'};
fs.writeFileSync(path.join(root,'CI_STATUS.json'),JSON.stringify(status,null,2)+'\n');
fs.writeFileSync(path.join(root,'logs/verified-axioms.json'),JSON.stringify(Object.fromEntries(reports),null,2)+'\n');
let audit='# Complete transitive axiom audit\n\nVerified code commit '+sha+', Linux CI '+run+'.\n\n'+
  'All '+expected.length+' project declarations compiled and audited. Allowed logical axioms: propext, Classical.choice, Quot.sound.\n'+
  'Source scan and kernel audit both passed. No sorry/admit/custom axiom/unsafe/implemented_by/native_decide is used.\n'+
  'No diagnostic enumeration is imported into Lean. All graph hypotheses appear in DECLARATION_STATEMENTS.md.\n'+
  'Unfinished results are absent proofs: complete type classification, Cost-6, sharp R335/R336, GATE47 and MainTheorem.\n\n'+
  '| Declaration | Transitive axioms |\n|---|---|\n';
for(const n of expected)audit+='| '+n+' | '+(reports.get(n).join(', ')||'none')+' |\n';
for(const f of ['LEAN_AXIOM_AUDIT.md','AXIOM_AUDIT.md'])fs.writeFileSync(path.join(root,f),audit);
console.log(JSON.stringify(status,null,2));
