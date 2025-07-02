import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
from shapely import wkt

def distance_to_nearest_pipeline(csv_path, site_lat, site_lon):
    """
    Computes the distance (in meters) from a site to the nearest pipeline segment,
    and returns info about that pipeline.

    Args:
        csv_path (str): Path to the CSV file with pipeline geometries.
        site_lat (float): Latitude of the site.
        site_lon (float): Longitude of the site.

    Returns:
        dict: Information about the nearest pipeline, including FID and distance.
    """

    # Step 1: Read the CSV into a DataFrame
    df = pd.read_csv(csv_path)
    df = df[df['geometry'].apply(lambda x: isinstance(x, str))].copy()

    df['geometry'] = df['geometry'].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')  # assuming WGS84

    # Step 3: Reproject to metric CRS for accurate distance (meters)
    gdf = gdf.to_crs(epsg=3857)

    # Step 4: Create site point and reproject it
    site_point = gpd.GeoSeries([Point(site_lon, site_lat)], crs='EPSG:4326').to_crs(epsg=3857)[0]

    # Step 5: Compute distance to each pipeline
    gdf['distance_m'] = gdf.geometry.distance(site_point)

    # Step 6: Identify closest pipeline
    closest = gdf.loc[gdf['distance_m'].idxmin()]

    # Step 7: Print and return relevant info
    pipeline_info = {
        "FID": closest["FID"],
        "TYPEPIPE": closest["TYPEPIPE"],
        "Operator": closest["Operator"],
        "Status": closest["Status"],
        "Shape_Leng": closest.get("Shape_Leng", None),
        "Distance_meters": round(closest["distance_m"], 2)
    }

    print("Closest pipeline info:")
    for key, val in pipeline_info.items():
        print(f"  {key}: {val}")
        return pipeline_info
    
csv_file = "pipeline-data/source1.csv"
lat = 29.65
lon = -94.60

info = distance_to_nearest_pipeline(csv_file, lat, lon)
print(f"\nClosest pipeline is FID {info['FID']} at {info['Distance_meters']} meters.")

csv_file = "pipeline-data/source3.csv"
lat = 29.65
lon = -94.60

info = distance_to_nearest_pipeline(csv_file, lat, lon)
print(f"\nClosest pipeline is FID {info['FID']} at {info['Distance_meters']} meters.")
