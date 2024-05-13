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
def my_python_tool() -> str:

    token_credential = sas_token

    container = ContainerClient(
        account_url="https://stonvanderai826500209528.blob.core.windows.net",
        credential=token_credential,
        container_name='raw'
    )

    markdown = []

    blob_list = container.list_blobs()
    for blob in blob_list:

        print(blob.name + '\n')
        bc = container.get_blob_client(blob=blob.name)
        with BytesIO() as input_blob:
            bc.download_blob().download_to_stream(input_blob)
            input_blob.seek(0)
            df = pd.read_csv(input_blob, compression='infer', index_col=0, encoding='unicode_escape')
        markdown.append(f'### {blob.name}')
        
        query = f'SELECT * FROM df LIMIT 10;'
        markdown.append(ps.sqldf(query).to_markdown())
        markdown.append('\n')


    table_info = '\n'.join(markdown)
    table_info= table_info+ '\n---\nReturn the TSQL Query for:'


    return table_info