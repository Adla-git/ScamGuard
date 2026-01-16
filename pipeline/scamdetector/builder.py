"""
This file contains main prompt development functionality.
"""

from llm.prompts import generate_prompt

def build_prompt(message: str, strategy: str = "react") -> str:
    """
    Build a prompt for the given user message based on selected strategy.
    """
    return generate_prompt(message, strategy)