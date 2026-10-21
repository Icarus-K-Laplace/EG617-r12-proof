# Front-end Line A V1 certificate

Status: `COMPUTATION_CERTIFIED` for the finite arithmetic recurrence only. This is **not** a graph-existence certificate and does not assert generic `R(4,49)` emptiness.

Source package SHA256:

`8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`

Local package manifest check performed on 2026-10-21:

- files checked: 73
- hash mismatches: 0

Independent replay performed successfully:

- recurrence nodes: 1752
- outer stopping comparisons: 144
- S30 scalar entries: 192
- unique surviving outer stop: `(d,j,a,n)=(11,6,5,61)`, floor397, budget408
- remaining S30 scalar cases: k0=14, k1=13, k2=0

To regenerate the large certificate and CSV tables from the source scripts:

```bash
python verify_frontend.py --write
python verify_frontend.py
```

The two recurrence implementations are independent integer transcriptions of the analytic recurrence in `front_end/RECURRENCE_PROOF.md`.
