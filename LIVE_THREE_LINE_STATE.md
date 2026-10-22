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

Repository promotion note: the uploaded ZIP could not be independently unpacked/replayed in the current chat runtime, so the package proof is recorded as `SOURCE_REPORTED_PROVED / INDEPENDENT_REPLAY_PENDING` rather than silently presented as independently replayed here.

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
- triangle-row union lemma;
- `G=4` empty;
- `G=5` empty;
- `G=6` empty;
- `G=7,h=0` empty.

The G=7,h=0 proof eliminates k=3,4,5 directly and then every k=6,7 incidence layer using active/inactive support counting, the degree1/degree2 low-repivot inequalities, pair-row coverage, and the triangle-row union lemma.

Current Line-C frontier is now exactly:

- `G=7,h=1`;
- exact `H2-G7-K4minusE`;
- `G=8,h=0`;
- `G=8,h=1`.

There is no h=2,G=8 state.

A useful coupling has been identified for the exact `H2-G7-K4minusE` cell: repivoting one of its nine low rows produces either another G7/h2 plateau view or a G8/h1 view, so closing G8/h1 is expected to kill the remaining two-high G7 cell as well.

The full EG617 r=12 theorem remains OPEN.
