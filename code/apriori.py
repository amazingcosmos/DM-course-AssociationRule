#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

MIN_SUPPORT = 0.2
MIN_CONFIDENT = 0.6

def load_dataset(file_path):
    """Load dataset from preprocess csv file.

    Args:
        file_path: the path of preprocessed .csv file

    Returns:
        data_set: a list contain the transaction, each transaction is also list represent the feature number"""
    data_set = []
    # check if the file exist
    if not os.path.isfile(file_path):
        print('Dataset file is wrong!\n')
        return data_set
    fp = open(file_path, 'r')
    # ignore the first line, which is a representation of feature number
    fp.readline()
    for line in fp:
        content = line.strip()
        content = '[' + content + ']'
        data_set.append(list(eval(content)))
    fp.close()
    return data_set


def create_c1(data_set):
    """Create the 1-item set.

    Create the 1-item set that each item occurs in data_set.

    Args:
        data_set: a list contains all transactions, which represented by feature number.

    Returns:
        c1: the 1-item set."""
    c1 = []
    for transaction in data_set:
        for item in transaction:
            if [item] not in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)


def create_ck(fkk, k):
    """Create the k-item set.

    Create the k-item set from frequent (k-1)-item set 'fkk'.

    Args:
        fkk: frequent (k-1)-item set
        k: the k-th round indicator

    Returns:
        ck: candidate k-item set"""


def calc_surpport(ck, data_set, min_support = 0.7):
    """Find frequent set.

    Find the frequent k-item set 'fk' from the candidate k-item set 'ck' by calculating support that match min_support.

    Args:
        ck: candidate k-item set
        data_set: a list contains all transactions, which represented by feature number.
        min_support: the threshold of support that frequent item must match

    Returns:
        fk: frequent k-item set
        fk_support: the dictionary of each fk's support value"""
    num_transaction = float(len(data_set))
    fk = []
    fk_support = {}
    for candidate in ck:
        for transaction in data_set:
            if candidate.issubset(transaction):
                if candidate not in fk_support:
                    fk_support[candidate] = 1
                else:
                    fk_support[candidate] += 1
        fk_support[candidate] = float(fk_support[candidate]) / num_transaction
        if fk_support[candidate] < min_support:
            fk_support.pop(candidate)
        else:
            fk.insert(0, candidate)
    return fk, fk_support





if __name__ == '__main__':
    data_set = load_dataset('../data/diagnosis.csv')
    print 'data_set first 5 line:\n', data_set[:5]
    c1 = create_c1(data_set)
    print '\nc1:\n', c1
    f1, f1_support = calc_surpport(c1, data_set, MIN_SUPPORT)
    print '\nf1:\n', f1
    print '\nf1_support\n', f1_support