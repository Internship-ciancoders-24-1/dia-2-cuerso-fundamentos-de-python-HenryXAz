from setuptools import setup


setup(
    name='pv',
    version='0.1',
    packages=['clients'],
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)