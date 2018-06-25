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

curdir=os.getcwd()

try:
    os.chdir(curdir+'/licenses')
except:
    os.mkdir(curdir+'/licenses')
    os.chdir(curdir+'/licenses')

default_org=input('what is the default organization? (leave blank for NeuroLex Laboratories, Inc.) ')
if default_org in ['', ' ']:
    default_org='NeuroLex Laboratories, Inc.'
default_shortname=input('what is the default organization shortname? (leave blank for NeuroLex) ')
if default_shortname in ['', ' ']:
    default_shortname='NeuroLex'
default_location=input("what is the organization's primary location? (leave blank for Seattle, WA' ")
if default_location in ['', ' ']:
    default_location=Seattle, WA
default_website=input("what is the organization's website? (leave blank for https://neurolex.ai)' ")
if default_website in ['', ' ']:
    default_website='https://neurolex.ai'
default_country=input("what is your default country? (leave blank for the United States of America) ")
if default_country in [""," "]:
    default_country='the United States of America'
default_legal_location=input('what state and country do you prefer to resolve legal disputes? (Leave blank for Delaware, United States of America). ')
if default_legal_location in [""," "]:
    default_legal_location = 'Delaware, United States of America'
default_email=input('what contact email would you would like to provide? (leave blank for develop@neurolex.ai)')
if default_email in ['', ' ']:
    defalut_email='develop@neurolex.ai'

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
