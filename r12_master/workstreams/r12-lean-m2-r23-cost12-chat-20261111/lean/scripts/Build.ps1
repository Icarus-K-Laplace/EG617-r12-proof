param([string]$Lake = 'lake', [string]$Node = 'node', [switch]$FullClean)
# A single worker avoids Windows memory-commit exhaustion on this host.
$env:LEAN_NUM_THREADS = '1'
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$taskTemp = Join-Path $projectRoot '.lake-tmp'
New-Item -ItemType Directory -Path $taskTemp -Force | Out-Null
$env:TEMP = $taskTemp
$env:TMP = $taskTemp
if (Test-Path -LiteralPath $Lake) { $env:PATH = (Split-Path -Parent $Lake) + ';' + $env:PATH }
Push-Location -LiteralPath $projectRoot
try {
  New-Item -ItemType Directory -Force -Path 'logs' | Out-Null
  'RUNNING; FINAL_THEOREM_NOT_PROVED' | Out-File -Encoding utf8 'logs/build-status.txt'
  & $Node 'scripts/check-source.mjs' | Out-File -Encoding utf8 'logs/source-scan-console.txt'
  if ($LASTEXITCODE -ne 0) { throw 'Source audit failed' }
  & $Lake --version 2>&1 | Tee-Object -FilePath 'logs/lake-version.txt'
  if ($LASTEXITCODE -ne 0) { throw 'Lake unavailable' }
  & $Lake env lean --version 2>&1 | Tee-Object -FilePath 'logs/lean-version.txt'
  if ($LASTEXITCODE -ne 0) { throw 'Lean unavailable' }
  if ($FullClean) {
    & $Lake clean 2>&1 | Tee-Object -FilePath 'logs/clean.txt'
    if ($LASTEXITCODE -ne 0) { throw 'lake clean failed' }
    'workspace clean; restore pinned dependency cache before build' | Out-File -Encoding utf8 'logs/clean-scope.txt'
    & $Lake exe cache get Mathlib.Combinatorics.SimpleGraph.Extremal.Turan Mathlib.Tactic.IntervalCases Mathlib.Tactic.NormNum Mathlib.Algebra.Order.BigOperators.Group.Finset 2>&1 | Tee-Object -FilePath 'logs/cache-restore.txt'
    if ($LASTEXITCODE -ne 0) { throw 'dependency cache restore failed' }
  } else {
    & $Lake clean eg617r12 2>&1 | Tee-Object -FilePath 'logs/clean.txt'
    if ($LASTEXITCODE -ne 0) { throw 'project clean failed' }
    'project package clean; pinned dependency artifacts retained' | Out-File -Encoding utf8 'logs/clean-scope.txt'
  }
  & $Lake build 2>&1 | Tee-Object -FilePath 'logs/build.txt'
  if ($LASTEXITCODE -ne 0) { throw 'lake build failed' }
  & $Lake build '+EG617.Audit.Axioms' 2>&1 | Tee-Object -FilePath 'logs/axioms.txt'
  if ($LASTEXITCODE -ne 0) { throw 'axiom print failed' }
  & $Node 'scripts/check-axioms.mjs' 2>&1 | Tee-Object -FilePath 'logs/axiom-check-console.txt'
  if ($LASTEXITCODE -ne 0) { throw 'axiom allowlist check failed' }
  & $Lake build '+EG617.Audit.Statements' 2>&1 | Tee-Object -FilePath 'logs/statements.txt'
  if ($LASTEXITCODE -ne 0) { throw 'statement inspection failed' }
  'PROJECT_BUILD_PASS; FINAL_THEOREM_NOT_PROVED' |
    Out-File -Encoding utf8 'logs/build-status.txt'
} catch {
  ('FAIL; FINAL_THEOREM_NOT_PROVED; ' + $_.Exception.Message) | Out-File -Encoding utf8 'logs/build-status.txt'
  throw
} finally { Pop-Location }
