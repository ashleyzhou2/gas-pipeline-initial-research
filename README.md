[Initial Gas Pipeline Research Google Doc](https://docs.google.com/document/d/1xnalyqEvUIzcW3oRSh6Txkgu_wSJqYs9mLQUwdprk4M/edit?usp=sharing)

1. pipeline-data - .csv files and corresponding images from source 1 and source 3 in "Analyzing Initial Datasets in Data Sources Spreadsheet" section in Google Doc
3. `dist_nearest_pipeline.py` - Reads through .csv files in pipeline-data and identifies nearest pipeline
4. `filter_pipelines_by_state.py` - Reads through .csv files in pipeline-data and filters pipelines by state
5. `gz_2010_us_040_00_500k.geojson` - State border data required for `filter_pipelines_by_state.py`
6. `load_pipeline_data.py` - Loads and prepares data from source 1 and source 3 in "Analyzing Initial Datasets in Data Sources Spreadsheet" section in Google Doc
