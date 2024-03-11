import random
import numpy as np


def no_local(size, sample):
    return random.choices(range(size), k=sample)


def x_ywork(size, sample, per_hwork, per_hpage):
    h_w = (100-per_hpage)/per_hpage
    h_w *= per_hwork/(100-per_hwork)
    w = np.ones(size)
    w[:round((size*per_hpage)/100)] = h_w
    return random.choices(range(size), weights=w, k=sample)


def loop(loopsize, size):
    ret = []
    i = 1
    while(loopsize*i < size):
        ret += range(loopsize)
        i += 1
    ret += range(size-(loopsize*(i-1)))
    return ret



