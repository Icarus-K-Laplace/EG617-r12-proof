# E406 q31 / lower-charge coexistence reduction

Status: `PROVED` for the structural reductions below. `E406` itself remains `OPEN`.

This is the assistant-owned Line-A subproblem. It deliberately does not overlap the new Astra-A assignment on E407--E408.

Assume the explicit T61 E406 parent contract:

- 61 vertices;
- `e(R)=406`;
- `delta(R)=13`;
- inherited hereditary caps;
- every degree-13 pivot has a 13-shell A and 47-core C;
- exact identity
  `406 = 91 + q + e(C)`;
- generic 47-core floor `e(C)>=284`;
- for `e(C)<=286`, the established Line-A lemma gives `delta(C)>=12`;
- exact subset-charge and repivot inequalities are available.

## 1. Global q ceiling and near-extremal core budgets

The 284-edge core floor gives

`q<=31`.

Hence the three top charge levels correspond exactly to

- `q=31 <=> e(C)=284`;
- `q=30 <=> e(C)=285`;
- `q=29 <=> e(C)=286`.

All three cores have minimum degree at least12.

Define the internal core excess over 12 by

`Xi(C)=sum_{v in C}(d_C(v)-12)=2e(C)-12*47`.

Therefore

- q31 core: `Xi=4`;
- q30 core: `Xi=6`;
- q29 core: `Xi=8`.

In particular a q31 core has at most four vertices of internal degree above12. Its degree multiset is obtained by partitioning4:

- `16,12^46`;
- `15,13,12^45`;
- `14,14,12^45`;
- `14,13,13,12^44`;
- `13^4,12^43`.

This is the first strong rigidity of the E406 q31 state.

## 2. No medium missing degree at q31

Let p be a q31 pivot and let y be any undecorated shell vertex, hence a legal degree-13 repivot. Put

- `d=d_M(y)`;
- `S=N_M(y)`;
- `X=t(S)-e_M(S)`.

The exact subset identity gives `X<=q=31`.

The repivot lower bound with `delta(C)>=12` gives

`q_y-q >= d(13-d)-X`.

Since q31 is globally maximal, `q_y-q<=0`. Hence

`d(13-d)<=31`.

For integer `0<=d<=12`, this forces

`d in {0,1,2,3,10,11,12}`.

Thus every undecorated shell vertex at a q31 pivot has extreme missing degree; degrees4 through9 are impossible.

## 3. The same extreme-degree restriction at q30

Let p be a q30 pivot. Again `delta(C)>=12`. Every legal repivot satisfies `q_y<=31`, so

`q_y-q<=1`.

Using `X<=30`,

`1 >= d(13-d)-X >= d(13-d)-30`.

Hence again

`d in {0,1,2,3,10,11,12}`.

So a q30 shell coexisting with a q31 maximum has exactly the same forbidden medium-degree interval.

## 4. Degree3 / degree10 rows almost consume the full shell charge

For q31, if d is3 or10, then `d(13-d)=30`. The non-increase condition gives

`X>=30`.

Since q=31 and

`q-X = e_M(A\S)+G_{A\S}`,

the complement of S carries at most one unit of shell charge:

`e_M(A\S)+G_{A\S}<=1`.

For q30, global ceiling q_y<=31 yields

`X>=29`,

and therefore the same conclusion:

`e_M(A\S)+G_{A\S}<=1`.

Thus any regular d3 or d10 row in either top shell forces an almost-total charge concentration around that row. This is the natural analytic replacement for an uncontrolled q30/q31 shell enumeration.

## 5. Exact final-rise exchange q30 -> q31

The Line-A V7 source package reports that a q30 no-immediate-rise state reaches q>=31 within at most two legal repivots. Under that reported theorem, any coexistence state contains a final adjacent transition

`q=30 -> q'=31`.

For this final transition, let C be the old 285-edge core and C' the new 284-edge core. If y is the legal shell pivot, put

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D=N_C(y)`.

Because y has global degree13, `|S|=|D|=d`, and

`C'=(C\D) union S`.

The edge count drops by exactly one:

`e(C')=e(C)-1`.

Let

`epsilon_C(D)=sum_{u in D}(d_C(u)-12)`,
`epsilon_C'(S)=sum_{s in S}(d_C'(s)-12)`.

Writing the core-edge change as removed incident edges minus inserted incident edges gives the exact excess-exchange identity

`epsilon_C(D)-epsilon_C'(S) = 1 + e_C(D)-e_F(S)`.   (E406-X)

The final-rise pivot also satisfies

`d in {1,2,3,10,11,12}`;

d=0 cannot raise q because then D=S=empty and the core is unchanged.

For d=1, (E406-X) reduces to

`epsilon_C(u)=epsilon_C'(s)+1`.

So every one-swap q30->q31 transition must remove a positive-excess core vertex and insert a shell vertex whose new core excess is exactly one smaller.

## 6. Current E406 target

S31 already supplies some degree-13 pivot with q<=30. V7 reports that q30 plateau behaviour reaches q31. Therefore the unresolved E406 issue can be sharpened to:

> Can a 406-edge T61 object contain both a q31 extremal pivot (284-edge, excess4 core) and a lower-charge pivot whose repivot chain terminates at q31?

The structural search space is now much smaller:

- q30/q31 shells have no undecorated missing degree4..9;
- every d3/d10 row leaves at most one charge unit outside its missing neighbourhood;
- every final q30->q31 edge obeys the exact excess-exchange equation (E406-X);
- the q31 core has only four total internal excess units.

The next attack should classify the six final-rise degrees `1,2,3,10,11,12`, beginning with d1/d2 via the tiny core-excess budget and d3/d10 via the one-unit complement-charge theorem.