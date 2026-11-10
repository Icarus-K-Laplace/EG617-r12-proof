# M1 declaration audit — LEVEL 1

Commit 64599f21f6d5f43a6c1fc385ee2eedb68525ee45; Linux run42620051771. Every entry below compiled, passed actual axiom inspection, and has its full type printed in the successful job log. M2 additions are excluded from this report.

## EG617.tau12

File: lean/EG617/Combinatorics/TuranArithmetic.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
def tau12 (n : ℕ) : ℕ
~~~

Transitive axioms: none.

## EG617.tau12_add_turanNumber

File: lean/EG617/Combinatorics/TuranArithmetic.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem tau12_add_turanNumber (n : ℕ) (hn : n ≤ 145) :
    tau12 n + SimpleGraph.turanNumber n 12 = Nat.choose n 2
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.inducedColorGraph

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
def inducedColorGraph (c : EdgeColoring) (i : Color) (S : Finset Vertex) :
    SimpleGraph S
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.colorEdgeCount

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
noncomputable def colorEdgeCount (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) : ℕ
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.colorEdgeCount_univ

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem colorEdgeCount_univ (c : EdgeColoring) (i : Color) :
    colorEdgeCount c i Finset.univ = (colorGraph c i).edgeFinset.card
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.inducedColorGraph_adj_iff

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem inducedColorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) (u v : S) :
    (inducedColorGraph c i S).Adj u v ↔
      ∃ h : (u : Vertex) ≠ (v : Vertex), c (edgeOf u v h) = i
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.induced_edge_unique_color

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem induced_edge_unique_color (c : EdgeColoring) (S : Finset Vertex)
    (u v : S) (h : u ≠ v) :
    ∃! i : Color, (inducedColorGraph c i S).Adj u v
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.induced_color_edges_disjoint

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem induced_color_edges_disjoint (c : EdgeColoring) (S : Finset Vertex) :
    ((Finset.univ : Finset Color) : Set Color).PairwiseDisjoint
      (fun i => (inducedColorGraph c i S).edgeFinset)
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.induced_color_edges_union

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem induced_color_edges_union (c : EdgeColoring) (S : Finset Vertex) :
    (Finset.univ.biUnion fun i : Color => (inducedColorGraph c i S).edgeFinset) =
      (⊤ : SimpleGraph S).edgeFinset
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.sum_colorEdgeCount

File: lean/EG617/Frontend/EdgeCounting.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem sum_colorEdgeCount (c : EdgeColoring) (S : Finset Vertex) :
    ∑ i : Color, colorEdgeCount c i S = S.card.choose 2
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.inducedColorGraph_compl_cliqueFree

File: lean/EG617/Frontend/TuranBounds.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem inducedColorGraph_compl_cliqueFree (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    (inducedColorGraph c i S)ᶜ.CliqueFree 13
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.tau12_le_colorEdgeCount

File: lean/EG617/Frontend/TuranBounds.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem tau12_le_colorEdgeCount (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) :
    tau12 S.card ≤ colorEdgeCount c i S
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.D

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
def D (n : ℕ) : ℕ
~~~

Transitive axioms: none.

## EG617.colorEdgeCount_add_eleven_tau_le

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem colorEdgeCount_add_eleven_tau_le (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    colorEdgeCount c i S + 11 * tau12 S.card ≤ S.card.choose 2
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.hereditary_color_cap

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem hereditary_color_cap (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) : colorEdgeCount c i S ≤ D S.card
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.hereditary_cap_subtraction_exact

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem hereditary_cap_subtraction_exact (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) : D S.card + 11 * tau12 S.card = S.card.choose 2
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.exists_least_color

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem exists_least_color (c : EdgeColoring) :
    ∃ i : Color, ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.least_color_edgeCount_le_870

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem least_color_edgeCount_le_870 (c : EdgeColoring) (i : Color)
    (hi : ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) :
    colorEdgeCount c i Finset.univ ≤ 870
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.exists_least_color_with_hereditary_cap

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem exists_least_color_with_hereditary_cap (c : EdgeColoring)
    (hc : ValidColoring c) :
    ∃ i : Color,
      (∀ j : Color, colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) ∧
      colorEdgeCount c i Finset.univ ≤ 870 ∧
      (∀ S : Finset Vertex, colorEdgeCount c i S ≤ D S.card)
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

## EG617.exists_colorGraph_card_edgeFinset_le_870

File: lean/EG617/Frontend/HereditaryCaps.lean. Kernel: PASS. Frozen paper: lem:caps, initial CAP/color-counting layer (conclusion or proof helper).

~~~lean
theorem exists_colorGraph_card_edgeFinset_le_870 (c : EdgeColoring) :
    ∃ i : Color, (colorGraph c i).edgeFinset.card ≤ 870
~~~

Transitive axioms: propext, Classical.choice, Quot.sound.

