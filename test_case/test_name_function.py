import unittest
from name_function import *

class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py。"""

    def test_city_country(self):
        """传入简单的城市和国家可行吗？"""
        santiago_chile = city_country('santiago','chile')
        self.assertEqual(santiago_chile, 'Santiago Chile')
    def test_city_countrys(self):
        santiago_chile = city_countrys('santiago','chile',population=5000000)
        self.assertEqual(santiago_chile,'Santiago,Chile - population 5000000')

unittest.main()
