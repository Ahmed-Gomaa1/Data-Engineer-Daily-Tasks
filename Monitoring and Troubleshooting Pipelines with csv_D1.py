import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename="pipeline.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Step 1: Extract
    logging.info("Extracting data...")
    data = pd.read_csv("netflix_titles.csv")
    logging.debug("Debugging info: Data columns are %s", data.columns)
    if data.empty:
        logging.warning("Extracted data is empty.")
    logging.info("Extraction successful!")
except FileNotFoundError:
    logging.error("Source file not found. Exiting.")
    exit()
except pd.errors.EmptyDataError:
    logging.error("Source file is empty. Exiting.")
    exit()

try:
    # Step 2: Transform
    logging.info("Transforming data...")
    data['date_added'] = pd.to_datetime(data['date_added'])
    cleaned_data = data.dropna()
    logging.info(f"Transformation complete! Rows before: {len(data)}, Rows after: {len(cleaned_data)}")
except KeyError as e:
    logging.error(f"KeyError during validation or transformation: {e}")
    exit()

try:
    # Step 3: Load
    logging.info("Loading data...")
    cleaned_data.to_csv("CleanedNetflix_titles.csv", index=False)
    logging.info("Data loaded successfully!")
except IOError as e:
    logging.error(f"I/O error during loading: {e}")
    exit()
