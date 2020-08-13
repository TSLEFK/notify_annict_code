from datetime import datetime
import os

from gql import gql, Client, AIOHTTPTransport

from src import get_logger
from src.utils import get_datetime_aws_fromat, get_date_aws_fromat

ENDPOINT = os.getenv("ANNICT_ENDPOINT", "https://api.annict.com/graphql")
ANNICT_TOKEN = os.getenv("ANNICT_TOKEN", "")

logger = get_logger(__name__)

class Annict:

    def __init__(self, url=ENDPOINT) -> None:
        headers = {
            "Authorization": f"Bearer {ANNICT_TOKEN}"
        }
        self.transport = AIOHTTPTransport(url=url, headers=headers)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def _execute_query(self, query_text: str) -> dict:
        query = gql(query_text)
        result = self.client.execute(query)
        return result

    def get_episodes(self):
        query = """
            query {
                viewer {
                    programs {
                        nodes {
                            work {
                                title
                            }
                            channel {
                                name
                            }
                            episode {
                                number
                                title
                            }
                            startedAt
                            rebroadcast
                        }
                    }
                }
            }
        """
        return self._execute_query(query_text=query)

    def get_stream_episode_specified_date(self, watch_date: str, programs: dict) -> dict:
        try:
            streams = programs["viewer"]["programs"]["nodes"]
        except KeyError as e:
            logger.error("query had no key programs or nodes.", extra={"viewer": programs['viewer']})
            # We should had notified to alert by 'Error' in log.
            # But I selected to notify by slack in same way with Annict notify.
            return {}

        if not streams:
            return {"episodes": []}

        episodes = []

        for stream in streams:
            if stream.get("rebroadcast", False):
                # I dont wanna watch rebroadcast anime.
                continue

            started_at = get_date_aws_fromat(stream.get("startedAt"))
            if watch_date == started_at:
                anime = stream.get("work")
                streamer = stream.get("channel")
                episode = stream.get("episode")

                stream = {
                    "title": anime.get("title"),
                    "number": episode.get("number", '0'),
                    "subtitle": episode.get("title", 'サブタイなし'),
                    "startedAt": get_datetime_aws_fromat(stream.get("startedAt")),
                    "channel": streamer.get("name")
                }

                episodes.append(stream)

        return {"episodes": episodes}
