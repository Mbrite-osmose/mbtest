# Hello World Python Application

A simple Python application that prints "Hello, World!" to the console.

## Project Structure

```
mbtest/
├── src/
│   ├── __init__.py
│   └── main.py          # Main application code
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Unit tests
├── setup.py             # Package configuration
├── requirements.txt     # Dependencies (currently empty)
└── README.md           # This file
```

## Usage

### Running the Application

To run the hello world application directly:

```bash
python src/main.py
```

This will output:
```
Hello, World!
```

### Running Tests

To run the unit tests:

```bash
python -m unittest tests.test_main -v
```

### Installing as a Package

To install the application as a package:

```bash
pip install -e .
```

After installation, you can run:

```bash
hello-world
```

## Requirements

- Python 3.6 or higher

## Development

This is a simple hello world application demonstrating basic Python project structure with:
- Modular code organization
- Unit testing
- Package configuration
- Documentation
