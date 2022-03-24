# stdlib
import sys
from typing import List

# 3rd party
import pytest
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus
from testing_tox import prepare_stdout, run_tox

example_tox = PathPlus(__file__).parent / "example_tox.ini"


@pytest.fixture()
def toxinidir(tmp_pathplus: PathPlus) -> PathPlus:
	(tmp_pathplus / "tox.ini").write_text(example_tox.read_text())
	return tmp_pathplus


manual_envs = f"py{sys.version_info[0]}{sys.version_info[1]},mypy"


@pytest.mark.parametrize(
		"command",
		[
				pytest.param(["-e", manual_envs], id="manual_envs"),
				pytest.param(["-e", manual_envs, "--", "--verbose"], id="manual_envs_posargs"),
				pytest.param(["--raspi-ci"], id="raspi"),
				pytest.param(["--raspi-ci", "--", "--verbose"], id="raspi_posargs"),
				pytest.param(["--raspi-ci", "-e", "mypy"], id="invalid_combo"),
				]
		)
def test_tox_raspi_ci(
		capsys,
		command: List[str],
		toxinidir: PathPlus,
		version: str,
		os_sep,
		advanced_file_regression: AdvancedFileRegressionFixture,
		):

	try:
		run_tox(command, toxinidir)

	finally:
		capout = capsys.readouterr()
		assert not capout.err
		advanced_file_regression.check(prepare_stdout(capout.out, toxinidir))


def test_tox_raspi_ci_no_command(capsys, toxinidir: PathPlus, os_sep, monkeypatch):
	# The output varies depending on the versions of python installed on the host
	monkeypatch.setenv("RASPI_CI", '0')

	try:
		run_tox([], toxinidir)

	finally:
		capout = capsys.readouterr()
		assert not capout.err
		assert capout.out


def test_tox_raspi_ci_envvar(capsys, toxinidir: PathPlus, os_sep, monkeypatch):
	# The output varies depending on the versions of python installed on the host

	monkeypatch.setenv("RASPI_CI", '1')

	try:
		run_tox([], toxinidir)

	finally:
		capout = capsys.readouterr()
		assert not capout.err
		assert capout.out
