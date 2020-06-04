"""
Flask-Simple
-------------

Just to test how flask's extensions work!
"""
from setuptools import setup


setup(
    name='Flask-Simple',
    version='1.0',
    url='https://nasser.cm',
    license='BSD',
    author='Abdou Nasser',
    author_email='abdounasser202@gmail.com',
    description="Just to test how flask's extensions work!",
    long_description="Just to test how flask's extensions work!",
    py_modules=['flask_simple'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
