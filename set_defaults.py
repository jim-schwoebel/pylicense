'''
script name: set_defaults.py
repository link: https://github.com/jim-schwoebel/make_licenses
license: Apache 2.0 license
author: Jim Schwoebel
email: js@neurolex.co 

Take in input from a user to generate the default .json file for generating
licenses. After you do this, you will no longer need to enter these fields into
the future for your organization.

This makes it easier to set defaults into the license.py code.
'''
import json, os

os.chdir(os.getcwd()+'/licenses')

default_org=input('what is the default organization? (e.g.NeuroLex Laboratories, Inc.)')
default_shortname=input('what is the default organization shortname? (e.g. NeuroLex)')
default_location=input("what is the organization's primary location? (e.g. Seattle, WA'")
default_website=input("what is the organization's website? (e.g. https://neurolex.ai)'")
default_country=input("what is your default country? (leave blank for the United States of America)")
if default_country in [""," "]:
    default_country='the United States of America'
default_legal_location=input('what state and country do you prefer to resolve legal disputes? Leave blank for Delaware (United States of America).')
if default_legal_location in [""," "]:
    default_legal_location = 'Delaware (United States of America)'
default_email=input('what contact email would you would like to provide?')

data={
    'default_org':default_org,
    'default_shortname':default_shortname,
    'default_location':default_location,
    'default_website':default_website,
    'default_country':default_country,
    'default_legal_location':default_legal_location,
    'default_email':default_email
    }

jsonfile=open('defaults.json','w')
json.dump(data,jsonfile)
jsonfile.close()
