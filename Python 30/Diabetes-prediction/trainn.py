import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from numpy import loadtxt
from tensorflow.keras.models import Sequential, model_from_json # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore

