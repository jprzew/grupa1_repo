from pathlib import Path
import os


def get_repo_path():
    current_path = Path(os.path.abspath('.'))
    path = current_path / Path(__file__)

    # Find .git folder in superdirectory
    while not os.path.exists(path / '.git'):
        path = path.parent
        if path == Path('/'):
            raise FileNotFoundError('Probably not inside git repository.')

    return path
