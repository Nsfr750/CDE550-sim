# Development Guide

This guide is for developers who want to contribute to CDE550-sim.

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- pip
- Virtual environment (recommended)

### Setting Up Development Environment

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/your-username/CDE550-sim.git
   cd CDE550-sim
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Unix/MacOS:
   source venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Project Structure

```
CDE550-sim/
├── src/                 # Source code
├── tests/              # Test files
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── .github/            # GitHub configurations
├── requirements.txt    # Production dependencies
└── requirements-dev.txt # Development dependencies
```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number-description
   ```

2. Make your changes and write tests

3. Run tests:
   ```bash
   pytest
   ```

4. Format your code:
   ```bash
   black .
   ```

5. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add: New feature description"
   ```

6. Push your changes and create a pull request

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_module.py

# Run tests with coverage report
pytest --cov=src
```

### Writing Tests

- Place test files in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names starting with `test_`
- Follow the Arrange-Act-Assert pattern

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Keep lines under 88 characters (Black's default)

## Documentation

- Update relevant documentation when making changes
- Follow the existing documentation style
- Add docstrings to all new functions and classes

## Versioning

We follow [Semantic Versioning 2.0.0](https://semver.org/). Update the version in `script/version.py` when making releases.

## Release Process

1. Update version in `script/version.py`
2. Update `CHANGELOG.md`
3. Create a release tag:
   ```bash
   git tag -a v1.0.0 -m "Version 1.0.0"
   git push origin v1.0.0
   ```
4. Create a GitHub release with release notes

## Contributing

Please read [CONTRIBUTING.md](../CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
