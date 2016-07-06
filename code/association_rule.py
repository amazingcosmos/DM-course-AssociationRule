#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apriori
import preprocess

DATA_FILE = '../data/diagnosis.data'
OUTPUT_FILE = '../data/diagnosis.csv'
MIN_SUPPORT = 0.2
MIN_CONFIDENT = 0.6
MIN_LIFT = 3.0

# prepocess the original data file
preprocess.preprocess(DATA_FILE, OUTPUT_FILE)

# get the data_set from .csv file
data_set = apriori.load_dataset(OUTPUT_FILE)

# get frequent items and their support value
f, f_support = apriori.apriori(data_set, MIN_SUPPORT)

# generate the rules
rules = apriori.gen_rules(f, f_support, MIN_CONFIDENT, MIN_LIFT)
print len(rules)
