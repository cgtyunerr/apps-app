"""Project configurations."""

from pydantic import BaseModel, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class RedisSettings(BaseSettings):
    """Redis settings for the project.

    Attributes:
        HOST: Hostname of the redis server.
        PORT: Port number of the redis server.
    """

    model_config = SettingsConfigDict(env_prefix="_")

    HOST: str
    PORT: int

class DatabaseConfigurations(BaseModel):
    """Sql DB configurations class.

    Attributes:
        HOST: Database host
        PORT: Database port.
        USER: Database user.
        PASSWORD: Database password.
        NAME: Database name.
    """

    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str

    @computed_field
    def db_url(self) -> PostgresDsn:
        """Generate database URL.

        Returns:
                Database URL.
        """
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            path=self.NAME,
            port=self.PORT,
        )

class Settings(BaseSettings):
    """Setting for the project.

    Attributes:
        DB: DatabaseSettings.
        TOKEN: token for main service.
        BASE_URL: Backend URL.
    """
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    REDIS: RedisSettings
    DB: DatabaseConfigurations
    TOKEN: str
    BASE_URL: str

settings: Settings = Settings()