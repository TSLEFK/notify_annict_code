from datetime import datetime

from src.utils import get_datetime_aws_fromat, get_date_aws_fromat

def test_get_datetime_aws_fromat():
    event = {
        "time": "2020-04-28T10:00:20Z",
        "detail": {
        }
    }

    actual = get_datetime_aws_fromat(event.get("time"))
    expected = "2020-04-28 19:00:20"

    assert actual == expected

def test_get_date_aws_fromat():
    event = {
        "time": "2020-04-28T10:00:20Z",
        "detail": {
        }
    }

    actual = get_date_aws_fromat(event.get("time"))
    expected = "2020-04-28"

    assert actual == expected