# GroqChat

GroqChat is a simple command-line chat application that uses the Groq API. It can optionally integrate with the Turkish NLP library Zemberek to demonstrate morphological analysis.

## Prerequisites

- **Python 3**
- **Java** (required only for Zemberek)
- Obtain your `GROQ_API_KEY` and create a `.env` file in the project root containing:

  ```
  GROQ_API_KEY=YOUR_KEY_HERE
  ```
- Download `zemberek-full.jar` (already included here) if you plan to use Zemberek features.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Chat with Groq

Run the chat application from the repository root:

```bash
python chat.py
```

The bot communicates in Turkish. Type `çık` (or `exit`/`quit`) to end the session.

### Zemberek Morphological Analysis

To try a simple Zemberek integration, run `zemberek_bridge.py` and pass the word
to analyze using the `--word` argument:

```bash
python zemberek_bridge.py --word kelime
```

If no word is provided, the script analyzes the default example word
`geliyormuşsunuz`.

The script invokes the included `zemberek-full.jar` to analyze the word and prints the result. You can modify `zemberek_bridge.py` to analyze any word you like.

## Project Purpose

This repository demonstrates a minimal Groq-based chat interface with an optional bridge to the Zemberek library for Turkish language morphological analysis.


GroqChat provides a simple command-line interface for interacting with the Groq API. The example script `chat.py` demonstrates a basic Turkish conversation assistant.

## Requirements

Install dependencies using `pip install -r requirements.txt`.

## License

This project is licensed under the [MIT License](LICENSE).


