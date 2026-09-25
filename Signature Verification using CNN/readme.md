# Signature Verification using Convolutional Neural Networks

## Project Description
This project focuses on developing a Convolutional Neural Network (CNN) for the task of signature verification. The goal is to accurately classify signatures as either genuine or forged, a critical component in document authentication and security systems.

## Dataset Information
The project utilizes the **CEDAR Signatures dataset**, a widely recognized benchmark for signature verification tasks. The dataset structure is as follows:

*   `full_forg`: Contains 1320 forgery signatures (24 forgeries for each of 55 writers).
*   `full_org`: Contains 1320 genuine signatures (24 genuines for each of 55 writers).

**Data Preparation and Pre-processing:**

The dataset was split into training and validation sets with an 80:20 ratio. `ImageDataGenerator` was employed for image pre-processing and augmentation:

*   **Rescaling**: Pixel values were rescaled to the range [0, 1] by dividing by 255.
*   **Data Augmentation**: Applied to the training set to enhance generalization, including shear range (0.2), zoom range (0.2), and horizontal flip.
*   **Image Size**: Images were resized to `(150, 150)` pixels.

## Experimentation

Two main experiments were conducted to evaluate different model configurations.

### Experimentation 1 Output

**Parameters:**
*   Batch size: 32
*   Dense layer activation: `relu`
*   Overall activation functions: `relu`, `sigmoid`
*   Optimizer: Adam
*   Loss function: `binary_crossentropy`
*   Epochs: 10

**Results:**
*   Validation Loss: 43.29%
*   Validation Accuracy: 79.21%

### Experimentation 2 Output

**Parameters:**
*   Batch size: 32
*   Dense layer activation: `tanh`
*   Overall activation functions: `relu`, `sigmoid`
*   Optimizer: Adam
*   Loss function: `binary_crossentropy`
*   Epochs: 10

**Results:**
*   Validation Loss: 41.44%
*   Validation Accuracy: 82.12%

### Conclusion
Experimentation 2, utilizing `tanh` activation in the dense layer, demonstrated superior performance with a higher validation accuracy, indicating its effectiveness for this signature verification task.
