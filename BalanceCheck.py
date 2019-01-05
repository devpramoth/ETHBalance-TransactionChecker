import requests
from pprint import pprint
import json

filename = 'abc.txt' #insert file to read addresses from

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    data = f.read().splitlines()

# Break down text file in blocks of 20 for multibalance return. Etherscan allows 20 addresses for multibalance check
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# break down the addresses into lists of 20 each
Arraysplits = list(chunks(data, 20))

sum = 0
outputfile = open('balanceoutput.txt', 'w')  #log balances into a textfile

#Calling the API from EtherScan.io for multi balance check. Insert your APIKEY
for i in range(len(Arraysplits)):
    payload = {'module': 'account', 'action': 'balancemulti', 'address': Arraysplits[i], 'tag': 'latest', 'apikey': 'APIKEY'}  
    r = requests.get('https://api.etherscan.io/api', params=payload)
    print("These are addresses: ",i*20," to ",(i+1)*20)
    mybalance = r.json()
    for account in mybalance['result']:
        sum = sum + int(account['balance'])
        print (account)
        outputfile.write(str(account))

outputfile.close()

print ("Total ETH balance :", (sum/1000000000000000000))
