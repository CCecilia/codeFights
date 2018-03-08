import ipaddress
inputString = "172.16.254.1"
inputString = "172.316.254.1"

def isIPv4Address(inputString):
	try: 
		ipaddress.ip_address(inputString)
	except ValueError: 
		return False	
	return True

isIPv4Address(inputString)