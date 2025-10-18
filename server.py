#!/usr/bin/env python3
"""
Server with OpenAI API integration.
Properly handles API key configuration from environment variables or direct configuration.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def get_openai_client():
    """
    Initialize and return an OpenAI client with proper API key configuration.
    
    The API key is retrieved from the OPENAI_API_KEY environment variable.
    If not found, raises a clear error message.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.\n"
            "You can:\n"
            "1. Create a .env file with: OPENAI_API_KEY=your-api-key-here\n"
            "2. Or export it in your shell: export OPENAI_API_KEY=your-api-key-here"
        )
    
    # Initialize OpenAI client with the API key
    client = OpenAI(api_key=api_key)
    return client


def main():
    """Main server function."""
    try:
        # Initialize OpenAI client with proper API key handling
        client = get_openai_client()
        
        print("✓ OpenAI client initialized successfully!")
        print("✓ API key configured properly")
        
        # Example: Test the client with a simple API call
        print("\nTesting OpenAI API connection...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello! API key is working correctly.'"}
            ],
            max_tokens=50
        )
        
        print(f"✓ API Response: {response.choices[0].message.content}")
        
    except ValueError as e:
        print(f"✗ Configuration Error: {e}")
        return 1
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
