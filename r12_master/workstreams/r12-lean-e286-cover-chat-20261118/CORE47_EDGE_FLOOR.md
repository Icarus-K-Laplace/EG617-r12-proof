# 287-edge floor (verified)

`EG617.core47_edge_floor_287 (G : SimpleGraph (Fin 47)) (hG : CoreAdmissible 4 G) : 287 ≤ G.edgeFinset.card`
passed [Linux CI 45610341669](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/45610341669)
at `db795a78673bb9f6c84175ca24880117a77f3eb1`.

At most 286 edges, GATE47 gives minimum degree 12 from all the original hereditary caps.
At most 285 edges, a degree-12 pivot exists. Double counting its neighborhood
produces a nonedge with at most nine common neighbors. Adding this edge preserves
the clique bound, independence bound and minimum degree. Induction on the edge
deficit reaches exactly 286, where E286 excludes the resulting graph. No hereditary
cap on an intermediate extension is used.
