import requests
import json

filename = 'abc.txt' . #Enter file name

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    address = f.read().splitlines()

outputtxfile = open('outputERC20.txt', 'a')

sum = 0

# Calling the API for transactions in address
for i in range(len(address)):
    payload = {'module': 'account', 'action': 'tokentx',
               'address': address[i], 'apikey': 'APIKEY'}
    r = requests.get('https://api.etherscan.io/api', params=payload)
    transaction = r.json()
    for account in transaction['result']:
        sum = sum + int(account['value'])
        print("Account: ", account['from'], " to ", account['to'], "value: ",
              account['value'], "Ref Block Number: ", account['blockNumber'])
        string = "Account: ", account['from'], " to ", account['to'], "value: ", account[
            'value'], "Ref Block Number: ", account['blockNumber'], "##"
        outputtxfile.write(str(string))

outputtxfile.close()
