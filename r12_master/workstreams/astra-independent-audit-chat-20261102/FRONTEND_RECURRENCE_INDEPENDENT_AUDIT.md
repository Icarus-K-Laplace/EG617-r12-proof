# Independent frontend recurrence audit

Date: 2026-11-02  
Frozen integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`

## Result

A third integer implementation of the contextual recurrence was written independently of the two frozen transcriptions. It reconstructs the 12-by-146 bound table from the theorem text, derives maximum orders, evaluates all 144 outer ((d,j)) stops, and reconstructs all 61 T61 minimum-degree rows.

Exact comparison with the frozen `FRONTEND_REPLAY.json` gives:

| Object | Recomputed | Exact matches |
|---|---:|---:|
| Recurrence nodes | 1,752 | 1,752 |
| Maximum-order entries | 13 | 13 |
| Outer stopping comparisons | 144 | 144 |
| T61 terminal rows | 61 | 61 |

The only surviving outer stop is
[
(d,j,a,n)=(11,6,5,61),qquad 397\le e(F)\le408.
]

The terminal rows are:

| Minimum degree (h) | Core order | Core floor | Shell (q)-floor | Total floor |
|---:|---:|---:|---:|---:|
| 12 | 48 | 308 | 20 | 406 |
| 13 | 47 | 284 | 22 | 397 |
| 14 | 46 | 262 | 33 | 427 |

Thus the 408-edge budget excludes (h\ge14), while the contextual R(4,49) exclusion rules out (h\le11). The remaining minimum degree is exactly 12 or 13, matching the terminal interface in the integrated proof.

The runnable third transcription is `RECHECK_FRONTEND_THIRD.js`; its comparison receipt is `FRONTEND_THIRD_REPLAY_RESULT.json`. It uses only integer arithmetic and Node's built-in file/path modules. It reads the frozen replay file from the sibling integration workstream and does not import either frozen recurrence implementation.

## Analytic rule audit

The recurrence rules were checked against the displayed graph argument:

1. For an (M)-edge, the union of its two core rows has size at least (eta=\max(0,m-N_{a-2})), since the common non-neighborhood in the core has independence at most (a-2). The exact shell identity gives (q\ge\beta-1), and the induced ((m+2))-set gives (e(C)+\beta\le D(m+2)).
2. A matching of size (t) gives (t\) disjoint endpoint pairs, each with row-union at least (eta). The target graph on the (2t) endpoints has at least (p_a(2t)) edges, so the missing graph has at most ({2t\choose2}-p_a(2t)) edges. The shell identity yields (q\ge t\beta-{2t\choose2}+p_a(2t)).
3. If the missing graph is triangle-free, Mantel gives the stronger endpoint bound (q\ge t\beta-t^2).
4. If it contains a triangle, the common non-neighborhood of the three independent target-shell vertices has independence at most (a-3); the induced ((m+3))-set gives (e(C)+\gamma\le D(m+3)), and the shell identity gives (q\ge\gamma-3).
5. The universal bound is the minimum of the triangle-free and triangle branches, because one of the two alternatives must hold. If the triangle density test fails, that branch is impossible and only the triangle-free bound remains.
6. The matching guarantees are (k=\max(\lceil(h-10)/2\rceil,1+[h\ge12]+[h\ge13])). The (h=12,13,14) special cases are supplied by the shell matching lemma; for (h\ge15), unmatched vertices of a maximum matching form an independent set.

These derivations are consistent with the code's use of the formulas. The replay verifies their arithmetic propagation, not the truth of the analytic graph lemmas themselves.

## Small correction in the h=13 matching lemma

COVER Section 4 says that a König vertex cover consisting of one point (s\) in the four matched endpoints (S) and one point (i\) in the unmatched nine-set (I) supports at most 12 cross edges.

The safe general bound is **13**, not 12: (s\) can be incident to at most 9 cross edges and (i\) to at most 4, and the two sets of incident edges are disjoint if (si\) is not itself an edge. If (si\) is an edge, the bound is 12. This is a one-edge overstatement in the prose.

It is harmless to the proof: even the corrected bound gives at most
[
13+{4\choose2}=19<22,
]
whereas the shell has (z\ge22). A cover of two unmatched vertices supports at most 8 cross edges, also below the required 16 cross edges. Therefore the cover must consist of two matched endpoints; the subsequent argument that at least 16 cross edges force two disjoint cross edges, and hence an independent 11-set from the other two endpoints plus (I), remains valid.

The frozen integration branch was not edited. The correction is recorded here for the authors to incorporate in a future proof-text revision.

## Certification boundary

- The exact integer recurrence and all retained stop rows are independently reproduced.
- The contextual R(4,49) premise is proved from the full-color setting in the integration package; it is not a generic uncolored R(4,49) theorem.
- The recurrence remains conditional on the analytic lower-order, matching, Turán/Mantel, and cap arguments stated in the frontend audit.
- This is not Lean kernel certification and not an external referee report.
