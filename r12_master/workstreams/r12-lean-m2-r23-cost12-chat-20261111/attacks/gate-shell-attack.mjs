// Independent finite diagnostics only; no output is a Lean premise.
import fs from 'node:fs';
let seed=47;
const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/2**32;};
let shellChecks=0,pairChecks=0,rowChecks=0;
for(let trial=0;trial<1000;trial++){
  const n=47, adj=Array.from({length:n},()=>Array(n).fill(false));
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)adj[i][j]=adj[j][i]=rand()<(trial%9+1)/10;
  const degree=adj.map(r=>r.filter(Boolean).length);
  const S=Array.from({length:n-1},(_,i)=>i+1).filter(i=>adj[0][i]);
  const C=Array.from({length:n-1},(_,i)=>i+1).filter(i=>!adj[0][i]);
  const edges=A=>A.reduce((s,a)=>s+A.filter(b=>a<b&&adj[a][b]).length,0);
  const cross=S.reduce((s,a)=>s+C.filter(b=>adj[a][b]).length,0);
  if(edges(Array.from({length:n},(_,i)=>i))!==edges(C)+degree[0]+edges(S)+cross)throw Error('Edge ledger');
  if(S.reduce((s,a)=>s+degree[a],0)!==degree[0]+2*edges(S)+cross)throw Error('Degree ledger');
  shellChecks++;
}
for(let trial=0;trial<2000;trial++){
  const n=11,adj=Array.from({length:n},()=>Array(n).fill(false));let z=0;
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(rand()<(trial%10+1)/11){adj[i][j]=adj[j][i]=true;z++;}
  const degree=adj.map(r=>r.filter(Boolean).length),r=degree.map(d=>d+Math.floor(rand()*4));
  for(let a=0;a<n;a++)for(let b=a+1;b<n;b++){
    if(degree[a]+degree[b]>z+1)throw Error('Incidence inequality');
    pairChecks++;
    if(r[a]+r[b]>=12){
      if(r.reduce((s,x)=>s+x,0)<z+11)throw Error('Row sum');
      rowChecks++;
    }
  }
}
const report={status:'NO_COUNTEREXAMPLE_IN_TESTED_DOMAIN',seed:47,shellChecks,pairChecks,rowChecks,
  negativeControls:[
    {missing:'distinct endpoints',example:'star K1,10; same center twice',lhs:20,rhs:11},
    {missing:'row-pair bound12',example:'one-edge M, rows equal degrees',rowSum:2,required:12},
    {missing:'every row dominates missing degree',example:'M=K11, two rows6, all others0',rowSum:12,required:66},
    {missing:'original R(4,47) graph class',example:'empty47-vertex graph',edges:0,minDegree:0,alpha:47}
  ],limitation:'Finite diagnostics, not exhaustive GATE47 enumeration and not a kernel proof.'};
fs.writeFileSync(new URL('../logs/gate-shell-attack.json',import.meta.url),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
