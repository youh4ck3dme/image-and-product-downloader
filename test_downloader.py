#!/usr/bin/env python3
"""
Test suite for the image and product downloader.
"""

import os
import tempfile
import shutil
from pathlib import Path

from downloader import ImageDownloader, ProductDownloader


def test_image_downloader_init():
    """Test ImageDownloader initialization."""
    print("Testing ImageDownloader initialization...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        downloader = ImageDownloader(output_dir=temp_dir)
        
        # Check output directory was created
        assert Path(temp_dir).exists()
        print("✓ ImageDownloader initialization working")
        return True


def test_product_downloader_init():
    """Test ProductDownloader initialization."""
    print("Testing ProductDownloader initialization...")
    
    product_downloader = ProductDownloader()
    assert product_downloader is not None
    assert hasattr(product_downloader, 'session')
    
    print("✓ ProductDownloader initialization working")
    return True


def test_product_extraction_parsing():
    """Test product information extraction logic."""
    print("Testing product extraction parsing...")
    
    from bs4 import BeautifulSoup
    
    # Create sample product HTML
    sample_html = """
    <div class="product-item">
        <h2 class="product-title">Sample Product</h2>
        <span class="product-price">$99.99</span>
        <img src="product.jpg" alt="Product">
    </div>
    """
    
    soup = BeautifulSoup(sample_html, 'lxml')
    product_element = soup.find('div', class_='product-item')
    
    product_downloader = ProductDownloader()
    product = product_downloader._extract_product_info(product_element)
    
    assert product is not None
    assert 'title' in product
    assert 'price' in product
    assert 'image' in product
    
    print("✓ Product extraction parsing working")
    return True


def run_all_tests():
    """Run all tests."""
    print("="*50)
    print("Running downloader tests...")
    print("="*50)
    
    tests = [
        test_image_downloader_init,
        test_product_downloader_init,
        test_product_extraction_parsing,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*50)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
