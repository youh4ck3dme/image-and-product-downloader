#!/usr/bin/env python3
"""
Image and Product Downloader

A utility for downloading images and extracting product information from websites.
"""

import os
import sys
import argparse
import logging
from urllib.parse import urljoin, urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup


class ImageDownloader:
    """Download images from web pages."""
    
    def __init__(self, output_dir="downloads", timeout=30):
        """
        Initialize the ImageDownloader.
        
        Args:
            output_dir: Directory to save downloaded images
            timeout: Request timeout in seconds
        """
        self.output_dir = Path(output_dir)
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def download_images(self, url, max_images=None):
        """
        Download images from a given URL.
        
        Args:
            url: The webpage URL to scrape images from
            max_images: Maximum number of images to download (None for all)
            
        Returns:
            List of downloaded image paths
        """
        self.logger.info(f"Fetching images from: {url}")
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch URL: {e}")
            return []
        
        soup = BeautifulSoup(response.content, 'lxml')
        images = soup.find_all('img')
        
        self.logger.info(f"Found {len(images)} images")
        
        downloaded_paths = []
        download_count = 0
        
        for img in images:
            if max_images and download_count >= max_images:
                break
                
            img_url = img.get('src') or img.get('data-src')
            if not img_url:
                continue
            
            # Convert relative URLs to absolute
            img_url = urljoin(url, img_url)
            
            # Download the image
            downloaded_path = self._download_image(img_url)
            if downloaded_path:
                downloaded_paths.append(downloaded_path)
                download_count += 1
        
        self.logger.info(f"Successfully downloaded {len(downloaded_paths)} images")
        return downloaded_paths
    
    def _download_image(self, img_url):
        """
        Download a single image.
        
        Args:
            img_url: URL of the image to download
            
        Returns:
            Path to the downloaded image or None if failed
        """
        try:
            response = self.session.get(img_url, timeout=self.timeout, stream=True)
            response.raise_for_status()
            
            # Extract filename from URL
            parsed_url = urlparse(img_url)
            filename = os.path.basename(parsed_url.path)
            
            # If no filename, generate one
            if not filename or '.' not in filename:
                filename = f"image_{hash(img_url) % 10000}.jpg"
            
            filepath = self.output_dir / filename
            
            # Save the image
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            self.logger.debug(f"Downloaded: {filename}")
            return str(filepath)
            
        except Exception as e:
            self.logger.error(f"Failed to download {img_url}: {e}")
            return None


class ProductDownloader:
    """Extract product information from web pages."""
    
    def __init__(self):
        """Initialize the ProductDownloader."""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def extract_products(self, url):
        """
        Extract product information from a URL.
        
        Args:
            url: The webpage URL to extract products from
            
        Returns:
            List of product dictionaries
        """
        self.logger.info(f"Extracting products from: {url}")
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch URL: {e}")
            return []
        
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Generic product extraction (can be customized for specific sites)
        products = []
        
        # Try to find common product elements
        product_elements = soup.find_all(['article', 'div'], class_=lambda x: x and ('product' in x.lower()))
        
        for element in product_elements:
            product = self._extract_product_info(element)
            if product:
                products.append(product)
        
        self.logger.info(f"Extracted {len(products)} products")
        return products
    
    def _extract_product_info(self, element):
        """
        Extract information from a product element.
        
        Args:
            element: BeautifulSoup element containing product info
            
        Returns:
            Dictionary with product information
        """
        product = {}
        
        # Try to extract title
        title_elem = element.find(['h1', 'h2', 'h3', 'h4'], class_=lambda x: x and ('title' in x.lower() or 'name' in x.lower()))
        if title_elem:
            product['title'] = title_elem.get_text(strip=True)
        
        # Try to extract price
        price_elem = element.find(class_=lambda x: x and 'price' in x.lower())
        if price_elem:
            product['price'] = price_elem.get_text(strip=True)
        
        # Try to extract image
        img_elem = element.find('img')
        if img_elem:
            product['image'] = img_elem.get('src') or img_elem.get('data-src')
        
        return product if product else None


def main():
    """Command line interface for the downloader."""
    parser = argparse.ArgumentParser(description='Download images and product information from websites')
    parser.add_argument('--url', required=True, help='URL to download from')
    parser.add_argument('--output', default='downloads', help='Output directory')
    parser.add_argument('--max-images', type=int, help='Maximum number of images to download')
    parser.add_argument('--mode', choices=['images', 'products', 'both'], default='images',
                       help='Download mode: images, products, or both')
    
    args = parser.parse_args()
    
    if args.mode in ['images', 'both']:
        downloader = ImageDownloader(output_dir=args.output)
        downloader.download_images(args.url, max_images=args.max_images)
    
    if args.mode in ['products', 'both']:
        product_downloader = ProductDownloader()
        products = product_downloader.extract_products(args.url)
        
        if products:
            print(f"\n{'='*50}")
            print(f"Found {len(products)} products:")
            print(f"{'='*50}")
            for i, product in enumerate(products, 1):
                print(f"\nProduct {i}:")
                for key, value in product.items():
                    print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
