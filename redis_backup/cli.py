import click

from core.config import Config
from core.logging import setup_logging
from services.restore_service import RestoreService


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--provider",
    type=click.Choice(["aws", "oracle", "google", "nfs"]),
    required=True,
    help="Provedor de armazenamento para restauração.",
)


@click.option(
    "--timestamp",
    required=True,
    help="Timestamp do backup a ser restaurado (formato: YYYY-MM-DD_HH-MM-SS).",
)
def restore(provider, timestamp):
    config = Config()
    logger = setup_logging()
    restore_service = RestoreService(config, logger)
    restore_service.restore_redis_data(provider, timestamp)


cli.add_command(restore)

if __name__ == "__main__":
    cli()
