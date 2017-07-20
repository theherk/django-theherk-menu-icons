import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-theherk-menu-icons',
    version='2.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-cms >= 3',
    ],
    license='see file LICENSE',
    description='Django CMS navigation modifier to attach icons to menus.',
    long_description=read('README.md'),
    url='https://github.com/theherk/django-theherk-menu-icons',
    download_url='https://github.com/theherk/django-theherk-menu-icons/archive/2.0.1.zip',
    author='Adam Sherwood',
    author_email='theherk@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
