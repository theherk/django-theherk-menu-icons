import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-theherk-menu-icons',
    version='1.1',
    packages=['menu_icons'],
    include_package_data=True,
    license='see file LICENSE',
    description='Django CMS navigation modifier to attach icons to menus.',
    long_description=read('README.md'),
    url='https://github.com/theherk/django-theherk-menu-icons',
    author='Adam Sherwood',
    author_email='theherk@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
