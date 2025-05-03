#!/usr/bin/env python3
import nbformat
from pathlib import Path
import sys

def collapse_notebook(path: Path):
    """Load a notebook, set code cells to collapsed+scrolled, and save if changed."""
    nb = nbformat.read(path, as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.cell_type == 'code':
            # only write metadata if it's not already set
            if not cell.metadata.get('collapsed', False) or not cell.metadata.get('scrolled', False):
                cell.metadata['collapsed'] = True
                cell.metadata['scrolled'] = True
                changed = True
    if changed:
        nbformat.write(nb, path)
        print(f"✅ Updated: {path}")

def main(root_dir: str):
    root = Path(root_dir)
    # Recursively find all .ipynb files
    for notebook_path in root.rglob("*.ipynb"):
        collapse_notebook(notebook_path)

if __name__ == "__main__":
    # Optional: pass target folder as first arg, defaults to current dir
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    main(target)
