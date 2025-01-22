from datetime import datetime

from services.google_service import GoogleCloudService
from services.nfs_service import NFSService
from services.oracle_service import OracleCloudService
from services.s3_service import S3Service


class BackupService:
    def __init__(self, config, redis_repository, logger):
        self.config = config
        self.redis_repository = redis_repository
        self.logger = logger

        # Inicializar os serviços de armazenamento com base nas configurações
        self.services = []
        if "aws" in config.storage_providers:
            print("aws")
            self.services.append(S3Service(config, logger))
        if "oracle" in config.storage_providers:
            print("oracle")
            #self.services.redis_backupend(OracleCloudService(config))
        if "google" in config.storage_providers:
            print("google")
            #self.services.append(GoogleCloudService(config))
        if "nfs" in config.storage_providers:
            print("nfs")
            #self.services.redis_backupend(NFSService(config))

    def backup_redis_data(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.logger.info("Iniciando backup dos arquivos Redis")

        # Backup dos arquivos Redis para os serviços de armazenamento configurados
        rdb_file = self.redis_repository.get_rdb_file()
        rdb_backup_name = f"dump_{timestamp}.rdb"
        for service in self.services:
            service.upload_file(rdb_file, rdb_backup_name)

        aof_file = self.redis_repository.get_aof_file()
        aof_backup_name = f"redis_backupendonly_{timestamp}.aof"
        for service in self.services:
            service.upload_file(aof_file, aof_backup_name)

        self.logger.info("Backup concluído com sucesso")
