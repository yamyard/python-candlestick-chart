import json
from runner import run_candlestick_workflow

def load_config(config_path = "config.json"):
    with open(config_path, "r", encoding = "utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    config = load_config()
    run_candlestick_workflow(**config)
