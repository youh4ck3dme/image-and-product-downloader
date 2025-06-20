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
        # Test URL request
        response = requests.get("https://www.python.org")
        print("✓ HTTP requests working")
        
        # Test BeautifulSoup
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        print("✓ HTML parsing working")
        
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
