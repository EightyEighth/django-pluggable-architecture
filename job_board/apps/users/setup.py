from setuptools import find_packages
from setuptools import setup

setup(
    name='users-service',
    version='1.0',

    description='All in one users service',

    author='Denys Rozlomii',
    author_email='example@example.com',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11',
                 'Programming Language :: Python :: 3.12',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['users.api',],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'users.api': [   # namespace
            'api = apps.users.src.pluggable_interface:PluggableAPI',
        ],
    },

    zip_safe=False,
)
