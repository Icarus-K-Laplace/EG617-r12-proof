import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
execFileSync(process.execPath, [path.join(root, 'scripts/check-source.mjs')]);
const scan = JSON.parse(fs.readFileSync(path.join(root, 'logs/source-scan.json'), 'utf8'));
if (scan.status !== 'PASS') throw Error('Source scan failed');
const header = 'module\n\npublic import EG617\n\n';
fs.writeFileSync(path.join(root, 'EG617/Audit/Axioms.lean'), header +
  scan.declarations.map(d => '#print axioms EG617.' + d.name).join('\n') + '\n');
fs.writeFileSync(path.join(root, 'EG617/Audit/Statements.lean'), header +
  scan.declarations.map(d => (['theorem', 'lemma'].includes(d.kind) ? '#check ' : '#print ') +
    'EG617.' + d.name).join('\n') + '\n');
console.log(`Generated entries for ${scan.declarations.length} declarations; kernel audit still required.`);
