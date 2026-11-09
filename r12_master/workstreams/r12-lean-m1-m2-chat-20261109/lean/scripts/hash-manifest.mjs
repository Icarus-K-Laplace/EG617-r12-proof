import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>{
 if(e.name==='.lake'||e.name==='.lake-tmp'||e.name==='.git'||e.name==='SHA256SUMS')return [];
 if(e.isSymbolicLink())throw Error('Unexpected symlink '+e.name);
 return e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)];
});}
const entries=walk(root).map(f=>({file:path.relative(root,f).split(path.sep).join('/'),hash:createHash('sha256').update(fs.readFileSync(f)).digest('hex')})).sort((a,b)=>a.file<b.file?-1:1);
const contents=entries.map(e=>e.hash+'  '+e.file).join('\n')+'\n';
const dest=path.join(root,'SHA256SUMS');
if(process.argv.includes('--check')){if(fs.readFileSync(dest,'utf8')!==contents)throw Error('Manifest mismatch');console.log('SHA256_MANIFEST_PASS: '+entries.length+' files');}
else{fs.writeFileSync(dest,contents);console.log('SHA256 manifest written for '+entries.length+' files');}
