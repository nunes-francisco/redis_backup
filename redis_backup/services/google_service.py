from google.cloud import storage
from loguru import logger


class GoogleCloudService:
    def __init__(self, config):
        self.client = storage.Client.from_service_account_json(
            config.google.google_credentials_file
        )
        self.bucket_name = config.google.google_bucket_name

    def upload_file(self, file_path, object_name):
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(object_name)
            blob.upload_from_filename(file_path)
            logger.info(
                f"Upload bem-sucedido para Google Cloud: {file_path} -> {object_name}"
            )
        except Exception as e:
            logger.error(f"Erro ao enviar para Google Cloud: {str(e)}")

    def download_file(self, object_name, local_file_path):
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(object_name)
            blob.download_to_filename(local_file_path)
            logger.info(
                f"Restauração bem-sucedida do Google Cloud: {object_name} -> {local_file_path}"
            )
        except Exception as e:
            logger.error(f"Erro ao restaurar do Google Cloud: {str(e)}")

    def get_upload_status(self):
        return self.client.list_blobs(self.bucket_name)

    def get_download_status(self):
        return self.client.list_blobs(self.bucket_name)

    def delete_file(self, object_name):
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(object_name)
            blob.delete()
            logger.info(f"Arquivo {object_name} excluído do Google Cloud")
        except Exception as e:
            logger.error(f"Erro ao excluir do Google Cloud: {str(e)}")

    def delete_bucket(self):
        try:
            bucket = self.client.bucket(self.bucket_name)
            bucket.delete()
            logger.info(f"Bucket {self.bucket_name} excluído do Google Cloud")
        except Exception as e:
            logger.error(f"Erro ao excluir do Google Cloud: {str(e)}")

    def create_bucket(self):
        try:
            bucket = self.client.create_bucket(self.bucket_name)
            logger.info(f"Bucket {self.bucket_name} criado no Google Cloud")
        except Exception as e:
            logger.error(f"Erro ao criar o bucket no Google Cloud: {str(e)}")