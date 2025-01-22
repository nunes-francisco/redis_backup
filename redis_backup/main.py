import schedule
import uvicorn
from fastapi import FastAPI

from api.v1.endpoints import restore
from core.config import Config
from core.logging import setup_logging
from core.scheduler import Scheduler
from repositories.redis_repository import RedisRepository
from services.backup_service import BackupService

# Inicializar o FastAPI
redis_backup = FastAPI()

# Configurações e logger
config = Config()
logger = setup_logging()

# Inicializar o repositório Redis
redis_repository = RedisRepository(config)

# Inicializar o serviço de backup
backup_service = BackupService(config, redis_repository, logger)

# Agendar o backup para ser executado a cada hora
#schedule.every().hour.at(":00").do(backup_service.backup_redis_data)

# Iniciar o agendador
logger.info("Serviço de backup Redis iniciado...")
#Scheduler.start()

# Registrar a rota de restauração
redis_backup.include_router(restore.router, prefix="/api/v1")

# Função de inicialização do FastAPI
@redis_backup.on_event("startup")
async def startup_event():
    """Função de inicialização do FastAPI."""
    logger.info("Aplicação FastAPI iniciada")


# Função de encerramento do FastAPI
@redis_backup.on_event("shutdown")
async def shutdown_event():
    """Função de encerramento do FastAPI."""
    logger.info("Aplicação FastAPI encerrada")


def main():
    """Função principal para iniciar o servidor FastAPI."""
    uvicorn.run(
        "main:redis_backup", host="0.0.0.0", port=8000, reload=True
    )


# Executar o servidor FastAPI diretamente ao rodar o script
if __name__ == "__main__":
    main()
