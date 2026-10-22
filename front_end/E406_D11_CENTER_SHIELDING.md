# E406 d11 terminal: center-shielding and cross-edge concentration

Status: `PROVED` under `E406_D11_EXACT_SHELL.md`, `E406_D11_TWO_MAXIMA.md`, and `E406_D11_THREE_STAR_BLOCKS.md`. `E406` remains `OPEN`.

We retain the d11 terminal:

- p is q30;
- y,T are adjacent q31 pivots;
- S is the common 11-point shell side anticomplete to y and T;
- D=N_C(y), E=N_C(T);
- the complements on S,D,E are stars;
- e(S,D)=0, e(S,E)<=1;
- previous work gave |D intersect E|<=1.

Let s0,d0,e0 denote the star centres of S,D,E.

## 1. In fact D and E are disjoint

Assume D intersect E={i}.

Repivoting y replaces D by S and produces a q31 core C_y of minimum degree at least12. Every v in E\{i} remains in the core, so

    d_C(v,D) <= epsilon_v + d_R(v,S).

Summing over E\{i},

    e_C(E\{i},D) <= epsilon_{E\{i}} + e_R(S,E\{i}).

The left side contains every target edge from i to E\{i}. Since the complement on E is a star with m_E missing edges, the internal E-degree of i is at least 10-m_E.

On the other hand the E-star equality is

    m_E + epsilon_E + e_R(S,E) = 9.

Hence the right side is at most 9-m_E, contradiction.

Therefore

    D intersect E = empty.

## 2. Cross edges are concentrated at the star centres

The D-star equality has

    m_D + epsilon_D = 9,

and all old-core excess on D is concentrated at d0. Thus every u in D\{d0} has old-core excess0.

In the T-core, E is removed and S is inserted. Since e(S,D)=0, every u in D\{d0} must retain core degree at least12 without compensation from S. Therefore

    d_C(u,E)=0.

So every D-E target edge is incident with d0.

Likewise every v in E\{e0} has old-core excess0. In the y-core it loses D-neighbours and gains only possible neighbours in S. Hence

    d_C(v,D) <= d_R(v,S).

Since e(S,E)<=1, at most one noncentre E-vertex can have a D-neighbour, and then it must also be the endpoint of the unique S-E edge.

Consequently

    e(D,E) <=2.

Apart from a possible single exceptional edge d0-v* where v* is the S-E endpoint, every D-E edge is d0e0.

## 3. q31 block-excess inequalities

Put

    r=e(D,E),
    c=e(S,E) in {0,1}.

In the q31 y-core the total excess on E is

    epsilon_E^y = epsilon_E-r+c = 9-m_E-r.

The inserted S-block has excess

    epsilon_S'=8-m_S.

Since the total q31-core excess is4,

    m_S+m_E+r >=13.

Similarly in the q31 T-core,

    m_S+m_D+r >=13.

The old q30 core has total excess6, giving

    m_D+m_E+c >=12.

## 4. Centre shielding is forced by alpha<=5

Suppose neither d0e0 nor s0e0 is a target edge.

Choose one star leaf in each of S,D,E, avoiding the at-most-one exceptional endpoint of the unique S-E edge and the at-most-one exceptional noncentre D-E endpoint. Each centre-leaf pair is internally target-independent. S-D is anticomplete, and the chosen leaves avoid every exceptional cross edge. The six selected vertices form an independent6-set, contradiction.

Therefore

    d0e0 in E(R)  OR  s0e0 in E(R).

## 5. Independent-five coverage in O

Let

    O=C\(D union E), |O|=25.

Choose an S-star leaf s which is not the endpoint of the possible exceptional S-E edge, and any D-star leaf d. Then

    {T,s0,s,d0,d}

is an independent5-set in the 61-point parent. Since T has no target neighbours in O, the four O-neighbourhoods of s0,s,d0,d must cover all25 points of O.

Let delta=1 if the unique S-E edge is incident with s0, and delta=0 otherwise. Their O-degrees are

- s0: 10-delta;
- s: 3;
- d0: 11-r;
- d: 3.

Hence every such leaf pair gives exactly

    27-r-delta

O-incidences covering25 points. Therefore

    r+delta <=2.

When r+delta=2 there is zero overlap budget beyond the forced cover structure: after the two centre-neighbourhoods are removed, the two 3-rows partition a fixed 6-point remainder.

## 6. Row-class multiplicity cap

Suppose k degree-13 shell vertices share the same 3-row P. Repivot at one member of the class. Every vertex of P has core degree at least12 and is adjacent to all k class members, hence has new-shell decoration at least k-1.

Therefore

    3(k-1) <= G'.

At q'=30, G'<=8, so k<=3.
At q'=31, G'<=9, so k<=4.

This cap is repeatedly used in the shielding reduction.

## 7. The zero-overlap-budget branches are impossible

Assume r+delta=2.

The O-cover has total size exactly25, so for every ordinary S-leaf s and D-leaf d the two 3-rows P_s,Q_d partition the same fixed6-point remainder. Hence all ordinary S-leaves have one common 3-row, and all D-leaves have the complementary common 3-row.

If delta=1,r=1, every S-leaf is ordinary and m_S>=4. Each S-leaf is a q30 plateau d3 pivot, so its row class has size at most3. Contradiction.

If delta=0,r=2 and c=0, again every S-leaf is ordinary and m_S>=4, contradiction.

If delta=0,r=2,c=1, at most one S-leaf is exceptional. If m_S>=5, at least four ordinary S-leaves share the same q30 3-row, contradiction. The only numerical residue is m_S=4.

Then the q31 excess inequalities force

    m_D=m_E=7.

All seven D-star leaves share the complementary 3-row. Their repivots have q<=31, so the q31 row-class cap gives size at most4, contradiction.

Therefore

    r+delta <=1.

## 8. Current shielding modes

Centre shielding plus r+delta<=1 leaves exactly two qualitative modes:

A. `r=0, delta=1`: pure S-centre shield, so the unique S-E edge is s0e0 and D-E is empty.

B. `r=1, delta=0`: pure D-centre shield, so the unique D-E edge is d0e0; the optional S-E edge is either absent or incident with an S-leaf.

The next reduction treats the one-unit overlap budget in these two modes.