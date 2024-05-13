"""
This script defines a Python tool that retrieves records from CSV files stored in an Azure Blob Storage container.
The tool takes a SQL query as input and applies it to each CSV file in the container, returning the result as a pandas DataFrame.

Dependencies:
- promptflow (core, connections)
- pandas
- sqlalchemy
- azure.storage.blob (ContainerClient)
- azure.identity (DefaultAzureCredential)
- pandasql

Usage:
1. Import the necessary modules and functions.
2. Define the `my_python_tool` function, which takes a SQL query as input and returns the result as a string.
3. Create a token credential for authentication.
4. Create a `ContainerClient` object to connect to the Azure Blob Storage container.
5. List all the blobs in the container.
6. Iterate over each blob and perform the following steps:
   - Get the blob client for the current blob.
   - Download the blob data into a BytesIO object.
   - Read the CSV data from the BytesIO object into a pandas DataFrame.
   - Replace occurrences of the blob name in the query with the DataFrame.
   - Execute the SQL query using `pandasql` and store the result in `sql_output`.
7. Return the `sql_output` as the result of the function.

Note: This code assumes that the Azure Blob Storage container and the CSV files are properly configured and accessible.

"""

from promptflow.core import tool
from promptflow.connections import CustomConnection
import pandas as pd
from sqlalchemy import create_engine, text
from azure.storage.blob import ContainerClient
from azure.identity import DefaultAzureCredential
import pandas as pd
from io import BytesIO
import pandasql as ps

sas_token = "SAS Token here"

@tool
def my_python_tool(query: str) -> str:
    """
    Retrieve records from CSV files stored in an Azure Blob Storage container.

    Args:
        query (str): SQL query to apply to the CSV files.

    Returns:
        str: Result of the SQL query as a string.
    """

    token_credential = sas_token

    container = ContainerClient(
        account_url="https://stonvanderai826500209528.blob.core.windows.net",
        credential=token_credential,
        container_name='raw'
    )

    sql_output = "[]"
    blob_list = container.list_blobs()
    for blob in blob_list:
        print(blob.name + '\n')
        bc = container.get_blob_client(blob=blob.name)
        with BytesIO() as input_blob:
            bc.download_blob().download_to_stream(input_blob)
            input_blob.seek(0)
            df = pd.read_csv(input_blob, compression='infer', index_col=0, encoding='unicode_escape')
        try:
            # replace 
            query = query.replace(blob.name[:-4], "df") 
            sql_output_temp = ps.sqldf(query)
            sql_output = sql_output_temp.to_markdown()
        except:
            pass
    

    return sql_output