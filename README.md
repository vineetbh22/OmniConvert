# 🔄 OmniConvert

**OmniConvert** is a fast, extensible command-line file conversion tool built in **Python**, designed to handle documents, images, data formats, and video/audio files with high quality and efficiency.

Built with Raspberry Pi compatibility in mind, OmniConvert leverages powerful underlying tools like **FFmpeg**, **Pillow**, and **Pandoc** to deliver reliable and high-performance conversions.

---

## ✨ Features

- 🔁 **Universal file conversion**
  - Documents (PDF, DOCX, TXT)
  - Images (PNG, JPG, WEBP)
  - Data (JSON, CSV, XML)
  - Media (MP4, AVI, MKV, MP3, WAV)

* ⚡ **Optimized for performance**
  - Uses native tools like FFmpeg for speed
  - Efficient on low-power devices like Raspberry Pi

* 🎯 **High-quality output**
  - Minimal loss in media conversions
  - Configurable encoding settings

* 🧩 **Modular & extensible**
  - Easily add new formats and converters

* 💻 **CLI-first design**
  - Simple and scriptable interface

---

## ⚙️ Requirements

- Python 3.8+
- FFmpeg (required for video/audio)
- Pandoc (for document conversion)
- LibreOffice (optional, for advanced document support)

---

## 📦 Installation

### 1. Clone the repository

```bash id="cln123"
git clone https://github.com/your-username/omni-convert.git
cd omni-convert
```

### 2. Install Python dependencies

```bash id="pip456"
pip install -r requirements.txt
```

### 3. Install system dependencies

#### On Raspberry Pi / Debian-based systems:

```bash id="apt789"
sudo apt update
sudo apt install ffmpeg pandoc libreoffice
```

---

#### On Windows:

Download from
_"https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"_

## ▶️ Usage

### Basic Command

```bash id="cmd001"
python cli.py input.mp4 output.avi
```

### With Options

```bash id="cmd002"
python cli.py input.mp4 output.mp4 --quality high --preset fast
```

---

## 🧪 Examples

### 🎥 Convert Video

```bash id="vid001"
python cli.py video.mp4 video.avi
```

### 🎵 Extract Audio from Video

```bash id="aud001"
python cli.py input.mp4 output.mp3
```

### 🖼️ Convert Image

```bash id="img001"
python cli.py image.png image.jpg
```

### 📄 Convert Document

```bash id="doc001"
python cli.py file.docx file.pdf
```

### 📊 Convert Data

```bash id="data001"
python cli.py data.json data.csv
```

---

## ⚡ Performance Tips (Raspberry Pi)

- Use hardware acceleration when available:

  ```bash id="hw001"
  --codec h264_v4l2m2m
  ```

- Reduce resolution for faster processing:

  ```bash id="res001"
  --resolution 1280x720
  ```

- Avoid re-encoding when possible:

  ```bash id="copy001"
  --copy
  ```

---

## 🧱 Project Structure

```id="struct001"
omni-convert/
│── logs/
│   ├── conversion_log.jsonl
│── omni/
│   ├── converters/
│   │   ├── video.py
│   │   ├── image.py
│   │   ├── document.py
│   │   └── data.py
│   ├── core/
│   │   └── dispatcher.py
│   ├── utils/
│   │   └── format_size.py
│   │   └── format_time.py
│   │   └── log_tracker.py
│   └── cli.py
│── requirements.txt
│── README.md
│── LICENSE
```

---

## 🧩 Extending OmniConvert

To add a new format:

1. Create a converter in `omni/converters/`
2. Implement conversion logic
3. Register it in the dispatcher

---

## 🚀 Roadmap

- [ ] Batch file conversion
- [ ] Interactive CLI mode
- [ ] Preset profiles (fast, high-quality, low-size)
- [ ] Web interface
- [ ] Plugin system
- [ ] GPU acceleration support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your branch (`git checkout -b feature/new-feature`)
3. Commit changes
4. Open a Pull Request

---

## 📄 License

MIT License

---

## 💡 Vision

OmniConvert aims to be a **universal, developer-friendly CLI tool** that makes file conversion simple, fast, and reliable — even on low-powered devices like Raspberry Pi.

---
