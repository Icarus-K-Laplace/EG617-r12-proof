import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const scan=JSON.parse(fs.readFileSync(path.join(root,'logs/source-scan.json'),'utf8').replace(/^\uFEFF/,''));
const output=fs.readFileSync(path.join(root,'logs/axioms.txt'),'utf8').replace(/^\uFEFF/,'');
const allowed=new Set(['propext','Classical.choice','Quot.sound']);
const reports=[];
for(const m of output.matchAll(/'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])/g)){
  reports.push({name:m[1],axioms:(m[2]||'').split(',').map(x=>x.trim()).filter(Boolean)});
}
const expected=scan.declarations.map(d=>'EG617.'+d.name);
const errors=[];
for(const name of expected) if(reports.filter(r=>r.name===name).length!==1) errors.push('Expected one axiom report for '+name);
for(const r of reports){if(!expected.includes(r.name))errors.push('Unexpected declaration '+r.name);for(const a of r.axioms)if(!allowed.has(a))errors.push(r.name+' uses disallowed axiom '+a);}
if(scan.status!=='PASS')errors.push('Source scan did not pass');
const result={status:errors.length?'FAIL':'PASS',scope:'All project declarations recognized by the source scanner; standard Lean logic only',allowed:[...allowed],reports,errors,finalTheoremProved:false};
fs.writeFileSync(path.join(root,'logs/axiom-check.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
if(errors.length)process.exitCode=1;
