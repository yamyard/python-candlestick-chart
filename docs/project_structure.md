# Project Structure
This document describes the directory and file organization of the project.
```
python-candlestick-chart/
├── main.py # Entry point of the application, loads config and runs the workflow
├── src/
│ ├── fetcher/ # Data fetching and preprocessing module (package)
│ │ ├── init.py
│ │ └── core.py # Main code for the fetcher module
│ ├── plotter/ # Candlestick chart plotting module (package)
│ │ ├── init.py
│ │ └── core.py # Main code for the plotter module
│ ├── runner.py # Workflow control and orchestration
├── config.json # Configuration file example
├── requirements.txt # List of project dependencies
├── docs/ # Project documentation
│ └── project_structure.md # This document
├── test/ # Unit tests and integration tests
└── README.md # Project overview and instructions
```