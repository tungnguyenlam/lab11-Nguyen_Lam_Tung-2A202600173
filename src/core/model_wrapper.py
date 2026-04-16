"""
Model Wrapper for Lab 11 - Supporting Multiple Providers
Supports OpenAI, OpenRouter, and custom ShopAIKey provider
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ModelWrapper:
    """Wrapper class to support multiple LLM providers."""

    def __init__(self, provider: str = "google"):
        """
        Initialize the model wrapper with a specific provider.

        Args:
            provider: The provider to use ("google", "openai", "openrouter", "shopaikey")
        """
        self.provider = provider.lower()
        self.client = None
        self.model_name = None

        if self.provider == "google":
            self._setup_google_client()
        elif self.provider == "openai":
            self._setup_openai_client()
        elif self.provider == "openrouter":
            self._setup_openrouter_client()
        elif self.provider == "shopaikey":
            self._setup_shopaikey_client()
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def _setup_google_client(self):
        """Setup Google GenAI client."""
        # For Google, we're using the existing ADK approach
        # The model name will be passed directly to ADK components
        self.model_name = "gemini-2.5-flash-lite"

    def _setup_openai_client(self):
        """Setup OpenAI client."""
        try:
            from openai import OpenAI

            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")

            self.client = OpenAI(api_key=api_key)
            self.model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4")
        except ImportError:
            raise ImportError("openai package not installed. Run: pip install openai")

    def _setup_openrouter_client(self):
        """Setup OpenRouter client."""
        try:
            from openai import OpenAI

            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise ValueError(
                    "OPENROUTER_API_KEY not found in environment variables"
                )

            self.client = OpenAI(
                api_key=api_key, base_url="https://openrouter.ai/api/v1"
            )
            self.model_name = os.getenv("OPENROUTER_MODEL_NAME", "openai/gpt-4")
        except ImportError:
            raise ImportError("openai package not installed. Run: pip install openai")

    def _setup_shopaikey_client(self):
        """Setup ShopAIKey client."""
        try:
            from openai import OpenAI

            api_key = os.getenv("SHOPAIKEY_API_KEY")
            if not api_key:
                raise ValueError("SHOPAIKEY_API_KEY not found in environment variables")

            self.client = OpenAI(
                api_key=api_key,
                base_url="https://api.shopaikey.com/v1",
                default_headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                },
            )
            self.model_name = os.getenv("SHOPAIKEY_MODEL_NAME", "gpt-4")
        except ImportError:
            raise ImportError("openai package not installed. Run: pip install openai")

    def generate_response(self, prompt: str, **kwargs) -> str:
        """
        Generate a response using the configured provider.

        Args:
            prompt: The input prompt
            **kwargs: Additional arguments for the model

        Returns:
            The generated response text
        """
        if self.provider == "google":
            # For Google, we're using ADK which handles generation differently
            # This method won't be used for Google provider in this context
            raise NotImplementedError(
                "Google provider uses ADK - call ADK components directly"
            )

        if not self.client:
            raise RuntimeError(f"Client not initialized for provider: {self.provider}")

        # Prepare the messages
        messages = [{"role": "user", "content": prompt}]

        # Add any additional kwargs
        generation_kwargs = {
            "model": self.model_name,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 1000),
        }

        # Add any other provided kwargs
        generation_kwargs.update(kwargs)

        # Generate response
        response = self.client.chat.completions.create(**generation_kwargs)

        # Extract and return the response text
        return response.choices[0].message.content

    @classmethod
    def from_env(cls) -> "ModelWrapper":
        """
        Create a ModelWrapper instance from environment variables.

        Expects MODEL_PROVIDER environment variable to be set.
        """
        provider = os.getenv("MODEL_PROVIDER", "google")
        return cls(provider)


# Convenience functions for backward compatibility
def get_model_wrapper(provider: str = "google") -> ModelWrapper:
    """Get a model wrapper instance for the specified provider."""
    return ModelWrapper(provider)


def get_default_model_wrapper() -> ModelWrapper:
    """Get a model wrapper instance based on environment variables."""
    return ModelWrapper.from_env()
