import os
from pathlib import Path
from natsort import natsorted

_ = [ os.system(f'python3 {file.resolve()}') for file in natsorted(Path('src').glob('*.py'), key=str) ]