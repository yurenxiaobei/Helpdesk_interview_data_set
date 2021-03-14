#!/usr/local/bin/python3
# coding:utf-8

# ====================================================
# Author: Wenkel
# Last modified: 2021-3-14
# Filename: analysislog.py
# Description:analysis Helpdesk_interview_data_set
#设备名称: (deviceName)
#进程/服务名称: (processName)
#错误的原因（描述）(description)
#发生的时间（小时级），例如 0100-0200，0300-0400, (timeWindow)
#在小时级别内发生的次数 (numberOfOccurrence)
# ====================================================
import os
import sys
File_Path = r"D:\work\Helpdesk_interview_data_set"
Log_Path = os.path.join(File_Path,"Helpdesk_interview_data_set")
datas=[]
print (File_Path)
"""分析日志并截取出所需基础数据"""
with open(Log_Path,'r') as f:
    print (Log_Path)
    Log_data = f.readlines()
    try:
        for lines in Log_data:
            str_list={}
            listline1 = lines.split()
            str_list["deviceName"] = listline1[3]
            str_list["processName"] = listline1[5]
            str_list["timeWindow"] = listline1[2].split(':')[0]
            listline2 = lines.split('):')[-1]
            str_list["description"] = listline2
            datas.append(str_list)
        print (str (datas))

    except Exception as e:
            print(e)
"""按照要求输出小时级别设备发生故障次数"""
result=[]
analysislog_rs = []
for i in datas:
    if i not in result:
        result.append(i)
print ("告警数量按小时、主机、异常类型除重的个数：",len(result))
for i in result:
    count = datas.count(i)
    i["numberOfOccurrence"]=count
    print (i)
    analysislog_rs.append(i)
