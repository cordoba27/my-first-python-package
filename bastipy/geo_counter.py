import geopandas as gpd

def geo_counter(input_path:str):
    """A function that counts the features in a geographic data file.
      
    Parameters
    ----------
    input_path : str
        Path to local file.

    Returns
    -------
    feature_count
        Number of features in file.
    
    """
    data = gpd.read_file(input_path)

    feature_count = len(data)

    return feature_count
