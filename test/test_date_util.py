import unittest

import src.date_util as date_util


DATE_STRING = '22/12/2019T19:59:59.123456-0500'
CURRENT_FORMAT_STRING = '%d/%m/%YT%H:%M:%S.%f%z'

class DateUtilTest(unittest.TestCase):
    
    def test_convert_format_sunny_day(self):
        expected = 'Sunday, December 22, 2019, 07:59:59 PM'

        self._assert_convert_format(expected, DATE_STRING, CURRENT_FORMAT_STRING)

    def test_convert_format_empty_date_string_returns_none(self):
        self._assert_convert_format(None, '', CURRENT_FORMAT_STRING)

    def test_convert_format_none_date_string_returns_none(self):
        self._assert_convert_format(None, None, CURRENT_FORMAT_STRING)

    def test_convert_format_empty_current_format_string_returns_none(self):
        self._assert_convert_format(None, DATE_STRING, '')

    def test_convert_format_none_current_format_string_returns_none(self):
        self._assert_convert_format(None, DATE_STRING, None)

    def test_convert_format_format_and_date_do_not_match_returns_none(self):
        self._assert_convert_format(None, DATE_STRING, '%A, %B %d, %Y, %I:%M:%S %p')

    def _assert_convert_format(self, expected, date_string, current_format_string):
        result = date_util.convert_format(date_string, current_format_string)

        self.assertEqual(expected, result)
