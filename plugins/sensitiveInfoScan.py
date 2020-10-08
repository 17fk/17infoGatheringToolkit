import os

def sensitiveInfoScan(inp):
	status = os.system('sh plugins/uDork.sh ' + inp)