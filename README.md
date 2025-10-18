# aryanglad-ultracore
realultracoreai

## Setup Instructions

This server uses the OpenAI API and requires proper API key configuration.

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key (get one from [OpenAI Platform](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository** (if you haven't already)
   ```bash
   git clone <repository-url>
   cd aryanglad-ultracore
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

   **Alternative:** Set the environment variable directly:
   ```bash
   export OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

### Running the Server

```bash
python server.py
```

### Troubleshooting

**Error: "The api_key client option must be set"**

This error occurs when the OpenAI API key is not properly configured. To fix:

1. Make sure you've created a `.env` file with your API key
2. Or ensure the `OPENAI_API_KEY` environment variable is set
3. Verify your API key is valid and starts with `sk-`

**Error: "OpenAI API key not found"**

The server couldn't find the API key in your environment. Follow the configuration steps above.

### Security Notes

- Never commit your `.env` file or expose your API key
- The `.env` file is already in `.gitignore` to prevent accidental commits
- Keep your API key secure and rotate it if compromised
