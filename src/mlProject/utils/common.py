# utility means helper functions or reusable functions
import os
from box.exceptions import BoxValueError # BoxValueError is used for type checking
from mlProject import logger # logger is used to log the information
import json # json is used for reading json files
import joblib # joblib is used for saving the model
from ensure import ensure_annotations # ensure is used for type checking
from box import ConfigBox # ConfigBox is used for type checking
from pathlib import Path # Path is used for file path
from typing import Any  # Any is used for type checking
import yaml

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json file

    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data from json file
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    Args:
        data (Any): data to be saved
        path (Path): path to binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: data from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data
    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path to file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
    