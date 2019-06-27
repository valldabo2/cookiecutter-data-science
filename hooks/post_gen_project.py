import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


create_template_project = '{{cookiecutter.create_template_project}}'

if not create_template_project:
    # remove top-level file inside the generated folder
    remove(os.path.join(os.getcwd(), '{{cookiecutter.project_name}}', 'test.py'))

