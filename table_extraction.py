

import pandas as pd
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def extract_and_convert_pdf_to_csv(pdf_file_path,result):
    # Extract key fields
    extracted_fields = {}
    key_mapping = {
        "invoice_number": "Invoice Number",
        "invoice_date": "Invoice Date",
        "Country": "Country",
        "seller_address": "Seller Address",
        "phone_number": "Phone No",
        "seller_taxid": "Seller TaxId",
        "po_number": "PO Number",
        "buyer_taxif": "Buyer TaxId",
        "seller_name": "Seller Name",
        "buyer_address": "Buyer Address"
    }
    for document in result.documents:
        for field_name, field_value in document.fields.items():
            new_field_name = key_mapping.get(field_name, field_name)
            extracted_fields[new_field_name] = field_value.value
    # Extract table data
    table_data = []
    table_rows = extracted_fields.get("table", [])
    for i, row in enumerate(table_rows):
        if hasattr(row, "value") and isinstance(row.value, dict):
            extracted_data = {key: field.content for key, field in row.value.items()}
            table_data.append(extracted_data)
        else:
            print(f"Skipping Row {i + 1} due to missing or invalid data.")

    # Convert table data to a DataFrame and return
    return pd.DataFrame(table_data)
