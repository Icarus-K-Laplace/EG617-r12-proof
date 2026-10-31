# Public-release checklist

This repository is currently private. This checklist is a gate before changing visibility or announcing a public release. A preliminary default-branch-only search found no matches for four common credential patterns; see [PRELIMINARY_SECURITY_SCAN.md](PRELIMINARY_SECURITY_SCAN.md). A full-history, all-refs scan is still required.

## Security and privacy

- [ ] Scan every reachable branch and the full Git history for API tokens, passwords, private keys, credentials, personal data and private correspondence.
- [ ] If any credential was ever committed, revoke/rotate it; removing it from the latest tree is insufficient.
- [ ] Check issue/PR comments, commit messages, release assets and Git LFS objects for sensitive content.
- [ ] Confirm all collaborators consent to publication of their workstream contents and attribution.
- [ ] Confirm raw source bundles and any third-party material may legally be redistributed.
- [ ] Check scripts for hard-coded local paths, usernames, environment details or private endpoints.

## Mathematical and publication integrity

- [ ] Keep the exact proof and certification commit pins in the public README.
- [ ] Preserve the distinction between the fixed (r=12) theorem and the general conjecture.
- [ ] Preserve the distinction between contextual (R(4,49)) impossibility and the still-open abstract high-energy problem.
- [ ] State that the audit is AI-assisted, informal and not external human peer review.
- [ ] State that Lean 4 formalization is not yet complete.
- [ ] Verify all external theorem citations and bibliographic metadata.
- [ ] Finalize human author list, affiliations, contributions and corresponding-author details.
- [ ] Obtain approval from any human contributor whose material is included.

## Completed preparation

- [x] Repository visibility confirmed Private.
- [x] Main README and canonical status synchronized with the pinned fixed-r12 proof.
- [x] All 44 branch names and HEADs captured in the workstream index.
- [x] Documentation/manuscript-preparation PR #2 merged into main.
- [x] Certification PR #1 opened for human review.
- [x] Preliminary default-branch credential-pattern search recorded.

## GitHub release steps

- [ ] Review and merge the documentation-only publication PR into `main`.
- [ ] Confirm the default-branch README and status documents match the pinned proof.
- [ ] Complete full-history security and licensing checks.
- [ ] Only then change repository visibility to Public.
- [ ] Create a GitHub Release tied to the exact proof/certification commits.
- [ ] Add a Zenodo DOI or equivalent archival snapshot.
- [ ] Submit the preprint only after human author approval.

No repository visibility change, branch deletion, history rewrite, PR merge or public release is performed by this checklist.
