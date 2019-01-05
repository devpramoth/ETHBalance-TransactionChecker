import requests
from pprint import pprint
import json

filename = 'addressblock3.txt'

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    address = f.read().splitlines()

outputtxfile = open('outputtx3start.txt', 'a')
outputlogfile = open('outputlog3start.txt', 'a')

trx = list()
sum = 0

#Calling the API for transactions in address
for i in range(len(address)):
    payload = {'module': 'account', 'action': 'txlist', 'address': address[i], 'apikey': 'UDQYZ59SVS5WHH56JYTZA5WC9N6XEZW2GX'}  
    r = requests.get('https://api.etherscan.io/api', params=payload)
    print("This is address: ",i+1," of ",len(address))
    strr = "This is address: ",i+1," of ",len(address)
    outputtxfile.write(str(strr))
    transaction = r.json()
    trx.append(transaction)
    for account in transaction['result']:
        sum = sum + int(account['value'])
        print ("Account: ", account['from'] , " to ", account['to'], "value: ", account['value'] , "Ref Block Number: ", account['blockNumber'])
        string = "Account: ", account['from'] , " to ", account['to'], "value: ", account['value'] , "Ref Block Number: ", account['blockNumber'], "##"
        outputtxfile.write(str(string))

print ("The total sum of Transactions (ETH) in all addresses is:", (sum/1000000000000000000))
string2 = "The total sum of Transactions (ETH) in all addresses is:", (sum/1000000000000000000)
outputtxfile.write(str(string2))
outputtxfile.close()


outputlogfile.write(str(trx))
outputlogfile.close()
