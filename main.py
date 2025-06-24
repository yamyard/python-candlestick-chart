import sys
import os
import json
import yaml

def add_src_to_path():
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

def load_config(config_path = None):
    if config_path is None:
        if os.path.exists("config.yaml"):
            config_path = "config.yaml"
        elif os.path.exists("config.json"):
            config_path = "config.json"
        else:
            raise FileNotFoundError("No config.yaml or config.json found in the current directory.")
    ext = os.path.splitext(config_path)[1].lower()
    with open(config_path, "r", encoding="utf-8") as file:
        if ext in [".yaml", ".yml"]:
            return yaml.safe_load(file)
        elif ext == ".json":
            return json.load(file)
        else:
            raise ValueError(f"Unsupported config file format: {ext}")

def main():
    add_src_to_path()
    from runner import run_candlestick_workflow
    try:
        config = load_config()
        print("Loaded config:", config)
    except FileNotFoundError:
        print(f"Error: Configuration file not found. Please make sure 'config.yaml' or 'config.json' exists in the directory: {os.path.abspath('.')}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid configuration file format. Details: {e}")
        sys.exit(1)
    run_candlestick_workflow(**config)

if __name__ == "__main__":
    main()
