# aryanglad-ultracore
realultracoreai

## OpenAI API Key Configuration

This project requires an OpenAI API key to function properly. Follow these steps to configure it:

### Quick Setup

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Add your API key:**
   Edit `.env` and replace `your-api-key-here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test the configuration:**
   ```bash
   python example_usage.py
   ```

### Alternative Methods

#### Method 1: Environment Variable
Set the environment variable directly:
```bash
export OPENAI_API_KEY=sk-your-actual-api-key-here
```

#### Method 2: .env File (Recommended)
Use the provided `.env` file for local development.

#### Method 3: Direct Initialization
```python
from openai import OpenAI
client = OpenAI(api_key="sk-your-actual-api-key-here")
```

### Security Notes

- Never commit your actual API key to version control
- The `.env` file is already added to `.gitignore`
- Use environment variables in production deployments
- Keep your API key secure and don't share it publicly

### Troubleshooting

If you encounter the error "The api_key client option must be set", ensure:
1. Your API key is valid and active
2. The environment variable is properly set
3. The `.env` file exists and contains the correct key
4. You've installed the required dependencies

### Getting an API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy the key and add it to your configuration
