# Python Learning Repository

A structured set of Python learning examples covering fundamentals, data structures, OOP, and advanced concepts.

## Repository purpose
This repository is for practicing and revising Python concepts through small focused scripts.

## Repository structure
- `python/` - core Python basics and practice scripts
- `Data Structure/` - list, tuple, dictionary, and algorithm practice
- `OOPS/` - object-oriented programming examples
- `Advance python/` - advanced language concepts such as decorators

## Local setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install quality tools:
   ```bash
   python -m pip install --upgrade pip
   pip install black ruff pytest
   ```

## Run checks locally
```bash
black --check tests
ruff check tests
pytest
```

## Running learning scripts
Most scripts are standalone and can be run directly:
```bash
python "Data Structure/calculator.py"
python "python/main.py"
```

## Environment variables
No environment variables are required for the current project setup.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution workflow and quality expectations.

## Security
See [SECURITY.md](SECURITY.md) for responsible vulnerability reporting.

## Code of Conduct
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License
This project is licensed under the [MIT License](LICENSE).
