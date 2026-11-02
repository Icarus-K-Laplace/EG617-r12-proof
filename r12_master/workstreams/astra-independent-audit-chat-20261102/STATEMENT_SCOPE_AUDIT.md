# Problem 617 statement-scope check

Date: 2026-11-02.

The public statement of Erdős Problem 617 is:

For every integer r>=3, every r-edge-coloring of K_(r^2+1) contains an (r+1)-vertex set whose induced clique omits at least one color.

Source: T. F. Bloom, *Erdős Problem #617*, https://www.erdosproblems.com/617 (checked 2026-11-02); the current Erdős Problems mirror gives the same statement and labels the universally quantified problem open: https://erdosproblems.ai/problems/617.

For r=12, the exact fixed-parameter instance is K_145 with 12 colors and a 13-vertex set. The integrated theorem in this repository targets precisely this fixed case. It does **not** prove the universally quantified statement for every r>=3. Therefore even if the K145 proof is correct, the accurate description is “a proposed proof of the r=12 case of Erdős Problem 617,” not “Erdős Problem 617 solved.”

The public problem page currently records the general problem as open and describes earlier fixed-r claims as partial/preprint claims; this is compatible with a new unreviewed r=12 claim, and does not itself refute or validate the present proof. The repository should request expert review and provide the exact fixed-r statement, complete manuscript, appendices, and reproducible artifacts before describing the result as accepted or independently verified.
