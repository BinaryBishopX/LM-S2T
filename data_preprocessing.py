# -*- coding: utf-8 -*-
"""Data Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oisot6ADPLlSLkiXnSKWweeShIVCjWDj
"""

import pandas as pd
import numpy as np

df = pd.read_csv('sample.tsv', sep="\t")

# read the data frame
df.head()

inps = df["path"] #X
outs = df["sentence"] #Y

"""# ***Output Preprocessing***"""

def RMChars(y): # Remove the special charachters
    chars = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':',
    ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}',
    '~'
]
    return ''.join(ch for ch in y if ch not in chars)

outs = np.array([RMChars(x) for x in outs]).astype(str)

outs

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences

# Create a tokenizer and fit it to the sentences.
tokenizer = Tokenizer()
tokenizer.fit_on_texts(outs)

# Convert the sentences to sequences of integers using the tokenizer.
outs = tokenizer.texts_to_sequences(outs)

print(outs)

#Pad sequences, having all same shape
outs = pad_sequences(outs)
print(outs)

