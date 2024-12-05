import bastipy
import unittest
import os

class TestFunction(unittest.TestCase):

  def test_functions(self):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    self.assertIsInstance(bastipy.geo_counter(input_path=r"..\data\NUTS_0.geojson"), int)
