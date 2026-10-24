# General-r Constant Dictionary

Status: WORKING DRAFT. Every entry must eventually be tagged `STRUCTURAL_R_FORMULA`, `R12_ACCIDENT`, or `UNKNOWN_ORIGIN` with a proof/source.

| r=12 constant | candidate symbolic form | current tag | proof/source status |
|---:|---|---|---|
|145|`r^2+1`|UNKNOWN_ORIGIN|Needs derivation from original EG617 reduction, not numeric fit.|
|61|`5r+1`|UNKNOWN_ORIGIN|Needs front-end recurrence provenance.|
|49|`4r+1`|UNKNOWN_ORIGIN|Needs derivation of Ramsey residual.|
|35|`3r-1`|PLAUSIBLE_SYMBOLIC|Matches pivot of degree `r+1` inside a `4r+1` residual; general source not yet certified.|
|13|`r+1`|PLAUSIBLE_SYMBOLIC|Likely pivot/shell size; general source not yet certified.|
|12|`r`|STRUCTURAL_R_FORMULA candidate|Core minimum-degree floor in r=12; general lower-order seed still open.|
|91|`C(r+2,2)`|PLAUSIBLE_SYMBOLIC|At r=12, `C(14,2)=91`; exact backend derivation pending.|
|211|`?`|UNKNOWN_ORIGIN|Likely minimum core-edge layer `((3r-1)r+K_min)/2`; requires general seed.|
|214|`?`|R12_DATA_POINT|Equals `(35*12+8)/2`; comes from r=12 near-anchor theorem `K>=8`. General `f(r)` unknown.|
|305|`?`|R12_DATA_POINT|From backend identity plus `e(H)>=214`: `91+214=305`; symbolic form depends on backend base term and general anchor excess.|
|284|`?`|UNKNOWN_ORIGIN|Requires provenance from q31 / 47-core shell identities.|
|27,30,31|`q_*(r)-O(1)` candidate|UNKNOWN_ORIGIN|Need symbolic critical-q derivation.|
|6,8,9 owner/support caps|`C_r(d,pattern,W)`|R12_DATA_POINT|Derived from r=12 hereditary cap; symbolic cap function still to derive.|
|3,6 allowance thresholds|functions of `d`, shallow-loss width|PARTLY_STRUCTURAL|`d-1`, `a=d`, `a-e_M(S)<=3` have structural origin; fixed numbers require symbolic rewrite.|

## Required proof archaeology

For every row above, locate the earliest theorem/reduction that introduces the number, then rewrite that argument with symbolic r before changing the tag.
