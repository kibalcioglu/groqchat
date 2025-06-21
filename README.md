# GroqChat

GroqChat is a simple command-line chat application that uses the Groq API.

## Spell Correction with LLM
This project uses Groq LLM to semantically correct both user inputs and model replies. It does not rely on any local NLP tools.

## Prerequisites

- **Python 3**
- Obtain your `GROQ_API_KEY` and create a `.env` file in the project root containing:

```
GROQ_API_KEY=YOUR_KEY_HERE
```

`groq_api.py` loads this variable and can be tweaked to work with the OpenAI API or a local model by editing the URL and headers.

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

## Project Purpose

GroqChat provides a minimal command-line interface for interacting with the Groq API. The helper module `groq_api.py` reads `GROQ_API_KEY` from a `.env` file and can be modified to call the OpenAI API or even a local model by adjusting the endpoint and headers. The example script `chat.py` demonstrates a basic Turkish conversation assistant.

The correction behavior is defined in `groq_api.py` inside the `correct_text` function. The system prompt there expands slang words to their full forms. Changing this prompt alters how text is cleaned. For instance, instructing it to keep slang would return `slm naber` instead of the default `selam ne haber`.

## Requirements

Install dependencies using `pip install -r requirements.txt`.

### Limitations

- The assistant cannot browse the web or verify live data. All responses come
  from the underlying language model without external retrieval.
- Answers may be outdated or incorrect, so you should verify important
  information independently.
- The default `temperature` in `groq_api.py` is set to `0.3`, yielding more
  deterministic replies with minimal creative variation.

## License

This project is licensed under the [MIT License](LICENSE).


