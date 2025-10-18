#!/usr/bin/env python3
"""
Example script demonstrating proper OpenAI API key configuration.
This script shows multiple ways to configure the API key.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

def method1_environment_variable():
    """Method 1: Using environment variable directly"""
    print("Method 1: Using environment variable")
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your-api-key-here':
        print("❌ OPENAI_API_KEY environment variable not set or still has placeholder value")
        return None
    
    try:
        client = OpenAI(api_key=api_key)
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
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your-api-key-here':
        print("❌ OPENAI_API_KEY not found in .env file or still has placeholder value")
        return None
    
    try:
        client = OpenAI(api_key=api_key)
        print("✅ Client created successfully with .env file")
        return client
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return None

def method3_direct_initialization():
    """Method 3: Direct initialization (not recommended for production)"""
    print("\nMethod 3: Direct initialization (for testing only)")
    
    # This is just for demonstration - don't hardcode API keys in production!
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your-api-key-here':
        print("❌ OPENAI_API_KEY not available for direct initialization")
        return None
    
    try:
        client = OpenAI(api_key=api_key)
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
        # This is a simple test - you can replace with actual API calls
        print("✅ API client is properly configured and ready to use")
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