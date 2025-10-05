#!/usr/bin/env python3

import sys
import requests
import bs4
import lxml
import logging

def test_dependencies():
    print("Testing Python version...")
    print(f"Python version: {sys.version}")
    
    print("\nTesting required packages:")
    print(f"requests version: {requests.__version__}")
    print(f"beautifulsoup4 version: {bs4.__version__}")
    print(f"lxml version: {lxml.__version__}")
    
    print("\nTesting basic functionality...")
    try:
        # Test BeautifulSoup with sample HTML
        sample_html = "<html><body><h1>Test</h1><img src='test.jpg'></body></html>"
        soup = bs4.BeautifulSoup(sample_html, 'lxml')
        print("✓ HTML parsing working")
        
        # Verify we can find elements
        assert soup.find('h1') is not None
        assert soup.find('img') is not None
        print("✓ Element finding working")
        
        # Test logging
        logging.basicConfig(level=logging.INFO)
        logging.info("✓ Logging system working")
        
        print("\nAll tests passed successfully! The installation is working correctly.")
        return True
        
    except Exception as e:
        print(f"\nError during testing: {str(e)}")
        return False

if __name__ == "__main__":
    test_dependencies()
