# E406 d11: corrected one-budget reduction

Status: `PROVED` under `E406_D11_CENTER_SHIELDING.md`. This file supersedes the earlier stronger wording that omitted the `c=e(S,E)` term in the T-view excess budget. `E406` remains `OPEN`.

The previous theorem leaves two shielding modes after proving `r+delta<=1`:

- Mode A: `r=0`, `delta=1`; hence `c=1`, D-E is anticomplete, and the unique S-E edge is `s0e0`.
- Mode B: `r=1`, `delta=0`; the unique D-E edge is `d0e0`; the optional S-E edge is absent or has its S-end at a star leaf.

Correct q31 block-excess inequalities are

    m_S+m_E+r >=13,                         (Y)
    m_S+m_D+r+c >=13,                       (T)
    m_D+m_E+c >=12.                         (OLD)

The extra `c` in (T) is necessary because the T-view removes E, so the inserted S-block loses the c S-E edges and has excess `8-m_S-c`.

Let `O=C\(D union E)`, `|O|=25`.

Every ordinary S-star leaf s and D-star leaf d gives the independent five-set

    {T,s0,s,d0,d}.

Hence the four O-neighbourhoods of s0,s,d0,d cover O.

## 1. Row-class caps

Every S-star leaf is a q30 plateau d3 pivot. A shared 3-row class of size k creates at least `3(k-1)` decoration after repivot, so q30 gives `k<=3`.

A shared 3-row class in a q31 shell has `k<=4`.

## 2. Mode A: only one residual family survives the cover argument

Assume `r=0`, `c=delta=1`.

The fixed centre O-neighbourhoods have sizes

    |A|=|N_O(s0)|=9,
    |B|=|N_O(d0)|=11.

For every S-leaf row P and D-leaf row Q,

    A union B union P union Q = O,

with total incidence26.

The Y-inequality and `m_E<=8` give `m_S>=5`.

If `|A intersect B|=1`, P and Q partition a fixed six-point remainder, forcing one common S-row for all at least five S-leaves, contradicting the q30 cap3. Hence `A intersect B=empty`.

Let R be the fixed five-point remainder.

Each S-row P is disjoint from A because the missing shell edge s0-s has row weights10 and3 and the E406 row-union floor is13.

If some P meets B, it meets B in exactly one point and contributes only two points of R; every D-row Q is then forced to be the same complementary 3-subset of R. This is impossible if `m_D>=5`, but is compatible with the q31 cap only when `m_D=4`.

If every P lies in R, then either a D-row has only two R-points, forcing all S-rows equal (impossible because `m_S>=5`), or all D-rows also lie in R. In the latter case `|P intersect Q|=1` for every cross pair. Passing to 2-subset complements in R, two distinct S-rows force all D-rows equal. Again the only possible multiplicity is `m_D=4`.

Using (T), `m_D=4` forces `m_S=8`.
Using (OLD), `m_E>=7`, while `c=1` gives `m_E<=8`.

Thus Mode A is reduced to exactly

    A1: (m_S,m_D,m_E,r,c)=(8,4,7,0,1) or (8,4,8,0,1).

The earlier claim that Mode A was empty was too strong and is retracted by this corrected file.

## 3. Mode B: finite corrected residual table

Assume `r=1`, `delta=0`, and `d0e0` is the unique D-E edge.

The centre O-neighbourhoods have sizes10 and10. Their two leaf rows again give a 26-incidence cover.

If the centre neighbourhoods meet, the leaf rows partition a fixed six-point remainder. If `c=0`, all S-leaves are ordinary and `m_S>=4`, contradicting q30 class cap3. If `c=1`, the only possible way to have at most three ordinary S-leaves is `m_S=4`, but then (T) gives `m_D>=7`, and all D-rows coincide, violating the q31 cap4. Therefore the two centre O-neighbourhoods are disjoint.

Let R be the fixed five-point remainder.

As in Mode A, either all D-rows are forced equal, or all ordinary S-rows coincide.

### B1. D-row class branch

If all D-rows coincide, the q31 cap gives `m_D<=4`.

- If `c=0`, (T) and (OLD) force

      (m_S,m_D,m_E)=(8,4,8).

- If `c=1`, the possibilities are

      m_D=3, (m_S,m_E)=(8,8),

  or

      m_D=4, m_S in {7,8}, m_E in {7,8}.

These are the corrected B1 rows.

### B2. Single ordinary S-row branch

If all ordinary S-rows coincide, q30 cap3 forces exactly three ordinary leaves. Hence

    c=1, m_S=4,

and the unique exceptional S-E edge is incident with the fourth S-leaf.

Now (Y) gives `m_E=8`, while (T) gives `m_D in {7,8}`.

Thus corrected B2 is

    c=1, m_S=4, m_E=8, m_D in {7,8}, r=1.

## 4. Correct current d11 table

After all proved reductions, d11 has only the following finite parameter rows:

- A1: `(8,4,7,0,1)` or `(8,4,8,0,1)`;
- B1a: `c=0`, `(m_S,m_D,m_E)=(8,4,8)`, `r=1`;
- B1b: `c=1`, `(m_S,m_D,m_E)=(8,3,8)`, `r=1`;
- B1c: `c=1`, `m_D=4`, `m_S,m_E in {7,8}`, `r=1`;
- B2: `c=1`, `m_S=4`, `m_E=8`, `m_D in {7,8}`, `r=1`.

This is still a drastic reduction from the original d11 family, but it is not yet a closure.

## 5. Next target

Rows with `m_D=4` force a saturated q31 3-row class of size4. Repivoting such a D-leaf yields `q=31`, `z=22`, `G=9`; the shared support is a P3 and the new missing shell is `K3,7` plus one internal missing edge and three isolates.

Rows with `m_S=4` force a saturated q30 S-row class of size3 plus one exceptional S-leaf.

These saturation geometries are the next analytic target.