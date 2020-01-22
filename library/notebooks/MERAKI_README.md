MERAKI_README.md
----------------

Now for the Meraki SDK lab exercises! In our demo environment, Python 3 and the Meraki SDK have been installed in the Docker image.

Refer to the following links for information on learning resources on Cisco DevNet.

 - https://developer.cisco.com/meraki/
 - https://developer.cisco.com/meraki/api/#/python/guides/python-sdk-quick-start
 - https://developer.cisco.com/meraki/api/#/python/getting-started

Using the Jupyter Notebook, enter and execute these blocks of Python code to examine how to use the Meraki SDK.

Import the Meraki SDK (Python library). The API_KEY shown is a read only access into the Meraki demo environment.
```python
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException
x_cisco_meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
```
Instanciate an instance of the Python object.
```python
meraki = MerakiSdkClient(x_cisco_meraki_api_key)
```
In using the Meraki dashboard or API, you must first determine the numerical ID associated with the organizations associated with your account.
```python
orgs = meraki.organizations.get_organizations()
```
Review the list of organizations returned from the previous API call.
```python
organization_id = None

for org in orgs:
  print('{} {}'.format(org.get('id'), org.get('name')))  
  if org.get('name') == 'WWT':
      organization_id = org.get('id')
```
Review the help assocated with the Python method.

```python
help(meraki.organizations)
```
Query the devices associated with the selected organization.
```python
collect = dict()
collect['organization_id'] = organization_id
result = meraki.devices.get_organization_devices(collect)
```

Add error processing around the query.
```python
try:
    result = meraki.devices.get_organization_devices(collect)
except (APIException, ValueError) as e:
    print('Failed to return devices: {}'.format(e))
```

Specify a valid organization ID and issue the query again.
```python
collect['organization_id'] = '537758'
try:
    result = meraki.devices.get_organization_devices(collect)
except APIException as e:
    print('APIException: {}'.format(e))

print(result)
```
Save the Notebook and exit the notebook Kernal.

Review the sample Python code at [https://github.com/joelwking/devnet-sdk/blob/master/library/notebooks/using_meraki_sdk.py](https://github.com/joelwking/devnet-sdk/blob/master/library/notebooks/using_meraki_sdk.py)

Execute the code. Inputs to the program are the *key* and *organization* you wish to query.

```bash
export MERAKI_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
export MERAKI_ORG=WWT
```
Execute the program and review the results.
```bash
python3 ./using_meraki_sdk.py
```
Set the environment variable with one of the organizations and run the program again.

```bash
export MERAKI_ORG='DevNet Sandbox'
python3 ./using_meraki_sdk.py
```

This is the end of the Meraki SDK demo. To save your notebook, from your laptop, you can retrieve the notebook configuration file by issuing a command similar to the following.

```bash
scp -i "~/amazon_web_service/sdk/devnet_sdk_demo.pem" ubuntu@ec2-54-208-198-12.compute-1.amazonaws.com:devnet-sdk/library/notebooks/Using_a_SDK.ipynb ./Using_a_SDK.ipynb
```
If you have entered any credentials in the notebook, be advised they are present in clear text within the file.