import smbclient
import conf as c
from AgentDetails.src import Agent as a


def log_json(host, ip, name, token):
    # Registers the credentials for the server
    smbclient.register_session(f'{c.wfs}', username=c.user, password=c.password)

    # Sets the agent information into json format to log
    a.Agent.set_log(a.Agent, host=host, ip=ip, name=name, token=token)

    # entry variable writes the info into json file
    entry = a.json.dumps(a.Agent.get_log(a.Agent))

    # Logging entry using SMB protocol
    with smbclient.open_file((f"{c.path}", "w")) as fd:
        fd.write(entry)
