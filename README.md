# GroqChat

GroqChat is a simple command-line chat application that uses the Groq API. It can optionally integrate with the Turkish NLP library Zemberek to demonstrate morphological analysis and spell correction.

## Prerequisites

- **Python 3**
- **Java (JDK)** – required for Zemberek spell checking
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

### Spell Correction with Zemberek

When `zemberek-full.jar` is available, `chat.py` automatically sends every
message through Zemberek's `TurkishSpellChecker`. Both your input and the model
reply are corrected before being added to the chat history. Ensure that `java`
and `javac` are installed and that the JAR is located in the project root.

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

### Limitations

- The assistant cannot browse the web or verify live data. All responses come
  from the underlying language model without external retrieval.
- Answers may be outdated or incorrect, so you should verify important
  information independently.
- The default `temperature` in `groq_api.py` is set to `0.7`, which encourages
  cautious replies and aims to reduce speculation.

## License

This project is licensed under the [MIT License](LICENSE).


