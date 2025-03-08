# Chatbot.ai

## Overview

This project implements a legal chatbot designed to provide users with accessible and understandable legal information related to Indian law. The chatbot leverages the Google Gemini API to provide concise answers to legal queries. This version has been simplified to remove the vector database for easier setup and execution.

## Architecture

The chatbot uses a simplified architecture:

1.  **User Query:** The user inputs a legal question.
2.  **Query Agent:** This agent receives the user's query and directly uses the Google Gemini API to generate an answer.  The agent formulates a prompt to provide to Gemini.
3.  **Response to User:** The summarized answer is presented to the user.

*(The previous version used a vector database, but that has been removed for simplicity.)*

## Key Features

*   Directly uses the Google Gemini API for question answering.
*   Legal Knowledge is based on the Generative AI model.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd legal-chatbot
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment:**
    *   **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```

5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Set up environment variables:**

    *   You'll need a Google API key. Get one at [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey).
    *   Set the `GOOGLE_API_KEY` environment variable:

        *   **Linux/macOS:**
            ```bash
            export GOOGLE_API_KEY="your_google_api_key"
            ```
        *   **Windows:**
            ```bash
            set GOOGLE_API_KEY="your_google_api_key"
            ```

    *   **Alternatively,** you can create a `.env` file in the project root directory with the following content:

        ```
        GOOGLE_API_KEY=your_google_api_key
        ```
        And then load it in `config.py` using `python-dotenv`.

## Usage

1.  **Run the chatbot:**
    ```bash
    python src/main.py
    ```

2.  **Interact with the chatbot:**
    *   The chatbot will prompt you to enter your legal query.
    *   Type your question and press Enter.
    *   The chatbot will provide an answer based on the Google Gemini model.
    *   Type `exit` to quit the chatbot.

### Example Queries

*   "What are the steps involved in filing a lawsuit in India?"
*   "Explain the concept of corporate social responsibility in Indian law."
*   "What are the key provisions of the Companies Act, 2013?"
*   "What are the different types of taxes levied in India?"

## Challenges Faced

*   **Data Scarcity:** The chatbot relies entirely on the pre-existing knowledge of the Gemini model and does not ingest data source from PDF
*   **Hallucinations:**  Large language models can sometimes generate inaccurate or fabricated information.
*   **Reliance on LLM knowledge**: The bot does not extract from the PDF and relies on prior LLM training.

## Possible Improvements

*   **PDF integration:** Implement data ingest.
*   **Knowledge Graph Integration:** Building a knowledge graph to better represent legal concepts and relationships.
*   **Human-in-the-Loop:** Incorporating human review for high-stakes legal advice.
*   **GUI:** Creating a graphical user interface for a better user experience.

## Disclaimer

This chatbot provides information for informational purposes only and does not constitute legal advice. Consult with a qualified legal professional for legal advice.# Chatbot.ai
