from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Whisper API"
    admin_api_key: str = "whisper_admin_test_12345"

    whisper_model: str = "base"
    device: str = "cpu"
    compute_type: str = "int8"

    free_limit: int = 50
    basic_limit: int = 50
    pro_limit: int = 2_000
    ultra_limit: int = 10_000
    mega_limit: int = 50_000


settings = Settings()