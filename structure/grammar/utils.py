import subprocess
import os


def regenerate():
    """Regenerates the grammar files."""

    dir_path = os.path.dirname(os.path.realpath(__file__))

    result = subprocess.call([
        'java',
        '-jar', os.path.join(dir_path, 'antlr-4.13.1-complete.jar'),
        '-Dlanguage=Python3', os.path.join(dir_path, 'Grammar.g4'),
        '-o', os.path.join(dir_path, 'generated')
    ])

    if result == 0:
        print('Grammar regenerated successfully.')

    else:
        raise RuntimeError(f'Grammar regeneration process returned with a non-zero result {result}.')
