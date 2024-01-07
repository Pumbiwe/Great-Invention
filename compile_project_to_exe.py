import os
import shutil


shutil.rmtree('dist', ignore_errors=True)

os.system(
    "pyinstaller -i assets/chemistry.png --noconfirm --noconsole main.py"
)
print('Compiled.')
for folder in {'assets', 'fonts'}:
    try:
        shutil.copytree(
            os.path.join(os.getcwd(), folder), os.path.join(os.getcwd(), 'dist', 'main', folder)
        )
    except FileExistsError as e:
        ...

for filename in {'database.db'}:
    shutil.copyfile(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), 'dist', filename))
shutil.rmtree('build', ignore_errors=True)