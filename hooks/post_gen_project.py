import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


create_template_project = '{{cookiecutter.create_template_project}}' == 'True'
print(type(create_template_project))
create_template_project = bool(create_template_project)

for i in range(10):
    print(create_template_project)

if not create_template_project:
    # remove top-level file inside the generated folder
    print('hej')
    path = os.path.join(os.getcwd(), '{{cookiecutter.python_package_name}}', 'test.py')
    print(path)
    remove(path)

print('end of post hook')
