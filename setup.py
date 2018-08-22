from setuptools import setup

setup(
    name='xout',
    version='0.1',
    py_modules=['xout'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        xout=xout:cli
    ''',
)
