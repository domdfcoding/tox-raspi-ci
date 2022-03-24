#!/usr/bin/env python3
#
#  __init__.py
"""
tox integration for raspi-ci.

The plugin does nothing unless the ``--raspi-ci`` option is given or the ``RASPI_CI`` environment variable is set.
If either of those is given, the plugin looks for the presence of an ``[envlists]`` section in ``tox.ini``.
This is used for configuring the `tox-envlist <https://github.com/python-coincidence/tox-envlist>`_ plugin.
If the section is present and contains an envlist named ``raspi``, the testenvs listed there are run.
If the section is present or doesn't contain a ``raspi`` envlist, ``tox`` runs its default envlist.
"""
#
#  Copyright © 2022 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import os
from itertools import chain
from typing import TYPE_CHECKING, Dict, List

# 3rd party
import pluggy  # type: ignore
import tox.config  # type: ignore
import tox.reporter  # type: ignore
from braceexpand import braceexpand
from tox_envlist import DELIMITERS

if TYPE_CHECKING:
	# 3rd party
	from iniconfig import IniConfig

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2022 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["option_name", "tox_addoption", "tox_configure"]

hookimpl = pluggy.HookimplMarker("tox")

#: The names of the options which may be passed on the command line to select the envlist to use.
option_name = "--raspi-ci"


@hookimpl
def tox_addoption(parser: tox.config.Parser):
	"""
	Add a command line option to choose a different envlist.
	"""

	parser.add_argument(
			option_name,
			action="store_true",
			help="Run the relevant tests for raspi-ci.",
			default=False,
			)


@hookimpl
def tox_configure(config: tox.config.Config):
	"""
	Parse the command line and ini options.
	"""

	args: List[List[str]] = [[]]

	while config.args:
		val: str = config.args.pop(0)
		if val == "--":
			break
		elif val.startswith('-'):
			args.append([val])
		else:
			args[-1].append(val)

	envlist_set = raspi_ci_envlist = False

	# Parse envlists
	ini_config: "IniConfig" = config._cfg
	envlists: Dict[str, List[str]] = {}

	for envlist_name, envlist in ini_config.sections.get("envlists", {}).items():
		envlist_elements = DELIMITERS.split(envlist)
		expanded_envlist = list(chain.from_iterable(map(braceexpand, envlist_elements)))
		envlists[envlist_name] = list(filter(None, expanded_envlist))

	for idx, arg in enumerate(args):
		if arg and arg[0] in {"-e", "--envlist"}:
			envlist_set = True
		elif arg and arg[0] == option_name:
			raspi_ci_envlist = True

	if raspi_ci_envlist and envlist_set:
		tox.reporter.warning(f"Ignoring {option_name!r} option as '-e / --envlist' option given.", )

	elif "raspi" in envlists:
		if raspi_ci_envlist:
			config.envlist = envlists["raspi"]

		elif not envlist_set and int(os.environ.get("RASPI_CI", 0)):
			config.envlist = envlists["raspi"]

	config.args = list(chain.from_iterable(args))

	return config
