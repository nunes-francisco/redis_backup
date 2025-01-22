from core.config import Config
from core.logging import setup_logging
from services.restore_service import RestoreService
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()


@router.post("/restore")
def restore_redis_data(
    provider: str = Query(..., enum=["aws", "oracle", "google", "nfs"]),
    timestamp: str = Query(
        ...,
        description="Timestamp do backup a ser restaurado (formato: YYYY-MM-DD_HH-MM-SS)",
    ),
):
    config = Config()
    logger = setup_logging()
    restore_service = RestoreService(config, logger)

    try:
        restore_service.restore_redis_data(provider, timestamp)
        return {"message": f"Restauração iniciada com sucesso a partir de {provider}"}
    except Exception as e:
        logger.error(f"Erro ao restaurar backup: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao restaurar backup")
    

@router.get("/restore/status")
def get_restore_status(provider: str = Query(..., enum=["aws", "oracle", "google", "nfs"])):
    config = Config()
    logger = setup_logging()
    restore_service = RestoreService(config, logger)

    try:
        if provider == "aws":
            status = restore_service.get_s3_upload_status()
        elif provider == "oracle":
            status = restore_service.get_oracle_upload_status()
        elif provider == "google":
            status = restore_service.get_google_upload_status()
        elif provider == "nfs":
            status = restore_service.get_nfs_upload_status()
        status = restore_service.get_restore_status(provider)
        return {"message": status}
    except Exception as e:
        logger.error(f"Erro ao obter status da restauração: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter status da restauração")
