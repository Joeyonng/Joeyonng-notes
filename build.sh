# Update _toc.yml based on the current file structure
python build.py toc

# Update each notebook's metdata to support hidden cells
python build.py metadata

# Allow block math without double new line
rm -r _build
jupyter-book config sphinx .
python build.py conf
sphinx-build . ./_build/html/ -b html
rm conf.py

# Push to the Github page
ghp-import -n -p -f _build/html