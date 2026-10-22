# E406 d11: close the S-centre shield and reduce the D-centre shield

Status: `PROVED` under `E406_D11_CENTER_SHIELDING.md`. `E406` remains `OPEN`.

The previous theorem leaves two shielding modes after proving `r+delta<=1`:

- Mode A: `r=0`, `delta=1`, so D-E is anticomplete and the unique S-E edge is `s0e0`.
- Mode B: `r=1`, `delta=0`, so the unique D-E edge is `d0e0`; the optional S-E edge is absent or has its S-end at a star leaf.

Here `r=e(D,E)` and `delta` records whether the unique S-E edge is incident with the S-star centre.

Let `O=C\(D union E)`, `|O|=25`.

For an ordinary S-star leaf s and a D-star leaf d, the independent five-set

`{T,s0,s,d0,d}`

forces the four O-neighbourhoods to cover O.

## 1. Row-class caps used below

Every S-star leaf is a q30 plateau d3 pivot. Its 3-row P is a degree-12 target triangle and a q30 row class has multiplicity at most3: if k vertices share P, repivoting one member gives at least `3(k-1)` decoration on P, while q30 allows only `G<=8`.

A 3-row class in a q31 shell has multiplicity at most4 by the same argument and `G<=9`.

## 2. Mode A is impossible

Assume `r=0`, `delta=1`.

The fixed centre O-neighbourhoods have sizes

`|A|=|N_O(s0)|=9`,
`|B|=|N_O(d0)|=11`.

For every S-leaf row P and D-leaf row Q,

`A union B union P union Q = O`,

with total incidence `9+11+3+3=26`.

Let `x=|A intersect B|`. Necessarily `x<=1`.

### 2.1 x=1

Then `|A union B|=19`; the six row incidences from P,Q must partition the fixed six-point remainder. Hence every S-leaf has the same P and every D-leaf the same Q.

The q31 excess inequality `m_S+m_E>=13`, together with `m_E<=8` in Mode A, gives `m_S>=5`. This contradicts the q30 row-class cap3.

### 2.2 x=0

Now `|A union B|=20`, with fixed remainder R of size5.

Every S-row P is disjoint from A because the missing shell edge `s0s` has row weights10 and3 and the E406 row-union floor is13.

If some P meets B, it can meet B in at most one point: otherwise P contributes at most one point of R and a 3-row Q cannot cover the other four. If `|P intersect B|=1`, P contributes exactly two points of R and every D-row Q must be the fixed complementary 3-subset of R. Since Mode A also gives `m_D>=5`, this violates the q31 row-class cap4.

Hence every S-row P is a 3-subset of R.

For a D-row Q, if `|Q intersect R|=2`, then every S-row must be the unique complementary 3-subset of R, again contradicting `m_S>=5` and the q30 cap3. Therefore every D-row is also a 3-subset of R.

For all P,Q we must have `P union Q=R`, hence `|P intersect Q|=1`. Passing to complements in R, the families of 2-subsets `R-P` and `R-Q` are cross-disjoint.

The S-side cannot have only one distinct P because `m_S>=5` and class size is at most3. Take two distinct S-complements. If they are disjoint, no 2-subset can be disjoint from both; if they meet, their union has size3 and there is exactly one 2-subset disjoint from both. Thus all D-rows are equal, contradicting `m_D>=5` and the q31 class cap4.

Therefore Mode A is empty.

## 3. Mode B has only two residual parameter patterns

Now assume `r=1`, `delta=0`. Centre shielding forces the unique D-E edge to be `d0e0`.

The centre O-neighbourhoods have sizes

`|A|=10`, `|B|=10`.

Again every ordinary S-leaf row P and D-leaf row Q gives a 26-incidence cover of O.

If `|A intersect B|=1`, the two 3-rows partition a fixed six-point remainder. Hence all D-leaf rows coincide. If there are at least five D-leaves this violates the q31 cap4; the only possible way to have at most four D-leaves would force `m_S=8,m_D=4`, but then all eight (or at least seven ordinary) S-leaves coincide as well, contradicting the q30 cap3. So `A intersect B=empty`.

Let R be the resulting fixed five-point remainder.

If an ordinary S-row P meets B, the same cover argument forces all D-rows equal. Therefore either `m_D=4` or every ordinary S-row lies in R.

If the ordinary S-rows contain at least two distinct 3-subsets of R, the cross-disjoint-complement argument forces all D-rows equal, so again `m_D=4`. The inequality `m_S+m_D>=12` then forces

`m_S=8, m_D=4`.      (B1)

The only alternative is that all ordinary S-rows coincide. The q30 class cap3 then forces exactly three ordinary leaves, so the unique exceptional S-E endpoint is a fourth leaf:

`c=1, m_S=4`.

The q31 excess inequalities and the upper bounds `m_D,m_E<=8` force

`m_D=m_E=8`.      (B2)

Thus the entire d11 terminal is reduced to exactly two residual parameter patterns:

- **B1:** `m_S=8, m_D=4, r=1`, with `m_E=8` if c=0 and `m_E in {7,8}` if c=1;
- **B2:** `c=1`, `(m_S,m_D,m_E)=(4,8,8)`, `r=1`, where the S-E edge is incident with the unique exceptional S-leaf.

No other d11 shielding parameters survive.

## 4. Next target

In B1, the four D-star leaves are forced into one q31 3-row class of size4, saturating the class cap. Repivoting such a leaf gives `q=31`, `z=22`, `G=9`; the shared support is forced into a P3 and the resulting missing shell is `K3,7` plus one internal edge and three isolates.

In B2, the three ordinary S-leaves form one q30 3-row class, while the eight D-leaves live over at most three possible 3-rows in the same five-point remainder.

These are now the only d11 compatibility problems.