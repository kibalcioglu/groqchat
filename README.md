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

To try a simple Zemberek integration, use `zemberek_bridge.py`:

```bash
python zemberek_bridge.py
```

The script invokes the included `zemberek-full.jar` to analyze a sample word and prints the result. You can modify `zemberek_bridge.py` to analyze any word you like.

## Project Purpose

This repository demonstrates a minimal Groq-based chat interface with an optional bridge to the Zemberek library for Turkish language morphological analysis.


