// Diagnostic counterexample search only. No output is imported into Lean.
// Enumerate EVERY independent set by include/exclude recursion, not maximal-clique search.
const pop = x => { let n=0; for(;x;x&=x-1)n++; return n; };
function graph(s, deletion) {
  const cls=[], adj=Array(23).fill(0); let offset=0;
  for(const n of s){cls.push(Array.from({length:n},(_,i)=>offset+i));offset+=n;}
  const edges=[];
  for(let i=0;i<5;i++)for(const a of cls[i])for(const b of cls[(i+1)%5]){
    if(deletion===i && a===cls[i][0] && b===cls[(i+1)%5][0])continue;
    adj[a]|=1<<b;adj[b]|=1<<a;edges.push([a,b]);
  }
  return {cls,adj,edges};
}
const mask=xs=>xs.reduce((a,b)=>a|(1<<b),0);
const records=[];
for(const [s,deletion] of [
  ...Array.from({length:10},(_,j)=>Array.from({length:6},(_,d)=>[[10,j+1,1,1,10-j],d-1])).flat(),
  [[9,9,2,1,2],-1]]){
  const {cls,adj,edges}=graph(s,deletion);
  const independent=[];
  function visit(i,chosen,forbidden){
    if(i===23){independent.push(chosen);return;}
    visit(i+1,chosen,forbidden);
    if(!(forbidden&(1<<i)))visit(i+1,chosen|(1<<i),forbidden|adj[i]);
  }
  visit(0,0,0);
  const alpha=Math.max(...independent.map(pop));
  if(alpha>11){records.push({sizes:s,deletion,alpha,excluded:true});continue;}
  const choices=s[0]===10 ? [[0,2,3],[1,4,2],[1,4,3]] : [[0,2,3],[1,3,4]];
  const ts=choices.map(cs=>mask(cs.flatMap(c=>cls[c])));
  if(ts.some(t=>pop(t)!==12))throw Error('Wrong witness cardinality');
  const costs=ts.map(t=>edges.filter(([a,b])=>(t&(1<<a))&&(t&(1<<b))).length);
  let worst=0;
  for(const I of independent){
    const best=Math.min(...ts.map((t,i)=>costs[i]+pop(t&I)));
    if(best>6)throw Error(JSON.stringify({counterexample:{s,deletion,I,best}}));
    worst=Math.max(worst,best);
  }
  records.push({sizes:s,deletion,alpha,independentSets:independent.length,worst});
}
const types=Array.from({length:5},(_,i)=>(1<<((i+4)%5))|(1<<((i+1)%5)));
const c=(i,j)=>(types[i]&types[j])===0;
const sets=Array.from({length:31},(_,i)=>Array.from({length:5},(_,j)=>j).filter(j=>(i+1)&(1<<j)));
let compatiblePairs=0,missingCases=0,extensions=0;
for(const A of sets)for(const B of sets)if(A.every(a=>B.every(b=>c(a,b)))){
  compatiblePairs++;
  if(Math.min(A.length,B.length)!==1 || Math.max(A.length,B.length)>2)throw Error('Type structure');
  const forbidden=B.reduce((m,b)=>m|types[b],0);
  for(let p=0;p<5;p++)if(!(forbidden&(1<<p))){
    extensions++;
    if(!types.some(t=>(t&(1<<p))&&!(t&forbidden)))throw Error('Singleton extension');
  }
  for(let u=0;u<5;u++)for(let v=0;v<5;v++)
    if(B.every(b=>c(u,b))&&A.every(a=>c(a,v))&&!c(u,v)){
      missingCases++;
      if(A.length!==1||B.length!==1)throw Error('Missing endpoint classification');
    }
}
const B=(n,k)=>2*k+1+k*(n-2*k-1)+Math.floor((n-2*k-1)**2/4);
console.log(JSON.stringify({status:'NO_COUNTEREXAMPLE_IN_TESTED_DOMAIN',
  warning:'Diagnostic only; not a Lean theorem or completeness proof for arbitrary graphs.',
  B23:Array.from({length:10},(_,i)=>[i+2,B(23,i+2)]),
  B18:Array.from({length:7},(_,i)=>[i+2,B(18,i+2)]),
  compatiblePairs,missingCases,extensions,
  validRepresentatives:records.filter(r=>!r.excluded).length,
  independentSetsChecked:records.reduce((n,r)=>n+(r.independentSets||0),0),records},null,2));
