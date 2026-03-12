from __future__ import annotations

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    sportmonks_api_token: str
    default_timezone: str = "Europe/Istanbul"
    default_league_ids: tuple[int, ...] = ()


def _parse_league_ids(value: str | None) -> tuple[int, ...]:
    if not value:
        return ()
    result: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if part.isdigit():
            result.append(int(part))
    return tuple(result)


def get_settings() -> Settings:
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    sportmonks_api_token = os.getenv("SPORTMONKS_API_TOKEN", "").strip()

    if not telegram_bot_token:
        raise ValueError("TELEGRAM_BOT_TOKEN eksik. Railway Variables veya .env içine ekle.")
    if not sportmonks_api_token:
        raise ValueError("SPORTMONKS_API_TOKEN eksik. Railway Variables veya .env içine ekle.")

    return Settings(
        telegram_bot_token=telegram_bot_token,
        sportmonks_api_token=sportmonks_api_token,
        default_timezone=os.getenv("DEFAULT_TIMEZONE", "Europe/Istanbul").strip(),
        default_league_ids=_parse_league_ids(os.getenv("DEFAULT_LEAGUE_IDS")),
    )
