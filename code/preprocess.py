#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
from chardet import detect

DATA_FILE = '../data/diagnosis.data'
OUTPUT_FILE = '../data/diagnosis.csv'
HEAD = 'temp,nausea,lumbar,urine,micturition,urethra,inflammation,nephritis\n'

def preprocess(file_path):
    fp_read = open(file_path, 'r')
    fp_write = open(OUTPUT_FILE, 'w')
    fp_write.write(HEAD)
    for line in fp_read:
        content = line.strip().split()
        # print content
        output = []
        temp = float(content[0].replace(',', '.'))
        if temp < 38.0:
            output.append('0')
        else:
            output.append('1')
        for item in content[1:]:
            if item == 'yes':
                output.append('1')
            elif item == 'no':
                output.append('0')
        fp_write.write(','.join(output)+'\n')
    fp_read.close()
    fp_write.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        while not os.path.exists(file_path):
            file_path = raw_input('File not exist! Please enter the data file path:')
    else:
        file_path = DATA_FILE
    preprocess(file_path)