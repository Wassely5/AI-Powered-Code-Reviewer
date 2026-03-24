
import openai
import os
import argparse

# --- Configuration ---
# Set your OpenAI API key as an environment variable
# For example: export OPENAI_API_KEY="your_openai_api_key"
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# --- Constants ---
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 500

# --- Helper Functions ---
def read_file_content(filepath: str) -> str:
    """Reads the content of a given file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        exit(1)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        exit(1)

def generate_code_review_prompt(code_content: str, filename: str) -> str:
    """Generates a prompt for the AI code reviewer."""
    return f"""You are an expert software engineer tasked with reviewing code. 
Review the following Python code from file '{filename}'. 
Provide constructive feedback on:
1. Potential bugs or logical errors.
2. Code style and readability (e.g., PEP 8 compliance).
3. Performance improvements.
4. Security vulnerabilities.
5. Best practices and design patterns.
6. Suggestions for better documentation or comments.

Focus on actionable advice. Keep the review concise but comprehensive.

```python
{code_content}
```
"""

def get_ai_review(prompt: str, model: str = DEFAULT_MODEL, 
                  temperature: float = DEFAULT_TEMPERATURE, 
                  max_tokens: int = DEFAULT_MAX_TOKENS) -> str:
    """Sends the code review prompt to the OpenAI API and returns the review."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for code review."}, 
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except openai.error.AuthenticationError:
        print("Error: OpenAI API key is invalid or not provided. Please check your OPENAI_API_KEY.")
        exit(1)
    except openai.error.OpenAIError as e:
        print(f"Error communicating with OpenAI API: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during AI review: {e}")
        exit(1)

# --- Main Function ---
def main():
    parser = argparse.ArgumentParser(description="AI-Powered Code Reviewer for Python files.")
    parser.add_argument("filepath", type=str, help="Path to the Python file to review.")
    parser.add_argument("--output", "-o", type=str, 
                        help="Optional: Path to save the review output. If not provided, prints to console.")
    parser.add_argument("--model", "-m", type=str, default=DEFAULT_MODEL, 
                        help=f"OpenAI model to use (default: {DEFAULT_MODEL}).")
    parser.add_argument("--temperature", "-t", type=float, default=DEFAULT_TEMPERATURE, 
                        help=f"Sampling temperature (0.0 to 1.0, default: {DEFAULT_TEMPERATURE}).")
    parser.add_argument("--max_tokens", "-mt", type=int, default=DEFAULT_MAX_TOKENS, 
                        help=f"Maximum tokens for the AI response (default: {DEFAULT_MAX_TOKENS}).")

    args = parser.parse_args()

    print(f"\nReviewing code in: {args.filepath}")
    code_content = read_file_content(args.filepath)
    
    if not code_content:
        print("No content to review.")
        return

    prompt = generate_code_review_prompt(code_content, os.path.basename(args.filepath))
    review = get_ai_review(prompt, args.model, args.temperature, args.max_tokens)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(review)
            print(f"Code review saved to: {args.output}")
        except Exception as e:
            print(f"Error saving review to {args.output}: {e}")
    else:
        print("\n--- AI Code Review ---")
        print(review)
        print("\n----------------------")

if __name__ == "__main__":
    main()
