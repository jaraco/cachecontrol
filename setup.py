import sys

import setuptools

long_description = open('README.rst').read()

VERSION = '0.10.2'

pytest_runner = ['pytest-runner'] if 'ptr' in sys.argv else []
tests_require = open('dev_requirements.txt').read().split('\n')
tests_require.remove('-e .')

setup_params = dict(
    name='CacheControl',
    version=VERSION,
    author='Eric Larson',
    author_email='eric@ionrock.org',
    license='MIT',
    url='https://github.com/ionrock/cachecontrol',
    keywords='requests http caching web',
    packages=setuptools.find_packages(),
    description='httplib2 caching for requests',
    long_description=long_description,
    install_requires=[
        'requests',
    ],
    setup_requires=[] + pytest_runner,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)
