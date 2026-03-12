from __future__ import annotations

import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import get_settings
from handlers.analysis import analysis_command
from handlers.live import live_command
from handlers.matches import matches_command
from handlers.start import start_command
from handlers.stats import stats_command
from services.analysis_service import AnalysisService
from services.prediction_service import PredictionService
from services.sportmonks_api import SportMonksAPI

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Beklenmeyen hata oluştu:", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text("bir hata oluştu kanka, loglardan bakalım.")


def build_app() -> Application:
    settings = get_settings()
    sportmonks_api = SportMonksAPI(settings.sportmonks_api_token)
    analysis_service = AnalysisService(sportmonks_api)
    prediction_service = PredictionService()

    app = Application.builder().token(settings.telegram_bot_token).build()

    app.bot_data["settings"] = settings
    app.bot_data["sportmonks_api"] = sportmonks_api
    app.bot_data["analysis_service"] = analysis_service
    app.bot_data["prediction_service"] = prediction_service

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("maclar", matches_command))
    app.add_handler(CommandHandler("canli", live_command))
    app.add_handler(CommandHandler("analiz", analysis_command))
    app.add_handler(CommandHandler("istatistik", stats_command))
    app.add_error_handler(error_handler)

    return app


if __name__ == "__main__":
    application = build_app()
    application.run_polling(allowed_updates=Update.ALL_TYPES)
