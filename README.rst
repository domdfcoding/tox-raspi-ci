############
tox-raspi-ci
############

.. start short_desc

**tox integration for raspi-ci.**

.. end short_desc

``raspi-ci`` is an experimental CI system for running Python tests on Raspberry Pi SBCs.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |coveralls|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/tox-raspi-ci/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/tox-raspi-ci/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/tox-raspi-ci/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/tox-raspi-ci/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/tox-raspi-ci/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/tox-raspi-ci/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/tox-raspi-ci/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/tox-raspi-ci/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/tox-raspi-ci/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/tox-raspi-ci?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/tox-raspi-ci?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/tox-raspi-ci
	:alt: CodeFactor Grade

.. |license| image:: https://img.shields.io/github/license/domdfcoding/tox-raspi-ci
	:target: https://github.com/domdfcoding/tox-raspi-ci/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/tox-raspi-ci
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/tox-raspi-ci/v0.0.0
	:target: https://github.com/domdfcoding/tox-raspi-ci/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/tox-raspi-ci
	:target: https://github.com/domdfcoding/tox-raspi-ci/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2024
	:alt: Maintenance

.. end shields


Configuration
----------------

In your ``tox.ini`` file, add the following:

.. code-block:: ini

	[envlists]
	raspi = py36, py37, py38

This will configure ``raspi-ci`` to run the environments ``py36``, ``py37`` and ``py38``.


Usage
-------

Run tox using the ``--raspi-ci`` option.


Installation
--------------

.. start installation

``tox-raspi-ci`` can be installed from GitHub.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install git+https://github.com/domdfcoding/tox-raspi-ci

.. end installation
