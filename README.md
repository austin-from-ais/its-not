# it's not

A CLI tool for an art installation featuring a receipt printer that endlessly generates negative responses to questions about America. Each response completes the phrase "it's not ___" — specific, visceral, like protest poetry on a receipt.

## Setup

1. Install Python 3.10 or newer
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python its_not.py
   ```
4. When prompted, paste your Anthropic API key (or set the `ANTHROPIC_API_KEY` environment variable before running)

## Usage

- Select a question from the menu (or enter your own)
- Choose Manual mode (press Enter for each response) or Auto mode (25 at a time)
- Press Enter to generate responses
- Type `b` to go back to the menu, `q` to quit
