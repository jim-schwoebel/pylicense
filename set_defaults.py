'''
================================================ 
          PYLICENSE REPOSITORY                     
================================================ 

repository name: PyLicense 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/pylicense 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: makes software licenses automatically to better document code bases. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-06-25 

This code (PyLicense) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
                LICENSE TERMS                      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
                SERVICE STATEMENT                    
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / python / docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ develop@neurolex.ai. 

================================================ 
        SET_DEFAULTS.PY SCRIPT      
================================================ 

This script takes in input from a user to generate the default .json file for generating
licenses. After you do this, you will no longer need to enter these fields into
the future for your organization.

This makes it easier to set defaults into the license.py code.

'''
import os

try:
    import pyttsx3 
except:
    os.system('pip3 install pyttsx3')
    import pyttsx3 

import json

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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
default_location=input("what is the organization's primary location? (leave blank for Seattle, WA) ")
if default_location in ['', ' ']:
    default_location='Seattle, WA'
default_website=input("what is the organization's website? (leave blank for https://neurolex.ai) ")
if default_website in ['', ' ']:
    default_website='https://neurolex.ai'
default_country=input("what is your default country? (leave blank for the United States of America) ")
if default_country in [""," "]:
    default_country='the United States of America'
default_legal_location=input('what state and country do you prefer to resolve legal disputes? (Leave blank for Delaware, United States of America) ')
if default_legal_location in [""," "]:
    default_legal_location = 'Delaware, United States of America'
default_author=input('what is your name? (leave blank for Jim Schwoebel)')
if default_author in ['',' ']:
    default_author='Jim Schwoebel'
default_author_email=input('what is your email address? (leave blank for js@neurolex.co) ')
if default_author_email in ['', ' ']:
    default_author_email='js@neurolex.co'
default_email=input('what contact organization email would you would like to provide? (leave blank for develop@neurolex.ai) ')
if default_email in ['', ' ']:
    default_email='develop@neurolex.ai'
default_service_statement=input('would you like to include a service statement in your code? (yes or no)')
while default_service_statement not in ['y','yes','n','no']:
    default_service_statement=input('input not recognized. Would you like to include a service statement in your code? (yes or no)')
if default_service_statement in ['yes', 'y']:
    speak_text('please edit this service statement to your needs and then save it; it will be used in your code base')
    os.system('open service_statement.txt')
    default_service_statement=True;
else:
    default_service_statement=False;

data={
    'default_org':default_org,
    'default_shortname':default_shortname,
    'default_location':default_location,
    'default_website':default_website,
    'default_country':default_country,
    'default_legal_location':default_legal_location,
    'default_author':default_author,
    'default_author_email':default_author_email,
    'default_email':default_email,
    'default_service_statement': default_service_statement,
    }

jsonfile=open('defaults.json','w')
json.dump(data,jsonfile)
jsonfile.close()

print('made defaults.json')
print(data)
