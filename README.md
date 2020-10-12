# 17infoGatheringToolkit 



```
| .--------------. |#| .--------------. |#| .--------------. |#| .--------------. |#| .--------------. |#
| |     __       | |#| |   _______    | |#| |              | |#| |    ______    | |#| |  _________   | |#
| |    /  |      | |#| |  |  ___  |   | |#| |      |_|     | |#| |  .' ___  |   | |#| | |  _   _  |  | |#
| |    `| |      | |#| |  |_/  / /    | |#| |              | |#| | / .'   \_|   | |#| | |_/ | | \_|  | |#
| |     | |      | |#| |      / /     | |#| |      | |     | |#| | | |    ____  | |#| |     | |      | |#
| |    _| |_     | |#| |     / /      | |#| |      | |     | |#| | \ `.___]  _| | |#| |    _| |_     | |#
| |   |_____|    | |#| |    /_/       | |#| |      |_|     | |#| |  `._____.'   | |#| |   |_____|    | |#
| |              | |#| |              | |#| |              | |#| |              | |#| |              | |#
| '--------------' |#| '--------------' |#| '--------------' |#| '--------------' |#| '--------------' |#
 '----------------' #  '---------------' # '----------------' # '----------------' # '----------------' #
```

![License](https://img.shields.io/pypi/l/req)![Release](https://img.shields.io/badge/release-0.1.0-green)



### What you might need

- An account at https://shodan.io     take a look at **honeypot.py** and config api_key accordingly
- An account at https://larger.io     take a look at **detectTech.py** and config api_key accordingly
- An account at https://facebook.com    scan sensitive info needs Facebook account, detailed instruction below

 

### Features

- Censys.io info for IP address
- Detect the possibility of honeypot
- NSlookup
- Port scan
- IP reverse lookup
- Whois lookup
- Web technologies detection
- Scan sensitive information/file leaks in a website/uDork v2.0  (not working in China)
- [GitHub Sensitive Information Leakage / GSIL v2.0](https://github.com/FeeiCN/GSIL) 



### Usage

```shell
git clone https://github.com/17fk/17infoGatheringTools.git

cd 17infoGatheringTools

#pip3 install -r requirements.txt
pip install -r requirements.txt

#python3 17iGT
python 17iGT
```



### Scan senstive information instruction

The feature is pure uDork(https://github.com/m3n0sd0n4ld/uDork), more details can be found at the original repo. 

uDork is a script written in Bash Scripting that uses advanced Google search techniques to obtain sensitive information in files or directories, find IoT devices, detect versions of web applications, and so on.

uDork does NOT make attacks against any server, it only uses predefined dorks and/or official lists from exploit-db.com (Google Hacking Database: https://www.exploit-db.com/google-hacking-database).



Configure the cookie in uDork.sh is a **MUST!** Steps are listed here:

https://github.com/m3n0sd0n4ld/uDork#steps-to-obtain-the-cookie-and-configure-the-cookie

 

Modifications will be made in future releases.



**Sample:**

target.com -e pdf									//Example of searching pdf files

target.com -s password						//Example of searching routes with the word "password"



**Usage:**

```shell
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain or IP address.
  -e EXTENSION, --extension EXTENSION
                        Search files by extension. Use 'all' to find the list
                        extension.
  -t TEXT, --text TEXT  Find text in website content.
  -s STRING, --string STRING
                        Locate text strings within the URL.
  -m MASSIVE, --massive MASSIVE
                        Attack a site with a predefined list of dorks. Review
                        list <-l / - list>
  -l LIST, --list LIST  Shows the list of predefined dorks (Exploit-DB).
  -f FILE, --file FILE  Use your own personalized list of dorks.
  -k DORK, --dork DORK  Specifies the type of dork <filetype | intext | inurl>
                        (Required for '<-f / - file'>).
  -p PAGES, --pages PAGES
                        Number of pages to search in Google. (By default 5
                        pages).
  -o OUTPUT, --output OUTPUT
                        Export results to a file.
```



### Clarification

This toolkit is only for study purpose, all the features are implemented using free resources on the Internet.

Any suggestions would be much appreciate.



17Fk.

