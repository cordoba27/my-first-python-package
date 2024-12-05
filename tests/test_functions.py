import bastipy
import unittest
import os

class TestFunction(unittest.TestCase):

  def test_functions(self):
    self.assertIsInstance(bastipy.geo_counter(input_path=r"data\NUTS_0.geojson"), int)
