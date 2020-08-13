import os
import re

from src import get_logger
from src.annict import Annict
from src.utils import get_today
from src.aws.sns import SNS

SNS_TOPIC = os.getenv("SNS_TOPIC_ARN")

logger = get_logger(__name__)

def handler(event, context):
    annict = Annict()

    programs: dict = annict.get_episodes()
    today_animes:dict = annict.get_stream_episode_specified_date(
        watch_date=get_specified_date(event),
        programs=programs
    )
    sns = SNS()
    sns.send_message(topic_arn=SNS_TOPIC, message=create_notify_message(today_animes))

def get_specified_date(event):
    is_matched = False

    if event.get('s_date'):
        # Only 0000-00-00 that is date.
        is_matched = re.match(r"\d{4}-\d{2}-\d{2}", event.get('s_date'))

    specified_date = event.get('s_date') if is_matched else get_today()

    logger.info(specified_date)
    return specified_date

def create_notify_message(animes:dict) ->str:

    if not animes:
        return "Occured unexpected response from graphql result."

    if not animes.get("episodes"):
        return "No stream episodes today. Got NO result."

    messages = ""
    for anime in animes.get("episodes"):
        message = f"""title: {anime.get('title')}
({anime.get('number')} 話 {anime.get('subtitle')})
時間: {anime.get('startedAt')}, 放送: {anime.get('channel')}
"""
        messages+=message

    logger.info(messages)
    return messages
