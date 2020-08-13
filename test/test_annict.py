from src.annict import Annict

def test_get_stream_episode_specified_date():
    episodes = {
        "viewer": {
            "programs": {
                "nodes": [
                    {
                        "work": {
                            "seasonName": "WINTER",
                            "seasonYear": 2018,
                            "title": "衛宮さんちの今日のごはん",
                            "viewerStatusState": "WATCHING"
                        },
                        "channel": {
                            "name": "ABEMA アニメ"
                        },
                        "episode": {
                            "number": 4,
                            "title": "春野菜とベーコンのサンドイッチ"
                        },
                        "startedAt": "2018-04-01T12:00:00Z",
                        "rebroadcast": False
                    }
                ]
            }
        }
    }

    annict = Annict(url="https://api.annict.com/graphql")
    actual = annict.get_stream_episode_specified_date(watch_date="2018-04-01", programs=episodes)

    expected = {
        "episodes": [
            {
                "title": "衛宮さんちの今日のごはん",
                "number": 4,
                "subtitle": "春野菜とベーコンのサンドイッチ",
                "startedAt": "2018-04-01 21:00:00",
                "channel": "ABEMA アニメ"
            }
        ]
    }

    assert actual == expected

def test_get_stream_episode_specified_date_if_get_unexpected_response():
    episodes = {
        "viewer": {}
    }

    annict = Annict(url="https://api.annict.com/graphql")

    actual = annict.get_stream_episode_specified_date(watch_date="2018-04-01", programs=episodes)
    assert actual == {}

def test_get_stream_episode_specified_date_if_get_no_episode():
    episodes = {
        "viewer": {
            "programs": {
                "nodes": []
            }
        }
    }

    annict = Annict(url="https://api.annict.com/graphql")

    actual = annict.get_stream_episode_specified_date(watch_date="2018-04-01", programs=episodes)
    assert actual == {"episodes":[]}