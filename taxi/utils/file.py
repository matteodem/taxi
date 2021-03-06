import codecs
import os
import shlex
import subprocess

def create_file(filepath):
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    if not os.path.exists(filepath):
        myfile = codecs.open(filepath, 'w', 'utf-8')
        myfile.close()

def spawn_editor(filepath, editor=None):
    if editor is None:
        editor = 'sensible-editor'

    editor = shlex.split(editor)
    editor.append(filepath)

    try:
        subprocess.call(editor)
    except OSError:
        if 'EDITOR' not in os.environ:
            raise Exception("Can't find any suitable editor. Check your EDITOR "
                            " env var.")

        editor = shlex.split(os.environ['EDITOR'])
        editor.append(filepath)
        subprocess.call(editor)
