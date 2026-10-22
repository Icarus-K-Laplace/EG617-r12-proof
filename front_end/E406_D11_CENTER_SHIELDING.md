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

Thus the tiny cross-edge count forces all three star defects toward the large end of their allowed ranges.

## 4. Centre shielding is forced by alpha<=5

Suppose neither d0e0 nor s0e0 is a target edge.

Choose one star leaf in each of S,D,E, avoiding the at-most-one exceptional endpoint of the unique S-E edge and the at-most-one exceptional noncentre D-E endpoint. This is possible because m_S>=4 and the E-star has at least two leaves when c=1 and at least three when c=0.

Each centre-leaf pair is internally target-independent. S-D is anticomplete. By Section 2 and the leaf choices there is no D-E or S-E target edge among the six selected vertices. Hence they form an independent6-set in the T61 parent, contradiction.

Therefore

    d0e0 in E(R)  OR  s0e0 in E(R).

This is the centre-shielding theorem.

## 5. The no-D-E-cross branch has a 26-incidence cover

Assume r=0. Then centre shielding forces c=1 and the unique S-E edge to be s0e0.

For any D-star leaf d and E-star leaf e, the four core vertices d0,d,e0,e are target-independent inside the old 47-core C. Since alpha(C)<=4, their O-neighbourhoods cover

    O=C\(D union E), |O|=25.

Their exact O-degrees are

- d0: 11;
- d: 3;
- e0: 10;
- e: 3.

Thus every leaf pair gives a 26-incidence cover of 25 points. In particular the two centre O-neighbourhoods intersect in at most one point, and the two 3-rows must cover all but at most one point outside their centre-neighbourhood union.

This is a repeated-row rigidity condition for the r=0 branch.

## 6. Current d11 terminal

Every surviving d11 final-rise configuration is therefore a centre-shielded three-star system with

- S,D,E pairwise disjoint;
- e(S,D)=0;
- e(S,E)<=1;
- e(D,E)<=2;
- all D-E edges incident with d0, except possibly one edge to the unique S-E endpoint;
- m_S+m_D+r>=13;
- m_S+m_E+r>=13;
- m_D+m_E+c>=12;
- at least one of d0e0 or s0e0 present.

The unresolved task is now a finite centre-shielding / repeated-row compatibility problem, not a general graph-classification problem.