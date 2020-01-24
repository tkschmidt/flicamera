# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flicamera']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17.4,<2.0.0',
 'sdss-basecam>=0.1.0,<0.2.0',
 'sdsstools>=0.1.0,<0.2.0']

extras_require = \
{'docs': ['Sphinx>=2.3.1,<3.0.0']}

entry_points = \
{'console_scripts': ['flicamera = flicamera.__main__:flicamera']}

setup_kwargs = {
    'name': 'sdss-flicamera',
    'version': '0.1.0a0',
    'description': 'A library to control Finger Lakes Instrumentation cameras.',
    'long_description': '# flicamera\n\n![Versions](https://img.shields.io/badge/python->3.7-blue)\n[![Documentation Status](https://readthedocs.org/projects/sdss-flicamera/badge/?version=latest)](https://sdss-flicamera.readthedocs.io/en/latest/?badge=latest)\n[![Travis (.org)](https://img.shields.io/travis/sdss/flicamera)](https://travis-ci.org/sdss/flicamera)\n[![codecov](https://codecov.io/gh/sdss/flicamera/branch/master/graph/badge.svg)](https://codecov.io/gh/sdss/flicamera)\n\nA library to control Finger Lakes Instrumentation cameras. It provides the SDSS `gfaCamera` and `fvcCamera` actors to control the Guide, Focus and Acquisition cameras and Field View Camera, respectively.\n\n## Installation\n\nIn general you should be able to install ``flicamera`` by doing\n\n```console\npip install sdss-flicamera\n```\n\nAlthough `flicamera` should handle all the compilation of the FLI libraries, you may still need to modify your system to give your user access to the FLI USB devices. See [here](https://github.com/sdss/flicamera/blob/master/cextern/README.md) for more details.\n\nTo build from source, use\n\n```console\ngit clone --recurse-submodules -j8 git@github.com:sdss/flicamera\ncd flicamera\npip install .[docs]\n```\n\nThe `--recurse-submodules -j8` flags and `[docs]` extras are only needed to build the documentation.\n\n## Development\n\n`flicamera` uses [poetry](http://poetry.eustace.io/) for dependency management and packaging. Unfortunately, poetry provides a ``setup.py``-less build system that prevents `python setup.py install` or `pip install .` from working (the latter due to the fact that `flicamera` requires compilation of extensions during the build process, see [here](https://github.com/python-poetry/poetry/issues/1516) for details). As a workaround, we provide a script, `create_setup.py` that generates a `setup.py` file with all the metadata from the `pyproject.toml` file.\n\nIn general you can use `poetry` for development as with any other project, but when you update the dependencies remember to also do `python create_setup.py` to update `setup.py`. To all effects, you can think of `setup.py` as a lockfile. You can still use `poetry install`, `poetry build`, and `poetry publish` without worrying about these issues.\n\n`flicamera` also disables the `poetry` build backend because the problems described above, so when building the package directly from source `setup.py` and the standard `setuptools` build system are used.\n',
    'author': 'José Sánchez-Gallego',
    'author_email': 'gallegoj@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdss/flicamera',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)

# This setup.py was autogenerated using poetry.
