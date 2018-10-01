# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 9. 28.
"""
import pandas as pd
from keras.activations import linear, tanh, relu
from keras.initializers import Zeros, lecun_normal, lecun_uniform, he_normal, he_uniform, glorot_normal, glorot_uniform
from keras.regularizers import l1, l2, l1_l2
from collections import OrderedDict

DATA_SET = 'data_set'
BATCH_SIZE = 'batch_size'
EPOCHS = 'epochs'
ACTIVATION = 'activation'
KERNEL_INITIALIZER = 'kernel_initializer'
BIAS_INITIALIZER = 'bias_initializer'
BIAS_REGULARIZER = 'bias_regularizer'
HIDDEN_LAYER = 'hidden_layer'
DROPOUT = 'dropout'
DROPOUT_RATE = 'dropout_rate'

# DATA_SET
ALL = 'all'
KOSPI = 'kospi'
KOSDAQ = 'kosdaq'

# ACTIVATION
LINEAR = 'linear'
TAHN = 'tahn'
RELU = 'relu'

# INITIALIZER
ZEROS = 'zeros'
LECUN_NORMAL = 'lecun_normal'
LECUN_UNIFORM = 'lecun_uniform'
HE_NORMAL = 'he_normal'
HE_UNIFORM = 'he_uniform'
GLOROT_NORMAL = 'glorot_normal'
GLOROT_UNIFORM = 'glorot_uniform'

# BIAS_REGULARIZER
NONE = 'none'
L1 = 'l1'
L2 = 'l2'
L1_L2 = 'l1_l2'

# HIDDEN_LAYER_NAME
NN3_1 = 'NN3_1'
NN3_2 = 'NN3_2'
NN3_3 = 'NN3_3'
NN3_4 = 'NN3_4'
DNN5_1 = 'DNN5_1'
DNN5_2 = 'DNN5_2'
DNN5_3 = 'DNN5_3'
DNN5_4 = 'DNN5_4'
DNN8_1 = 'DNN8_1'
DNN8_2 = 'DNN8_2'
DNN8_3 = 'DNN8_3'
DNN8_4 = 'DNN8_4'


def get_all():
    data = pd.read_csv('data/all.csv', parse_dates=['date'])
    return data


def get_kospi():
    data = None
    return data


def get_kosdaq():
    data = None
    return data


data_sets = {
    ALL: get_all(),
    KOSPI: get_kospi(),
    KOSDAQ: get_kosdaq(),
}

activations = {
    LINEAR: linear,
    TAHN: tanh,
    RELU: relu
}

initializers = {
    LECUN_NORMAL: lecun_normal(),
    LECUN_UNIFORM: lecun_uniform(),
    HE_NORMAL: he_normal(),
    HE_UNIFORM: he_uniform(),
    GLOROT_NORMAL: glorot_normal(),
    GLOROT_UNIFORM: glorot_uniform()
}

regularizers = {
    NONE: None,
    L1: l1(),
    L2: l2(),
    L1_L2: l1_l2()
}

hidden_layers = {
    NN3_1: [70],
    NN3_2: [80],
    NN3_3: [100],
    NN3_4: [120],
    DNN5_1: [100, 50, 10],
    DNN5_2: [100, 70, 50],
    DNN5_3: [120, 70, 20],
    DNN5_4: [120, 80, 40],
    DNN8_1: [100, 100, 50, 50, 10, 10],
    DNN8_2: [100, 100, 70, 70, 50, 50],
    DNN8_3: [120, 120, 70, 70, 20, 20],
    DNN8_4: [120, 120, 80, 80, 40, 40]
}


def get_data_set(data_set_name):
    data_set = data_sets[data_set_name]
    return data_set


def get_activation(activation_name):
    activation = activations[activation_name]
    return activation


def get_initializer(initializer_name):
    initializer = initializers[initializer_name]
    return initializer


def get_regularizer(regularizer_name):
    regularizer = regularizers[regularizer_name]
    return regularizer


def get_hidden_layer(hidden_layer_name):
    hidden_layer = hidden_layers[hidden_layer_name]
    return hidden_layer
