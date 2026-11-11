// Independent arithmetic smoke test, never imported by Lean and not a proof oracle.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const choose2=n=>n*(n-1)/2;
const rows=[];
for(let n=0;n<=145;n++){
  const parts=Array(12).fill(0);
  for(let v=0;v<n;v++)parts[v%12]++;
  const fromParts=parts.reduce((a,b)=>a+choose2(b),0);
  const q=Math.floor(n/12),s=n%12;
  const fromFormula=12*choose2(q)+q*s;
  const rawCap=choose2(n)-11*fromParts;
  if(fromParts!==fromFormula||rawCap<0||Math.max(...parts)-Math.min(...parts)>1)
    throw Error('Arithmetic counterexample at n='+n);
  rows.push({n,fromParts,fromFormula,rawCap});
}
const result={status:'NO_ARITHMETIC_COUNTEREXAMPLE_IN_TESTED_RANGE',
  scope:'Independent balanced-part construction for n=0..145; not a Lean proof, not a graph-exhaustiveness claim',
  graphEdges:choose2(145),colors:12,average:choose2(145)/12,rows};
fs.mkdirSync(path.join(root,'logs'),{recursive:true});
fs.writeFileSync(path.join(root,'logs/m1-independent-arithmetic.json'),JSON.stringify(result,null,2)+'\n');
console.log(result.status,rows.length,'cases; no proof imported into Lean');
