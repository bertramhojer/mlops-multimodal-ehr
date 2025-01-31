from pathlib import Path

import pydantic
import pydantic_settings
import torch

PROJECT_DIR: Path = Path(__file__).parent.parent.parent


class ProjectSettings(pydantic_settings.BaseSettings):
    """Base settings for client configurations."""

    model_config = pydantic_settings.SettingsConfigDict(extra="ignore", protected_namespaces=("settings_",))
    WANDB_PROJECT: str = "ModernBERTQA"
    WANDB_ENTITY: str = "mlops_55"
    WANDB_API_KEY: str = pydantic.Field(default="", description="Wandb API key")
    DEVICE: torch.device = torch.device(
        "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    GCP_REGION: str = "europe-north1"
    GCP_PROJECT_ID: str = "flash-rock-447808-n2"
    GCP_REGISTRY: str = "mlops-55"
    GCP_JOB: bool = False
    GCP_BUCKET: str = "mlops-55-bucket"


settings = ProjectSettings()  # type: ignore  # noqa: PGH003
