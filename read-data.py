import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers


# Load the dataset
Higgs_dataset = pd.read_csv("../Higgs-ML-data/atlas-higgs-challenge-2014-v2.csv.csv")


# Display the first few entries
Higgs_dataset.head()

# Display the last few entries
Higgs_dataset.tail()
