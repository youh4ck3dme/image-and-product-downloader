#!/usr/bin/env python3
"""
Test suite for the image and product downloader.
"""

import tempfile

from downloader import ImageDownloader, ProductDownloader, _validate_url, _sanitize_filename


def test_image_downloader_init():
    """Test ImageDownloader initialization."""
    print("Testing ImageDownloader initialization...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        ImageDownloader(output_dir=temp_dir)
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


def test_validate_url():
    """Test URL scheme validation."""
    print("Testing URL scheme validation...")
    
    # Valid URLs should not raise
    _validate_url("http://example.com")
    _validate_url("https://example.com/page")
    
    # Invalid schemes should raise ValueError
    for bad_url in ["file:///etc/passwd", "ftp://example.com", "javascript:alert(1)", ""]:
        try:
            _validate_url(bad_url)
            assert False, f"Should have raised ValueError for: {bad_url}"
        except ValueError:
            pass
    
    print("✓ URL scheme validation working")
    return True


def test_sanitize_filename():
    """Test filename sanitization."""
    print("Testing filename sanitization...")
    
    # Normal filenames should pass through (mostly unchanged)
    assert _sanitize_filename("image.jpg") == "image.jpg"
    assert _sanitize_filename("photo_1.png") == "photo_1.png"
    
    # Path traversal attempts should be neutralized
    result = _sanitize_filename("../../etc/passwd")
    assert "/" not in result
    assert ".." not in result
    
    # Hidden files should have leading dots removed
    assert not _sanitize_filename(".hidden").startswith(".")
    
    # Empty input should return a default
    assert _sanitize_filename("") == "download"
    
    # Special characters should be replaced
    result = _sanitize_filename("file<>:\"|?*.jpg")
    assert "<" not in result
    assert ">" not in result
    
    print("✓ Filename sanitization working")
    return True


def test_url_validation_blocks_ssrf():
    """Test that ImageDownloader and ProductDownloader reject non-http(s) URLs."""
    print("Testing SSRF protection...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        img_downloader = ImageDownloader(output_dir=temp_dir)
        # file:// URL should return empty list, not attempt file access
        result = img_downloader.download_images("file:///etc/passwd")
        assert result == []
    
    product_downloader = ProductDownloader()
    result = product_downloader.extract_products("file:///etc/passwd")
    assert result == []
    
    print("✓ SSRF protection working")
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
        test_validate_url,
        test_sanitize_filename,
        test_url_validation_blocks_ssrf,
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
