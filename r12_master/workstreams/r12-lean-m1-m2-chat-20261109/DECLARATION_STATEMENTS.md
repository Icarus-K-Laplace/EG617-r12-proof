# All declaration statements and kernel evidence

Commit ee2dbe9d6d0c5298dc6cfc8a4f8c91e5d8bcdf06; [complete run](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/42953650338). All entries below PASS the kernel build and transitive axiom inspection. The source headers retain section variables: Admissibility.lean uses {V : Type u}; R224.lean uses {V : Type u} [Fintype V]. Machine-elaborated full types are in logs/statement-inspection.txt; complete source proofs are in the linked standard .lean files. Definitions are NOT proofs of their propositions.

## EG617.colorGraph

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
def colorGraph (c : EdgeColoring) (i : Color) : SimpleGraph Vertex where
  Adj u v
~~~

## EG617.colorGraph_adj_iff

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem colorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (u v : Vertex) (h : u ≠ v) :
    (colorGraph c i).Adj u v ↔ c (edgeOf u v h) = i
~~~

## EG617.validColoring_iff_colorGraph

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem validColoring_iff_colorGraph (c : EdgeColoring) :
    ValidColoring c ↔ ∀ S : Finset Vertex, S.card = 13 →
      ∀ i : Color, ∃ u ∈ S, ∃ v ∈ S, (colorGraph c i).Adj u v
~~~

## EG617.colorGraph_partition

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem colorGraph_partition (c : EdgeColoring) (u v : Vertex) (h : u ≠ v) :
    ∃! i : Color, (colorGraph c i).Adj u v
~~~

## EG617.no_independent_thirteen

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem no_independent_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v)
~~~

## EG617.no_monochromatic_thirteen

Source: [lean/EG617/Basic/ColoringLemmas.lean](lean/EG617/Basic/ColoringLemmas.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem no_monochromatic_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i)
~~~

## EG617.Vertex

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: none.

~~~lean
abbrev Vertex
~~~

## EG617.Color

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: none.

~~~lean
abbrev Color
~~~

## EG617.Edge

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
abbrev Edge
~~~

## EG617.EdgeColoring

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
abbrev EdgeColoring
~~~

## EG617.edgeOf

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
def edgeOf (u v : Vertex) (h : u ≠ v) : Edge
~~~

## EG617.Inside

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def Inside (e : Edge) (S : Finset Vertex) : Prop
~~~

## EG617.edgeOf_swap

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem edgeOf_swap (u v : Vertex) (h : u ≠ v) :
    edgeOf u v h = edgeOf v u h.symm
~~~

## EG617.edgeOf_eq_iff

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem edgeOf_eq_iff
    (u v x y : Vertex) (huv : u ≠ v) (hxy : x ≠ y) :
    edgeOf u v huv = edgeOf x y hxy ↔
      (u = x ∧ v = y) ∨ (u = y ∧ v = x)
~~~

## EG617.edge_has_endpoints

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem edge_has_endpoints (e : Edge) :
    ∃ u v : Vertex, u ≠ v ∧ e.val = s(u, v)
~~~

## EG617.edgeOf_surjective

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Quot.sound.

~~~lean
theorem edgeOf_surjective (e : Edge) :
    ∃ u v : Vertex, ∃ h : u ≠ v, edgeOf u v h = e
~~~

## EG617.edgeOf_inside_iff

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem edgeOf_inside_iff
    (u v : Vertex) (h : u ≠ v) (S : Finset Vertex) :
    Inside (edgeOf u v h) S ↔ u ∈ S ∧ v ∈ S
~~~

## EG617.inside_mono

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem inside_mono {e : Edge} {S T : Finset Vertex}
    (hST : S ⊆ T) (he : Inside e S) : Inside e T
~~~

## EG617.mem_complete_iff

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem mem_complete_iff (e : Sym2 Vertex) :
    e ∈ (SimpleGraph.completeGraph Vertex).edgeSet ↔ ¬ e.IsDiag
~~~

## EG617.edgeEquivComplete

