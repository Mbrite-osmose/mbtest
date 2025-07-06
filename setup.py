from setuptools import setup, find_packages

setup(
    name='codex_github_interface',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
    entry_points={'console_scripts': ['codex-gh=src.github_cli:main']},
)
