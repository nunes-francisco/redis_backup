import os
import shutil

from loguru import logger


class NFSService:
    def __init__(self, config):
        self.backup_path = config.nfs_backup_path

    def upload_file(self, file_path, object_name):
        try:
            destination = os.path.join(self.backup_path, object_name)
            shutil.copy2(file_path, destination)
            logger.info(f"Backup bem-sucedido em NFS: {file_path} -> {destination}")
        except Exception as e:
            logger.error(f"Erro ao realizar backup em NFS: {str(e)}")

    def download_file(self, object_name, local_file_path):
        try:
            source = os.path.join(self.backup_path, object_name)
            shutil.copy2(source, local_file_path)
            logger.info(
                f"Restauração bem-sucedida de NFS: {source} -> {local_file_path}"
            )
        except Exception as e:
            logger.error(f"Erro ao restaurar do NFS: {str(e)}")

    def get_upload_status(self):
        return os.listdir(self.backup_path)

    def get_download_status(self):
        return os.listdir(self.backup_path)

    def delete_file(self, object_name):
        try:
            os.remove(os.path.join(self.backup_path, object_name))
            logger.info(f"Arquivo {object_name} excluído do NFS")
        except Exception as e:
            logger.error(f"Erro ao excluir do NFS: {str(e)}")

    def delete_folder(self):
        try:
            shutil.rmtree(self.backup_path)
            logger.info(f"Pasta {self.backup_path} excluída do NFS")
        except Exception as e:
            logger.error(f"Erro ao excluir a pasta do NFS: {str(e)}")

    def delete_bucket(self):
        try:
            shutil.rmtree(self.backup_path)
            logger.info(f"Pasta {self.backup_path} excluída do NFS")
        except Exception as e:
            logger.error(f"Erro ao excluir a pasta do NFS: {str(e)}")

    def create_bucket(self):
        try:
            os.makedirs(self.backup_path)
            logger.info(f"Pasta {self.backup_path} criada no NFS")
        except Exception as e:
            logger.error(f"Erro ao criar a pasta do NFS: {str(e)}")

    def create_folder(self, folder_name):
        try:
            os.makedirs(os.path.join(self.backup_path, folder_name))
            logger.info(f"Pasta {folder_name} criada no NFS")
        except Exception as e:
            logger.error(f"Erro ao criar a pasta do NFS: {str(e)}")

    def delete_namespace(self):
        try:
            shutil.rmtree(self.backup_path)
            logger.info(f"Pasta {self.backup_path} excluída do NFS")
        except Exception as e:
            logger.error(f"Erro ao excluir a pasta do NFS: {str(e)}")

    def get_namespace(self):
        return os.listdir(self.backup_path)

    def get_bucket(self):
        return os.listdir(self.backup_path) 

    def get_object(self, object_name):
        return os.path.join(self.backup_path, object_name)

    def get_file_size(self, object_name):
        return os.path.getsize(os.path.join(self.backup_path, object_name))

    def get_folder_size(self, folder_name):
        return sum(
            os.path.getsize(os.path.join(folder_name, f))
            for f in os.listdir(folder_name)
            if os.path.isfile(os.path.join(folder_name, f))
        )

    def get_folder_size_recursive(self, folder_name):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_name):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def get_folder_count(self, folder_name):
        return sum(
            len(files)
            for r, d, files in os.walk(folder_name)
        )

    def get_folder_count_recursive(self, folder_name):
        return sum(
            1
            for r, d, files in os.walk(folder_name)
        )

    def get_file_count(self, folder_name):
        return sum(
            len(files)
            for r, d, files in os.walk(folder_name)
        )

    def get_file_count_recursive(self, folder_name):
        return sum(
            1
            for r, d, files in os.walk(folder_name)
        )

    def get_folder_files(self, folder_name):
        return os.listdir(folder_name)

    def get_folder_files_recursive(self, folder_name):
        return os.listdir(folder_name)
    