import shodan
import pandas as pd
from time import sleep

import warnings
warnings.filterwarnings("ignore")

SHODAN_API_KEY = "your shodan api key"
api = shodan . Shodan ( SHODAN_API_KEY )

query = "cisco router"

df = pd.DataFrame(columns=["product", "ip", "country", "port", "cve_name/exploits"])

try :
	print ('Searching exposed and exploted : {} in Shodan'. format ( query))
	
	# Search using Shodan API
	results = api . search ( query )
	print ('Total number of exposed devices are : {} '. format ( results ['total']))
	# print(len(results["matches"][0]))
	# print(type(results["matches"][0]))
	# print(len(results["matches"][0].keys()))
	for result in results ['matches']:
		#print(result.keys())
		product = query
		exploits = 0
		vulnerability = 0
		# data = result["data"]
		# print(type(data))
		# print(f"data_hey hey: {data}")
		# print(result)

		# Print IP, port and country for every obtained result
		print ('IP: {}'. format ( result ['ip_str'])) # The IP for each result is printed
		# print ( result [' data ']) # To print raw data for each result
		host = api . host ( result ['ip_str'])
		port = result ['port']
		#print(f"count: {len(result.keys())}")
		# product = result ['product']
		print(f"port: {port}")
		print(f"product: {product}")
		print ('- Country : {0}'. format ( host . get ('country_name', 'n/a')))
		print ('')
		sleep (1) # A 1- second delay is necessary to respect Shodan API restrictions
		
		#For each device IP , vulnerabilities and exploits are listed
		try :
			if str ( host . get ('vulns')) != 'None':
				print (' -------------------- Exploit list --------------------')
				exploit_list = []
				cve_name_list = []

				for vulnerability in host . get ('vulns'):
					exploits = api. exploits . search ( vulnerability )
					sleep (1)
					print ('Found {0} exploits for vulnerability "{1}" \n'. format (exploits .get ('total'), vulnerability ))
					exploits = exploits.get("total")
					exploit_list.append(exploits)
					cve_name_list.append(vulnerability)

				dict1 = {"product":product,"ip":result ['ip_str'], "country": host . get ('country_name', 'n/a'), "port":result ['port'],"cve_name/exploits": list(zip(cve_name_list, exploit_list))}
				df = df.append(dict1, ignore_index=True)
			else:
				dict1 = {"product":product,"ip":result ['ip_str'], "country": host . get ('country_name', 'n/a'), "port":result ['port'],"cve_name/exploits": 0}
				df = df.append(dict1, ignore_index=True)
			
		except (shodan . APIError, KeyboardInterrupt) as erro :
			print ('Error during exploit query : "{0}" '. format ( query ))
			print ('Shodan error : {0}'. format ( erro ))

except (shodan . APIError, KeyboardInterrupt) as e:
	print ('Error : {}'. format (e))
df.to_csv(f"{query}.csv", index=False)
