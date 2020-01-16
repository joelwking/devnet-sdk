#!/usr/bin/env python
"""

    using_meraki_sdk.py

    Copyright (c) 2020 World Wide Technology, LLC
    All rights reserved.

    author: joel.king@wwt.com (@joelwking)
    
    usage:
            export MERAKI_KEY=12345678901234567890
            export MERAKI_ORG=WWT
            python3 ./using_meraki_sdk.py

"""

import os
import sys
import yaml

from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException

KEYNAME = 'MERAKI_KEY'
ORGNAME = 'MERAKI_ORG'

def get_devices(dashboard=None, organization_id=None):
    """
        query all devices for the specified organization
        return a list of devices
    """
    collect = dict(organization_id=organization_id)

    return dashboard.devices.get_organization_devices(collect)
    

def get_org_id(dashboard=None, org_name=None):
    """
        determine the organization ID from the more human friendly organization name
        return either the organization ID or None
    """
    orgs = []

    if org_name:
        try:
            orgs = dashboard.organizations.get_organizations()
        except APIException as e:
            print('Ops! {} \n verify the API key specified is correct'.format(e))
            sys.exit()

    for org in orgs:
        if org_name == org.get('name'):
            return org.get('id')
    
    return None

def main():
    """
        The API key and Organization name must be configured as environmental variables
        First obtain the numerical Org ID from the Org name specified, then dump the 
        devices for that Org as YAML and exit.
    """
    x_cisco_meraki_api_key = os.environ.get(KEYNAME)

    if not x_cisco_meraki_api_key:
        print('Ops! you need to set environmental variable, {} to your cisco Meraki API key'.format(KEYNAME))
        return

    meraki = MerakiSdkClient(x_cisco_meraki_api_key)

    org_id = get_org_id(dashboard=meraki, org_name=os.environ.get(ORGNAME))

    if not org_id:
        print('Ops! you need to set environmental variable, {} to specify the organization name'.format(ORGNAME))
        return

    print(yaml.dump(get_devices(dashboard=meraki, organization_id=org_id)))


if __name__ == '__main__':
    main()