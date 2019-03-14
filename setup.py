import os
import sys

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'src'))
from wagtail_marketing import get_version  # noqa isort:skip

docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]

tests_require = [
    # Required for test and coverage
    'pytest',
    'pytest-cov',
    'pytest-django',
    'coverage',
    'factory-boy',
    'psycopg2>=2.5.4',
    # Linting
    'flake8',
    'isort',
]

setup(
    name='wagtail-marketing-addons',
    version=get_version().replace(' ', '-'),
    description='A Wagtail add-on for supporting marketeers in daily activities',
    author='Lukkien BV',
    author_email='support@lukkien.com',
    url='https://lukkien.com/',
    extras_require={
        'test': tests_require,
        'doc': docs_require,
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',  
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Wagtail',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)