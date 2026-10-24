# Symbolic Terminal Types

Status: **FINITE TERMINAL TAXONOMY PROVED; uniform elimination open**.

## 1. Internal recurrence terminals

After decompilation, every stopped row/node belongs to one of the following constant-size schemas.

### I0 — base/cutoff terminal

The state is empty by a declared lower-a order cutoff or the contextual extraction exclusion.

### I1 — core-empty terminal

For a proposed minimum degree h, the pivot core `(a-1,n-h-1)` is already empty.

### I2 — pair-density terminal

The forced union of two core rows has size beta but

`B_r(a-1,m)+beta>D_r(m+2)`.

Hence that h-row cannot exist.

### I3 — triangle-alternative terminal

The triangle branch fails its inherited density cap. This removes only the triangle alternative; if the triangle-free alternative also fails, the h-row is terminal.

### I4 — no-surviving-degree terminal

All possible minimum-degree rows h have been eliminated.

### I5 — cap-overflow terminal

The certified lower floor exceeds `D_r(n)`, so the contextual class is empty.

### I6 — outer-budget terminal

The contextual class itself is not empty, but its recurrence floor is compared with the anchor/block upper budget `U_r(d,j)`. If the floor is larger, that outer state is impossible; otherwise it survives for structural analysis.

Thus the recurrence has a finite terminal family independent of the 1752-node implementation size.

## 2. Desired outer terminal cones

The outer coordinates are

`a=r-1-j`,
`n=r^2-d-jr`,
`U_r(d,j)=r(r^2+1)/2-C(d+1,2)-j C(r,2)`.

The target uniform dominance theorem would leave only two symbolic cones at `d=r-1`:

### R4 — extraction cone

`j=r-5`, hence

`a=4`, `n=4r+1`.

Under the reductio assumption this is contextually empty; without the reductio it is the desired residual extraction.

### R5 — design-terminal cone

`j=r-6`, hence

`a=5`, `n=5r+1`.

This is the symbolic analogue of the r=12 T61 survivor.

At r=12 the stored arithmetic certificate proves that every other outer state is eliminated and R5 is the unique nonexcluded survivor.

## 3. Equality/plateau family

Equality in the local inequalities does not create additional recurrence states. It can, however, refine R5 into finitely many structural subtypes:

- Turan equality in the core or shell complement;
- minimum matching equality;
- pair-cover equality;
- Mantel equality in the triangle-free branch;
- triangle-cover equality;
- equality in the hereditary cap;
- equality in the outer anchor budget, meaning all omitted nonnegative embedding charges vanish.

These are the correct objects for a future design/stability classification. They should not be expanded into fixed-r node casework before the seed-envelope theorem is settled.

## 4. Uniform terminal theorem — exact missing statement

A sufficient general-r theorem is:

> For all r in a specified range, the symbolic recurrence closure satisfies
> `B_r(r-1-j,r^2-d-jr)>U_r(d,j)`
> for every admissible `(d,j)` other than `(r-1,r-6)` and the extraction coordinate `(r-1,r-5)`.

If this holds, the front end automatically terminates in

`(4r+1) residual OR (5r+1) design terminal`.

The theorem is currently proved numerically only at r=12 using the certified seed package. Its abstract implication is proved for every r>3.
