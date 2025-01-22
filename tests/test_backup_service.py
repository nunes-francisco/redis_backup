import unittest
from unittest.mock import MagicMock

from app.core.config import Config
from app.services.backup_service import BackupService


class TestBackupService(unittest.TestCase):
    def setUp(self):
        config = Config()
        self.s3_service = MagicMock()
        self.redis_repository = MagicMock()
        self.logger = MagicMock()
        self.backup_service = BackupService(
            config, self.s3_service, self.redis_repository, self.logger
        )

    def test_backup_redis_data(self):
        self.backup_service.backup_redis_data()
        self.s3_service.upload_file.assert_called()
        self.logger.info.assert_called_with("Backup concluído com sucesso")
