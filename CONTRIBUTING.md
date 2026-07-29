# Contributing

Thanks for your interest in contributing to this repository.

## Getting started
1. Fork the repository and create a branch from `main`.
2. Set up a local virtual environment.
3. Install quality tools:
   ```bash
   python -m pip install --upgrade pip
   pip install black ruff pytest
   ```
4. Run checks before opening a PR:
   ```bash
   black --check tests
   ruff check tests
   pytest -q
   ```

## Pull request expectations
- Keep changes focused and easy to review.
- Update documentation when behavior or workflow changes.
- Use clear commit messages.
- Ensure CI is passing.

## Reporting issues
Please use the issue templates for bugs and feature requests.
