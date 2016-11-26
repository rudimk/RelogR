from setuptools import setup

setup(name='logit',    
    version='0.1',
    description='A generic logger with RethinkDB as the primary logstore.',
    url='https://github.com/rudimk/logit',
    author='Rudraksh MK',
    author_email='rudraksh.mk@gmail.com',
    license='MIT',
    packages=['logit'],
    install_requires=[
        'rethinkdb',
        'arrow',
    ],
    zip_safe=False)