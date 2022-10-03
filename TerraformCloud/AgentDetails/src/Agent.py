import ipaddress
import socket
import json
import getpass
import requests
import smbclient
import conf as c
from collections import OrderedDict


class Agent:

    def __init__(self, name, token, log):
        self._name = name
        self._token = token
        self._log = log

    @staticmethod
    def get_dc():
        hostname = socket.gethostname()  # Gets hostname to get IP address
        ip = socket.gethostbyname(hostname)  # Gets IP address through hostname
        dc = []  # Datacenter list that will be filled in based on second quartet in the IP address
        #        **Should only be 1 datacenter when list is appended**

        #  Args to see which datacenter the host resides in
        while ip[3:6] in [c.nblip]:  # While the second quartet matches the range for this datacenter
            dc.append = c.n          # Append the dc variable to the matching datacenter
        else:
            pass

        while ip[3:6] in [c.tblip]:
            dc.append = c.t
        else:
            pass

        while ip[3:6] in [c.cblip]:
            dc.append = c.c
        else:
            pass

        return dc

    def set_name(self, ip):  # When filling this out use a.set_name(c.hosts, c.ip)
        dc = Agent.get_dc()
        alloc = []
        apid = []
        aid = []

        Agent.get_dc()  # Calls for the datacenter

        #            *-*-*-*check conf.py file to get c references*-*-*-*           #
        while dc is c.n:
            if ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nd)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nc)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.ndvq)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nh)
            else:
                print("Outside of internal network.")
                quit()

        #         This is to see which network allocation the vm belongs to         #
        #         Each datacenter has different ip addresses for allocations        #
        # If the vm is in this datacenter, and it's IP address fits in this network #
        #            Set the allocation instance to the allocation                  #

        apid.append = f'{dc[0:3]}{alloc[0:3]}'  # Ex Output: NDCO (NDC + CORP)

        # Registers the credentials for the server
        smbclient.register_session(f'{c.wfs}', username=c.user, password=c.password)

        with smbclient.open_file(f"{c.path}", "r") as f:  # Opening file
            file = json.load(f)

        list_components = []  # List to hold all current ID's

        for k in file.keys():  # Accessing all serial ID's already created in json log
            if file[k][c.aid] == 'comp':
                list_components.append(k)

        ids = [{v: k for k, v in enumerate(  # Adds 1 to the largest used ID
            OrderedDict.fromkeys(list_components))}
               [n] for n in list_components]

        aid.append = list(map(lambda x: str(x).zfill(4), ids))

        self._name = f'{dc}_{alloc}_{apid}_{aid}'

    def get_name(self):
        return self._name

    def set_token(self, ip):
        dc = Agent.get_dc()
        alloc = []
        apid = f'{dc[0:3]}{alloc[0:3]}'

        Agent.get_dc()  # Refer to line 49

        #            *-*-*-*check conf.py file to get c references*-*-*-*           #

        while dc is c.n:
            if ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nd)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nc)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.ndvq)
            elif ip in ipaddress.IPv4Network(f'{ip}/{c.sub6}'):
                alloc.append(c.nh)
            else:
                print("Outside of internal network.")
                quit()

        #         This is to see which network allocation the vm belongs to         #
        #         Each datacenter has different ip addresses for allocations        #
        # If the vm is in this datacenter, and it's IP address fits in this network #
        #            Set the allocation instance to the allocation                  #

        url = []  # Different agent pools have different url. This is checking to see which url.
        if c.nhp in apid:
            url.append = c.nhurl
        elif c.ncp in apid:
            url.append = c.ncurl
        elif c.thp in apid:
            url.append = c.thurl
        elif c.tcp in apid:
            url.append = c.tcurl
        elif c.chp in apid:
            url.append = c.churl
        elif c.ccp in apid:
            url.append = c.ccurl
        else:
            print('Invalid pool ID.')
            quit()

        # POST request for a new agent token
        response = requests.post(url, data=json.dumps(c.todo), headers=c.header)
        response.json()
        # To ensure the response is a valid response
        json_response = response.json() if response and response.status_code == 201 else None

        if json_response and 'data' in json_response:  # Parses through "data" in response for token
            for item in json_response:
                token = item.get('token')
                self._token = token  # sets the agent token attribute to the actual

    def get_token(self):
        return self._token

    def set_log(self, host, ip, name, token):
        network = ipaddress.IPv4Network(f'{ip}/{c.sub6}')
        file = []  # variables will be filled in through the arguments below
        dcnetwork = []
        vname = []
        vid = []

        Agent.get_dc()  # Again, look at line 49

        if ip in c.ndip:  # If ip address is in this ip network
            file.append(c.ndzjson)  # Append file variable to json directory
            dcnetwork.append = c.ndip  # Datacenter network appended
        elif ip in c.ncip:
            file.append(c.ncjson)
            dcnetwork.append = c.ncip
        elif ip in c.ndvqip:
            file.append(c.ndvqjson)
            dcnetwork.append = c.ndvqip
        elif ip in c.nhip:
            file.append(c.nhjson)
            dcnetwork.append = c.nhip
        with open(file, 'r') as x:
            load = json.load(x)  # Loading json file

        network_ip = []  # When appended, should hold the network ip that the address resides in

        for i in load[c.ipn]:  # Grabs all IP networks in file
            if ip in dcnetwork[i] is True:  # Host IP is in which network?
                for f in network:  # For IP network hosting the address
                    network_ip.append(f)  # Sets variable to the parsed IP network

        data = load[c.sbnn][c.v]  # Parses through json content

        while network_ip in data:  # Print name from matching network ips
            vname.append = data[c.vn]  # for logs
            vid.append = data[c.vid]

        self._log = [  # Agent info to log
            {
                f'{c.a}': {
                    f'{c.an}': name,
                    f'{c.at}': token,
                    f'{c.aid}': name[13:17],
                    f'{c.ad}': [
                        {
                            f'{c.dc}': Agent.get_dc(),
                            f'{c.h}': host,
                            f'{c.add}': ip,
                            f'{c.al}': name[4:8],
                            f'{c.avn}': vname,
                            f'{c.avid}': vid,
                            f'{c.ap}': f'{name[0:3] / name[4:8]}',
                            f'{c.u}': getpass.getuser()
                        }
                    ]
                }
            }
        ]

    def get_log(self):
        return self._log
