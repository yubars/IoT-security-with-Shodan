#This script first load proxy IP (collected from darknet/other sources) to the IoT IP collected from Shodan as seperate csv files.
#then it extract matched IPs between these two files as create a new csv file with these matched IPs
import csv
import pandas as pd
from time import sleep

with open('online_proxy.csv', 'r') as t1, open('shodan_IP_test.csv', 'r') as t2:
    readerP = csv.reader(t1)
    readerS = csv.reader(t2)
    proxy_file = list(readerP)
    shodan_file = list(readerS)
outList = []
i=0
k=0
for rowP in proxy_file:
    k=k+1
    print(k, i)
    for rowS in shodan_file:
        if(rowP[0] == rowS[0]):
            i=i+1
            outList.append([rowP[0],rowP[1],rowP[2],rowP[3],rowS[2],rowS[3]])

with open('matched_online.csv', 'w') as outFile:
   for ip, countryCode, proxyPort, proxyType, product, vendor in outList:
       outFile.write(f"{ip}, {countryCode}, {proxyPort}, {proxyType}, {product}, {vendor}")
       outFile.write("\n")

    
 
