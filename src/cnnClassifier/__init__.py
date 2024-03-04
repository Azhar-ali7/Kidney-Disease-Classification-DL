import os
import sys
import logging

# current time stamp, information level log, name of module (ex template.py), message about error
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create log folder
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# make dir
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,

    handlers=[
        # get file and print it out
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")


# why log here instead of creating a logger folder in src?
# if we do this from cnnClassifier import loogger it will still work because we already installer cnnClassifier as our local package in setup.py
# if we want to write logger file in logger folder then we have to import like this src.cnnClassifier.logger import logger