# Take tha last 100 rounds of the https://www.cloudflare.com/en-gb/leagueofentropy/ services and transform them in a binary
# Also print the longest string of 0s and the longest string of 1s

from urllib.request import Request, urlopen
import json


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


# Transform the random string in a binary string. 
# First we convert every character to ASCII(orb(i)) and 
# then we convert it in binary(format- 08b|the b is converts the number to binary and 08 formats the number to eight digits zero-padded on the left).
# Last we join the binary string to a string.
def binary_str(randomness):
    b_str = ''.join(format(ord(i), '08b') for i in randomness)
    return b_str

# Calculate the longest string of 0s and the longest string of 1s
def longest_string(binary_str):
    # Find the longest string of 1s
    # First we split the string in a list of strings
    list_1s=binary_str.split('0')

    # Find the longest string of 0s
    # First we split the string in a list of strings
    list_0s=binary_str.split('1')

    # Then we find the longest string in the list
    lstring1s=max(list_1s, key=len)
    lstring0s=max(list_0s, key=len)
    return lstring1s,lstring0s


# Set tha last round
last_round=get_round()
# print("Last round: "+str(last_round))

text=''
# Greate a list for the random number from the last 100 rounds
my_rounds=list(range(last_round-10,last_round+1))
for r in my_rounds:
    randomness=get_randomness(r)
    b_string=binary_str(randomness)
    # print("Round: "+str(r)+" Randomness: "+str(randomness)+" Binary string: "+b_string)
    text=text+b_string

print()
print("Text: "+text)
print()
print("Longest string of 1s: "+longest_string(text)[0]+" Length: "+str(len(longest_string(text)[0])))
print("Longest string of 0s: "+longest_string(text)[1]+" Length: "+str(len(longest_string(text)[1])))

