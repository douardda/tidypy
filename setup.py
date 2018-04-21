from setuptools import setup, find_packages


setup(
    name='tidypy',
    version='0.5.0',
    description='A tool that executes a suite of static analysis tools upon a'
    ' Python project.',
    long_description=open('README.rst', 'r').read(),
    keywords='tidypy lint linter static analysis pep8 pep257 pylint',
    author='Jason Simeone',
    author_email='jay@classless.net',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    url='https://github.com/jayclassless/tidypy',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tidypy = tidypy.cli:main',
        ],
        'tidypy.tools': [
            'pycodestyle = tidypy.tools.pycodestyle:PyCodeStyleTool',
            'pydocstyle = tidypy.tools.pydocstyle:PyDocStyleTool',
            'pyroma = tidypy.tools.pyroma:PyromaTool',
            'vulture = tidypy.tools.vulture:VultureTool',
            'bandit = tidypy.tools.bandit:BanditTool',
            'eradicate = tidypy.tools.eradicate:EradicateTool',
            'pyflakes = tidypy.tools.pyflakes:PyFlakesTool',
            'mccabe = tidypy.tools.mccabe:McCabeTool',
            'pylint = tidypy.tools.pylint:PyLintTool',
            'jsonlint = tidypy.tools.jsonlint:JsonLintTool',
            'yamllint = tidypy.tools.yamllint:YamlLintTool',
            'rstlint = tidypy.tools.rstlint:RstLintTool',
            'polint = tidypy.tools.polint:PoLintTool',
            '2to3 = tidypy.tools.lib2to3:Lib2to3Tool',
        ],
        'tidypy.reports': [
            'console = tidypy.reports.console:ConsoleReport',
            'pycodestyle = tidypy.reports.pycodestyle:PyCodeStyleReport',
            'json = tidypy.reports.structured:JsonReport',
            'toml = tidypy.reports.structured:TomlReport',
            'yaml = tidypy.reports.structured:YamlReport',
            'csv = tidypy.reports.structured:CsvReport',
            'pylint = tidypy.reports.pylint:PyLintReport',
            'null = tidypy.reports.null:NullReport',
        ],
        'tidypy.extenders': [
            'github = tidypy.extenders.github:GithubExtender',
            'github-gist = tidypy.extenders.github_gist:GithubGistExtender',
            'bitbucket = tidypy.extenders.bitbucket:BitbucketExtender',
            'bitbucket-snippet = tidypy.extenders.bitbucket_snippet:BitbucketSnippetExtender',  # noqa
            'gitlab = tidypy.extenders.gitlab:GitlabExtender',
            'gitlab-snippet = tidypy.extenders.gitlab_snippet:GitlabSnippetExtender',  # noqa
            'pastebin = tidypy.extenders.pastebin:PastebinExtender',
        ],
        'pytest11': [
            'tidypy = tidypy.plugin.pytest',
        ],
        'nose.plugins.0.10': [
            'tidypy = tidypy.plugin.nose:TidyPy',
        ],
        'distutils.commands': [
            'tidypy = tidypy.plugin.setuptools:TidyPyCommand',
        ],
    },
    install_requires=[
        'six',
        'click>=6,<7',
        'tqdm>=4.11,<5',
        'pytoml>=0.1,<0.2',
        'pyyaml>=3.12,<4',
        'requests>=2,<3',

        'pycodestyle>=2.3,<2.4',
        'pep8-naming>=0.4,<0.6',
        'pydocstyle>=2,<3',
        'pyroma>=2.2,<3',
        'vulture>=0.25,<0.27',
        'bandit>=1.4,<2',
        'pyflakes>=1.5,<1.7',
        'mccabe>=0.6,<0.7',
        'pylint>=1.7,<1.9',
        'demjson>=2.2.4,<3',
        'yamllint>=1.8,<2',
        'restructuredtext-lint>=1.1,<2',
        'dennis>=0.9,<1',
    ],
    extras_require={
        ':python_version<"3.4"': [
            'pathlib2',
            'backports.csv',
            'eradicate>=0.2,<0.3',
        ],
    },
)

