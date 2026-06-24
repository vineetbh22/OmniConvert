# Contributing to OmniConvert

Thank you for your interest in contributing to OmniConvert.

Whether you're fixing a bug, improving documentation, adding tests, or implementing a new converter, your contributions are welcome.

---

## Before You Start

Please read:

- README.md
- ARCHITECTURE.md
- CONVENTIONS.md
- ROADMAP.md

These documents describe the project's goals, architecture, coding standards, and future direction.

---

## Development Setup

### Clone the Repository

```bash
git clone https://github.com/vineetbh22/OmniConvert.git
cd OmniConvert
```

### Install Dependencies

OmniConvert uses uv for dependency management.

```bash
uv sync --group dev
```

### Install Pre-commit Hooks

```bash
uv run pre-commit install
```

This ensures code quality checks run automatically before commits.

---

## Running Checks

Before opening a Pull Request, ensure all local checks pass.

### Run Tests

```bash
uv run pytest
```

### Run Ruff

```bash
uv run ruff check .
```

### Auto-fix Ruff Issues

```bash
uv run ruff check . --fix
```

### Run All Pre-commit Checks

```bash
uv run pre-commit run --all-files
```

---

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feat/add-webp-support
```

### 2. Make Changes

Keep changes focused on a single feature, fix, or improvement.

### 3. Add or Update Tests

New functionality should include tests whenever practical.

Bug fixes should include a regression test when possible.

### 4. Run Local Checks

```bash
uv run pytest
uv run ruff check .
uv run pre-commit run --all-files
```

### 5. Commit Changes

Recommended commit format:

```text
feat(image): add webp conversion
fix(video): improve ffmpeg error handling
docs(readme): update installation instructions
```

### 6. Open a Pull Request

Push your branch and open a Pull Request against the main branch.

---

## Pull Request Guidelines

Pull Requests should:

- Focus on a single change
- Include tests when applicable
- Update documentation when needed
- Pass all GitHub checks
- Follow project conventions

Large changes should be discussed in an issue before implementation.

---

## Reporting Bugs

Please use the provided [Bug Report template](.github\ISSUE_TEMPLATE\bug_report.md).

Include:

- Operating system
- Python version
- Input format
- Output format
- Error output
- Steps to reproduce

The more details provided, the easier the issue is to diagnose.

---

## Requesting Features

Please use the [Feature Request template](.github\ISSUE_TEMPLATE\feature_request.md).

Helpful information includes:

- The problem being solved
- Expected behavior
- Alternative approaches considered
- Example workflows

---

## Adding New Converters

When adding support for a new format:

1. Implement the converter
2. Register it with the dispatcher
3. Add tests
4. Update documentation
5. Verify all checks pass

Converters should follow the standards defined in CONVENTIONS.md.

---

## GitHub Checks

All Pull Requests are validated using automated CI checks.

Typical checks include:

- Ruff linting
- Test execution
- Repository validation

Pull Requests should not be merged while checks are failing.

---

## Community

Please be respectful and constructive when participating in discussions, reviews, and issue threads.

We welcome contributors of all experience levels.

Happy converting.
