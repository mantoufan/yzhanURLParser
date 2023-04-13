import unittest, sys
sys.path.append('..')
from lib.ip import is_ip, get_info, get_country

class UrlTest(unittest.TestCase):
  ip = '8.8.8.8'
  non_ip = '123'
  country_short = 'US'

  def test_is_ip(self):
    self.assertEqual(is_ip(self.ip), True)
    self.assertEqual(is_ip(self.non_ip), False)

  def test_get_info(self):
    info = get_info(self.ip)
    self.assertEqual(info.ip, self.ip)
    self.assertEqual(info.country_short, self.country_short)

  def test_get_country(self):
    self.assertEqual(get_country(self.ip), self.country_short)