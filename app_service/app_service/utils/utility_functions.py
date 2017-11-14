from datetime import datetime
import pytz

def get_iso_date(date):
    try:
        return datetime.strptime(date, '%d-%B-%Y').strftime('%Y-%m-%d')
    except:
        return

def get_str_date(date):
    try:
        return date.strftime('%d-%B-%Y')
    except:
        return ''

def get_str_datetime(date):
    try:
        return utc_to_time(date).strftime('%d-%B-%y %X')
    except:
        return ''

