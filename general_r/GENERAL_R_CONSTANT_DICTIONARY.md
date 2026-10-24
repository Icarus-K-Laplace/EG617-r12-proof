# General-r Constant Dictionary

Status: UPDATED AFTER SYMBOLIC PROOF ARCHAEOLOGY.

Tags:

- `STRUCTURAL_R_FORMULA`: derived symbolically from the problem/reduction once its stated setup holds;
- `R12_ACCIDENT`: no surviving symbolic interpretation is known;
- `UNKNOWN_ORIGIN`: provenance/general formula still unresolved.

A conditional structural formula is still tagged structural when the formula itself is proved, but its upstream forcing hypothesis is stated explicitly.

| r=12 constant | symbolic form | tag | exact status |
|---:|---|---|---|
|145|`r^2+1`|STRUCTURAL_R_FORMULA|The original Erdős–Gyárfás conjecture is stated on `K_(r^2+1)`.|
|870|`r(r^2+1)/2`|STRUCTURAL_R_FORMULA|Least-color average edge upper bound.|
|61|`5r+1`|STRUCTURAL_R_FORMULA|In the anchor/block schema `|R|=r^2-d-jr`; at `d=r-1,j=r-6` this is `5r+1`. General forcing to this stop remains OPEN.|
|49|`4r+1`|STRUCTURAL_R_FORMULA|Same schema with `d=r-1,j=r-5`. General forcing to this stop remains OPEN.|
|35|`3r-1`|STRUCTURAL_R_FORMULA|Conditional on a `4r+1` residual and a degree-`r+1` pivot: `(4r+1)-1-(r+1)=3r-1`.|
|13|`r+1`|STRUCTURAL_R_FORMULA|Shell/pivot size in the symbolic backend setup. The all-r theorem forcing minimum degree `r+1` is OPEN.|
|12|`r`|STRUCTURAL_R_FORMULA|Baseline core degree/excess coordinate. The all-r theorem `delta(H_r)>=r` is OPEN.|
|91|`C(r+2,2)`|STRUCTURAL_R_FORMULA|Exact symbolic backend edge-partition constant.|
|301|`2r^2+r+1`|STRUCTURAL_R_FORMULA|Exact excess identity `K_r=2(E-q-(2r^2+r+1))`.|
|211|`[r(3r-1)+2]/2`|STRUCTURAL_R_FORMULA|For every `r>=12` under the general residual-core contract, AES excludes `K_r=0`, so `K_r>=2`.|
|214|`[r(3r-1)+8]/2` candidate|UNKNOWN_ORIGIN as all-r theorem|At r=12 this follows from exact/near three-anchor `K>=8`. General exact-three-anchor theorem remains OPEN.|
|305|`C(r+2,2)+[r(3r-1)+f(r)]/2`|STRUCTURAL SCHEMA|At r=12, `f(12)=8`, giving305. General `f(r)` is the anchor-excess problem.|
|284|unknown symbolic lower-order floor|UNKNOWN_ORIGIN|r=12 front/core seed; needs lower-order general Ramsey/cap theorem.|
|27,30,31|roots/window of `d(r+1-d)<=Q` plus layer arithmetic|PARTLY_STRUCTURAL|The quadratic repivot base is symbolic, but the exact critical q-window forced by the front/backend layers is not yet generalized.|
|36|`4(r-3)` only at d=4 is not fundamental; general base is `d(r+1-d)`|R12_ACCIDENT as standalone constant|The real structural object is the quadratic `d(r+1-d)` and symmetry `d<->r+1-d`.|
|9 (d2 owner cap)|`r-3+o(1)`|STRUCTURAL_R_FORMULA|Exact formula: `N<=r-3+(k^2-3k+6)/(2(r-k))`.|
|8 (d3 Type-H/P cap)|`r-4+o(1)`|STRUCTURAL_R_FORMULA|Exact Type-H/P formulas in `GENERAL_R_OWNER_CAPACITY.md`; the r=12 Type-H k=3 exception is a small-r equality artifact.|
|3 zero-signature cap|`alpha(H)`|STRUCTURAL_R_FORMULA|General incidence-signature theorem gives at most `alpha(H)` zero signatures; here the residual target is `alpha(H)<=3`.|
|allowance overlap threshold `d-1`|`d-1`|STRUCTURAL_R_FORMULA|From `h(d-h)>=d-1` for proper overlap.|
|first high slack `a=d`|`d`|STRUCTURAL_R_FORMULA|Exact loss-layer threshold, not a fixed-r constant.|
|near-anchor excess threshold3|currently constant `h<=3`|UNKNOWN as optimal all-r threshold|r=12 theorem reduces this to exact three-anchor `K>=8`; symbolic reduction works for r>=12, but exact-anchor closure is open.|

## Main conclusion

Most conspicuous r=12 backend constants are not accidents. The unresolved constants now concentrate in two upstream objects:

1. lower-order/front-end Ramsey-cap floors that force the `4r+1`, degree-`r+1` residual-core setup;
2. the general exact-three-anchor excess function `f(r)`.

The owner/support constants 8 and9 are fully explained as evaluations of symbolic hereditary-cap formulas and therefore should no longer be treated as fixed-case phenomena.
