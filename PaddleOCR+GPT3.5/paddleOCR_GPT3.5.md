# PaddleOCR + GPT3.5
This code allows you to extract relevant information from invoice or receipt images using OCR + Doctran (OpenAI GPT-3.5 and LangChain)

## Prerequisites

- Python 3.x
- OpenAI API key (set as an environment variable)

## Installation

Install the required dependencies using pip:

- Doctran: !pip install doctran

- Working with paddleOCR
  
    installing PaddleOCR cpu version: `!pip install paddlepaddle`

    package installation: !pip install `paddleocr>=2.0.6" # 2.0.6` version is recommended

    Clone paddle OCR repo to get FONTS for visualization: `!git clone https://github.com/PaddlePaddle/PaddleOCR`

## Usage

1. Set your OpenAI API key as an environment variable (`OPENAI_API_KEY`).
2. Run the script and provide the image file path when prompted.
3. The script will use PaddleOCR to perform Optical Character Recognition (OCR) on the image and extract the text content.
4. The extracted text is then parsed using Doctran and OpenAI's GPT-3.5 model to extract relevant information such as the merchant name, transaction amount, date, and receipt/invoice number.
5. The extracted information will be printed in a dictionary format.
