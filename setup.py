from setuptools import setup

install_requires = [
    'pytest',
    'tox',
    'sphinx',
    'tornado',
    'plan'
]

setup(
    name='webcron',
    version='0.1',
    packages=['webcron'],
    install_requires=install_requires,
    url='https://github.com/luzhongqiu/webcron.git',
    license='MIT',
    author='zq.deer',
    author_email='zq.lu@foxmail.com',
    description='web cron for python'
)
