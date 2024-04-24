# Scrabble

Modifies a given string by replacing each word with a random word that starts with the same letter and has the same length. If no matching word is found, the original word is retained.

## Prerequisites

Before you begin, ensure you have installed:
- **Git**: [Download & Install Git](https://git-scm.com/downloads)
- **Python**: [Download & Install Python](https://www.python.org/downloads/)

Make sure Python 3.8 or higher is installed and that Python and Git are added to your system's PATH.

## Setting Up Your Development Environment

### Cloning the Repository

To clone the repository and navigate into the project directory, use the following commands:

`git clone https://github.com/RudolfxJ/scrabble.git`

### Navigate into the repository

`cd scrabble`

### Creating and activate a Virtual Environment

#### Windows

`py -m venv venv`
`venv\Scripts\activate`

#### Linux

`python3 -m venv venv`
`source venv/bin/activate`

## Running the Application

### Run on Windows

`python main.py`

### Run on Linux

`python3 main.py`

## Creating an executable

`pyinstaller --onefile main.py`
