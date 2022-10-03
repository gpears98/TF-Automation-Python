from configparser import ConfigParser
import os

# Reading conf.ini file
config = ConfigParser()
folder = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(folder, 'conf.ini')
config.read(file)

# Windows File Server
wfs = config.get('Server', 'host')
domain = config.get('Server', 'domain')
ipaddr = config.get('Server', 'ipaddr')
user = config.get('Server', 'user')
password = config.get('Server', 'password')
folder = config.get('Server', 'folder')
path = config.get('Server', 'path')

# JSON Files
ndzjson = config.get('JSONFiles', 'ndcdmzjson')
ncjson = config.get('JSONFiles', 'ndccorpjson')
ndvqjson = config.get('JSONFiles', 'ndcdevqajson')
nhjson = config.get('JSONFiles', 'ndchsecjson')
log = config.get('JSONFiles', 'agentlogjson')

# JSON Content
b = config.get('JSONContent', 'b')
bip = config.get('JSONContent', 'bip')
sbnn = config.get('JSONContent', 'sbnn')
sbn = config.get('JSONContent', 'sbn')
sbip = config.get('JSONContent', 'sbip')
v = config.get('JSONContent', 'v')
ipn = config.get('JSONContent', 'ipn')
vn = config.get('JSONContent', 'n')
vid = config.get('JSONContent', 'id')

# Subnet Mask
sub6 = config.get('SubnetMask', 'sub6')
sub9 = config.get('SubnetMask', 'sub9')
sub2 = config.get('SubnetMask', 'sub2')

# Datacenter Network Allocation
ndip = config.get('DCNtwkAlloc', 'ndip')
ncip = config.get('DCNtwkAlloc', 'ncip')
ndvqip = config.get('DCNtwkAlloc', 'ndvqip')
nhip = config.get('DCNtwkAlloc', 'nhip')

# Datacenter
n = config.get('Datacenters', 'n')
t = config.get('Datacenters', 't')
c = config.get('Datacenters', 'c')

# Datacenter Block IP
nblip = config.get('DCBlockList', 'nblip')
tblip = config.get('DCBlockList', 'tblip')
cblip = config.get('DCBlockList', 'cblip')

# Datacenter Allocation
nd = config.get('DCAlloc', 'nd')
nc = config.get('DCAlloc', 'nc')
ndvq = config.get('DCAlloc', 'ndvq')
nh = config.get('DCAlloc', 'nh')

# Agent pool Url
nhurl = config.get('PoolURL', 'nhurl')
ncurl = config.get('PoolURL', 'ncurl')
thurl = config.get('PoolURL', 'thurl')
tcurl = config.get('PoolURL', 'tcurl')
churl = config.get('PoolURL', 'churl')
ccurl = config.get('PoolURL', 'ccurl')

# Agent Pool
nhp = config.get('AgentPool', 'nh')
ncp = config.get('AgentPool', 'nc')
thp = config.get('AgentPool', 'th')
tcp = config.get('AgentPool', 'tc')
chp = config.get('AgentPool', 'ch')
ccp = config.get('AgentPool', 'cc')

# Agent Log
a = config.get('AgentLog', 'a')
an = config.get('AgentLog', 'an')
at = config.get('AgentLog', 'at')
aid = config.get('AgentLog', 'aid')
ad = config.get('AgentLog', 'ad')
dc = config.get('AgentLog', 'dc')
h = config.get('AgentLog', 'h')
add = config.get('AgentLog', 'add')
al = config.get('AgentLog', 'all')
avn = config.get('AgentLog', 'vn')
avid = config.get('AgentLog', 'vid')
ap = config.get('AgentLog', 'ap')
u = config.get('AgentLog', 'u')

# Functions
hosts = config.get('Functions', 'hosts')
ip = config.get('Functions', 'ip')

# Token API
todo = config.get('TokenAPI', 'todo')
header = config.get('TokenAPI', 'header')
