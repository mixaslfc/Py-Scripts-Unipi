# Take tha last 20 rounds of the https://www.cloudflare.com/en-gb/leagueofentropy/ services and transform them in a text of hexadecimal strings.
# Also calculate the entropy of the string (https://en.wikipedia.org/wiki/Entropy_(information_theory)/) 

from urllib.request import Request, urlopen
import json
import math 

# Get the last round of the https://www.cloudflare.com/en-gb/leagueofentropy/ services. With this header the server will think that we are a browser
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

# Transform the random string in a hexadecimal string. First we need to encode the random string in utf-8 and then we convert it in hexadecimal.
def hex_str(randomness): 
    string=randomness.encode('utf-8')
    hex_str=string.hex()
    return hex_str
    

# Calculate the entropy of the text.
def entropy(hex_text):
    # Calculate the probability of each character in the text.
    probabilty=[ float(hex_text.count(c)/len(hex_text)) for c in set(hex_text) ]
    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in probabilty ])
    return entropy

                
# Set tha last round
last_round=get_round()
# print("Last round: "+str(last_round))

# Greate a list for the random number from the last 20 rounds
my_rounds=list(range(last_round-20,last_round+1))

text=''
# Get the random number from the last 20 rounds and transform it in a hexadecimal string and add it to the text
for r in my_rounds:
    randomness=get_randomness(r)
    hex_string=hex_str(randomness)
    text=text+hex_string
    # print("Round: "+str(r)+" Randomness: "+str(randomness)+" Hexadecimal string: "+hex_string)

# print()
# Print the text
print("Text: "+text)
print()
# Calculate the entropy of the text
print("Entropy: "+str(entropy(text)))

