Terraform Cloud Agent Python Environment Variables Package
========================

Little Note 8/11/22
----------------------

Hello!

Thank you for trusting me with handling this project. It has been a real honor and privilege getting to work on this during the summer. I have worked to the best of my abilities to practice the correct formatting and structure that I have learned during the duration of my internship. I hope that my work has been productive enough to be effective for you and takes a load off your back.

Best regards,

Garrett Pearson

Table of Contents
------------------------

``*`` TerraformCloud Directory

``*`` Imports used

``*`` Python version used

``*`` GitHub location

``*`` Teams location

``*`` License

``*`` Requirements

``*`` Makefile

``*`` conf.ini/conf.py

``*`` Functions

``*`` Classes

``*`` __main__

``*`` Problems + Where I'm stuck

Directory
-------------------------

``*`` DIRECTORY TREE:

::

| TerraformCloud
| ├── .vscode
|     └── settings.json
| ├── AgentDetails
|     ├── src
|     |   ├── __init__.py
|     |   ├── Agent.py
|     |   ├── FuLogJSON.py
|     ├── LICENSE
|     ├── pyproject.toml
|     ├── README.rst
|     └── setup.py
| ├── jsonfiles
| │   └── XXXDatacenterXXXX-Template.JSON
| ├── tests
| ├── venv
| ├── .gitignore
| ├── __main__.py
| ├── conf.ini
| ├── conf.py
| └── LICENSE
| └── Makefile
| └── MANIFEST.in
| └── README.rst
| └── requirements.txt

Directory Folders
---------------------------

**.vscode**:

``*`` Contains a ``settings.json`` file that ignores the git limit warning. Nothing much

**AgentDetails**:

``*`` The ``AgentDetails`` package is used to gather the needed environment variables to set the name and token for the TFC agent.

``*`` >> Contains the ``Agent`` class and ``LogJson`` function.

**jsonfiles**:

``*`` The ``jsonfiles`` folder holds the VLAN information for NDC Datacenter. **Contains sensitive data .gitignore**

``XXXDatacenterXXXX-Template.JSON`` (hopefully) gives the skeleton for future datacenter VLAN information

**tests**: The ``tests`` folder was **supposed** to be the folder to hold test files for ``Agent.py`` and ``FuLogJSON.py``

*unfortunately did not get to this part

**venv**: The ``venv`` folder contains a virtual environment that will be used as the Python Interpreter for this package. *Files are not listed in the directory tree because its a similar directory to a local machine

Imports
------------------------------

``ipaddress``: Used for converting host ips into networks for this project. ``ipaddress.IPv4Network`` specifically

``requests``: Used for API calls to get the TFC-Agent token

``datetime``: Used to get the user that created the TFC-Agent

``ConfigParser``: Used in the conf.py to translate data from the conf.ini "dictionary"

``setuptools``: Used for setup.py in ``~/TerraformCloud/AgentDetails``

**Other imports are native Python library packages**

Python Version
-------------------------------

Python ~=3.10.5 Make sure to set the ``PYTHONPATH`` to venv. Oracle Linux has 3.6.8 installed natively.

GitHub Link
-------------------------------

As of right now, full file is located in "Teams Location".

Teams Location
-------------------------------

On Microsoft Teams, go to IT - Automation/Platforms/Files/Terraform

This folder should contain the python package (``TerraformCloud``) as well as YAML runbook, Network Topology diagram,
and DPS document.

License
-------------------------------

``BSD 2-Clause "Simplified" License``

A permissive license that comes in two variants, the BSD 2-Clause and BSD 3-Clause. Both have very minute differences to the MIT license.

Requirements.txt
-------------------------------

Installs all ``imports`` in second section.

Makefile
-------------------------------

This ``Makefile`` should change the ``PYTHONPATH`` to the ``venv`` folder in this project.

It will also clean the pycache folder.

conf.ini/conf.py
-------------------------------

