import requests
import json

filename = 'abc.txt' #insert filename to read addresses from

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    address = f.read().splitlines()

outputtxfile = open('outputtx.txt', 'a') #writing transactions that happended

sum = 0

#Calling the API from EtherScan to return transactions from an address. Insert your APIKEY
for i in range(len(address)):
    payload = {'module': 'account', 'action': 'txlist', 'address': address[i], 'apikey': 'APIKEY'}  
    r = requests.get('https://api.etherscan.io/api', params=payload)
    print("This is address: ",i+1," of ",len(address))
    strr = "This is address: ",i+1," of ",len(address)
    outputtxfile.write(str(strr))
    transaction = r.json()
    for account in transaction['result']:
        sum = sum + int(account['value'])
        # Print or write specifics for your own needs
        print ("Account: ", account['from'] , " to ", account['to'], "value: ", account['value'] , "Ref Block Number: ", account['blockNumber'])
        string = "Account: ", account['from'] , " to ", account['to'], "value: ", account['value'] , "Ref Block Number: ", account['blockNumber'], "##"
        outputtxfile.write(str(string))

print ("The total sum of Transactions (ETH) in all addresses is:", (sum/1000000000000000000))
string2 = "The total sum of Transactions (ETH) in all addresses is:", (sum/1000000000000000000)
outputtxfile.write(str(string2))
outputtxfile.close()
