from pathlib import Path
from utils import load_file

PROMPTS_DIR = Path(__file__).parent / "prompt"

def load_prompt(filename: str) -> str:
    """
    Load prompt template from file.
    """
    return load_file(PROMPTS_DIR / filename)

# Load all available prompts
PROMPTS = {
    "react": load_prompt("react.md"),
    "simple": load_prompt("simple.md"),
    "detailed": load_prompt("detailed.md")
}

def generate_prompt(user_input: str, strategy: str = "react") -> str:
    """
    Generate prompt based on strategy.
    """
    if strategy not in PROMPTS:
        raise ValueError(f"Unknown strategy: {strategy}. Available: {list(PROMPTS.keys())}")
    
    template = PROMPTS[strategy]
    return f"{template}\n\nUser Message:\n{user_input.strip()}"