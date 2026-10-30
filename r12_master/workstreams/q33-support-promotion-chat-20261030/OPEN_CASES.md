# Q33 support promotion — exact remaining OPEN frontier

Status: **OPEN / NOT_CERTIFIED**.

## Excluded by sharp U reserve + W reserve + component-pair charge
- m=8: v=31,32,33;
- m=9: v=32,33,34;
- m=10: v=34,35.

## First remaining scalar/profile-feasible cells
- m=8, v=34, h=7;
- m=9, v=35, h in {5,6,7,8,9};
- m=10, v=36, h in {3,4,5,6,7,8,9,10}.

All larger support sizes through47 also remain feasible in this necessary screen.

## Next structural attack

### m=8,v=34,h=7
Here w=13, B_W=60, B_U=18. There are31 unselected component K4s. The charge has only three units of slack:
\[
3(31)=93,\qquad B_W+2B_U=96.
\]
Seek equality/stability consequences for the 31 component U/W pair profiles, together with the full core degree ledger.

### m=9,v=35,h=5,...,9
Here w=12, B_W=54 and B_U=1+4h. Use the ninth exact color's ten component sets, pairwise gadget-intersection bound, and four units of core excess.

### m=10,v=36,h=3,...,10
Here w=11, B_W=55 and B_U=16+4h. Use all ten exact-color component systems and the single nonexact color.

## Missing structural theorem

A source-correct theorem must couple labelled component K4s, gadget witnesses, U/W incidence, core degree excess, and edge ownership. Current scalar/profile inequalities do not eliminate these cells.

Do not set |U|=31 without proof, promote a feasible h to a graph witness, or change global root status.
