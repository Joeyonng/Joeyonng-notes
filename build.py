import os
import yaml
import glob
import nbformat
import argparse

def get_files(path):
    entries = {}
    with os.scandir(path) as it:
        for entry in it:
            name = entry.name
            name_ext = name.split('.')

            # Skip if the entry is a hidden entry (.*) or a jupyter-book entry (_*)
            if name.startswith('.') or name.startswith('_'):
                continue
                
            if entry.is_file():
                if len(name_ext) > 1 and name_ext[-1] == 'ipynb':
                    entries[name_ext[0]] = None
            else:
                entries[name_ext[0]] = get_files(os.path.join(path, name))
            
    return entries

def files_to_yaml(files, dirname):
    sub_yaml = []
    for key, value in files.items():
        if key.split('.')[0] == 'index':
            continue
        new_dirname = os.path.join(dirname, key)

        entry = {}
        if value is not None:
            sections = files_to_yaml(value, new_dirname)
            if len(sections) == 0:
                continue
            entry['sections'] = sections
        entry['file'] = new_dirname if value is None else os.path.join(new_dirname, 'index')
        entry['title'] = key

        sub_yaml.append(entry)
        
    return sub_yaml


def change_metadata(path):
    notebook = nbformat.read(path, nbformat.NO_CONVERT)

    changed = False
    for cell in notebook.cells:
        metadata = cell.get('metadata', {})
        tags = set(metadata.get('tags', []))
        jupyter = metadata.get('jupyter', {})

        hiddens = [jupyter.get('source_hidden', False), jupyter.get('output_hidden', False)]
        new_tags = tags - {'hide-cell', 'hide-input', 'hide-output', 'remove-cell', 'remove-input', 'remove-output'}
        if all(hiddens):
            new_tags.add('remove-cell')
        elif hiddens[0]:
            new_tags.add('remove-input')
        elif hiddens[1]:
            new_tags.add('remove-output')

        if new_tags != tags:
            cell['metadata']['tags'] = list(new_tags)
            changed = True

    if changed:
        nbformat.write(notebook, path)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Tools to build Jupyter Book.')
    parser.add_argument('action', type=str, choices=['toc', 'metadata', 'conf'])
    args = parser.parse_args()
    action = args.action
    
    # Update toc.yml based on the current file structure
    if action == 'toc':
        files = get_files('.')
        toc_yaml = {
            'format': 'jb-book',
            'root': 'root',
            'parts': [],
        }
        for key, value in files.items():
            if value is None:
                continue
            entry = {}
            entry['caption'] = key
            entry['chapters'] = files_to_yaml(value, key)
            toc_yaml['parts'].append(entry)
        with open('_toc.yml', 'w') as file:
            yaml.dump(toc_yaml, file)
       
    # Change every notebook's metadata
    if action == 'metadata':
        files = get_files('.')
        for key, value in files.items():
            if value is None:
                continue 
            notebook_paths = glob.glob(f'./{key}/**/*.ipynb', recursive=True)
            for notebook_path in notebook_paths:
                change_metadata(notebook_path)

    # Append to conf.py to allow block math
    if action == 'conf':
        if (os.path.exists('conf.py')):
            settings = ['suppress_warnings = ["myst.header"]', 'myst_dmath_double_inline = True']
            with open('conf.py', 'a') as file:
                file.write('\n# Belows are more customized settings')
                for setting in settings:
                    file.write(f'\n{setting}')
        else:
            print('conf.py not found, please run "jupyter-book config sphinx ." first.' )