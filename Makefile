# debloat-android-tv — Makefile
# Curated markdown list + debloat scripts. The debloat scripts REQUIRE ROOT on
# a real device — NEVER run them here or in CI. The safe gates are the README
# consistency checks, the script syntax check and the --dry-run fixture test.
#
#   make check     README + script consistency, syntax, dry-run fixture
#   make clean     remove nothing (docs and scripts are checked in)

PYTHON ?= python3
# Respect $TMPDIR when set; fall back to Termux path on Android, /tmp on Linux.
TMPDIR ?= $(shell if [ -n "$$TERMUX_VERSION" ]; then echo "/data/data/com.termux/files/usr/tmp"; else echo "/tmp"; fi)
export TMPDIR

.PHONY: check clean

check:
	$(PYTHON) tests/check_readme.py
	$(PYTHON) tests/check_scripts.py
	bash -n debloat.sh debloat-safe.sh restore.sh
	bash tests/check_debloat_dryrun.sh
	bash tests/check_audit.sh

clean:
	@true