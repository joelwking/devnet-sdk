


https://developer.cisco.com/meraki/api/#/python/guides/python-sdk-quick-start


from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException

x_cisco_meraki_api_key = '621e3462293939393939398cafd7'

meraki = MerakiSdkClient(x_cisco_meraki_api_key)

orgs = meraki.organizations.get_organizations()


for org in orgs:
  print('{} {}'.format(org.get('id'), org.get('name')))  
  if org.get('name') == 'WWT':
      organization_id = org.get('id')


help(meraki.organizations)


collect = dict()
collect['organization_id'] = organization_id

result = meraki.devices.get_organization_devices(collect)



