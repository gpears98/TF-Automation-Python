import socket
import AgentDetails.src.Agent as A
import AgentDetails.src.FuLogJSON as f
from AgentDetails.src.Agent import Agent as a


def main():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    a.set_name(A, host, ip)  # Sets Agent Name
    a.set_token(A, host, ip)  # Sets Agent Token
    f.log_json(host, ip, a.get_name(A), a.get_token(A))  # Sets and log agent environment variable info
    print(a.get_name(A))  # TFC_AGENT_NAME = ${a.get_name(A)}
    print(a.get_token(A))  # TFC_AGENT_TOKEN = ${a.get_token(A)}


if __name__ == '__main__':
    main()
