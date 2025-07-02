[Initial Gas Pipeline Research Google Doc](https://docs.google.com/document/d/1xnalyqEvUIzcW3oRSh6Txkgu_wSJqYs9mLQUwdprk4M/edit?usp=sharing)

1. pipeline-data .csv files and corresponding images from source 1 and source 3 in "Analyzing Initial Datasets in Data Sources Spreadsheet" section in Google Doc
2. `dist_nearest_pipeline.py` - reads through .csv files in pipeline-data and identifies nearest pipeline
3. `filter_pipelines_by_state.py` - reads through .csv files in pipeline-data and filters pipelines by state
4. `gz_2010_us_040_00_500k.geojson` - state border data required for `filter_pipelines_by_state.py`
5. `load_pipeline_data.py` - loads and prepares data from source 1 and source 3 in "Analyzing Initial Datasets in Data Sources Spreadsheet" section in Google Doc
