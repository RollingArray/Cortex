import logging
import logging.config
from pathlib import Path
from pathlib import Path

import yaml

from backend.core.config import settings


def configure_logging() -> None:
    
    Path("logs").mkdir(exist_ok=True)

    config_file = (
        Path("configs/logging")
        / f"{settings.environment.value}.yaml"
    )

    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)