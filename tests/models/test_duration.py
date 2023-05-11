from datetime import datetime, timedelta
from src.models.duration import Duration


def test_hours():
    now = datetime.now()
    assert Duration(now - timedelta(hours=4), now).hours() == 4
    assert Duration(now - timedelta(hours=4.3), now).hours() == 5
