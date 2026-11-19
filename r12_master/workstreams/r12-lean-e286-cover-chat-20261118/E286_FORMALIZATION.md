# Original E286 contract

Frozen source: frozen/E286.md, Theorem E286 and Sections1-12. Original repository
path and immutable source revision are recorded in SOURCE_PROVENANCE.json.

E286Hypotheses is exactly:47 vertices,286 edges, every degree>=12, alpha<=4,
omega<=11. The abstract frozen theorem requires NO hereditary D cap. E286Statement
is only a definition of the nonexistence target; no proof of it is declared.

Verified reduction (CI44194246540): degree sum572, excess sum8, exceptional support<=8,
individual degrees<=20, at least39 regular vertices, exceptional degree sum12q+8,
and exact regular/excess-support edge ledger. No enumeration or oracle is used.
These initial ledgers are not E286 exclusion.

At86e9970 (CI44498020540), the original five hypotheses imply actual regular
independent seeds, the exact private-clique/multiple-support partition, surplus5,
and a complete ten-orbit classification of actual support multiplicities.
The complete finite domain is proved structurally by e286_weighted_profiles_complete;
the finite orbit check uses kernel reduction, not an external enumeration oracle.

Frozen Section3's actual forced blocker edges and six-unit K11/K11 local excess
charge are proved. Section5's complementary K11 pair obstruction is proved using
disjoint actual charged sets and the total excess8. Missing-set positivity follows
from omega<=11; forced cross edges follow from alpha<=4. None is assumed in the
private-clique wrapper. Full types are in DECLARATION_STATEMENTS.md and the CI log.

The oriented seed realization and elimination of the first count representative
are VERIFIED at90130d8 (CI44498770093). The main certified reduction
e286_actual_support_nine_remaining assumes only E286Hypotheses and produces
actual regular seeds and a count vector in the tail of the ten-representative list.
No extra terminal premise is introduced. The remaining nine orbit exclusions, shared-center overlap
accounting and triple-K11 local cost are still unproved. LEVEL5A is not attained.
