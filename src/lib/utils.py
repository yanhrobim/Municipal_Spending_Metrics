from pathlib import Path

def get_path_to_file():
    """
    # This function will helps by pointing to and finding the folder: data_raw (scraping data).
    # It take all the files individually, and builds the path auttomatically.
    """

    current = Path(__file__) # Current path. (...src/lib)

    root = current.parent.parent.parent.parent.parent # Root of the project path. (municipal_spending_metrics/)

    path_scraping_data = root / "data" / "scraping" / "data_raw"
     
    return path_scraping_data