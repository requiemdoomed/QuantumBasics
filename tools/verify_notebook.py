# Verifying Qiskit fundamentals by Swayam Shakya in an empty temporary folder.
from pathlib import Path
import tempfile
import os
import io
import tokenize
import nbformat
import matplotlib

# Selecting a noninteractive plotting backend for automated verification.
matplotlib.use('Agg')
root=Path(__file__).resolve().parents[1]
notebook=nbformat.read(root/'qiskit_fundamentals_colab.ipynb',as_version=4)
nbformat.validate(notebook)
code_cells=[c for c in notebook.cells if c.cell_type=='code']

# Checking every comment against the requested -ing-word style.
for cell in code_cells:
    for token in tokenize.generate_tokens(io.StringIO(cell.source).readline):
        if token.type==tokenize.COMMENT:
            assert token.string.lstrip('# ').split()[0].lower().endswith('ing'),token.string

# Running all lessons without inheriting files or variables from a previous run.
previous=Path.cwd()
with tempfile.TemporaryDirectory() as directory:
    try:
        os.chdir(directory)
        namespace={'__name__':'__main__'}
        for index,cell in enumerate(code_cells,1):
            exec(compile(cell.source,f'notebook-cell-{index}','exec'),namespace)
        assert len(list(Path('assets').glob('*.png')))==21
        assert len(list(Path('assets').glob('*.svg')))==21
        assert Path('qiskit_generated_results.zip').is_file()
        print(f'PASS: {len(code_cells)} code cells; 21 PNG and 21 SVG exports.')
    finally:
        os.chdir(previous)
