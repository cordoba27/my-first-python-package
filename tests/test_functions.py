import bastipy
import unittest
import os

class TestFunction(unittest.TestCase):

  def test_functions(self):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../data/NUTS_0.geojson")
    self.assertIsInstance(bastipy.geo_counter(input_path), int)
