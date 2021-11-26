# load train and test files
# train algorithm
# save the matrices, params

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json

def train_and_evaluate(config_path):
    config_path = read_params(config_path)
    train_data_path = config_path["split_data"]["train_path"]
    test_data_path = config_path["split_data"]["test_path"]
    random_state =
    model_dir =
    alpha =
    l1_ratio =
    target =

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)


