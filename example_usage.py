#!/usr/bin/env python3
"""
Example usage of the Image and Product Downloader.

This script demonstrates how to use the downloader library.
"""

from downloader import ImageDownloader, ProductDownloader


def example_image_download():
    """Example: Download images from a webpage."""
    print("Example 1: Downloading images")
    print("-" * 50)
    
    # Initialize the downloader
    downloader = ImageDownloader(output_dir="downloads/images")
    
    # Example URL (replace with actual URL when using)
    url = "https://example.com/products"
    
    print(f"URL: {url}")
    print("Note: This is a demonstration. Replace with a real URL to download.")
    print()
    
    # Download images
    # images = downloader.download_images(url, max_images=10)
    # print(f"Downloaded {len(images)} images to downloads/images/")


def example_product_extraction():
    """Example: Extract product information."""
    print("Example 2: Extracting product information")
    print("-" * 50)
    
    # Initialize the product downloader
    product_downloader = ProductDownloader()
    
    # Example URL (replace with actual URL when using)
    url = "https://example.com/products"
    
    print(f"URL: {url}")
    print("Note: This is a demonstration. Replace with a real URL to extract.")
    print()
    
    # Extract products
    # products = product_downloader.extract_products(url)
    # for i, product in enumerate(products, 1):
    #     print(f"\nProduct {i}:")
    #     for key, value in product.items():
    #         print(f"  {key}: {value}")


def example_combined():
    """Example: Download images and extract products."""
    print("Example 3: Combined - Images and Products")
    print("-" * 50)
    
    url = "https://example.com/shop"
    
    print(f"URL: {url}")
    print("Note: This is a demonstration. Replace with a real URL.")
    print()
    
    # Initialize both downloaders
    image_downloader = ImageDownloader(output_dir="downloads/combined")
    product_downloader = ProductDownloader()
    
    # Download images and extract product info
    # images = image_downloader.download_images(url, max_images=5)
    # products = product_downloader.extract_products(url)
    # 
    # print(f"Downloaded {len(images)} images")
    # print(f"Extracted {len(products)} products")


def example_programmatic_usage():
    """Example: Using the library in Python code."""
    print("Example 4: Programmatic Usage")
    print("-" * 50)
    
    from bs4 import BeautifulSoup
    
    # Sample HTML for demonstration
    sample_html = """
    <html>
        <body>
            <div class="product">
                <h2 class="product-title">Example Product</h2>
                <span class="price">$49.99</span>
                <img src="product1.jpg" alt="Product 1">
            </div>
            <div class="product">
                <h2 class="product-title">Another Product</h2>
                <span class="price">$79.99</span>
                <img src="product2.jpg" alt="Product 2">
            </div>
        </body>
    </html>
    """
    
    # Parse HTML
    soup = BeautifulSoup(sample_html, 'lxml')
    products = soup.find_all('div', class_='product')
    
    print(f"Found {len(products)} products in sample HTML")
    
    # Extract product information
    product_downloader = ProductDownloader()
    for i, product_elem in enumerate(products, 1):
        product_info = product_downloader._extract_product_info(product_elem)
        if product_info:
            print(f"\nProduct {i}:")
            for key, value in product_info.items():
                print(f"  {key}: {value}")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("Image and Product Downloader - Example Usage")
    print("=" * 70 + "\n")
    
    examples = [
        example_image_download,
        example_product_extraction,
        example_combined,
        example_programmatic_usage,
    ]
    
    for i, example in enumerate(examples, 1):
        example()
        if i < len(examples):
            print("\n" + "=" * 70 + "\n")
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("\nTo use with real URLs:")
    print("  python downloader.py --url <URL> --mode images")
    print("  python downloader.py --url <URL> --mode products")
    print("  python downloader.py --url <URL> --mode both")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
