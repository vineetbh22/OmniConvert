# OmniConvert Architecture

This document describes the architectural principles and major components of OmniConvert.

## Design Goals

The architecture is designed around:

- Simplicity
- Extensibility
- Maintainability
- Cross-platform support
- Minimal runtime overhead

---

## High-Level Flow

```text
User Input
    │
    ▼
CLI
    │
    ▼
Dispatcher
    │
    ├── Image Converter
    ├── Video Converter
    ├── Document Converter
    └── Data Converter
    │
    ▼
Output File
```

---

## Components

### CLI Layer

Responsibilities:

- Parse user arguments
- Validate inputs
- Display progress and results
- Forward requests to the dispatcher

The CLI should remain thin and contain minimal business logic.

---

### Dispatcher Layer

Responsibilities:

- Determine conversion type
- Select the correct converter
- Coordinate execution
- Handle common validation

The dispatcher acts as the central routing layer.

---

### Converter Layer

Converters are responsible for:

- Format validation
- Dependency validation
- Conversion execution
- Error reporting

Each converter should operate independently.

Examples:

```text
converters/
├── image.py
├── video.py
├── document.py
└── data.py
```

---

### Utilities

Utilities provide shared functionality.

Examples:

```text
utils/
├── log_tracker.py
├── format_size.py
└── format_time.py
```

Utilities should remain generic and reusable.

---

## External Dependencies

OmniConvert intentionally delegates specialized work to mature tools.

### Pillow

Used for image processing.

### FFmpeg

Used for media conversion.

### Pandoc

Used for document conversion.

### LibreOffice

Optional support for advanced document workflows.

---

## Error Handling Strategy

Errors should:

- Fail fast
- Be actionable
- Preserve useful debugging information
- Avoid silent failures

---

## Logging Strategy

Conversion operations should be logged consistently.

Logs should help answer:

- What was converted?
- How long did it take?
- Did it succeed?
- If not, why?

---

## Extensibility

New converters should require minimal changes outside:

1. Converter implementation
2. Dispatcher registration
3. Tests
4. Documentation

This keeps the system modular as supported formats grow.

---

## Future Architecture

Potential future additions include:

```text
CLI
├── Interactive Mode
├── Plugin Manager
├── REST API
└── Web Interface
```

These features should integrate without requiring major changes to the existing conversion pipeline.
