import re

dBm_list=[]

with open('RSS_File.txt', 'r') as t:
    for l in t:
        sp = l.split()
        for i in re.findall(r'\d+', sp[3]):
            dBm_list.append(int(i))
print("dBm List:",dBm_list)
average_in_list = sum(dBm_list)/len(dBm_list)
print("Total dBm:",len(dBm_list))
print("Average dBm:",average_in_list)