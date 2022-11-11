import uuid

from django.conf import settings
from django.core.files.storage import Storage
from azure.storage.blob import BlobServiceClient


def get_blob_with_name(container_name, blob_name):
    blob_service_client_instance = BlobServiceClient(
        account_url=settings.AZURE_CUSTOM_DOMAIN,
        credential=settings.AZURE_STORAGE_KEY_NAME)

    blob_client_instance = blob_service_client_instance.get_blob_client(
        container_name, blob_name, snapshot=None)

    blob_data = blob_client_instance.download_blob()
    data = blob_data.readall()
    return data


class AzureUpload(Storage):
    def __init__(self, container_name, option=None):
        self.container_name = container_name
        if not option:
            pass

    def _save(self, name, content):
        blob_service_client = BlobServiceClient.from_connection_string(settings.CONNECT_STR)
        content.open()

        content_str = content.read()
        uid = str(uuid.uuid4())
        blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=uid)

        blob_client.upload_blob(
            content_str
        )

        content.close()
        return uid

    def get_available_name(self, name, max_length=None):
        return name
