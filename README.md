
# Azure Form Extractor Training for Invoice Field Extraction

This repository contains tools and resources to help users train and utilize the Azure Form Recognizer service for extracting key fields and tables from invoices. Additionally, it includes best practices for labeling data to enhance the model's performance.

## Repository Structure

The repository contains the following components:

### 1. **Field Extraction Guide (`field_extraction.ipynb`)**

This notebook demonstrates how to extract specific fields from the results returned by the Azure Form Recognizer poller.  
- **Purpose**: Guides the user through parsing the JSON response from the Form Recognizer API to retrieve meaningful field data.  
- **Key Features**:  
  - Step-by-step instructions to interpret the poller's JSON response.  
  - Code to extract common invoice fields like invoice number, date, total amount, etc.  
  - Tips for handling optional or missing fields in the extracted data.

### 2. **Handling Tables in Invoices (`table_handling.ipynb`)**

This notebook focuses on managing tables extracted from invoices using the Azure Form Recognizer.  
- **Purpose**: Demonstrates how to process and structure the tabular data extracted from invoices.  
- **Key Features**:  
  - Parsing the table structure from the poller's results.  
  - Converting table data into usable formats like Pandas DataFrames or CSV files.  
  - Addressing challenges like merged cells, missing headers, or misaligned data.  

### 3. **Labeling Best Practices (`labeling_best_practices.ipynb`)**

A comprehensive guide for labeling documents to achieve better results with Azure Form Recognizer training.  
- **Purpose**: Provides best practices and tips for creating high-quality labeled datasets for training custom models.  
- **Key Features**:  
  - Guidelines on selecting representative training samples.  
  - Tips for accurately labeling fields and tables in complex documents.  
  - Common pitfalls to avoid during the labeling process.  
  - Recommendations on the optimal number of samples for training robust models.

## Prerequisites

- An active Azure subscription with access to the Form Recognizer service.
- Python environment with necessary dependencies installed (refer to the individual notebooks for library requirements).
- Access to labeled training documents (for custom model training).

## Getting Started

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/azure-form-extractor-training.git
   cd azure-form-extractor-training
   ```
2. Open the desired notebook in Jupyter Notebook or any compatible environment (e.g., VS Code, Google Colab).
3. Follow the instructions provided in each notebook to perform field extraction, table handling, or labeling.

## Additional Resources

- [Azure Form Recognizer Documentation](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/)
- [Quickstart: Train a Form Recognizer Model](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/)


