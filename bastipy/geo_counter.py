import geopandas as gpd
import os

def geo_counter(input_path:str=None):
    """A function that counts the features in a geographic data file.
      
    Parameters
    ----------
    input_path : str
        Path to local file. Defaults to exemplary file in package.

    Returns
    -------
    feature_count
        Number of features in file.
    
    """
    if input_path == None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(base_dir, "../data/NUTS_0.geojson")
    
    data = gpd.read_file(input_path)

    feature_count = len(data)

    return feature_count
