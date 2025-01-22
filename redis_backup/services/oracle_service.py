import oci
from loguru import logger


class OracleCloudService:
    def __init__(self, config):
        self.config = config
        self.bucket_name = config.oracle.oracle_bucket_name

        # Configurar o cliente do Oracle Cloud
        # config = oci.config.from_file(
        #     file_location=None,
        #     profile_name=None,
        #     key_file=config.oracle.oracle_key_file,
        #     pass_phrase=None,
        # )

        config = oci.config.from_file(file_location="~/.oci/config", profile_name="DEFAULT")
        
        # self.client = oci.object_storage.ObjectStorageClient(config)
        
        self.client = oci.object_storage.ObjectStorageClient(config)
        self.namespace = self.config.oracle.oracle_namespace

    def upload_file(self, file_path, object_name):
        try:
            with open(file_path, "rb") as f:
                self.client.put_object(self.namespace, self.bucket_name, object_name, f)
            logger.info(
                f"Upload bem-sucedido para Oracle Cloud: {file_path} -> {object_name}"
            )
        except Exception as e:
            logger.error(f"Erro ao enviar para Oracle Cloud: {str(e)}")

    def download_file(self, object_name, local_file_path):
        try:
            response = self.client.get_object(
                namespace_name=self.namespace,
                bucket_name=self.bucket_name,
                object_name=object_name,
            )
            with open(local_file_path, "wb") as f:
                for chunk in response.data.raw.stream(
                    1024 * 1024, decode_content=False
                ):
                    f.write(chunk)
            logger.info(
                f"Restauração bem-sucedida do Oracle Cloud: {object_name} -> {local_file_path}"
            )
        except Exception as e:
            logger.error(f"Erro ao restaurar do Oracle Cloud: {str(e)}")

    def get_upload_status(self):
        return self.client.list_objects(
            namespace_name=self.namespace, bucket_name=self.bucket_name
        )

    def get_download_status(self):
        return self.client.list_objects(
            namespace_name=self.namespace, bucket_name=self.bucket_name
        )

    def delete_file(self, object_name):
        try:
            self.client.delete_object(
                namespace_name=self.namespace,
                bucket_name=self.bucket_name,
                object_name=object_name,
            )
            logger.info(f"Arquivo {object_name} excluído do Oracle Cloud")
        except Exception as e:
            logger.error(f"Erro ao excluir do Oracle Cloud: {str(e)}")

    def delete_bucket(self):
        try:
            self.client.delete_bucket(
                namespace_name=self.namespace, bucket_name=self.bucket_name
            )
            logger.info(f"Bucket {self.bucket_name} excluído do Oracle Cloud")
        except Exception as e:
            logger.error(f"Erro ao excluir do Oracle Cloud: {str(e)}")

    def delete_namespace(self):
        try:
            self.client.delete_namespace(namespace_name=self.namespace)
            logger.info(f"Namespace {self.namespace} excluído do Oracle Cloud")
        except Exception as e:
            logger.error(f"Erro ao excluir do Oracle Cloud: {str(e)}")  

    def get_namespace(self):
        return self.client.get_namespace(namespace_name=self.namespace)

    def get_bucket(self):
        return self.client.get_bucket(namespace_name=self.namespace, bucket_name=self.bucket_name)

    def get_object(self, object_name):
        return self.client.get_object(
            namespace_name=self.namespace,
            bucket_name=self.bucket_name,
            object_name=object_name,
        )
