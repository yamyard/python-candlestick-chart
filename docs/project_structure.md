# Project Structure
This document describes the directory and file organization of the project.
```
📦 python-candlestick-chart/
├── 🏃 main.py
├── 📚 docs/
│   └── 📄 project_structure.md
├── 📂 src/
│   ├── 📦 fetcher/
│   │   ├── 📄 __init__.py
│   │   └── 📄 core.py
│   ├── 📦 plotter/
│   │   ├── 📄 __init__.py
│   │   └── 📄 core.py
│   └── 🧩 runner.py
├── 🧪 test/
├── ⚙️ config.json
├── 📦 requirements.txt
└── 📄 README.md
```
## Description
```
| File/Folder           | Description                              
|-----------------------|------------------------------------------
| `main.py`             | Entry point, loads config and runs workflow
| `docs/`               | Project documentation
| `src/fetcher/`        | Data fetching and preprocessing module
| `src/plotter/`        | Candlestick chart plotting module
| `src/runner.py`       | Workflow control and orchestration
| `test/`               | Unit and integration tests
| `config.json`         | Configuration file example
| `requirements.txt`    | Project dependencies
| `README.md`           | Project overview and instructions
```
