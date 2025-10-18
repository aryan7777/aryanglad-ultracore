#!/usr/bin/env python3
"""
Example script demonstrating proper OpenAI API key configuration.
This script shows multiple ways to configure the API key.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

def get_valid_api_key_from_env():
    """Return a likely-valid API key from env or None.

    Rejects common placeholders and obviously malformed values to avoid
    false positives where a placeholder is treated as a real key.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return None

    # Reject known placeholders and malformed formats
    if api_key in ('your-api-key-here', 'sk-your-actual-api-key-here'):
        return None
    if not api_key.startswith('sk-') or len(api_key) < 20:
        return None
    return api_key

def method1_environment_variable():
    """Method 1: Using environment variable directly"""
    print("Method 1: Using environment variable")
    
    # Check if API key is set and looks valid
    api_key = get_valid_api_key_from_env()
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable missing or invalid")
        return None
    
    try:
        # Rely on environment variable; avoid passing secrets directly
        client = OpenAI()
        print("✅ Client created successfully with environment variable")
        return client
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return None

def method2_dotenv_file():
    """Method 2: Using python-dotenv to load from .env file"""
    print("\nMethod 2: Using .env file with python-dotenv")
    
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = get_valid_api_key_from_env()
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file or invalid")
        return None
    
    try:
        client = OpenAI()
        print("✅ Client created successfully with .env file")
        return client
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return None

def method3_direct_initialization():
    """Method 3: Direct initialization (not recommended for production)"""
    print("\nMethod 3: Direct initialization (for testing only)")
    
    # This is just for demonstration - don't hardcode API keys in production!
    api_key = get_valid_api_key_from_env()
    if not api_key:
        print("❌ OPENAI_API_KEY not available or invalid for direct initialization")
        return None
    
    try:
        # Even for "direct" initialization, avoid passing secrets explicitly
        client = OpenAI()
        print("✅ Client created successfully with direct initialization")
        return client
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return None

def test_api_connection(client):
    """Test the API connection with a simple request"""
    if not client:
        print("❌ No client available for testing")
        return
    
    try:
        print("\nTesting API connection...")
        # Make a lightweight call to verify credentials and connectivity
        models = client.models.list()
        sample = models.data[0].id if getattr(models, "data", []) else "no models"
        print(f"✅ API client authenticated; sample model: {sample}")
        print("You can now make API calls using the client object")
    except Exception as e:
        print(f"❌ API test failed: {e}")

def main():
    """Main function to demonstrate all methods"""
    print("OpenAI API Key Configuration Examples")
    print("=" * 50)
    
    # Try different methods
    client1 = method1_environment_variable()
    client2 = method2_dotenv_file()
    client3 = method3_direct_initialization()
    
    # Test with the first successful client
    client = client1 or client2 or client3
    test_api_connection(client)
    
    print("\n" + "=" * 50)
    print("Setup Instructions:")
    print("1. Copy .env.example to .env")
    print("2. Replace 'your-api-key-here' with your actual OpenAI API key")
    print("3. Install required packages: pip install openai python-dotenv")
    print("4. Run this script: python example_usage.py")

if __name__ == "__main__":
    main()