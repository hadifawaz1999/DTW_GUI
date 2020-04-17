import numpy as np
import os

def load_data(file_name):
    folder_path = "/media/hadi/laban/data_sets/UCRArchive_2018/"
    folder_path += (file_name + "/")
    train_path = folder_path + file_name + "_TRAIN.tsv"
    test_path = folder_path + file_name + "_TEST.tsv"
    if (os.path.exists(test_path) <= 0):
        print("File not found")
        return None, None, None, None
    train = np.loadtxt(train_path, dtype=np.float64)
    test = np.loadtxt(test_path, dtype=np.float64)
    ytrain = train[:, 0]
    ytest = test[:, 0]
    xtrain = np.delete(train, 0, axis=1)
    xtest = np.delete(test, 0, axis=1)
    return xtrain, ytrain, xtest, ytest