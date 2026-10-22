# Live three-line research state — 2026-10-22

This is the synchronized human-readable live state for Lines A/B/C. It contains research results only, not agent prompts.

## Line A — T61 front end

Repository-canonical proved layers: `E397..E400` empty.

Latest supplied V6 package reports a uniform theorem closing

`E401, E402, E403, E404`.

Reported interface:

`q<=29, G<=7, delta(C)>=12, every M-edge uv has t_u+t_v>=13`

forces a legal degree-13 repivot with `q_y>=30`, while the parent-layer core floor gives `q_y<=E-375<=29` for `E<=404`.

V6 also corrects the repivot equality by restoring three omitted nonnegative terms and removes `(q,z,G)=(25,21,4)` as an illegal cell via `D(14)=69`.

Reported certificate: 127 exact rational rows replayed successfully by the source package.

Current package-level front-end window: `E405..E408`.

Repository promotion note: the uploaded ZIP could not be independently unpacked/replayed in the current chat runtime, so the package proof is recorded separately as `SOURCE_REPORTED_PROVED` rather than silently presented as independently replayed here.

## Line B — high backend E333..E340

All edge layers remain `OPEN`.

V2 reports:

- a complete adjacent two-pivot exchange system;
- exact q-difference and `tau_y-tau_p = |D cap high| - |S cap high|`;
- proof that reverse-pivot equality is not an independent second inequality;
- q34-q35 true-twin branch compressed to 76 necessary quotient rows (44 bipartite, 29 K4-free triangle, 3 q35 K4);
- triangle-free non-bipartite branch eliminated;
- four exact local q30-q33 two-pivot certificates showing naive one-step `Phi=(q,tau)` monotonicity is false.

Therefore the next high-layer theorem must use a third pivot, joint constraints across distinct S-rows, or a nonadjacent-pivot weighted inequality.

Reported replay: 44 scalar states, 76 q34/q35 rows, 4 local certificates, q36-q38 atomic-defect table.

## Line C — E332 q30+211

This line is repository-canonical and has standalone proof files.

Now proved:

- undecorated d=4..9 impossible by profitable repivot;
- d10 branch empty;
- d3 branch empty;
- regular missing degrees reduced to `{0,1,2,11,12}`;
- at most two regular high vertices;
- strengthened zero-gap theorem;
- `G=4` empty;
- `G=5` empty;
- `G=6` empty.

The full G=6 closure uses the triangle-row union lemma

`M-triangle r,s,t => |D_r union D_s union D_t|>=24`,

kills the exact `H2-G6-K4` state by a 36-in-35 row-disjointness contradiction, and eliminates every unique-high state by exact support accounting.

Current Line-C frontier:

- `G=7,h=0`;
- `G=7,h=1`;
- exact `H2-G7-K4minusE`;
- `G=8,h=0`;
- `G=8,h=1`.

New ongoing reduction for `G=7,h=0`: support sizes `k=3,4,5` are analytically eliminated; the active h=0 work is therefore concentrated on `k=6,7` plus the remaining exact incidence subcases.

The full EG617 r=12 theorem remains OPEN.
