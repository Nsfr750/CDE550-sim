# Contributing to CDE550-sim

Thank you for your interest in contributing to CDE550-sim! We welcome all contributions, including bug reports, feature requests, documentation improvements, and code contributions.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)
- [Code Review Process](#code-review-process)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check [existing issues](https://github.com/Nsfr750/CDE550-sim/issues) to see if the problem has already been reported.

When creating a bug report, please include:
1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Screenshots if applicable
6. Environment details (OS, Python version, etc.)

### Feature Requests

We welcome feature requests! Please open an issue with:
1. A clear, descriptive title
2. A description of the proposed feature
3. The problem it solves
4. Any alternative solutions considered

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Workflow

1. Set up your development environment (see [Development Guide](./development.md))
2. Create a new branch for your changes
3. Make your changes
4. Run tests and ensure they pass
5. Update documentation as needed
6. Submit a pull request

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Keep lines under 88 characters (Black's default)
- Run `black .` to format your code

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

## Code Review Process

1. A maintainer will review your PR
2. You may receive feedback or be asked to make changes
3. Once approved, your PR will be merged
4. Thank you for your contribution!

## Recognition

All contributors will be recognized in the project's README.md and release notes.

## Questions?

If you have any questions, feel free to:
- Open an issue
- Join our [Discord server](https://discord.gg/ryqNeuRYjD)
- Contact the maintainer directly
