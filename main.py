import sys
import os
import json

def add_src_to_path():
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

def load_config(config_path = "config.json"):
    with open(config_path, "r", encoding = "utf-8") as file:
        return json.load(file)

def main():
    add_src_to_path()
    from runner import run_candlestick_workflow

    try:
        config = load_config()
        print("Loaded config:", config)
    except FileNotFoundError:
        print(f"Error: Configuration file not found. Please make sure '{os.path.abspath('config.json')}' exists.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid configuration file format. Details: {e}")
        sys.exit(1)

    run_candlestick_workflow(**config)

if __name__ == "__main__":
    main()