``conf.ini`` is essentially being treated as a dictionary in this project.
This file will store all sensitive information and when updating the info in the ``.ini``
file, the information is updated throughout the folder.

``conf.py`` acts as a translator/parser for the ``conf.ini`` file. Calling the variables in this file
will input the information from ``conf.ini``.

Functions
-------------------------------

**Using standalone function and classes per file in this project.**

``*`` ``FuLogJSON.py``

``log_json(host, ip, name, token)``: The parameters ``host``, ``ip``, ``name``, and ``token`` will be entered in through the main script.

``host`` == **Hostname** of machine

``ip`` == **IP address** of machine

``name`` == The **name** of the TFC-Agent being created. (Previously set in main script)

``token`` == The **token** of the TFC-Agent being created. (Also, previously set in main script)

This function should take all of the information given from the parameters to log all of the needed Agent environment variables details.

``log_json`` also calls for the ``Agent`` class ``set_log`` method to format the information into the JSON syntax

The JSON file is stored in a Windows File Server with a shared folder. The account used to log into this file server is SVC-MSSC

Classes
-------------------------------

``*`` ``Agent.py``

Used getter and setter methods to assign class attributes

``Agent.get_dc()`` (dc = 'Datacenter'): Used as a static method since it just needs a hostname and ip address to return the datacenter

``Agent.set_name()``

"TFC_AGENT_NAME" = "{``datacenter``}_{``block_allocation``}_{``agent_pool_id``}_{``agent_id``}"

Args within the method will retrieve the ``datacenter``, ``block_allocation``, ``agent_pool_id``, and ``agent_id`` data

``datacenter`` == ``Agent.get_dc``

``block_allocation``: Checks the second quartet of IP address and matches which allocation the quartet resides in within the specific datacenter

``agent_pool_id`` = {``datacenter[0:2]``}{``block_allocation[0:2]``}
(or the first two letters of datacenter and block allocation and combine them.

``agent_id``: Uses SMB protocol to read the agent log file in the Windows File Server. It will grab all listed agent ids already created
and adds +1 to the ID for the most recent creation.

``Agent.set_token()``

Only parameter for this method is ``ip``.

``set_token()`` is designed to get the agent pool ID through args similar to ``set_name()``.
The agent pool ID is used to get the proper Terraform API links to get the token for the TFC-Agent.
``set_token()`` will send a request for a new token based on the proper link, and parses through the JSON response to set
``self._token`` to the token portion of response.

``Agent.set_log()``

This method should be called after ``set_name()`` and ``set_token()`` were called.

``Parameters = (self, host, ip, name, token)``

In the main script, ``name`` and ``token`` should be filled out with ``get_name()`` and ``get_token()``
``get`` will acquire the previously set ``Agent`` attributes.

``set_log`` is designed to compile the information that was acquired through the previously ``set`` methods
and format it into the ``JSON`` syntax.

main.py
-------------------------------

``main.py`` is designed to set the Agent ``name``, ``token``, and ``log`` attributes first. Next, it will log the ``log`` attribute
to a Windows File Server. Finally it will return the ``name`` and ``token`` for the YAML runbook.

Problems "aka where I am stuck at"
-------------------------------

``ConfigParser`` issue:

SVC-MSSC password contains an illegal character for the parser. *push to change password without ``&``

``smbclient`` issue:

::

Traceback (most recent call last):
  File "Agent.py", line 6, in <module>
    import smbclient

``ModuleNotFoundError``: No module named ``'smbclient'``

Having import issues with this module, all required imports are in ``requirements.txt``.

Tried ``PYTHONPATH=/path/to/venv`` (venv contains the required imports) however, still getting errors

**extra notes**

``pip3 install -r requirements.txt`` will spit out HTTP errors if given only user privileges in Oracle Linux

``Makefile`` should configure everything for the ``venv`` folder. However, it will still not install packages

All imported packages should also be in the ``/venv/lib/python3.10/site-packages`` directory, but still having import issues
