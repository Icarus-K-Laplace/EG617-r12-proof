# Q33 support promotion — exact remaining OPEN frontier

Status: **OPEN / NOT_CERTIFIED**.

## Excluded cells
- m=8: v=31,32;
- m=9: v=32,33;
- m=10: v=34.

## First remaining scalar-feasible cells
- m=8, v=33, h=5;
- m=9, v=34, h in {4,5,6};
- m=10, v=35, h in {2,...,8}.

Every larger v through47 also has at least one scalar-feasible h. These are not graph witnesses.

## Next attack: tightest cell (m,v,h)=(8,33,5)

Here w=14, f0=5, f1=10:
- selected component W-edge contribution >=3*5+5*10=65;
- three nonexact colors need >=3p12(14)=6 additional W-edges;
- t4(14)=73, leaving at most two W-edge units.

On U:
- 56 selected witness blocks occupy336 edges;
- 51 component witnesses own306 edges;
- three nonexact colors need at least3p12(33)=90 U-edges;
- e(L_U)<=398, leaving at most two U-edge units beyond those 306 component-owned and 90 nonexact edges.

The next proof should exploit this simultaneous near-saturation with the full labelled component/gadget incidence matrix and the core degree ledger.

## Other first survivors
- (m,v)=(9,34): use the ninth exact color's ten component sets, pairwise gadget-intersection bound, and four units of core excess.
- (m,v)=(10,35): all ten exact colors are selected; use the one nonexact color and the sharper rho_10=4 bound.

## Missing structural theorem

A source-correct theorem must couple all component K4s, selected gadget witnesses, U/W incidence, core degree excess, and nonexact edge ownership. The scalar inequalities do not imply this theorem.

Do not set |U|=31 without proof, promote a feasible h to a graph witness, or change global root status.
