# Computer Vision Projects

Welcome to my collection of computer vision projects! This repository showcases my work in computer vision, including image processing, object detection, OCR and image classification. Each project demonstrates my expertise in building computer vision models to solve real-world problems and tasks.

## Project Highlights

- **[Google Vision API for Logo detection](https://github.com/jahnvisikligar/Computer-Vision/tree/main/Google_Vision_API)**: This code utilizes the Google Vision API for logo detection. It processes an image file containing logos, annotating each detected logo with its description and confidence score. Additionally, it visualizes the detected logos by drawing bounding boxes around them using the provided vertices.
- **[OCR-Image identification](https://github.com/jahnvisikligar/Computer-Vision/tree/main/OCR_Image%20identification)**: This project aims to implement Optical Character Recognition (OCR) utilizing EasyOCR to extract text from a P&ID (Piping and Instrumentation Diagram) PDF. Additionally, it incorporates symbol detection using the YOLOv8 model to precisely identify symbols within the same document, showcasing a comprehensive approach to document analysis and information extraction.
- **[PaddleOCR+GPT3.5](https://github.com/jahnvisikligar/Computer-Vision/tree/main/PaddleOCR%2BGPT3.5)**: This code leverages PaddleOCR for Optical Character Recognition (OCR) to extract text from invoice or receipt images. The extracted text is then processed using Doctran along with LangChain library that utilizes OpenAI's GPT-3.5 model. Specific properties are defined, such as merchant name, transaction amount, date, and receipt number that are extracted from the document using Doctran's `ExtractProperty` functionality.
- **[LangChain+GPT4 Vision](https://github.com/jahnvisikligar/Computer-Vision/tree/main/LangChain%2BGPT4%20Vision)**: This approach utilizes the GPT-4 Vision model in combination with LangChain for extracting relevant information from invoice or receipt images. The code encodes the input image into base64 format and then invokes the GPT-4 Vision model to process the image. The model's response is parsed using a Pydantic model (`ImageInformation`) to extract specific details like the merchant name, transaction amount, date, and receipt/invoice number.

## Technologies Used

- GCP-Vertex AI
- TensorFlow
- Keras
- Pytorch
- Transformers
- LangChain


Feel free to explore each project and don't hesitate to reach out if you have any questions or feedback!
