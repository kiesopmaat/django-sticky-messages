import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-sticky-messages',
    version = '0.3',
    packages = ['stickymessages'],
    install_requires = ['django-tinymce4-lite'],
    include_package_data = True,
    license = 'MIT',
    description = 'A simple Django app to display "sticky" messages that expire after a given time period.',
    long_description = README,
    url = 'https://github.com/kiesopmaat/django-sticky-messages',
    author = 'Roland van Laar',
    author_email = 'rvanlaar@kiesopmaat.nl',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
