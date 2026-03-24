# AI-Powered-Code-Reviewer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?style=for-the-badge&logo=openai)
![Code Review](https://img.shields.io/badge/Code%20Review-Automated-orange?style=for-the-badge&logo=github)

An intelligent command-line tool that leverages OpenAI's powerful language models to perform automated code reviews for Python files. This tool helps developers identify potential bugs, improve code quality, ensure adherence to best practices, and enhance overall code readability.

## ✨ Features

*   **Automated Code Analysis**: Get instant feedback on your Python code.
*   **Bug Detection**: Identifies potential logical errors and common pitfalls.
*   **Style & Readability**: Provides suggestions for PEP 8 compliance and improved code clarity.
*   **Performance Insights**: Offers recommendations for optimizing code execution speed.
*   **Security Vulnerability Checks**: Highlights potential security risks in your codebase.
*   **Best Practices**: Guides developers towards robust design patterns and coding standards.
*   **Customizable**: Easily configure the OpenAI model, temperature, and max tokens for tailored reviews.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Wassely5/AI-Powered-Code-Reviewer.git
    cd AI-Powered-Code-Reviewer
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set your OpenAI API Key:**
    Ensure your OpenAI API key is set as an environment variable named `OPENAI_API_KEY`.
    ```bash
    export OPENAI_API_KEY="your_openai_api_key_here"
    ```
    (Replace `"your_openai_api_key_here"` with your actual key)

## 💡 Usage

To review a Python file, simply run the `code_reviewer.py` script with the path to your file:

```bash
python code_reviewer.py your_script.py
```

### Example:

```bash
python code_reviewer.py my_project/main.py --output review_results.txt --model gpt-4 --temperature 0.5
```

This command will review `my_project/main.py`, save the output to `review_results.txt`, use the `gpt-4` model, and set the sampling temperature to `0.5`.

## 📚 Project Structure

```
AI-Powered-Code-Reviewer/
├── code_reviewer.py      # Main script for AI-powered code review
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this tool.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Wassely5/AI-Powered-Code-Reviewer&type=Date)](https://star-history.com/#Wassely5/AI-Powered-Code-Reviewer&Date)
