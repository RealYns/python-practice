import unittest
from city_function import city_country

class TestNameCase(unittest.TestCase):

    def test_city_country(self):
        place = city_country('safi', 'morocco', 2000000)
        self.assertEqual(place, 'Safi, Morocco - Population 2000000')

if __name__ == "__main__":
    unittest.main()