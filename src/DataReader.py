#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'SenTR'

from Record import Record


class DataReader:

    @staticmethod
    def file_read(file_name):
        file = open(file_name)
        line = file.readline()
        while line:
            if len(line) < 10:
                line = file.readline()
                continue
            record = Record(line)
            print(record.beginTime)

            #再读一行
            line = file.readline()

DataReader.file_read("/Users/SenTR/PythonWorkSpace/MobHandlerProject/Data/20160615.log")
