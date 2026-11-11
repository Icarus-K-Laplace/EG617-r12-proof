import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
function mask(s) {
  let out='',i=0,depth=0;
  while(i<s.length){
    if(depth){if(s.slice(i,i+2)==='/-'){depth++;out+='  ';i+=2}
      else if(s.slice(i,i+2)==='-/'){depth--;out+='  ';i+=2}
      else{out+=s[i]==='\n'?'\n':' ';i++}continue}
    if(s.slice(i,i+2)==='/-'){depth=1;out+='  ';i+=2;continue}
    if(s.slice(i,i+2)==='--'){while(i<s.length&&s[i]!=='\n'){out+=' ';i++}continue}
    if(s[i]==='"'){out+=' ';i++;while(i<s.length){
      if(s[i]==='\\'){out+='  ';i+=2;continue}
      if(s[i]==='"'){out+=' ';i++;break}
      out+=s[i]==='\n'?'\n':' ';i++}continue}
    out+=s[i++]
  } if(depth)throw Error('unclosed comment');return out;
}
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>
  ['.lake','.lake-tmp','.git'].includes(e.name)?[]:e.isDirectory()?walk(path.join(d,e.name)):
  e.name.endsWith('.lean')?[path.join(d,e.name)]:[])}
const files=walk(root).sort(), hits=[],declarations=[];
for(const f of files){
 const code=mask(fs.readFileSync(f,'utf8'));
 for(const m of code.matchAll(/\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b/g))
   hits.push({file:path.relative(root,f),line:code.slice(0,m.index).split('\n').length,token:m[0]});
 for(const m of code.matchAll(/\b(theorem|lemma|def|abbrev)\s+([A-Za-z_][A-Za-z_0-9]*)/g))
   declarations.push({kind:m[1],name:m[2],file:path.relative(root,f)});
}
const result={scope:'source lexical audit only; not a Lean build or axiom audit',
  files:files.map(f=>path.relative(root,f)),hits,declarations,
  finalTheoremDeclared:declarations.some(d=>d.kind==='theorem'&&d.name==='eg617_r12'),
  mainTheoremDeclared:declarations.some(d=>d.kind==='theorem'&&d.name==='MainTheorem'),
  status:hits.length?'FAIL':'PASS'};
fs.mkdirSync(path.join(root,'logs'),{recursive:true});
fs.writeFileSync(path.join(root,'logs','source-scan.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
if(hits.length)process.exitCode=1;
