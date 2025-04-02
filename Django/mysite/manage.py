'''
INF601 - Programming in Python
Assignment - Mini Project 4
I, Dawsyn Birtell, affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. 
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

""" Please submit a link to your GitHub project.   Do not submit your project files here!
This project will be using Django to deploy a small web app of your choice. The goal here is to come up with a small web application that meets the requirements below. If you get stuck here, please email me!
(5/5 points) Initial comments with your name, class and project at the top of your .py file.
(5/5 points) Proper import of packages used.
(70/70 points) Using Django you need to setup the following:
(10/10 points) Setup a proper folder structure, use the tutorial as an example. You need a minimum of one app.
(20/20 points) You need to have a minimum of 5 pages, using a proper template structure.
(10/10 points) You need to have at least one page that utilizes a form.
(10/10 points) You need to setup Django admin and style your models for proper entry. No tight restrictions here, just make use of the admin system.
(10/10) You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but the more practice here the better. You need to at least make use of a modal.
(10/10) You need to setup some sort of register and login system, do some simple research to find examples.
(5/5 points) There should be a minimum of 5 commits on your project, be sure to commit often!
(5/5 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
(10/10 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. You will need to explain the steps of initializing the database and then how to run the development server for your project.


Remember to run these commands and have them in your README:

python manage.py makemigrations (this will create any SQL entries that need to go into the database)
python manage.py migrate (this will apply the migrations)
"""


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
