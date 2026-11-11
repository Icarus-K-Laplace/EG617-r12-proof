// Supplementary adversarial check, NEVER imported by Lean as proof evidence.
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=path.dirname(fileURLToPath(import.meta.url));
const n=47;
const cls=v=>Math.floor((v-22)/5);
function adj(x,y){
  if(x===y)return false;
  if(x<11||y<11)return x<11&&y<11;
  if(x<22||y<22)return x<22&&y<22;
  const a=cls(x),b=cls(y),d=(a-b+5)%5;
  return a===b||d===1||d===4;
}
const verts=Array.from({length:n},(_,i)=>i);
const edges=S=>S.reduce((s,x,i)=>s+S.slice(i+1).filter(y=>adj(x,y)).length,0);
const degrees=verts.map(x=>verts.filter(y=>adj(x,y)).length);
const cycleAdj=(a,b)=>(a-b+5)%5===1||(a-b+5)%5===4;
let cycleAlpha=0,cycleOmega=0;
for(let mask=0;mask<32;mask++){
  const S=[0,1,2,3,4].filter(i=>mask>>i&1);
  const pairs=S.flatMap((x,i)=>S.slice(i+1).map(y=>[x,y]));
  if(pairs.every(([a,b])=>!cycleAdj(a,b)))cycleAlpha=Math.max(cycleAlpha,S.length);
  if(pairs.every(([a,b])=>cycleAdj(a,b)))cycleOmega=Math.max(cycleOmega,5*S.length);
}
const choose2=n=>n*(n-1)/2;
const tau=n=>12*choose2(Math.floor(n/12))+Math.floor(n/12)*(n%12);
const D=n=>choose2(n)-11*tau(n);
const U=Array.from({length:14},(_,i)=>22+i);
const result={
  scope:'Independent finite computation; not a Lean theorem or an external proof oracle',
  graph:'K11 disjoint-union K11 disjoint-union C5[K5]',
  vertices:n,edges:edges(verts),minDegree:Math.min(...degrees),
  independence:2+cycleAlpha,clique:Math.max(11,cycleOmega),
  alphaOmegaMethod:'Enumerate all 32 class supports of C5. Each clique class contributes at most one independent vertex, and all five vertices to a clique. Disjoint-union alpha adds; omega takes maximum.',
  capViolation:{vertices:U,card:U.length,edges:edges(U),D:D(U.length)},
  conclusion:'Counterexample ONLY to GATE47 with hereditary caps omitted. NOT a counterexample to the frozen theorem.'
};
if(result.edges!==285||result.minDegree!==10||result.independence!==4||result.clique!==11||edges(U)!==71||D(14)!==69)throw Error('Unexpected adversarial graph data');
fs.writeFileSync(path.join(root,'logs/cap-necessity.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
