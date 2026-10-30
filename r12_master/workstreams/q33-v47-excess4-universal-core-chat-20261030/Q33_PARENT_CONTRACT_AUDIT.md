# Q33 parent-contract audit

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL application audit**

## 1. Read-only branch freeze

The following branch heads were inspected before creating this isolated workstream:

| Source | Observed HEAD | Use |
|---|---|---|
| Global E408 root | b0459807acd4b7e386148056ddf77d7998918893 | Parent and charge identity |
| C / Q33 support-promotion | ca088347124f4ea7706a63129d7ed63d4e4090d7 | Read-only current Q33 state |
| Astra Q32 universal attack | c5062fcdf5ac83ea9d0d51b9bc34a8f9f3619c0f | Read-only contrast only |
| This workstream base | b0459807acd4b7e386148056ddf77d7998918893 | Isolated branch base |

The requested new branch did not exist at inspection time. It was created from the observed global root HEAD. No sibling path or global canonical file was written.

## 2. Genuine E408/Q33 parent

The parent is a genuine 61-vertex h13 T61 target residual F with

- e(F)=408;
- delta(F)=13;
- alpha(F)<=5;
- omega(F)<=11.

Choose a degree-13 pivot p. Let A=N_F(p), so |A|=13, and define

H=F[V(F) minus (A union {p})].

Then |V(H)|=61-1-13=47.

The E408 pivot identity is

408 = 91 + q_p + e(H).

On the Q33 branch q_p=33, so

e(H)=408-91-33=284.

## 3. Five hypotheses, separately audited

| Core hypothesis | Parent derivation | Status |
|---|---|---|
| |V(H)|=47 | Remove p and its 13-neighborhood from the 61-point residual | **PROVED** |
| e(H)=284 | Exact E408 pivot identity with q_p=33 | **PROVED** |
| alpha(H)<=4 | If H had an independent 5-set, adjoining p (anticomplete to H) gives an independent 6-set in F, contradicting alpha(F)<=5 | **PROVED** |
| omega(H)<=11 | H is induced in F and omega(F)<=11 | **PROVED** |
| delta(H)>=12 | The retained Q33 core minimum-degree interface states this at the 284-edge cell | **PROVED_CONDITIONAL** |

## 4. Minimum-degree dependency warning

The root file front_end/E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md explicitly says the 284-edge core has delta(H)>=12 by the retained V11 interface.

However, the root file front_end/T61_H13_V11_SOURCE_AUDIT.md currently records:

- V11 package present / source-reported;
- independent replay pending;
- retained lower-order seed dependencies remain conditional.

Therefore this workstream does **not** claim that delta(H)>=12 has been independently re-proved from the four other parent facts. The universal theorem below is unconditional once all five graph hypotheses are supplied, but its use against every genuine Q33 parent remains conditional on acceptance/replay of that minimum-degree interface.

The global assumption ledger also records an R(4,47) edge/minimum-degree result. This workstream does not use that ledger entry as a substitute for the V11 source gate without its proof body.

## 5. Q32 firewall

Astra's theorem concerns e(H)=285 and total excess six. The present parent identity is e(H)=284 and total excess four. The Q32 theorem is not imported, and its 285-edge conclusion is not used to establish any Q33 statement.

## 6. Current parent consequence

Conditional on the retained V11 minimum-degree interface, every genuine E408/Q33 parent would produce a graph satisfying the five hypotheses. The universal 284-edge theorem proves that such a core cannot exist.

This is a valid conditional parent contradiction, not a claim that the entire EG617(r=12) theorem is already certified.
