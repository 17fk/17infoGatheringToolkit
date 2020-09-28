import sys
from requests import get


def honeypot(inp):
    api_key=''
    honey = 'https://api.shodan.io/labs/honeyscore/'+inp+'?key='+api_key
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write(' No information available' + '\n')
    if result:
        probability = str(float(result) * 10)
        sys.stdout.write(' Honeypot chances: ' + probability +'%\n')
