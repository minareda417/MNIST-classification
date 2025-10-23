# MNIST-classification
Lab 2 - introduction to machine learning

## Prerequistes
 - Python 3.11 or higher
 - Kaggle account with API token (if you want to run `data_extractor.py`)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/minareda417/MNIST-classification.git
   cd MNIST-classification
    ```
2. Create and activate a virtual environment:
   **Linux/MacOS:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) If you want to run `data_extractor.py`, set up your Kaggle API token:
   Go to [Kaggle Account Settings](https://www.kaggle.com/account)
   Scroll to the "API" section
   Click "Create New API Token" - this downloads `kaggle.json`
   Place the file in the correct location:

   **Linux/macOS:**
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

   **Windows:**
   ```bash
   mkdir %USERPROFILE%\.kaggle
   move %USERPROFILE%\Downloads\kaggle.json %USERPROFILE%\.kaggle\
   ```

   **Extract the data:**
   ```bash
   python data_extractor.py
   ```

5. Install Pytorch by following the instructions at [PyTorch Get Started](https://pytorch.org/get-started/locally/) based on your system configuration and your CUDA version.


