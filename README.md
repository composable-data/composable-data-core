# composable-data-core: Professional Components for Useful Python

[![PyPI](https://img.shields.io/pypi/v/composable-data-core?logo=pypi&label=pypi)](https://pypi.org/project/composable-data-core/)
[![Python Versions](https://img.shields.io/pypi/pyversions/composable-data-core.svg)](https://pypi.org/project/composable-data-core/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://composable-data.github.io/composable-data-core/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/composable-data/composable-data-core)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/composable-data/composable-data-core/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/composable-data/composable-data-core/actions/workflows/ci-python-zensical.yml)
[![Docs-Deploy](https://github.com/composable-data/composable-data-core/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/composable-data/composable-data-core/actions/workflows/deploy-zensical.yml)
[![Release](https://github.com/composable-data/composable-data-core/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/composable-data/composable-data-core/actions/workflows/release-pypi.yml)
[![Links](https://github.com/composable-data/composable-data-core/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/composable-data/composable-data-core/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/composable-data/composable-data-core/security)

<img
src="https://raw.githubusercontent.com/composable-data/composable-data-core/main/docs/images/profile.png"
alt="profile logo"
width="110">

> Reusable, typed analytical primitives (decision grammar) for Python.

## Purpose

Enable analysts to focus on higher-level analysis skills.

## Design

- Components compute.
- Plans and requests express analytical intent.
- Results carry structured evidence.
- Reporters control representation.
- Integrations connect professional libraries.
- Domain- and dataset-specific behavior lives outside this project.
- Core is dependency-free.
- Protocols and dependency injection preferred over inheritance.
- Analytical decisions are explicit.
- Exact artifacts may be identified with content hashes.

## Developer Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/composable-data/composable-data-core

cd composable-data-core
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

# types, tests, docs
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Documentation

- [Documentation](https://composable-data.github.io/composable-data-core/)

## Annotations

[.annotations/annotations.md](./.annotations/annotations.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
