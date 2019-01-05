import requests
from pprint import pprint
import json

filename = 'addresses.txt'

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    data = f.read().splitlines()

# Break down text file in back of 20 for multibalance return
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# break down in lists of 20 each
Arraysplits = list(chunks(data, 20))

sum = 0
outputfile = open('output.txt', 'w')

#Calling the API for multi balance
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

print ("The total sum of Ether in all addresses is:", (sum/1000000000000000000))