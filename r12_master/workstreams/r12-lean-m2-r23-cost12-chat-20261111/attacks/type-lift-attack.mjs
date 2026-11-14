// Diagnostic only: no result of this program is used by Lean.
import fs from 'node:fs';
const mod = i => (i + 10) % 5;
const adjacent = (i,j) => mod(i-j)===1 || mod(i-j)===4;
const types = Array.from({length:5},(_,i)=>[mod(i-1),mod(i+1)]);
const compatible = (i,j) => types[i].every(x=>!types[j].includes(x));
const sets = Array.from({length:31},(_,m)=>Array.from({length:5},(_,i)=>i).filter(i=>(m+1)&(1<<i)));
const pairs = sets.flatMap(A=>sets.filter(B=>A.every(a=>B.every(b=>compatible(a,b)))).map(B=>[A,B]));
const assignments = (labels,n) => labels.length===1 ? [Array(n).fill(labels[0])] :
  Array.from({length:n-1},(_,j)=>[...Array(j+1).fill(labels[0]),...Array(n-j-1).fill(labels[1])]);
let excluded810=0, checked99=0;
for(const [A,B] of pairs){
  if(A.length>2 || B.length>2)throw Error('Unexpected support size');
  for(const aa of assignments(A,8))for(const bb of assignments(B,10)){
    const witness=[...Array.from({length:10},(_,i)=>13+i),...types[aa[0]]];
    const edge=(x,y)=> x<5&&y<5 ? adjacent(x,y) : x<5 ? (y<13?types[aa[y-5]]:types[bb[y-13]]).includes(x) : y<5 ? edge(y,x) : (x<13)!==(y<13);
    if(witness.length!==12 || witness.some((x,i)=>witness.slice(i+1).some(y=>edge(x,y))))throw Error('K8,10 witness failed');
    excluded810++;
  }
  for(const aa of assignments(A,9))for(const bb of assignments(B,9)){
    const t=[0,1,2,3,4,...aa,...bb];
    const edge=(x,y)=>x<5&&y<5 ? adjacent(x,y) : x<5 ? types[t[y]].includes(x) : y<5 ? edge(y,x) : (x<14)!==(y<14);
    for(let x=0;x<23;x++)for(let y=0;y<23;y++)if(edge(x,y)!==adjacent(t[x],t[y]))throw Error('Presentation failed');
    checked99++;
  }
}
// Necessary-condition negative control: deleting a compatible cross edge breaks
// adjacency equivalence, so compatibility alone cannot justify the presentation.
const nt=[0,1,2,3,4,...Array(9).fill(0),...Array(9).fill(1)];
const deleted=(x,y)=>adjacent(nt[x],nt[y]) && !((x===5&&y===14)||(x===14&&y===5));
let deletedEdges=0;
for(let x=0;x<23;x++)for(let y=x+1;y<23;y++){
  if(deleted(x,y))deletedEdges++;
  for(let z=y+1;z<23;z++)if(deleted(x,y)&&deleted(y,z)&&deleted(z,x))throw Error('Negative control triangle');
}
if(deletedEdges!==121 || deleted(5,14) || !compatible(nt[5],nt[14]))throw Error('Negative control failed');
const report={status:'NO_COUNTEREXAMPLE_IN_STATED_TEST_DOMAIN',compatibleSupportPairs:pairs.length,
  excluded810Witnesses:excluded810,complete99Presentations:checked99,
  compatibleMissingEdgeIsNotForced:true,negativeControlEdges:deletedEdges,
  limitations:'Multiplicity distributions within every compatible type support pair; this test is not a completeness proof for arbitrary R23 graphs and is not imported into Lean.'};
fs.writeFileSync(new URL('../logs/type-lift-attack.json',import.meta.url),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
