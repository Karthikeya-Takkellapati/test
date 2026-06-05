import argparse
from utils import count_tokens
from pricing import PRICING

DEFAULT_MODEL = "gpt-4o-mini"

def estimate_cost(tokens, model):
    price_per_1k = PRICING[model]["input"]
    return (tokens / 1000) * price_per_1k

def choose_model():
    models = list(PRICING.keys())
    
    print("Available Models:")
    for i, model in enumerate(models, 1):
        print(f"{i}. {model}")
    
    choice = input(f"Enter model number (default = {DEFAULT_MODEL}): ")

    if choice.isdigit() and 1 <= int(choice) <= len(models):
        return models[int(choice) - 1]
    else:
        print(f"Invalid choice. Using default: {DEFAULT_MODEL}")
        return DEFAULT_MODEL

def main():
    parser = argparse.ArgumentParser(description="Token Counter CLI")
    parser.add_argument("file", help="Path to text file")
    args = parser.parse_args()

    # 🔹 Model selection
    model = choose_model()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found!")
        return

    # 🔹 Token count
    tokens = count_tokens(text, model)

    # 🔹 Only input cost
    cost = estimate_cost(tokens, model)

    # 🔹 Output
    print("Results:")
    print(f"Model: {model}")
    print(f"Tokens: {tokens}")
    print(f"Estimated Input Cost: ${cost:.6f}")

if __name__ == "__main__":
    main()