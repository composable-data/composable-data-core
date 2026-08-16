# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.0.5] - 2026-08-16

### Changed

- Changed `ModelPlan.parameters` to use an empty mapping
  by default instead of `None`.

---

## [0.0.4] - 2026-08-16

### Changed

- Replaced `ExperimentPlan` with `ExperimentSpec` as the pre-run experiment specification.
- Removed `available_features` from the experiment specification
  because available features are observed from loaded data during execution.
- Consolidated experiment meaning, design, resolution, split,
  baseline, and candidate model declarations into `ExperimentSpec`.

---

## [0.0.3] - 2026-08-16

### Added

- Updated release of `composable-data-core`.
- Added typed-package support with `py.typed`.
- Added professional project documentation, testing, type checking, linting, CI, and release infrastructure.

---

## Notes on Versioning and Releases

- We use **SemVer**:
  - **MAJOR** - breaking changes
  - **MINOR** - backward-compatible additions
  - **PATCH** - fixes, documentation, tooling
- Versions are driven by git tags.
- Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

## Release Procedure

Follow these steps when creating a new release.

### Task 1. Update release metadata

1. Update `CITATION.cff`: change `version` and `date-released`
2. Update `CHANGELOG.md`: move from unreleased, add entry, update links
3. Update `pyproject.toml`: update `[tool.hatch.version] fallback-version`

### Task 2. Validate

```shell
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# rerun if changes made
uv run pre-commit run --all-files

npx markdownlint-cli2 --fix
uvx cffconvert --validate

uv run ty check
uv run python -m pytest
uv run python -m zensical build

uv run python -c "import shutil; from pathlib import Path; shutil.rmtree(Path('dist'), ignore_errors=True)"

uv build
uvx twine check dist/*
```

### Task 3. Commit, push, tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/composable-data/composable-data-core/compare/v0.0.5...HEAD
[0.0.5]: https://github.com/composable-data/composable-data-core/releases/tag/v0.0.5
[0.0.4]: https://github.com/composable-data/composable-data-core/releases/tag/v0.0.4
[0.0.3]: https://github.com/composable-data/composable-data-core/releases/tag/v0.0.3

<!-- markdownlint-enable MD024 -->
