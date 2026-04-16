"""
Lab 11 — Configuration & API Key Setup
"""

import os


def setup_api_key():
    """Load Google API key from environment or prompt."""
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = input("Enter Google API Key: ")
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
    print("API key loaded.")


def setup_model_provider():
    """Ensure required environment variables are set for the selected provider."""
    provider = os.getenv("MODEL_PROVIDER", "google").lower()

    if provider == "openai" and "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = input("Enter OpenAI API Key: ")
    elif provider == "openrouter" and "OPENROUTER_API_KEY" not in os.environ:
        os.environ["OPENROUTER_API_KEY"] = input("Enter OpenRouter API Key: ")
    elif provider == "shopaikey" and "SHOPAIKEY_API_KEY" not in os.environ:
        os.environ["SHOPAIKEY_API_KEY"] = input("Enter ShopAIKey API Key: ")

    print(f"Model provider '{provider}' configured.")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking",
    "account",
    "transaction",
    "transfer",
    "loan",
    "interest",
    "savings",
    "credit",
    "deposit",
    "withdrawal",
    "balance",
    "payment",
    "tai khoan",
    "giao dich",
    "tiet kiem",
    "lai suat",
    "chuyen tien",
    "the tin dung",
    "so du",
    "vay",
    "ngan hang",
    "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack",
    "exploit",
    "weapon",
    "drug",
    "illegal",
    "violence",
    "gambling",
    "bomb",
    "kill",
    "steal",
]
