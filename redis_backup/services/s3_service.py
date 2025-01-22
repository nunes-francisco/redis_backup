import boto3
from botocore.exceptions import NoCredentialsError


# TODO: Adicionar um teste para saber se o arquivo existe
class S3Service:
    def __init__(self, config, logger):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=config.aws.aws_access_key_id,
            aws_secret_access_key=config.aws.aws_secret_access_key,
        )
        self.bucket_name = config.aws.aws_bucket_name
        self.logger = logger

    def upload_file(self, file_path, s3_file_path):
        try:
            self.s3.upload_file(file_path, self.bucket_name, s3_file_path)
            self.logger.info(f"Upload bem-sucedido: {file_path} -> {s3_file_path}")
        except FileNotFoundError:
            self.logger.error(f"Arquivo não encontrado: {file_path}")
        except NoCredentialsError:
            self.logger.error("Credenciais AWS não encontradas")

    def download_file(self, s3_file_path, local_file_path):
        try:
            self.s3.download_file(self.bucket_name, s3_file_path, local_file_path)
            self.logger.info(
                f"Download bem-sucedido de S3: {s3_file_path} -> {local_file_path}"
            )
        except Exception as e:
            self.logger.error(f"Erro ao baixar do S3: {str(e)}")
            
    def get_upload_status(self):
        return self.s3.list_objects(Bucket=self.bucket_name)

    def get_download_status(self):
        return self.s3.list_objects(Bucket=self.bucket_name)
