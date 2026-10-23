# Global Zero-Charge Incidence-Signature Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- common-S row closure;
- a core independence bound.

Purpose: explain, in one theorem, why common hubs, common pairs and small sunflower cores repeatedly emerge in equality states. The controlling object is the incidence signature of zero-charge core vertices.

## 1. Setup

Let H be a residual core with

`alpha(H)<=r`.                                               (I1)

Let Y be any common-S support family, with support classes

`D in F`.

For each support-union vertex v define its incidence signature

> `sigma(v)={D in F : v in D}`.                             (I2)

Write

`w_v=kappa_v+e_F(v,S)`.

Assume the common-S row closure

> for every support D and every `v notin D`,
> `e_H(v,D)<=w_v`.                                          (I3)

## 2. Zero-charge target edges force identical signatures

Let u,v be support-union vertices with

`w_u=w_v=0`.                                                (I4)

Suppose there is a support D with

`v in D`, `u notin D`.

Then row closure gives

`e_H(u,D)<=w_u=0`.

In particular

`uv` is a target nonedge.                                   (I5)

Therefore if uv is a target edge, every support containing v also contains u:

`sigma(v) subseteq sigma(u)`.                               (I6)

By symmetry, applying the same argument with u and v exchanged gives

`sigma(u) subseteq sigma(v)`.                               (I7)

Hence:

> **Zero-charge signature lemma.**
> If `w_u=w_v=0` and uv is a target edge, then
>
> `sigma(u)=sigma(v)`.                                      (I8)

Equivalently:

> zero-charge vertices with different incidence signatures are target-nonadjacent.   (I9)

## 3. Signature capacity from the core independence number

Suppose there are r+1 distinct incidence signatures among zero-charge support-union vertices.

Choose one zero-charge vertex from each signature class.

Every pair of chosen vertices has different signatures, so by (I9) every pair is a target nonedge.

Thus the chosen vertices form an independent `(r+1)`-set in H, contradicting `alpha(H)<=r`.

Therefore:

> **Incidence-signature capacity theorem**
>
> the number of distinct incidence signatures represented by zero-charge support-union vertices is at most r.   (I10)

For the r=12 residual core, `alpha(H)<=3`, hence

> at most three distinct zero-charge incidence signatures occur.   (I11)

## 4. Signature classes are canonical common cores

Let C be one zero-charge signature class:

`C={v:w_v=0, sigma(v)=Sigma}`.                              (I12)

Every support in Sigma contains every vertex of C, and every support outside Sigma contains none of C.

Thus C is a genuine common core of exactly the support classes indexed by Sigma.

For d-uniform supports,

`|C|<=d`.                                                    (I13)

If `|C|=d`, all supports in Sigma are the same support class. Hence in a family of distinct support classes, every nontrivial common-core signature has size at most d-1.

This gives the canonical interpretations:

- signature class of size1: common hub;
- signature class of size2 in d=3: common pair;
- larger signature classes: higher common-core analogues.

These objects arise from row closure automatically, not from ad hoc case classification.

## 5. Private zero-charge vertices consume signature classes

A private support vertex v with

`lambda_v=1`, `w_v=0`                                       (I14)

has signature

`sigma(v)={D}`,                                              (I15)

where D is its unique support class.

Distinct support classes give distinct singleton signatures.

Therefore, by (I10):

> at most r distinct support classes can possess a private zero-charge vertex.   (I16)

For `alpha(H)<=3`, at most three support classes in the entire common-S family can contain a private zero-charge point.

This is a major rigidity statement for one-loss equality systems.

## 6. One-loss d=3 corollary

Consider the first-high-slack d3/A3 one-loss layer from `GLOBAL_FIRST_HIGH_SLACK_DECOMPOSITION.md`.

Every interacting support D has exact defect

`Delta(D)=2`.                                               (I17)

For any proper overlap, all shared vertices have zero charge.

Also

`mu(D)=3-e_H(D)`,

so

`e_H(D)=1+w(D)`.                                            (I18)

If D has overlap size1 with the rest of its component, it has two private support points.

Unless D belongs to one of the at most r exceptional support classes from (I16), both private points must have positive charge. Since their total charge is at most2, this forces

> both private charges equal1,
> `w(D)=2`,
> `e_H(D)=3`.                                               (I19)

Thus every nonexceptional one-overlap triple is a target K3 with two unit-charge private petals and a zero-charge shared point.

If D has two shared vertices and one private point, then outside the at-most-r private-zero exceptions, the private point has positive charge. Hence

`w(D)>=1`,
`e_H(D)>=2`.                                                (I20)

Therefore:

> in a large d3 one-loss system, all but at most r support classes are forced to be dense (K3 in the one-shared-point case, at least two-edge in the two-shared-point case).   (I21)

For the r=12 core, the exceptional count is at most3.

## 7. Connection to hereditary packing

The signature theorem converts support-incidence complexity into internal support density:

- many distinct zero-charge private patterns are impossible by independence;
- hence most supports must carry positive private charge;
- exact defect then forces those supports to have many internal target edges.

Those internal edges appear directly in `GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md`.

Thus a large one-loss component is forced into one of two globally expensive resources:

1. few zero-charge signature classes => common-hub/common-pair concentration;
2. positive private charge => dense supports consuming hereditary edge capacity.

This is the desired bridge from incidence signatures to global packing.

## 8. Front-end analogue

The proof only uses a row-closure inequality of the form

`e(v,D)<=charge(v)`.

If the front-end 47-core correction variables can be translated into such a labelled charge, the same incidence-signature theorem applies verbatim. This is a concrete candidate for a shared front/backend multi-pivot compatibility principle.

## 9. Generalization

The theorem is already parameterized by the core independence number r. It does not depend on support size, core size, edge layer, or r=12.