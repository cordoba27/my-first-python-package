import bastipy
import unittest

class TestFunction(unittest.TestCase):

  def test_functions(self):
    self.assertIsInstance(bastipy.geo_counter(input_path=r"C:\Users\bonvi\OneDrive - istari.ai GmbH\Paper Garfagnana\Data\firms_garfagnana.shp"), int)