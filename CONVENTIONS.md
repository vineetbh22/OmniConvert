# OmniConvert Development Conventions

This document defines the coding and contribution standards used throughout the project.

## Python Version

OmniConvert targets:

```text
Python >= 3.11
```

All new code should be compatible with the minimum supported version.

---

## Tooling

### Package Management

The project uses:

```text
uv
```

Install dependencies:

```bash
uv sync
```

Install development dependencies:

```bash
uv sync --group dev
```

---

### Linting

The project uses Ruff.

Run checks:

```bash
uv run ruff check .
```

Apply fixes:

```bash
uv run ruff check . --fix
```

---

### Testing

Run tests locally before opening a pull request.

```bash
uv run pytest
```

---

### Pre-Commit

Install hooks:

```bash
uv run pre-commit install
```

Run manually:

```bash
uv run pre-commit run --all-files
```

---

## Naming Conventions

### Files

Use snake_case.

Good:

```text
image_converter.py
log_tracker.py
```

Bad:

```text
ImageConverter.py
imageConverter.py
```

### Functions

Use snake_case.

```python
def convert_image():
    ...
```

### Classes

Use PascalCase.

```python
class ImageConverter:
    ...
```

### Constants

Use UPPER_CASE.

```python
DEFAULT_QUALITY = "high"
```

---

## Imports

Order imports as:

1. Standard library
2. Third-party packages
3. Local imports

Example:

```python
from pathlib import Path

from PIL import Image

from omniconvert.converters.image import ImageConverter
```

---

## Error Handling

Avoid generic exceptions.

Preferred:

```python
raise UnsupportedFormatError(format_name)
```

Avoid:

```python
raise Exception("Something went wrong")
```

Provide actionable error messages whenever possible.

---

## Logging

Use project logging utilities rather than print statements.

Preferred:

```python
logger.info("Starting conversion")
```

Avoid:

```python
print("Starting conversion")
```

---

## Testing

Test files should follow:

```text
tests/test_image.py
tests/test_video.py
```

Test names should describe behavior:

```python
def test_png_to_jpg_conversion():
    ...
```

---

## Documentation

Public APIs should include docstrings.

User-facing changes should update documentation when appropriate.

---

## Commit Messages

Recommended format:

```text
type(scope): description
```

Examples:

```text
feat(image): add webp support
fix(video): handle ffmpeg failures
docs(readme): update installation guide
```

Common types:

- feat
- fix
- docs
- refactor
- test
- chore
- perf
