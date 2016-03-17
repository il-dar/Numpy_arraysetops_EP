from setuptools import setup, find_packages

import pkg_conf


setup(
    keywords = "numpy group_by",
    name=pkg_conf.PKG_NAME,
    version=pkg_conf.get_version(),
    packages=find_packages(),
    package_data={
        "{}.data".format(pkg_conf.PKG_ROOT): pkg_conf.DATA_FILES
    },
    description=pkg_conf.get_recipe_meta()['about']['summary'],
    long_description=pkg_conf.get_readme(),
    author=pkg_conf.AUTHOR,
    author_email=pkg_conf.AUTHOR_EMAIL,
    url=pkg_conf.get_recipe_meta()['about']['home'],
    license=pkg_conf.get_recipe_meta()['about']['license'],
    platforms='any',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        "Topic :: Utilities",
        'Topic :: Scientific/Engineering',
        "License :: Freely Distributable",
        'License :: {}'.format(pkg_conf.get_recipe_meta()['about']['license']),
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)