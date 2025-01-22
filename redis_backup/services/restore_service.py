from repositories.redis_repository import RedisRepository
from services.google_service import GoogleCloudService
from services.nfs_service import NFSService
from services.oracle_service import OracleCloudService
from services.s3_service import S3Service
from loguru import logger


class RestoreService:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        # Inicializar os serviços de armazenamento
        self.providers = {
            "aws": S3Service(config, logger),
            "oracle": OracleCloudService(config),
            "google": GoogleCloudService(config),
            "nfs": NFSService(config),
        }

    def restore_redis_data(self, provider_name, timestamp):
        if provider_name not in self.providers:
            logger.error(f"Provedor de armazenamento {provider_name} não suportado.")
            return

        service = self.providers[provider_name]
        rdb_backup_name = f"dump_{timestamp}.rdb"
        aof_backup_name = f"appendonly_{timestamp}.aof"

        rdb_local_path = self.config.redis_rdb_path
        aof_local_path = self.config.redis_aof_path

        self.logger.info(
            f"Restaurando backup de {provider_name} com timestamp {timestamp}"
        )

        service.download_file(rdb_backup_name, rdb_local_path)
        service.download_file(aof_backup_name, aof_local_path)

        self.logger.info("Restauração concluída com sucesso.")
        
    def get_s3_upload_status(self):
        return self.providers["aws"].get_upload_status()
    
    def get_oracle_upload_status(self):
        return self.providers["oracle"].get_upload_status()
    
    def get_google_upload_status(self):
        return self.providers["google"].get_upload_status()
    
    def get_nfs_upload_status(self):
        return self.providers["nfs"].get_upload_status()
