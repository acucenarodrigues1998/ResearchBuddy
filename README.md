# ResearchBuddy

ResearchBuddy is a powerful research assistant tool designed to streamline the process of finding and summarizing academic literature. Utilizing Google's advanced Gemini model and the SerpAPI for enhanced search capabilities, ResearchBuddy provides an efficient interface for researchers to access scholarly articles and extract meaningful insights.

## Features

- **Intelligent Query Processing**: Enter research topics to retrieve pertinent scholarly articles using SerpAPI.
- **Automatic Summarization**: Summarize the main points of research papers using Google's Gemini model.
- **Reference Management**: Extract and format citations automatically.
- **Flexible Web Interface**: An easy-to-use Streamlit-based web interface for seamless interaction with the tool.

## Installation

### Prerequisites

To use ResearchBuddy, you need to set up API keys for Google's Gemini model and SerpAPI. Sign up and generate your API keys at the following links:

- [Google AI](https://ai.google.dev/)
- [SerpAPI](https://serpapi.com/users/sign_up)

Once you have your API keys, store them in a `credentials.yaml` file in the project root directory.

### Setting up the Environment

You can set up the project using either `venv` or `conda` as your Python environment manager.

#### Using venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### Using conda:

```bash
conda create --name myenv python=3.8
conda activate myenv
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## Usage

Launch the application through your terminal using the command above, and input your query into the web interface. The tool processes your query using Google's Gemini and SerpAPI to provide a list of relevant articles, their summaries, and formatted references.

## Contributing

Contributions to ResearchBuddy are welcomed! Here’s how you can contribute:

- Report bugs and request features.
- Review and propose improvements to the code.
- Contribute directly by submitting bug fixes or new features via pull requests.

## License

ResearchBuddy is distributed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Python community for the robust libraries.
- Google for the Gemini AI model.
- SerpAPI for their search API services.
- All contributors to the ResearchBuddy project.
