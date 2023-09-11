import json as j
client_information=open("client_information.json", "r")
client_information=j.load(client_information)
print(client_information)