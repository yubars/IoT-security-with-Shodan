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

    
    # outList = []
    # for rowP in readerP:
    # 	print("HI")
    # 	readerS = csv.reader(t2)
    # 	#next(readerS)
    # 	for rowS in readerS:
    # 		print(f": {rowS[0]}")
    # 		if(rowP[0] == rowS[0]):
    # 			print("hello")
    # 			outList.append([rowP[0],rowP[1],rowP[2],rowP[3],rowS[2],rowS[3]])

#print(outList)
# with open('match.csv', 'w') as outFile:
# 	for ip, countryCode, proxyPort, proxyType, product, vendor in outList:
# 		outFile.write(f"{ip}, {countryCode}, {proxyPort}, {proxyType}, {product}, {vendor}")
# 		outFile.write("\n")
	# out.write(str(outFile))
    # with open('matched.csv', 'w') as outFile:
    # 	for rowP in readerP:
    # 		print("hello")
    # 		out = rowP[0]+rowP[1]
    # 		outFile.write(out)


# with open('matched.csv', 'w') as outFile:
# 	for rowP in readerP:
# 		for rowS in readerS:
# 			if (rowP[0] == rowS[0]):
# 				print(rowP[0])
# 				outFile.write(rowP)
# with open('proxy_IP_test.csv', 'r') as t1, open('shodan_IP_test.csv', 'r') as t2:
#     file_proxy = t1.readlines()
#     file_shodan = t2.readlines()         
# with open('matched1.csv', 'w+') as outFile:
# 	for lineP in file_proxy:
# 		for lineS in file_shodan:
# 			if(lineP.split(',')[0] == lineS.split(',')[0]):
# 				print(f"matched IP address are: {lineP.split(',')[0]}")
# 				outFile.write(lineP)