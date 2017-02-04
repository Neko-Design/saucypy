from setuptools import setup

setup(
    name='saucypy',
    packages=['saucypy'],
    install_requires=[
        'requests'
    ],
    version='__VER_TAG__',
    description='SauceLabs API Python Wrapper',
    author='Ewen McCahon',
    author_email='ewen.m.mccahon@student.uts.edu.au',
    url='https://github.com/Neko-Design/saucypy',
    download_url='https://github.com/Neko-Design/saucypy/tarball/__VER_TAG__',
    keywords=['saucelabs', 'api', 'wrapper', 'interface', 'sauce'],
    classifiers=[]
)