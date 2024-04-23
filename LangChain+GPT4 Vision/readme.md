# GPT4 with LangChain 4 Invoice details extraction

This code is designed to process images (specifically, invoices or receipts) using LangChain and the OpenAI `GPT-4 Vision` model. It takes an image file path as input, encodes the image into base64 format, and then uses the GPT-4 Vision model to extract relevant information from the image, such as the merchant name, transaction amount, date, and receipt/invoice number.

## Prerequisites

- Python 3.x
- OpenAI API key (set as an environment variable)
  
## Installation

Install the required dependencies using pip:
`!pip install langchain langchain_openai`

## Usage

1. Set your OpenAI API key as an environment variable (`OPENAI_API_KEY`).
2. Run the script and enter the file path of the image you want to process when prompted: `Enter image file path: `.
3. The script will process the image and print the extracted information in JSON format:

```json
{
  "Name": "Name of the merchant",
  "Amount": "Transaction amount with currency symbol",
  "Date": "Transaction date in DD-MM-YYYY format",
  "Receipt_num": "Receipt/invoice number"
}```
