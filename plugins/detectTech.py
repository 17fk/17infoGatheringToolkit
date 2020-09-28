import sys
import json
from requests import get


def detectTech(url):

    api_key=''
    data = get('https://api.larger.io/v1/search/key/'+api_key+'?domain=' + url).text
    jsoned_data = json.loads(data)
    technologies = jsoned_data["apps"]
    techs =[]
    for element in technologies:
        if element['version']:
            techs.append(element['name']+":"+element['version'])
        else:
            techs.append(element['name'])
    for tech in techs:
        sys.stdout.write(tech+"\n")
