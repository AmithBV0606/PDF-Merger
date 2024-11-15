# PDF-Merger

This is a Python-based tool that merges multiple PDF files into a single PDF document. The project uses the `PyPDF2` library for handling PDF operations.

## Project Overview

This tool reads multiple PDF files from a specified list, merges them in the given order, and outputs a single combined PDF file.

## Prerequisites

1. **Python 3.6 or higher**: Make sure Python is installed on your system.
2. **PyPDF2 library**: This library is required to work with PDF files in Python.

## Setting Up the Project

### 1. Clone the Repository (optional)

If you have the code in a repository, you can clone it. Otherwise, download the code directly.

```bash
git clone <repository-url>
```

### 2. Install Required Libraries

Open a terminal, navigate to the project directory, and install the required libraries with:

```bash
pip install PyPDF2
```

### 3. Add Your PDF Files

Place the PDF files you want to merge in the project directory and ensure they are named according to the pdfiles list in the script, e.g. `1.pdf`, `2.pdf`, etc. 

You can also modify the pdfiles list(Array) in the code to specify different filenames if needed.

### 4. Run the Application

Run the PDF Merger tool by using:

```bash
python main.py
```

## Customization

- **Changing the List of PDFs:** Modify the `pdfiles` list in the code to specify which PDF files to merge and in what order.

- **Output Filename:** By default, the merged PDF is saved as `Merged.pdf`. You can change this by modifying the merger.write(`Merged.pdf`) line to a different filename.

## Usage

- The script will read the PDF files specified in the pdfiles list.

- It merges them in the listed order.

- The merged PDF is saved as Merged.pdf by default.