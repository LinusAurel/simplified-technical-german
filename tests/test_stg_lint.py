import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LINTER=ROOT/'tools/stg_lint.py'

def run(text,*args):
    cp=subprocess.run([sys.executable,str(LINTER),'-','--format','json',*args],input=text,text=True,capture_output=True,check=True)
    return json.loads(cp.stdout)

class LintTests(unittest.TestCase):
    def test_semicolon(self):
        r=run('Öffnen Sie die Abdeckung; prüfen Sie den Stecker.','--text-type','procedure')
        self.assertEqual(r['result'],'FAIL')
        self.assertTrue(any(f['rule']=='STG-DE-8.1' for f in r['findings']))
    def test_prohibited_term(self):
        r=run('Prüfen Sie gegebenenfalls den Stecker.')
        self.assertTrue(any((f.get('term') or '').casefold()=='gegebenenfalls' for f in r['findings']))
    def test_project_preference(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'.stg-de.yaml'
            p.write_text('version: 1\npreferred_terms:\n  - preferred: Fehler\n    avoid: [Problemfall]\n',encoding='utf-8')
            r=run('Der Problemfall ist dokumentiert.','--project',str(p))
            self.assertTrue(any(f['rule']=='STG-DE-9.4' for f in r['findings']))
    def test_unknown_not_error(self):
        r=run('Das Quantenflussteil ist aktiv.','--lexicon-report')
        self.assertNotEqual(r['result'],'FAIL')
        self.assertTrue(any(term=='quantenflussteil' for term,_ in r['unknown_lexicon']))

if __name__=='__main__': unittest.main()