Source: [lean/EG617/Basic/Definitions.lean](lean/EG617/Basic/Definitions.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def edgeEquivComplete :
    Edge ≃ (SimpleGraph.completeGraph Vertex).edgeSet where
  toFun e
~~~

## EG617.ValidColoring

Source: [lean/EG617/Basic/OriginalProblem.lean](lean/EG617/Basic/OriginalProblem.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def ValidColoring (c : EdgeColoring) : Prop
~~~

## EG617.EG617R12Statement

Source: [lean/EG617/Basic/OriginalProblem.lean](lean/EG617/Basic/OriginalProblem.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def EG617R12Statement : Prop
~~~

## EG617.validColoring_iff_endpoints

Source: [lean/EG617/Basic/OriginalProblem.lean](lean/EG617/Basic/OriginalProblem.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem validColoring_iff_endpoints (c : EdgeColoring) :
    ValidColoring c ↔
      ∀ S : Finset Vertex, S.card = 13 → ∀ i : Color,
        ∃ u ∈ S, ∃ v ∈ S, ∃ h : u ≠ v, c (edgeOf u v h) = i
~~~

## EG617.originalProblem_iff_missingColor

Source: [lean/EG617/Basic/OriginalProblem.lean](lean/EG617/Basic/OriginalProblem.lean). Paper: Original K145 graph-coloring statement and equivalence helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem originalProblem_iff_missingColor :
    EG617R12Statement ↔
      ∀ c : EdgeColoring, ∃ S : Finset Vertex, S.card = 13 ∧
        ∃ i : Color, ∀ e : Edge, Inside e S → c e ≠ i
~~~

## EG617.tau12

Source: [lean/EG617/Combinatorics/TuranArithmetic.lean](lean/EG617/Combinatorics/TuranArithmetic.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: none.

~~~lean
def tau12 (n : ℕ) : ℕ
~~~

## EG617.tau12_add_turanNumber

Source: [lean/EG617/Combinatorics/TuranArithmetic.lean](lean/EG617/Combinatorics/TuranArithmetic.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem tau12_add_turanNumber (n : ℕ) (hn : n ≤ 145) :
    tau12 n + SimpleGraph.turanNumber n 12 = Nat.choose n 2
~~~

## EG617.CoreIndependenceBound

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def CoreIndependenceBound (a : ℕ) (G : SimpleGraph V) : Prop
~~~

## EG617.CoreCliqueBound

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def CoreCliqueBound (k : ℕ) (G : SimpleGraph V) : Prop
~~~

## EG617.coreInducedEdgeCount

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
noncomputable def coreInducedEdgeCount (G : SimpleGraph V) (S : Finset V) : ℕ
~~~

## EG617.CoreAdmissible

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def CoreAdmissible (a : ℕ) (G : SimpleGraph V) : Prop
~~~

## EG617.core_induced_edge_count_univ

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_induced_edge_count_univ [Fintype V] (G : SimpleGraph V) :
    coreInducedEdgeCount G Finset.univ = G.edgeFinset.card
~~~

## EG617.core_independenceBound_induce

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_independenceBound_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound a G) (S : Finset V) :
    CoreIndependenceBound a (G.induce (S : Set V))
~~~

## EG617.core_cliqueBound_induce

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_cliqueBound_induce (G : SimpleGraph V) (k : ℕ)
    (hG : CoreCliqueBound k G) (S : Finset V) :
    CoreCliqueBound k (G.induce (S : Set V))
~~~

## EG617.core_independence_nonNeighbors

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_independence_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound (a + 1) G) (v : V) (S : Finset V)
    (hS : ∀ w ∈ S, w ≠ v ∧ ¬ G.Adj v w) (hind : G.IsIndepSet (S : Set V)) :
    S.card ≤ a
~~~

## EG617.core_compl_edge_count

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_compl_edge_count [Fintype V] (G : SimpleGraph V) :
    G.edgeFinset.card + Gᶜ.edgeFinset.card = (Fintype.card V).choose 2
~~~

## EG617.core_induced_edge_count_image

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_induced_edge_count_image (G : SimpleGraph V) (S : Finset V)
    (T : Finset S) :
    coreInducedEdgeCount (G.induce (S : Set V)) T =
      coreInducedEdgeCount G (T.image fun x : S => (x : V))
~~~

## EG617.core_admissible_induce

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_admissible_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible a G) (S : Finset V) :
    CoreAdmissible a (G.induce (S : Set V))
~~~

## EG617.core_admissible_nonNeighbors

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_admissible_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible (a + 1) G) (v : V) (S : Finset V)
    (hS : ∀ w ∈ S, w ≠ v ∧ ¬ G.Adj v w) :
    CoreAdmissible a (G.induce (S : Set V))
~~~

## EG617.Gate47Statement

Source: [lean/EG617/Core/Admissibility.lean](lean/EG617/Core/Admissibility.lean). Paper: Frozen low preamble R(a,n) contract and induced inheritance; nonneighbor helper used in M4-M6. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def Gate47Statement : Prop
~~~

## EG617.core_not_two_colorable_of_card_24

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_not_two_colorable_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
~~~

## EG617.core_triangleFree_edges_lt_132_of_card_24

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_triangleFree_edges_lt_132_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
~~~

## EG617.core_R224_empty_of_card

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R224_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 24) : ¬ CoreAdmissible 2 G
~~~

## EG617.core_not_two_colorable_24

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_not_two_colorable_24 (L : SimpleGraph (Fin 24))
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
~~~

## EG617.core_triangleFree24_edges_lt_132

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_triangleFree24_edges_lt_132 (L : SimpleGraph (Fin 24))
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
~~~

## EG617.core_R224_empty

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M1, R(2,24) emptiness and its AES proof helpers. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R224_empty (G : SimpleGraph (Fin 24)) : ¬ CoreAdmissible 2 G
~~~

## EG617.core_R3_card_le_degree_add_24

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M4 first step, delta>=11 ONLY. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R3_card_le_degree_add_24 (G : SimpleGraph V)
    (hG : CoreAdmissible 3 G) (v : V) : Fintype.card V ≤ G.degree v + 24
~~~

## EG617.core_R335_degree_ge_11

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M4 first step, delta>=11 ONLY. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R335_degree_ge_11 (G : SimpleGraph (Fin 35))
    (hG : CoreAdmissible 3 G) (v : Fin 35) : 11 ≤ G.degree v
~~~

## EG617.core_R337_empty_of_card

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M5, R(3,37) exclusion. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R337_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 37) : ¬ CoreAdmissible 3 G
~~~

