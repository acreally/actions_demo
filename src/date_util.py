'''
Module for various date functions.
'''


from datetime import datetime


FORMAT_STRING = '%A, %B %d, %Y, %I:%M:%S %p'


def convert_format(date_string, current_format_string):
    '''
        Convert a date string from its format to a standard format.
    '''
    if not date_string or not current_format_string:
        return None

    try:
        datetime_obj = datetime.strptime(date_string, current_format_string)
        return datetime_obj.strftime(FORMAT_STRING)
    except ValueError:
        return None
