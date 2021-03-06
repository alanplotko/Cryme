from geopy.geocoders import Nominatim
import time
import datetime

addrdict = {}

def getDate(full):

	date = (full.split(' '))[0].split('/')
	time = (full.split(' '))[1].split(':')

	if(int(time[0])<10):
		time[0] = "0" + time[0]

	date1 = date[2] + "-" + date[0] + "-" + date[1]
	time1 = time[0] + ":" + time[1] + ":" + time[2]
	pattern = "%Y-%m-%d %H:%M:%S"
	ans = datetime.datetime.strptime(date1 + ' ' + time1, pattern)
	return str(ans.strftime("%s"))

def getAddr(words):
	ind = 0
	splitwords = ["OF", "AND", "UNDER", "OVER"]
	print(words)

	strnum = words[0]
	addrlist = None

	while(addrlist == None):
		for sw in splitwords:
			try:
				#we need to handle corners
				strnum = ""
				addrlist = words[words.index(sw)+1:]
				break
			except:
				addrlist = None

	if addrlist == None:
		return None

	strnam = "".join(str(e)+" " for e in addrlist)
	genaddr = strnum + " "+ strnam + "Washington, DC"
	
	try:
		ltuple = addrdict[genaddr]
	except:
		geolocator = Nominatim()
		try:
			location = geolocator.geocode(genaddr)
		except:
			return None
		if location == None:
			return None
		ltuple = (location.latitude, location.longitude)
		addrdict[genaddr] = ltuple
	return ltuple

def getOffense(off):
	ret = [0,0,0,0,0,0,0,0,0]
	possible = [
	"THEFT/OTHER",
	"THEFT F/AUTO",
	"ROBBERY",
	"BURGLARY",
	"MOTOR VEHICLE THEFT",
	"ASSAULT W/DANGEROUS WEAPON",
	"SEX ABUSE",
	"HOMICIDE",
	"ARSON"
	]
	for i in range(0, len(possible)):
		if(off == possible[i]):
			ret[i] = 1
	return ret


def main():
    inputfile = open('data/crime_data.csv')
    outputfile = open('data/crime_data_out.csv', 'w')
    i = 1 
    for line in inputfile:
        cm = (line).split(',')
        if(cm[0] == "CCN"):
            continue
        datetime = getDate(cm[1])
        addr = getAddr(cm[6].strip().split(' '))
        if(addr == None):
            #Address not found
            continue
        outstr = datetime + "," + str(addr[0]) + "," + str(addr[1])
        #offsparce = getOffense(cm[3])

        #outstr += "".join(str(e)+"," for e in offsparce)
        outstr += "\n"

        outputfile.write(outstr)
        print("Wrote line {0} of {1}.".format(i, 20000))
        i += 1

    inputfile.close()
    outputfile.close()

main()


