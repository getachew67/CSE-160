import sys

import numpy

EXPECTED_MAJOR = 3
EXPECTED_MINOR = 7


def foo():
    print('Foo runs');
    bar();


def bar():
    print('Bar runs');


def main():
    print('Main runs');
    foo();

    version = sys.version_info
    if version.major != EXPECTED_MAJOR or version.minor != EXPECTED_MINOR:
        print('⚠️  Warning! Detected Python version '
              f'{version.major}.{version.minor} but expected version '
              f'{EXPECTED_MAJOR}.{EXPECTED_MINOR}')


if __name__ == '__main__':
    main()
