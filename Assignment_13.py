# Take tha last round of the https://www.cloudflare.com/en-gb/leagueofentropy/ services and convert them in a hex duo.
#After convert the hex duo in integer and modulo by 80
# Last check if the number is in the range of the https://api.opap.gr/draws/v3.0/1100/last-result-and-active last draw.

from urllib.request import Request, urlopen
import json

from numpy import append


# Get the last round of the https://www.cloudflare.com/en-gb/leagueofentropy/ services. 
# With this header the server will think that we are a browser
def get_round(): 
    req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = json.loads(data)
    round=data['round']
    return round

# Get the random number from the https://www.cloudflare.com/en-gb/leagueofentropy/ services.
def get_randomness(id):
    req = Request('https://drand.cloudflare.com/public/'+str(id), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = json.loads(data)
    randomness=data['randomness']
    return randomness

# Convert string into hex duo
def hex_str(randomness):
    hex_str=[randomness[i:i+2] for i in range(0, len(randomness), 2)]
    return hex_str

# Convert the hex duo in integer and modulo by 80
def convert_to_int(hex_str):
    int_str=int(hex_str,16)
    return int_str%80

# Get the last result of the https://api.opap.gr/draws/v3.0/1100/last-result-and-active   
def get_last_result(number):
    req = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = json.loads(data)
    last_result=data['last']['winningNumbers']['list']    
    if number in last_result:
        return True
    else:
        return False

last_round=get_round()
randomness=get_randomness(last_round)
hex_duo=hex_str(randomness)

int_list=[]
result_list=[]
new_list=[]

for i in hex_duo:
    int_duo=convert_to_int(i)
    print(i)
    # check if number is arleady in the list
    if int_duo not in int_list:
        new_list.append(int_duo)
        if get_last_result(int_duo):
            result_list.append(int_duo)
    # Add the number to the list to avoid duplicates
    int_list.append(int_duo)

# Sort the lists
int_list.sort()   
new_list.sort()
result_list.sort()

print("Round: "+str(last_round)+"\nRandomness: "+str(randomness)+"\nHexadecimal duo: "+str(hex_duo)+"\nIntegers: "+str(int_list))
print("Final List of Numbers:"+str(new_list)+"\nNumbers of list in the last draw: "+str(result_list))
