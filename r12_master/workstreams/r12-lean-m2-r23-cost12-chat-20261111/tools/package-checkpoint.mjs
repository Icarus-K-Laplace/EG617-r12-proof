import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const dest=path.resolve(process.argv[2]||'');
if(!process.argv[2]||fs.existsSync(dest))throw Error('Provide a new, non-existing staging directory');
const evidence=JSON.parse(fs.readFileSync(path.join(root,'CI_STATUS.json'),'utf8'));
if(evidence.cleanLinuxBuild!=='PASS'||evidence.fullAxiomAudit!=='PASS')throw Error('No verified checkpoint');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
for(const h of evidence.hashes)if(hash(fs.readFileSync(path.join(root,'lean',h.file)))!==h.sha256)
  throw Error('Source no longer matches CI: '+h.file);
const sums=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
  if(['.git','.lake','.lake-tmp','releases','release-stage'].includes(e.name))continue;
  if(e.isSymbolicLink())throw Error('Unexpected symlink');
  const f=path.join(dir,e.name),rel=path.relative(root,f).split(path.sep).join('/');
  if(e.isDirectory()){walk(f);continue;}
  if(rel==='SHA256SUMS')continue;
  const b=fs.readFileSync(f),target=path.join(dest,rel);
  fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,b);
  sums.push(hash(b)+'  '+rel);
}}
walk(root);sums.sort();fs.writeFileSync(path.join(dest,'SHA256SUMS'),sums.join('\n')+'\n');
console.log(JSON.stringify({stage:dest,files:sums.length,verifiedCode:evidence.sha,gate47:evidence.Gate47}));
