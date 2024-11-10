from setuptools import find_packages
from setuptools import setup

setup(
    name='jobs-service',
    version='1.0',

    description='All in one jobs service',

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

    provides=['jobs.api',],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'jobs.api': [   # namespace
            'api = apps.jobs.src.pluggable_interface:PluggableAPI',
        ],
    },

    zip_safe=False,
)
