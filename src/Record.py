#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Record:

    def __init__(self, record_line):
        self.beginTime = ""
        self.endTime = ""
        self.callingNumber = ""
        self.calledNumber = ""
        self.disconnectCause = ""
        self.answerDuring = ""
        self.alertStatus = ""
        self.split_record_line(record_line)

    def split_record_line(self, record_line):
        #record_dict = dict()
        print(record_line)
        params = record_line.split(',')
        for param in params:
            key_valus = param.split('=')
            key = key_valus[0]
            value = key_valus[1]
            if key == "btime":
                self.beginTime = value
            elif key == "etime":
                self.endTime = value
            elif key == "callingnum":
                self.callingNumber = value
            elif key == "callednum":
                self.calledNumber = value




'''
def split_record_line(record_line):
    params = record_line.split(',')
    print('Param:' + str(params))
'''
#record = Record("btime=20160615101642.474,etime=20160615101650.709,callingnum=02160405520,callednum=15601750196,disconncause=16,answerdur=0,alertstatus=1")