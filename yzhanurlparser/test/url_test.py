import unittest, sys
sys.path.append('..')
from lib.url import get_hostname, get_ip, get_info, get_country
from lib.ip import is_ip

class UrlTest(unittest.TestCase):
  url = 'https://www.163.com/news/article/I275S396000189FH.html'
  hostname = 'www.163.com'
  country_short = 'CN'

  def test_get_hostname(self):
    self.assertEqual(get_hostname(self.url), self.hostname)

  def test_get_ip(self):
    self.assertEqual(is_ip(get_ip(self.url)), True)

  def test_get_info(self):
    info = get_info(self.url)
    self.assertEqual(is_ip(info.ip), True)
    self.assertEqual(info.country_short, self.country_short)
  
  def test_get_country(self):
    self.assertEqual(get_country(self.url), self.country_short)