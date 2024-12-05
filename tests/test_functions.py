import bastipy
import unittest

class TestFunction(unittest.TestCase):

  def test_functions(self):
    self.assertIsInstance(bastipy.geo_counter(input_path="../data/NUTS_0.geojson"), int)