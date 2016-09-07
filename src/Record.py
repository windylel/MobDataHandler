#!/usr/bin/python
# -*- coding: UTF-8 -*-19880528


class Record:

    def __init__(self, record_line):
        split_record_line(record_line)

    def split_record_line(self, record_line):
        record_dict = dict()
        params = record_line.split(',')
        for param in params:
            key_valus = param.split('=')
            key = key_valus[0]
            value = key_valus[1]

        print("Param:" + str(params))


def split_record_line(record_line):
    params = record_line.split(',')
    print('Param:' + str(params))

record = Record('1=1,2=2,3=3')
record = Record('1=1,2=2,3=3')