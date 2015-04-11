from geopy.geocoders import Nominatim
import datetime

def getDate(full):
    date = (full.split(' '))[0].split('/')
    time = (full.split(' '))[1].split(':')
    if(int(time[0]) < 10):
        time[0] = "0" + time[0]

    date1 = date[2] + "-" + date[0] + "-" + date[1]
    time1 = time[0] + ":" + time[1] + ":" + time[2]
    pattern = "%Y-%m-%d %H:%M:%S"
    ans = datetime.datetime.strptime(date1 + ' ' + time1, pattern)
    return str(ans.strftime("%s"))

def getAddr(words):
    strnum = words[0]
    try:
        ind = words.index("OF")
        addrlist = words[ind+1:]
    except:
        addrlist = None

    if addrlist == None:
        #we need to handle corners
        strnum = ""
        addrlist = words[words.index("AND")+1:]

    strnam = "".join(str(e)+" " for e in addrlist)
    genaddr = strnum + " " + strnam + "Washington, DC"
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(genaddr)
    except:
        return None
    if location == None:
        return None

    return (location.latitude, location.longitude)

def getOffense(off):
    ret = [0, 0, 0, 0, 0, 0, 0, 0, 0]
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
        offsparce = getOffense(cm[3])

        outstr += "".join(str(e)+"," for e in offsparce)
        outstr += "\n"

        outputfile.write(outstr)

    inputfile.close()
    outputfile.close()

main()
