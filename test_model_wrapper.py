#!/usr/bin/env python3
"""
Test script for the ModelWrapper class
Demonstrates how to use different providers
"""

import os
import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from core.model_wrapper import ModelWrapper


def test_providers():
    """Test different model providers."""
    # Test Google (ADK-based - will show not implemented since we're using a different approach)
    print("=== Testing Google Provider (ADK-based) ===")
    try:
        google_wrapper = ModelWrapper("google")
        print(f"Provider: {google_wrapper.provider}")
        print(f"Model: {google_wrapper.model_name}")
        print("Note: Google provider uses ADK components directly")
    except Exception as e:
        print(f"Error: {e}")

    # Test OpenAI (if API key is available)
    print("\n=== Testing OpenAI Provider ===")
    if os.getenv("OPENAI_API_KEY"):
        try:
            openai_wrapper = ModelWrapper("openai")
            print(f"Provider: {openai_wrapper.provider}")
            print(f"Model: {openai_wrapper.model_name}")

            # Test generation
            response = openai_wrapper.generate_response(
                "What is the capital of France?", temperature=0.7, max_tokens=100
            )
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping OpenAI test - OPENAI_API_KEY not set")

    # Test OpenRouter (if API key is available)
    print("\n=== Testing OpenRouter Provider ===")
    if os.getenv("OPENROUTER_API_KEY"):
        try:
            openrouter_wrapper = ModelWrapper("openrouter")
            print(f"Provider: {openrouter_wrapper.provider}")
            print(f"Model: {openrouter_wrapper.model_name}")

            # Test generation
            response = openrouter_wrapper.generate_response(
                "What is the capital of Germany?", temperature=0.7, max_tokens=100
            )
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping OpenRouter test - OPENROUTER_API_KEY not set")

    # Test ShopAIKey (if API key is available)
    print("\n=== Testing ShopAIKey Provider ===")
    if os.getenv("SHOPAIKEY_API_KEY"):
        try:
            shopaikey_wrapper = ModelWrapper("shopaikey")
            print(f"Provider: {shopaikey_wrapper.provider}")
            print(f"Model: {shopaikey_wrapper.model_name}")

            # Test generation
            response = shopaikey_wrapper.generate_response(
                "What is the capital of Italy?", temperature=0.7, max_tokens=100
            )
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping ShopAIKey test - SHOPAIKEY_API_KEY not set")


def test_from_env():
    """Test creating wrapper from environment variables."""
    print("\n=== Testing ModelWrapper.from_env() ===")
    try:
        wrapper = ModelWrapper.from_env()
        print(f"Provider from env: {wrapper.provider}")
        print(f"Model from env: {wrapper.model_name}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv

    load_dotenv()

    print("Model Wrapper Test Script")
    print("=" * 50)

    test_providers()
    test_from_env()

    print("\n" + "=" * 50)
    print("Test complete!")
