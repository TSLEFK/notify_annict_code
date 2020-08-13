import freezegun
from src.main import get_specified_date, create_notify_message

def test_get_specified_date():
    event = {
        's_date': '2020-08-13'
    }

    actual = get_specified_date(event=event)
    expected = '2020-08-13'
    assert actual == expected

@freezegun.freeze_time('2020-08-12')
def test_get_specified_date_missed_format():
    event = {
        's_date': '2020/08/13'
    }

    actual = get_specified_date(event=event)
    expected = '2020-08-12'
    assert actual == expected

@freezegun.freeze_time('2020-08-12')
def test_get_specified_date_no_specify():
    event = {}

    actual = get_specified_date(event=event)
    expected = '2020-08-12'
    assert actual == expected

def test_create_notify_message():
    anime = {
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
    actual = create_notify_message(animes=anime)
    expected = "title: 衛宮さんちの今日のごはん\n(4 話 春野菜とベーコンのサンドイッチ)\n時間: 2018-04-01 21:00:00, 放送: ABEMA アニメ\n"
    assert actual == expected