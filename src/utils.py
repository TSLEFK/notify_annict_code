from datetime import datetime, timedelta, timezone, date

JST = timezone(timedelta(hours=9), 'JST')

def get_today() -> str:
    today = date.today()
    return today.strftime('%Y-%m-%d')


def get_datetime_aws_fromat(event_time: str) -> str:
    event_datetime = datetime.strptime(event_time, '%Y-%m-%dT%H:%M:%SZ')
    jst_event_datetime = event_datetime + timedelta(hours=9)

    return jst_event_datetime.strftime('%Y-%m-%d %H:%M:%S')

def get_date_aws_fromat(event_time: str) -> str:
    event_datetime = datetime.strptime(event_time, '%Y-%m-%dT%H:%M:%SZ')
    jst_event_datetime = event_datetime + timedelta(hours=9)

    return jst_event_datetime.strftime('%Y-%m-%d')