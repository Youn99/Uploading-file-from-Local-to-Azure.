from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import sys
from sys import path
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

def Upload_file_on_Azure(connection_str,storage_account_name, container_name, local_file_name):
    """
    Upload_file_on_Azure function.
      it uploads file from local in Azure cloud.
    Parameter:
     connection_str => Your azure connection string.
     storage_account_name => The name of your azure storage account.
     container_name => the name of your container in azure.
     local_file_name => The path of your local file.
    Return:
     uploading to Azure Storage as blob + local file name.
    
    """
    upload_file_path = os.path.join(container_name, local_file_name)
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    blob_client = blob_service_client.get_blob_client(container=storage_account_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
