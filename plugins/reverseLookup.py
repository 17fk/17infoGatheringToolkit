import sys
from requests import get


def reverseLookup(inp):
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=' + inp
    try:
        result = get(lookup).text
        sys.stdout.write(result)
    except:
        sys.stdout.write(' Invalid IP address' )
