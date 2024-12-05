import geopandas as gpd

def geo_counter(input_path):
    data = gpd.read_file(input_path)

    print(f"Your file contains {len(data)} features.")