## EG617.core_R337_empty

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M5, R(3,37) exclusion. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R337_empty (G : SimpleGraph (Fin 37)) : ¬ CoreAdmissible 3 G
~~~

## EG617.core_R4_card_le_degree_add_37

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M6, d<=9 exclusion ONLY. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R4_card_le_degree_add_37 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (v : V) : Fintype.card V ≤ G.degree v + 37
~~~

## EG617.core_R447_degree_ge_10

Source: [lean/EG617/Core/R224.lean](lean/EG617/Core/R224.lean). Paper: Frozen low M6, d<=9 exclusion ONLY. Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem core_R447_degree_ge_10 (G : SimpleGraph (Fin 47))
    (hG : CoreAdmissible 4 G) (v : Fin 47) : 10 ≤ G.degree v
~~~

## EG617.independent_card_le_twelve

Source: [lean/EG617/Frontend/ColoringReduction.lean](lean/EG617/Frontend/ColoringReduction.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem independent_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hind : ∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v) :
    S.card ≤ 12
~~~

## EG617.monochromatic_card_le_twelve

Source: [lean/EG617/Frontend/ColoringReduction.lean](lean/EG617/Frontend/ColoringReduction.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem monochromatic_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hmono : ∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i) :
    S.card ≤ 12
~~~

## EG617.colorGraph_clique_card_le_twelve

Source: [lean/EG617/Frontend/ColoringReduction.lean](lean/EG617/Frontend/ColoringReduction.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem colorGraph_clique_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hclique : ∀ u ∈ S, ∀ v ∈ S, u ≠ v → (colorGraph c i).Adj u v) :
    S.card ≤ 12
~~~

## EG617.inducedColorGraph

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
def inducedColorGraph (c : EdgeColoring) (i : Color) (S : Finset Vertex) :
    SimpleGraph S
~~~

## EG617.colorEdgeCount

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
noncomputable def colorEdgeCount (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) : ℕ
~~~

