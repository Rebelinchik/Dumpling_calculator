from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")


def date():
    now = datetime.now()
    return now.strftime("%d %B %Y (%A)")
