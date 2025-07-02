import geopandas as gpd
import matplotlib.pyplot as plt
import os

def process_geojson(input_geojson_path, output_csv_path, output_image_path):
    """
    Loads a GeoJSON file, prints preview info, saves to CSV, and saves a map image.
    
    Args:
        input_geojson_path (str): Path to the input GeoJSON file.
        output_csv_path (str): Path to save the output CSV file.
        output_image_path (str): Path to save the map image.
    """
    # Create output directories if they don't exist
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Load GeoJSON file
    gdf = gpd.read_file(input_geojson_path)

    # Preview
    print(gdf.head())
    print("CRS:", gdf.crs)

    # Save to CSV
    gdf.to_csv(output_csv_path, index=False)
    print(f"Saved CSV to: {output_csv_path}")

    # Save plot as image
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax)
    plt.savefig(output_image_path)
    print(f"Saved image to: {output_image_path}")

# Call the function with your file paths
'''
process_geojson(
    input_geojson_path="../Downloads/Natural_Gas_Interstate_and_Intrastate_Pipelines_1_-6811572933051500569.geojson",
    output_csv_path="../Desktop/pipeline-data/source1.csv",
    output_image_path="../Desktop/pipeline-data/source1.png"
)
'''

process_geojson(
    input_geojson_path="../Downloads/NaturalGas_InterIntrastate_Pipelines_US_EIA_-8459149917124532102.geojson",
    output_csv_path="../Desktop/pipeline-data/source3.csv",
    output_image_path="../Desktop/pipeline-data/source3.png"
)
