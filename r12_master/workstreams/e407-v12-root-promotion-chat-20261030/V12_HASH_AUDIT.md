# V12 hash and source-provenance audit

Date: 2026-10-30

## Archive identity
- V12 archive: `T61_H13_V12.zip`; 190,249 bytes.
- SHA-256: `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`.
- Historical SHA reported in `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`: exact match.
- `sha256sum -c SHA256SUMS.txt`: **29/29 files OK**.
- ZIP entry count: **29 files**.

## Per-file SHA-256

| Path inside ZIP | Bytes | SHA-256 |
|---|---:|---|
| `T61_H13_V12/E407_D3_RHO1_EXCLUSION.md` | 4,301 | `ae360279c44d309a43474164483dc39cdaccf6f49fb8cb9b62defc2781c6a2e1` |
| `T61_H13_V12/E407_Q32_CERTIFICATE.json` | 2,374,602 | `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30` |
| `T61_H13_V12/E407_Q32_FULL_CLOSURE.md` | 3,032 | `d77d37bc46598649729cd0f3c32628c24bb99544510229e57794bb3c0f4f32da` |
| `T61_H13_V12/E407_Q32_SCREEN.json` | 456,376 | `7699129490c87827d5a0e28b1a95b0e9a682aae0daace9b6cc8dc9d32ef6dfc5` |
| `T61_H13_V12/E408_Q32_EXTENSION.md` | 1,645 | `f877e2be77baeb4df9437a9a1f50bfc1b81c0e6c67a565e1b2e93bcc4cf52e65` |
| `T61_H13_V12/INDEPENDENT_Q32_REPLAY.json` | 2,141 | `e5dde0d4b6e65d9090a40a841fa9d6b7ce08b54b1bdbfc4dbb44883a6c1b10dd` |
| `T61_H13_V12/INPUTS/COMPLETION_LIFT_V11.md` | 4,107 | `91e6c850b04c0f0e5fabfa4569bac174e01a4b87cbfc4befae26671a02972bd1` |
| `T61_H13_V12/INPUTS/CORE_INTERFACE_V6.md` | 4,433 | `1cd48664e8d0d4e87737008331fb1af17f0ddba28a819dab85cdaed0afb01dbb` |
| `T61_H13_V12/INPUTS/EXCHANGE_V8.md` | 11,301 | `3eed9b226482611a57545daf662af81014596e3ffac06593ae967e8ee5032206` |
| `T61_H13_V12/INPUTS/PAIR_ROW_CAPACITY_V11.md` | 4,663 | `2caca093099b9c843739e5f893b7535beeb3c6c3b3e1d8cfcad15a968ff699e8` |
| `T61_H13_V12/INPUTS/Q32_Q33_SLACK_V10.md` | 2,691 | `61b53beedcc33de31a13b951fa07c95e0c903f43c6b97eb9c0dec59445fca786` |
| `T61_H13_V12/INPUTS/TASK_V12.txt` | 6,255 | `91e14862be5fb64df04b23327cacd71072c251faf4ee4931c9cd8bf22785a102` |
| `T61_H13_V12/INPUT_SOURCE_HASHES.json` | 1,920 | `a729d5de6901d75f3b0c5ed326c0861d8bd305a5ad22857af9ee6ced0c6d1f4e` |
| `T61_H13_V12/K9_PAIR_ROW_COMPLETION.md` | 4,215 | `8a28302fbd8b4d15267200c7ada7a7149a64bb297ff548d0063de05f9123c96d` |
| `T61_H13_V12/NEAR_K12_CAPACITY_EXTENSION.md` | 4,000 | `dfa9c11c99c2832f2884f2f1c8d7b77e5a1654c5d6044fc702dca70be763bbc4` |
| `T61_H13_V12/Q32_COMMON_K10_CAPACITY.md` | 5,141 | `f34df849b94461e858b695e2a8a2badee5399a1b20b535bcaa3935bdec9cbc66` |
| `T61_H13_V12/Q32_KERNEL_CASE_TABLE.csv` | 229,271 | `b658c8ff480f5434a9e36b776b42cc1fc8cc09503464e7e3c8858e744bdb89e5` |
| `T61_H13_V12/Q32_KERNEL_COVERAGE.md` | 10,080 | `2e928f6d4a3e208534a2e1b6375288d8826616dd9c260d6121039774aa3cb3d8` |
| `T61_H13_V12/Q32_ONE_DEFECT_LOCALIZATION.md` | 3,155 | `d9dfe1628eecccc953503a41204c1281f513b994716deace784fdff42e2b64d4` |
| `T61_H13_V12/Q32_SLACK_SENSITIVITY_AUDIT.md` | 3,023 | `a4f573d0f081f506c3cd02a2b382477651a19575231346f5546f69eef8ecf8fd` |
| `T61_H13_V12/Q33_TWO_DEFECT_CLASSIFICATION.md` | 2,026 | `67c975b499988262b93b41226763d0d25d664f1224448f152e0ea507f5bc9e4c` |
| `T61_H13_V12/README.md` | 1,795 | `7526de1c185d65a16f141c0f77476234636c8f00734ce9c07f9cf3382ea88ebd` |
| `T61_H13_V12/SHA256SUMS.txt` | 2,577 | `9b1ab658f627e2cfaafb38fb2d4e6e5803fd33566c28b5f00a01d905cf7493da` |
| `T61_H13_V12/T61_DEPENDENCY_DAG_V12.md` | 3,328 | `e2aed851c43019b0a7723d6598078660103599916b30efb3bd1fdf06c4635ddb` |
| `T61_H13_V12/T61_H13_MASTER_V12.md` | 6,415 | `8cbd631b2e1e8f7ad17e091c8587478180315c547c10055d257058802f3e4a8c` |
| `T61_H13_V12/build_package.py` | 3,176 | `f7b1d214c7a5084234f3076ba7e79fabd92909ba7ef3ed584c55e84070e804be` |
| `T61_H13_V12/enumerate_q32_kernels.py` | 5,540 | `4fe4f614ded9f86d3daa52822274b4561a594a2ecafbabd30e7830beab1398ad` |
| `T61_H13_V12/screen_q32.py` | 2,183 | `020a3cd0ac25868cb7449f960f19622a07cfc3e6c363e2e866348beed83293fa` |
| `T61_H13_V12/verify_q32_certificate.py` | 9,773 | `46ba7420f9fca130941fce1fb4746e36885fa83799f458bf420a6ef7794624d5` |

