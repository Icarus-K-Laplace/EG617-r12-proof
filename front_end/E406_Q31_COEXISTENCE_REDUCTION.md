# E406 q31 / lower-charge coexistence reduction

Status: `PROVED` for the structural reductions below. `E406` itself remains `OPEN`.

This is the assistant-owned Line-A subproblem. It deliberately does not overlap the new Astra-A assignment on E407--E408.

Assume the explicit T61 E406 parent contract:

- 61 vertices;
- `e(R)=406`;
- `delta(R)=13`;
- inherited hereditary caps;
- every degree-13 pivot has a 13-shell A and 47-core C;
- exact identity `406 = 91 + q + e(C)`;
- generic 47-core floor `e(C)>=284`;
- for `e(C)<=286`, the established Line-A lemma gives `delta(C)>=12`;
- the 14-point cap gives `z=e(M)>=22`;
- exact subset-charge and repivot inequalities are available.

## 1. Global q ceiling and near-extremal core budgets

The 284-edge core floor gives `q<=31`.

Hence

- `q=31 <=> e(C)=284`;
- `q=30 <=> e(C)=285`;
- `q=29 <=> e(C)=286`.

All three cores have minimum degree at least12.

Define

`Xi(C)=sum_{v in C}(d_C(v)-12)=2e(C)-12*47`.

Then

- q31 core: `Xi=4`;
- q30 core: `Xi=6`;
- q29 core: `Xi=8`.

In particular a q31 core has at most four vertices of internal degree above12. Its degree multiset is one of

- `16,12^46`;
- `15,13,12^45`;
- `14,14,12^45`;
- `14,13,13,12^44`;
- `13^4,12^43`.

## 2. Pivot-graph degree lower bounds

Since `q=z+G` and `z>=22`,

- at q31: `G<=9`;
- at q30: `G<=8`.

A decorated shell vertex consumes at least one unit of G. Therefore a q31 shell contains at least four undecorated vertices and a q30 shell contains at least five.

Undecorated shell vertices are exactly the degree-13 neighbours available as legal adjacent repivots. Thus in the graph whose vertices are degree-13 pivots and whose edges are adjacency in R,

- every q31 pivot has pivot-graph degree at least4;
- every q30 pivot has pivot-graph degree at least5.

Under the source-reported V6/V7 ladder, S31 supplies a pivot q<=30, q<=29 states rise to q30, and q30 plateau states reach q31. Hence any E406 coexistence object contains an actual pivot-graph boundary edge

`q30 -- q31`.

This converts the global coexistence problem into a local boundary-edge classification problem.

## 3. No medium missing degree at q31

Let p be a q31 pivot and y any undecorated shell vertex. Put

- `d=d_M(y)`;
- `S=N_M(y)`;
- `X=t(S)-e_M(S)`.

The subset identity gives `X<=31`, while the repivot lower bound gives

`q_y-q >= d(13-d)-X`.

Since q31 is globally maximal, `q_y-q<=0`; therefore

`d(13-d)<=31`.

Hence

`d in {0,1,2,3,10,11,12}`.

Thus q31 has no undecorated missing degree4 through9.

## 4. The same extreme-degree restriction at q30

For q30, every legal repivot has `q_y<=31`, so

`1 >= d(13-d)-X >= d(13-d)-30`.

Therefore again

`d in {0,1,2,3,10,11,12}`.

So both sides of every q30--q31 boundary edge have the same forbidden medium-degree interval.

## 5. Degree3 / degree10 rows almost consume all shell charge

If d is3 or10, then `d(13-d)=30`.

At q31 the non-increase condition gives `X>=30`; at q30 the global q31 ceiling gives `X>=29`.

Using the exact subset identity

`q-X=e_M(A\S)+G_{A\S}`,

both cases imply

`e_M(A\S)+G_{A\S}<=1`.

Thus every regular d3/d10 row on either side of the boundary edge forces all but at most one unit of shell charge to be incident with its missing-neighbour set.

## 6. Exact final-rise exchange q30 -> q31

Take a boundary edge oriented from a q30 pivot p to the adjacent q31 pivot y. Let C be the old 285-edge core and C' the new 284-edge core. Put

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D=N_C(y)`.

Because y has global degree13,

`|S|=|D|=d`,
`C'=(C\D) union S`,
`e(C')=e(C)-1`.

Define

`epsilon_C(D)=sum_{u in D}(d_C(u)-12)`,
`epsilon_C'(S)=sum_{s in S}(d_C'(s)-12)`.

Exact incident-edge exchange gives

`epsilon_C(D)-epsilon_C'(S) = 1 + e_C(D)-e_F(S)`.   (E406-X)

The boundary distance satisfies

`d in {1,2,3,10,11,12}`;

d=0 cannot change the core and cannot raise q.

For d=1,

`epsilon_C(u)=epsilon_C'(s)+1`.

So a one-swap rise must remove a positive-excess vertex from the 285-edge core and replace it by a vertex whose excess in the 284-edge core is exactly one smaller.

## 7. Current E406 target

The unresolved E406 issue is now sharply local:

> classify and eliminate a pivot-graph boundary edge q30--q31 under the six possible distance classes d=1,2,3,10,11,12.

Available rigidity:

- q31 core has only four total internal excess units;
- q30 core has only six;
- q30/q31 shells have no regular degree4..9;
- each endpoint has at least five/four legal pivot-graph neighbours respectively;
- d3/d10 forces one-unit complement charge;
- every final rise obeys (E406-X).

Next attack order:

1. d1/d2: use the tiny 6->4 core-excess drop and multiple boundary-neighbour counting;
2. d3/d10: exploit the almost-complete charge concentration on both views;
3. d11/d12: use the fact that the exchanged 11/12-sets contain many degree12 vertices in both near-extremal cores and enforce (E406-X) simultaneously.