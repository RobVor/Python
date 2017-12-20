# Application updates the 'hosts' files with redirects to block access to specific sites
# Paths for hosts are:
# MAC     - etc/hosts
# Linux   - etc/hosts
# Windows - C:\Windows\System32\drivers\etc\hosts

import platform, time, datetime

RedirHost = "127.0.0.1"

def GetHosts():
    if platform.system() == "Windows":
        HostsFile = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        HostsFile = r"/etc/hosts"
    return HostsFile

def GetSites():
    Sites = input("Please type in the sites you want to block separated by a semi-colon ';' \n")
    Web_List = "".join(Sites.split()).split(";")
    return Web_List

def GetTimes():
    Access_Times = []
    Times = input("Please type in the access times for allowed access to the sites listed above. \n"
                  "Note that the sites will be blocked when the current time falls inside the times listed here. \n"
                  "The format that you SHOULD use will be 'From - To';'From - To';'...' \n"
                  "Please note that multiple schedules are allowed and should be split by a semi-colon ';' \n"
                  "ie 08 - 13; 14 - 17 \n")
    Access_Times_All = "".join(Times.split()).split(";")
    for i in Access_Times_All:
        Access_Times.append(i.split("-"))
    return Access_Times

def CheckTime(Times):
    Check=[]
    TimeNow = datetime.datetime.now()
    TimeHour = TimeNow.strftime("%H")
    for i in Times:
        Check.append([int(j) for j in i])
    Times = Check

    for k in Times:
        if int(TimeHour) in range(k[0],k[1]):
            return "Blocked"

Sites = GetSites()
BlockedTimes = GetTimes()
NewContent = []

while True:
    try:
        Block_Unblock = CheckTime(BlockedTimes)
        if Block_Unblock == "Blocked":
            with open(GetHosts(),"r+") as Hosts:
                Content = Hosts.read()
                for Site in Sites:
                    if Site in Content:
                        pass
                    else:
                        Hosts.write(RedirHost+" www."+Site+".com"+"\n")
            Hosts.close()
        else:
            with open(GetHosts(),"r+") as Hosts:
                Content = Hosts.readlines()
                Hosts.seek(0)
                for l in Content:
                    if not any(Site in l for Site in Sites):
                        Hosts.write(l)
                Hosts.truncate()
        time.sleep(60)
    except InterruptedError:
        break