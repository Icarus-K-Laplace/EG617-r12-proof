// Diagnostic only. No output is imported into Lean.
import fs from 'node:fs';
let state=335;
function rand(){state=(Math.imul(state,1664525)+1013904223)>>>0;return state/2**32;}
const records=[];
for(let trial=0;trial<1000;trial++){
  const g=Array.from({length:14},()=>Array(14).fill(false));
  const density=(trial%10+1)/11;
  for(let i=0;i<14;i++)for(let j=i+1;j<14;j++)g[i][j]=g[j][i]=rand()<density;
  const T=Array.from({length:12},(_,i)=>i), x=12,y=13;
  let inside=0, complement=0,cross=0,common=0;
  for(const a of T){
    for(const b of T)if(a<b){if(g[a][b])inside++;else complement++;}
    cross+=Number(g[a][x])+Number(g[a][y]);
    if(!g[a][x]&&!g[a][y])common++;
  }
  const all=g.flatMap((r,i)=>r.map((b,j)=>i<j&&b)).filter(Boolean).length;
  if(inside+complement!==66 || cross+common<12 || all!==inside+cross+Number(g[x][y]))throw Error('Ledger failure');
  if(complement+common<=6&&all<72)throw Error('Fourteen-point counterexample');
  records.push({trial,cost:complement+common,edges:all});
}
// If the endpoints are allowed inside T, K12 has cost0 but only66 total edges.
// This refutes a weakened ledger lacking the two explicit exclusion hypotheses.
const report={status:'NO_COUNTEREXAMPLE_IN_TESTED_DOMAIN',seed:335,graphs:records.length,
  lowCostGraphs:records.filter(r=>r.cost<=6).length,
  negativeControl:{graph:'K12',T:'all12 vertices',endpoints:'two vertices INSIDE T',cost:0,totalEdges:66,missingHypothesis:'x,y outside T'},
  limitation:'Finite diagnostic only; not a Lean proof or exhaustive R335 graph search.'};
fs.writeFileSync(new URL('../logs/r335-fourteen-attack.json',import.meta.url),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
