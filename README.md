# Image and Product Downloader

A Python utility for downloading images and product information from websites.

## Features

- Download images from web pages
- Extract product information
- Support for multiple websites
- Customizable download options
- Automatic file organization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/youh4ck3dme/image-and-product-downloader.git
cd image-and-product-downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from downloader import ImageDownloader

# Initialize downloader
downloader = ImageDownloader()

# Download images from a URL
downloader.download_images("https://example.com", output_dir="downloads")
```

### Command Line Usage

```bash
python downloader.py --url "https://example.com" --output downloads/
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- lxml

## Testing

Run the installation test to verify dependencies:

```bash
python test_installation.py
```

## Project Structure

```
image-and-product-downloader/
├── downloader.py          # Main downloader module
├── test_installation.py   # Dependency verification
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## License

This project is provided as-is for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
