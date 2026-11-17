import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const assert=(b,m)=>{if(!b)throw Error(m)};
const pc=n=>n.toString(2).replaceAll('0','').length;
function perms(a){return a.length?a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(p=>[x,...p])):[[]]}
const p4=perms([0,1,2,3]);
const rename=(m,p)=>p.reduce((r,v,i)=>r|((m>>i&1)<<v),0);
const canon=a=>p4.map(p=>a.map(m=>rename(m,p)).sort((a,b)=>a-b).join(',')).sort()[0];
const masks=Array.from({length:16},(_,i)=>i).filter(m=>pc(m)>=2);
const expected=[[15,3,12],[3,13,14],[3,3,13,12],[3,7,9,12],[3,5,9,14],
 [3,3,5,9,12],[3,5,5,10,10],[3,5,9,6,10],[3,3,5,10,12],[3,3,3,12,12]];
const target=new Set(expected.map(canon)),found=new Map();let tuples=0,legal=0;
function visit(a,start,h){
 if(a.length===h){
  tuples++;
  if(a.reduce((s,m)=>s+pc(m),0)!==h+5)return;
  if([0,1,2,3].some(i=>a.filter(m=>m>>i&1).length<2))return;
  legal++;const k=canon(a);found.set(k,(found.get(k)||0)+1);return;
 }
 for(let i=start;i<masks.length;i++)visit([...a,masks[i]],i,h);
}
for(let h=3;h<=5;h++)visit([],0,h);
assert(target.size===10,'Frozen representatives not distinct');
assert(found.size===target.size&&[...found.keys()].every(k=>target.has(k)),'Orbit domain mismatch');
const pos=x=>Math.max(0,x);
const specs=[
 ['f11',10,10,6,(a,b)=>pos(10-a-b)+a*pos(b-2)+b*pos(a-2)],
 ['f10_11',9,10,4,(a,b)=>pos(9-a-b)+a*pos(b-3)+b*pos(a-2)],
 ['f9_11',8,10,2,(a,b)=>pos(8-a-b)+a*pos(b-4)+b*pos(a-2)],
 ['f10_10',9,9,2,(a,b)=>pos(8-a-b)+a*pos(b-3)+b*pos(a-3)],
 ['star',9,10,6,(a,b)=>pos(9-a-b)+a*(b-1)+b*pos(a-2)],
 ['two_completers',8,10,5,(a,b)=>pos(8-a-b)+a*(b-1)+b*pos(a-2)],
 ['extra_completer',9,10,5,(a,b)=>pos(9-a-b)+a*pos(b-2)+b*pos(a-2)]];
const scalars=specs.map(([name,A,B,min,f])=>{
 const equal=[];let tested=0;
 for(let a=1;a<=A;a++)for(let b=1;b<=B;b++){
  const v=f(a,b);tested++;assert(v>=min,name+' violation '+[a,b]);
  if(v===min)equal.push([a,b]);
  if(name==='f11'&&v<=8){assert(Math.min(a,b)<=2,'small side');if(a===2)assert(b<=4,'size2 upper');}
 }
 return {name,tested,min,equal};
});
for(const[name,pair]of [['f10_11',[2,3]],['f9_11',[2,4]],['f10_10',[3,3]]])
 assert(JSON.stringify(scalars.find(x=>x.name===name).equal)===JSON.stringify([pair]),'unique minimum '+name);
let overlaps=0;
for(let a=0;a<=10;a++)for(let b=0;b<=10;b++){
 assert(pos(a+b-2)>=pos(a-2)+pos(b-2),'shared leaf');overlaps++;
}
const floors=Array.from({length:9},(_,q)=>({q,bound:(47-q)*(46-q)/2-Math.floor((47-q)**2/3)+12*q+8-q*(q-1)/2}));
assert(floors.every(x=>x.bound>286),'regular seed bound');
const degreeList=[21,11,...Array(45).fill(12)];
assert(degreeList.reduce((a,b)=>a+b,0)===572,'negative-control sum');
const edges=[];let residual=degreeList.map((d,v)=>({v,d}));
while(residual.some(x=>x.d)){
 residual.sort((a,b)=>b.d-a.d||a.v-b.v);const x=residual.shift();
 assert(x.d<=residual.length,'nongraphical degree sequence');
 for(let i=0;i<x.d;i++){assert(residual[i].d>0,'nongraphical degree sequence');edges.push([x.v,residual[i].v]);residual[i].d--;}
}
assert(edges.length===286,'degree negative control');
const result={status:'NO_COUNTEREXAMPLE_IN_STATED_DIAGNOSTIC_DOMAIN',
 support:{multisetsTested:tuples,legalLabeledMultisets:legal,orbits:[...found].map(([canonical,multiplicity])=>({canonical,multiplicity})),completeDomainCondition:'h=3..5; supports subsets of4 labels of size>=2; total incidence=h+5; each seed incidence>=2'},
 scalarChecks:scalars,sharedLeafChecks:overlaps,regularSeedBounds:floors,
 negativeControl:{missingHypothesis:'minimum degree>=12',vertices:47,edges:edges.length,degreeList,totalDegree:572,truncatedExcess:9,adjacencyEdges:edges},
 limitation:'Diagnostic only. The graph-to-support reduction and orbit completeness are not yet Lean-certified. No output is imported into Lean.'};
fs.writeFileSync(path.join(root,'logs/e286-diagnostic-attack.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,tuples,legal,orbits:found.size,scalarCases:scalars.reduce((s,x)=>s+x.tested,0),negativeControlExcess:9}));

