import geopandas as gpd
import pandas as pd
from shapely import wkt
import os

def filter_pipelines_by_state(pipeline_csv_path, state_name, states_shapefile_path, output_csv_path):
    """
    Filters pipeline segments that intersect a given U.S. state.

    Args:
        pipeline_csv_path (str): Path to the CSV file with pipeline data (WKT geometry).
        state_name (str): Name of the U.S. state to filter by.
        states_shapefile_path (str): Path to the shapefile or GeoJSON of U.S. states.
        output_csv_path (str): Path to save the filtered pipeline CSV.
    """

    # Load pipeline data
    df = pd.read_csv(pipeline_csv_path)
    df = df[df['geometry'].apply(lambda x: isinstance(x, str))].copy()
    df['geometry'] = df['geometry'].apply(wkt.loads)
    pipeline_gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")

    # Load state boundaries
    states = gpd.read_file(states_shapefile_path)
    states = states.to_crs("EPSG:4326")  # ensure same CRS

    # Get the target state polygon
    target_state = states[states['NAME'].str.lower() == state_name.lower()]
    if target_state.empty:
        print(f"State '{state_name}' not found.")
        return

    state_geom = target_state.geometry.values[0]

    # Filter pipelines that intersect the state
    pipeline_gdf = pipeline_gdf[pipeline_gdf.intersects(state_geom)]

    # Save result
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    pipeline_gdf.to_csv(output_csv_path, index=False)
    print(f"Saved {len(pipeline_gdf)} pipeline segments to: {output_csv_path}")

pipeline_csv = "../Desktop/pipeline-data/source1.csv"
state_name = "Texas"
states_geojson = "../Desktop/gz_2010_us_040_00_500k.geojson"  # or shapefile .shp
output_csv = "../Desktop/pipeline-data/texas_pipelines.csv"

filter_pipelines_by_state(pipeline_csv, state_name, states_geojson, output_csv)