## Key artifacts

- Certificate: `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.
- Screen: `7699129490c87827d5a0e28b1a95b0e9a682aae0daace9b6cc8dc9d32ef6dfc5`.
- Kernel case table: `b658c8ff480f5434a9e36b776b42cc1fc8cc09503464e7e3c8858e744bdb89e5`.
- Source manifest: `a729d5de6901d75f3b0c5ed326c0861d8bd305a5ad22857af9ee6ced0c6d1f4e`.
- Original verifier: `46ba7420f9fca130941fce1fb4746e36885fa83799f458bf420a6ef7794624d5`.
- Original generator: `4fe4f614ded9f86d3daa52822274b4561a594a2ecafbabd30e7830beab1398ad`.
- Embedded replay receipt: `e5dde0d4b6e65d9090a40a841fa9d6b7ce08b54b1bdbfc4dbb44883a6c1b10dd`.

## V11 source-copy verification

- V11 archive SHA-256: `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`; this matches the V11 archive hash recorded in the global root DAG.
- The five V12 copies whose manifest status is `CONDITIONAL` were byte-compared with the corresponding files in the recovered V11 archive. All five hashes match both the V12 source manifest and the V11 source bytes.

| V12 copy | V11 source | SHA-256 | Result |
|---|---|---|---|
| `INPUTS/CORE_INTERFACE_V6.md` | `INPUTS/CORE_INTERFACE_V6.md` | `1cd48664e8d0d4e87737008331fb1af17f0ddba28a819dab85cdaed0afb01dbb` | **MATCH** |
| `INPUTS/EXCHANGE_V8.md` | `INPUTS/EXCHANGE_V8.md` | `3eed9b226482611a57545daf662af81014596e3ffac06593ae967e8ee5032206` | **MATCH** |
| `INPUTS/Q32_Q33_SLACK_V10.md` | `INPUTS/Q32_Q33_SLACK_V10.md` | `61b53beedcc33de31a13b951fa07c95e0c903f43c6b97eb9c0dec59445fca786` | **MATCH** |
| `INPUTS/PAIR_ROW_CAPACITY_V11.md` | `NINE_D2_SUPPORT_CAPACITY.md` | `2caca093099b9c843739e5f893b7535beeb3c6c3b3e1d8cfcad15a968ff699e8` | **MATCH** |
| `INPUTS/COMPLETION_LIFT_V11.md` | `Q32_Q33_COMPLETION_LIFT.md` | `91e6c850b04c0f0e5fabfa4569bac174e01a4b87cbfc4befae26671a02972bd1` | **MATCH** |

`INPUTS/TASK_V12.txt` is the task input attached to the package, not a V11 source file; its hash is covered by the 29-file ZIP manifest.

## Repository versus Library

- The global root branch and dedicated E407 closure branch contain the historical V12 source-report audit but no raw V12 ZIP, certificate, or original verifier at the reported path.
- GitHub release inventory returned zero releases; exact-path commit history for `T61_H13_V12.zip` returned zero commits.
- The actual source archive was recovered from ChatGPT Library. This resolves archive availability, not the analytic parent hypotheses.


## Re-execution order and duplicate archive audit

The pristine V12 extraction passes all 29 SHA256SUMS entries. Run sha256sum -c before executing verify_q32_certificate.py: the original verifier writes a regenerated INDEPENDENT_Q32_REPLAY.json into its working directory, so a post-execution checksum against the original manifest can report a false mismatch on that mutated working copy. The archive itself remains byte-identical across the three Library copies.

The V11 archive was also recovered and independently checked: all 22 internal SHA entries pass, and the five V12 source copies marked CONDITIONAL match the mapped V11 files byte-for-byte.
