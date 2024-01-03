import os
import shutil


os.system(
    "pyinstaller -i assets/chemistry.png --onefile --noconfirm --noconsole main.py"
)
print('Compiled.')
for folder in {'assets', 'fonts'}:
    try:
        shutil.copytree(
            os.path.join(os.getcwd(), folder), os.path.join(os.getcwd(), 'dist', folder)
        )
    except FileExistsError as e:
        ...

for filename in {'database.db'}:
    shutil.copyfile(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), 'dist', filename))