# 🔄 OmniConvert

**OmniConvert** is a fast, extensible command-line file conversion tool built in Python.

The goal of OmniConvert is simple:

> Convert files reliably, efficiently, and with minimal dependencies.

Designed with automation, scripting, and low-powered devices in mind, OmniConvert aims to provide a consistent conversion experience across images, documents, data formats, and media files.

---

## Features

### Universal File Conversion

Support for common file formats including:

#### Images

- PNG
- JPG / JPEG
- WEBP

#### Documents

- PDF
- DOCX
- TXT

#### Data

- JSON
- CSV
- XML

#### Media

- MP4
- AVI
- MKV
- MP3
- WAV

---

### CLI First

OmniConvert is built for:

- Terminal users
- Automation workflows
- Shell scripting
- CI/CD pipelines

---

### Extensible Architecture

New formats can be added without major architectural changes.

Converters are isolated and routed through a central dispatcher, making the project easy to extend and maintain.

---

### Raspberry Pi Friendly

OmniConvert is designed to work efficiently on low-powered hardware while still supporting high-quality conversions.

---

## Installation

### Requirements

- Python 3.11+
- uv
- FFmpeg (for media conversions)
- Pandoc (for document conversions)
- LibreOffice (optional)

---

### Clone the Repository

```bash
git clone https://github.com/vineetbh22/OmniConvert.git
cd OmniConvert
```

### Install Dependencies

```bash
uv sync
```

### Install Development Dependencies

```bash
uv sync --group dev
```

---

## Usage

Basic example:

```bash
python -m omni.cli "input.png" "output.jpg" --enhance
```

Media conversion:

```bash
python -m omni.cli "video.mkv" "video.mp4" --compatibility windows
```

Document conversion:

```bash
python -m omni.cli "input.docx" "output.pdf"
```

Data conversion:

```bash
python -m omni.cli "data.json" "data.csv"
```

---

## Development

Run tests:

```bash
uv run pytest
```

Run Ruff:

```bash
uv run ruff check .
```

Install pre-commit hooks:

```bash
uv run pre-commit install
```

Run all repository checks:

```bash
uv run pre-commit run --all-files
```

---

## Documentation

Additional project documentation:

- CONTRIBUTING.md
- CONVENTIONS.md
- ARCHITECTURE.md
- ROADMAP.md

---

## Project Structure

```text
omniconvert/
├── omni/
│   ├── converters/
│   ├── core/
│   └── utils/
├── tests/
├── logs/
├── README.md
├── CONTRIBUTING.md
├── CONVENTIONS.md
├── ARCHITECTURE.md
└── ROADMAP.md
```

---

## Roadmap Highlights

Planned features include:

- Batch conversion
- Preset profiles
- Interactive CLI mode
- Plugin system
- Hardware acceleration support
- REST API
- Web interface

See ROADMAP.md for details.

---

## Contributing

Contributions are welcome.

Please read CONTRIBUTING.md before opening an issue or Pull Request.

---

## License

MIT License

---

## Vision

OmniConvert aims to become a universal, developer-friendly conversion toolkit that prioritizes:

- Reliability
- Performance
- Simplicity
- Extensibility

One tool. Many formats.
