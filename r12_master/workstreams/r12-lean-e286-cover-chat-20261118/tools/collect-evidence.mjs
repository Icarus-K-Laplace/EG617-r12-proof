import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const [run,sha]=process.argv.slice(2);
const log=fs.readFileSync(path.join(root,'logs',`linux-${run}-full.txt`),'utf8').replace(/^\d{4}-\d\d-\d\dT\S+Z /gm,'');
if(!log.includes('KERNEL_AND_AXIOM_CHECKS_PASS; ORIGINAL_MAIN_THEOREM_NOT_PROVED'))throw Error('No complete build/audit marker');
const scan=JSON.parse(fs.readFileSync(path.join(root,'lean/logs/source-scan.json'),'utf8'));
const axioms=new Map();
for(const m of log.matchAll(/'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])/g))
 axioms.set(m[1],(m[2]||'').split(',').map(s=>s.trim()).filter(Boolean));
const allowed=['propext','Classical.choice','Quot.sound'];
for(const d of scan.declarations){
 const name='EG617.'+d.name;
 if(!axioms.has(name))throw Error('Missing audit '+name);
 for(const a of axioms.get(name))if(!allowed.includes(a))throw Error('Unexpected axiom '+a);
}
const hashes=[];
for(const m of log.matchAll(/^SOURCE_SHA256 ([a-f0-9]{64}) (.+)$/gm)){
 const f=m[2].trim(),b=fs.readFileSync(path.join(root,'lean',f));
 const actual=crypto.createHash('sha256').update(b).digest('hex');
 if(actual!==m[1])throw Error('Local/CI mismatch '+f);
 hashes.push({file:f,sha256:actual});
}
if(hashes.length<scan.files.length+2)throw Error('Incomplete hashes');
const pins=[...log.matchAll(/^PIN_PASS (\S+) ([a-f0-9]{40})$/gm)].map(m=>({name:m[1],rev:m[2]}));
const manifest=JSON.parse(fs.readFileSync(path.join(root,'lean/lake-manifest.json')));
if(pins.length!==9||manifest.packages.some(p=>!pins.some(q=>p.name===q.name&&p.rev===q.rev)))throw Error('Dependency pins');
const baseline=JSON.parse(fs.readFileSync(path.join(root,'baseline-ci.json')));
const excluded=['EG617.lean','EG617/Audit/Axioms.lean','EG617/Audit/Statements.lean'];
const preserved=baseline.hashes.filter(h=>!excluded.includes(h.file));
for(const h of preserved)if(!hashes.some(n=>n.file===h.file&&n.sha256===h.sha256))throw Error('Baseline source changed '+h.file);
const dag=log.includes('E286_ELABORATED_DEPENDENCY_AUDIT_PASS');
if(hashes.some(h=>h.file==='EG617/Audit/E286Dependencies.lean')&&!dag)throw Error('Missing elaborated dependency audit');
if(dag)for(const n of ['e286_actual_oriented_support_orbit','e286_first_support_orbit_impossible','e286_finite_support_orbit_check','e286_weighted_profiles_complete','e286_pair_blocker_complete','e286_k11_pair_local_charge','e286_excess_sum'])
 if(!log.includes('PROJECT_DEPENDENCIES EG617.'+n+':'))throw Error('Incomplete proof-body traversal: '+n);
const status={sha,run:Number(run),cleanLinuxBuild:'PASS',fullAxiomAudit:'PASS',statementInspection:'PASS',localMatchesCISHA256:'PASS',declarations:scan.declarations.length,theorems:scan.declarations.filter(d=>d.kind==='theorem'||d.kind==='lemma').length,pins,hashes,inheritedFilesPreserved:preserved.length,E286:'FORMALIZATION_GAP',edgeFloor287:'FORMALIZATION_GAP',COVER:'FORMALIZATION_GAP',MainTheorem:'ABSENT'};
status.elaboratedProjectDependencyAudit=dag?'PASS':'NOT_RUN';
status.remainingSupportOrbits=scan.declarations.some(d=>d.name==='e286_actual_support_seven_remaining')?7:scan.declarations.some(d=>d.name==='e286_actual_support_eight_remaining')?8:9;
status.strongestE286Reduction=status.remainingSupportOrbits===7?'e286_actual_support_seven_remaining':status.remainingSupportOrbits===8?'e286_actual_support_eight_remaining':'e286_actual_support_nine_remaining';
if(status.remainingSupportOrbits<=8)for(const n of ['e286_actual_support_eight_remaining','e286_private_pair_concentrated_charge','e286_private_triple_k11_charge','e286_second_support_orbit_impossible'])
 if(!log.includes('PROJECT_DEPENDENCIES EG617.'+n+':'))throw Error('Missing h3 proof path: '+n);
if(status.remainingSupportOrbits===7)for(const n of ['e286_actual_support_seven_remaining','e286_private_mixed_pair_dichotomy','e286_double_count_actual_witnesses','e286_third_support_orbit_impossible','e286_ten_clique_completers_excess'])
 if(!log.includes('PROJECT_DEPENDENCIES EG617.'+n+':'))throw Error('Missing first h4 proof path: '+n);
if(dag){
 const begin=log.indexOf('PROJECT_DEPENDENCIES EG617.e286_actual_support_nine_remaining:');
 const end=log.indexOf('E286_ELABORATED_DEPENDENCY_AUDIT_PASS',begin);
 if(begin<0||end<begin)throw Error('Missing root dependency trace');
 fs.writeFileSync(path.join(root,'logs/e286-elaborated-dependencies.txt'),log.slice(begin,end)+'E286_ELABORATED_DEPENDENCY_AUDIT_PASS\n');
}
fs.writeFileSync(path.join(root,'CI_STATUS.json'),JSON.stringify(status,null,2)+'\n');
fs.writeFileSync(path.join(root,'logs/verified-axioms.json'),JSON.stringify(Object.fromEntries(axioms),null,2)+'\n');
let audit='# Transitive axiom audit\n\nVerified code '+sha+', CI '+run+'. All project declarations below compiled.\nOnly propext, Classical.choice and Quot.sound are used. E286/COVER/MainTheorem remain unproved.\n\n| Declaration | Axioms |\n|---|---|\n';
let statements='# Exact Lean source statements\n\nCode '+sha+', CI '+run+'. Full proof bodies are in standard .lean files.\nThe declarations below retain their source section context; universe and implicit section\nvariables are given in those files. The full CI log also contains elaborated #check output\nincluding all implicit binders. No additional terminal hypothesis is hidden.\n\n';
for(const d of scan.declarations){
 const name='EG617.'+d.name;
 audit+='| '+name+' | '+(axioms.get(name).join(', ')||'none')+' |\n';
 const source=fs.readFileSync(path.join(root,'lean',d.file),'utf8');
 const re=new RegExp('^(?:@\\[[^\\]]+\\]\\s*)?(?:noncomputable )?(?:theorem|lemma|def|abbrev) '+d.name+'\\b','m');
 const m=re.exec(source);if(!m)throw Error('Missing source statement '+name);
 let dep=0,stop=-1;
 for(let i=m.index;i<source.length;i++){
  if('([{'.includes(source[i]))dep++;
  if(')]}'.includes(source[i]))dep--;
  if(dep===0&&source.slice(i,i+2)===':='){stop=i;break;}
 }
 if(stop<0)throw Error('No body '+name);
 statements+='## '+name+'\n\nSource: '+d.file.replaceAll('\\','/')+'\n\n```lean\n'+source.slice(m.index,stop).trim()+'\n```\n\n';
}
fs.writeFileSync(path.join(root,'LEAN_AXIOM_AUDIT.md'),audit);
fs.writeFileSync(path.join(root,'DECLARATION_STATEMENTS.md'),statements);
console.log(JSON.stringify({sha,run,status:'PASS',declarations:status.declarations,theorems:status.theorems,preserved:preserved.length}));