## EG617.colorEdgeCount_univ

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem colorEdgeCount_univ (c : EdgeColoring) (i : Color) :
    colorEdgeCount c i Finset.univ = (colorGraph c i).edgeFinset.card
~~~

## EG617.inducedColorGraph_adj_iff

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem inducedColorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) (u v : S) :
    (inducedColorGraph c i S).Adj u v ↔
      ∃ h : (u : Vertex) ≠ (v : Vertex), c (edgeOf u v h) = i
~~~

## EG617.induced_edge_unique_color

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem induced_edge_unique_color (c : EdgeColoring) (S : Finset Vertex)
    (u v : S) (h : u ≠ v) :
    ∃! i : Color, (inducedColorGraph c i S).Adj u v
~~~

## EG617.induced_color_edges_disjoint

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem induced_color_edges_disjoint (c : EdgeColoring) (S : Finset Vertex) :
    ((Finset.univ : Finset Color) : Set Color).PairwiseDisjoint
      (fun i => (inducedColorGraph c i S).edgeFinset)
~~~

## EG617.induced_color_edges_union

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem induced_color_edges_union (c : EdgeColoring) (S : Finset Vertex) :
    (Finset.univ.biUnion fun i : Color => (inducedColorGraph c i S).edgeFinset) =
      (⊤ : SimpleGraph S).edgeFinset
~~~

## EG617.sum_colorEdgeCount

Source: [lean/EG617/Frontend/EdgeCounting.lean](lean/EG617/Frontend/EdgeCounting.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem sum_colorEdgeCount (c : EdgeColoring) (S : Finset Vertex) :
    ∑ i : Color, colorEdgeCount c i S = S.card.choose 2
~~~

## EG617.D

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: none.

~~~lean
def D (n : ℕ) : ℕ
~~~

## EG617.colorEdgeCount_add_eleven_tau_le

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem colorEdgeCount_add_eleven_tau_le (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    colorEdgeCount c i S + 11 * tau12 S.card ≤ S.card.choose 2
~~~

## EG617.hereditary_color_cap

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem hereditary_color_cap (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) : colorEdgeCount c i S ≤ D S.card
~~~

## EG617.hereditary_cap_subtraction_exact

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem hereditary_cap_subtraction_exact (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) : D S.card + 11 * tau12 S.card = S.card.choose 2
~~~

## EG617.exists_least_color

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem exists_least_color (c : EdgeColoring) :
    ∃ i : Color, ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ
~~~

## EG617.least_color_edgeCount_le_870

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem least_color_edgeCount_le_870 (c : EdgeColoring) (i : Color)
    (hi : ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) :
    colorEdgeCount c i Finset.univ ≤ 870
~~~

## EG617.exists_least_color_with_hereditary_cap

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem exists_least_color_with_hereditary_cap (c : EdgeColoring)
    (hc : ValidColoring c) :
    ∃ i : Color,
      (∀ j : Color, colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) ∧
      colorEdgeCount c i Finset.univ ≤ 870 ∧
      (∀ S : Finset Vertex, colorEdgeCount c i S ≤ D S.card)
~~~

## EG617.exists_colorGraph_card_edgeFinset_le_870

Source: [lean/EG617/Frontend/HereditaryCaps.lean](lean/EG617/Frontend/HereditaryCaps.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem exists_colorGraph_card_edgeFinset_le_870 (c : EdgeColoring) :
    ∃ i : Color, (colorGraph c i).edgeFinset.card ≤ 870
~~~

## EG617.inducedColorGraph_compl_cliqueFree

Source: [lean/EG617/Frontend/TuranBounds.lean](lean/EG617/Frontend/TuranBounds.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem inducedColorGraph_compl_cliqueFree (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    (inducedColorGraph c i S)ᶜ.CliqueFree 13
~~~

## EG617.tau12_le_colorEdgeCount

Source: [lean/EG617/Frontend/TuranBounds.lean](lean/EG617/Frontend/TuranBounds.lean). Paper: Frozen CAP / frontend initial color-counting layer (including least-color selection). Kernel PASS. Axioms: propext, Classical.choice, Quot.sound.

~~~lean
theorem tau12_le_colorEdgeCount (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) :
    tau12 S.card ≤ colorEdgeCount c i S
~~~

