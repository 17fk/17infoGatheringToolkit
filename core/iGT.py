import re
import sys
import requests


from plugins.whois import whois
from plugins.nsLookup import nsLookup
from plugins.portScan import portScan
from plugins.detectTech import detectTech
from plugins.honeypot import honeypot
from plugins.censys import censys
from plugins.reverseLookup import reverseLookup
from plugins.sensitiveInfoScan import sensitiveInfoScan

database = {
    '1': [censys, 'ip'],
    '2': [nsLookup, 'domain'],
    '3': [portScan, 'domip'],
    '4': [whois, 'domip'],
    '5': [honeypot, 'ip'],
    '6': [reverseLookup, 'ip'],
    '7': [detectTech, 'url'],
    '8': [sensitiveInfoScan, 'domain and arguments']
}

if sys.version_info < (3, 0):
    input = raw_input


def getInput(typ):
    if typ == 'domip':
        typ = 'domain or ip'
    inp = input('%s~: ' % (typ))
    return inp


def validate(inp, typ):
    if typ == 'ip':
        match = re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', inp)
        if match:
            return inp
        else:
            return False
    elif typ == 'url':
        if inp.startswith('http'):
            return inp
        else:
            try:
                requests.get('https://' + inp)
                return 'https://' + inp
            except:
                return 'http://' + inp
    else:
        return inp


def iGT(choice):
    if choice == '0':
        inp = getInput('all')
        for func in list(database.values()):
            try:
                func[0](inp)
                print (red + ('-' * 60) + end)
            except:
                pass
    else:
        typ = database[choice][1]
        inp = getInput(typ)
        validatedInp = validate(inp, typ)
        if validatedInp:
            plugin = database[choice][0]
            plugin(validatedInp)
        else:
            print (' Invalid input, press any key to go back')
