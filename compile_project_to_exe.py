import os
import shutil

os.system(
    "pyinstaller -i assets/chemistry.png --onefile --noconfirm --noconsole main.py"
)

for folder in {'assets', 'fonts'}:
    try:
        shutil.copytree(
            os.path.join(os.getcwd(), folder), os.path.join(os.getcwd(), 'dist', folder)
        )
    except FileExistsError as e:
        ...