import os
import pathlib

from pydantic import Field, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

# os.environ["NFS_BACKUP_PATH"] = "dummy"
#os.environ["ENVIRONMENT"] = "development"
#os.environ["AWS_ACCESS_KEY_ID"] = "12345sfsfegsa6546s4f6a"

env_file = [f for f in pathlib.Path().glob("**/*.env")][0]


class AWSConfig(BaseSettings):
    """Configurações do AWS"""

    aws_access_key_id: str = Field(..., env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: SecretStr = Field(..., env="AWS_SECRET_ACCESS_KEY")
    aws_bucket_name: str = Field(..., env="AWS_BUCKET_NAME")

    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class OracleConfig(BaseSettings):
    """Configurações do Oracle"""

    oracle_key_file: str = Field(..., env="ORACLE_KEY_FILE")
    oracle_bucket_name: str = Field(..., env="ORACLE_BUCKET_NAME")
    oracle_namespace: str = Field(..., env="ORACLE_NAMESPACE")

    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class GoogleConfig(BaseSettings):
    """Configurações do Google"""

    google_credentials_file: str = Field(..., env="GOOGLE_CREDENTIALS_FILE")
    google_bucket_name: str = Field(..., env="GOOGLE_BUCKET_NAME")

    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class NFSConfig(BaseSettings):
    """Configurações do NFS"""

    nfs_backup_path: str = Field(..., env="NFS_BACKUP_PATH")

    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class RedisConfig(BaseSettings):
    """Configurações do Redis"""

    redis_rdb_path: str = Field(..., env="REDIS_RDB_PATH")
    redis_aof_path: str = Field(..., env="REDIS_AOF_PATH")

    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class StorageProviders(BaseSettings):
    """Configurações do Storage Providers"""
    storage_providers: str = Field(default_factory=list, env="STORAGE_PROVIDERS") or ["aws", "oracle", "google", "nfs"]
 
    model_config = SettingsConfigDict(env_file=env_file, extra="allow")


class Config(BaseSettings):
    """Configurações do Redis"""
     
    redis: RedisConfig = RedisConfig()
    _providers: StorageProviders = StorageProviders()
    
    try:
        if "aws" in _providers.storage_providers.split(','):
            print("aws")
            #aws: AWSConfig = AWSConfig()
        if "oracle" in _providers.storage_providers.split(','):
            print("oracle")
            #oracle: OracleConfig = OracleConfig()
        if "google" in _providers.storage_providers.split(','):
            print("google")
            #google: GoogleConfig = GoogleConfig()
        if "nfs" in _providers.storage_providers.split(','):
            print("nfs")
            #nfs: NFSConfig = NFSConfig()

        model_config = SettingsConfigDict(env_file=env_file, extra="allow")

    except ValidationError as exc:
        model_config = SettingsConfigDict(env_file=env_file, extra="ignore")
        # print(repr(exc.errors()[0]['type']))
        # > 'extra_forbidden'
