# PyLicense

This repo is dedicated to generating software licenses automatically for your code base. 

![](https://media.giphy.com/media/MbHWZv6FFWDnO/giphy.gif)

This script can create 3 classes of software licenses: commercial licenses (no redistribution at all), research licenses (restrictions to not use code for commercial use), and open-source licenses (no restrictions). 

In this way, you can paste such licenses as .txt files inside of all distributions of software and make sure the software is released under the appropriate license.

Happy license-making :) 

## Getting started 

To make a license, run this in the terminal:
        
        cd ~
        git clone git@github.com:jim-schwoebel/pylicense.git
        cd pylicense
        python3 license.py

You will then be asked some basic information:

        what type of license? (commercial, research, opensource)? opensource
        what is the name of the repository? testrepo
        what is the version? (can leave blank for 1.0)
        what does this repo do? this is a test
        what is the link to this repository? 
        what is the author(s) name(s)? (blank for Jim Schwoebel) 
        what is the contact author email? (blank for js@neurolex.co) 
        what is the organization name? (leave blank for NeuroLex Laboratories, Inc.) 
        what is the location of the organization? (blank for Seattle, WA)
        what is the website for the organization? (blank for https://neurolex.ai)
        what is the date of publication (e.g. July 2018)? (leave blank for current date) 
        what type of opensource license would you like? Options are apache, mit, or 3bsd. (leave blank to default to apache 2.0 license)apache
        generating apache 2.0 license

You then output a .txt file with the appropriate license terms (output to name_license.txt in the ../licenses folder). 

        ================================================ 
                  TESTREPO REPOSITORY                     
        ================================================ 

        repository name: testrepo 
        repository version: 1.0 
        repository link: n/a 
        author: Jim Schwoebel 
        author contact: js@neurolex.co 
        description: this is a test 
        license category: opensource 
        license: Apache 2.0 license 
        organization name: NeuroLex Laboratories, Inc. 
        location: Seattle, WA 
        website: https://neurolex.ai 
        release date: 2018-06-25 

        This code (testrepo) is hereby released under a Apache 2.0 license license. 

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

        If you would like to work with us let us know @ develop@neurolex.co. 

## Changing defaults 

You can easily change default settings. If you'd like to do this, type this into the terminal:

        cd ~
        cd pylicense
        python3 set_defaults.py

You then will be asked a series of questions to set defaults to change the defaults.json file in the /licenses folder. 

        what is the default organization? (leave blank for NeuroLex Laboratories, Inc.) 
        what is the default organization shortname? (leave blank for NeuroLex) 
        what is the organization's primary location? (leave blank for Seattle, WA) 
        what is the organization's website? (leave blank for https://neurolex.ai) 
        what is your default country? (leave blank for the United States of America) 
        what state and country do you prefer to resolve legal disputes? (Leave blank for Delaware, United States of America) 
        what is your name? (leave blank for Jim Schwoebel)
        what is your email address? (leave blank for js@neurolex.co) 
        what contact organization email would you would like to provide? (leave blank for develop@neurolex.ai) 
        would you like to include a service statement in your code? (yes or no)
        made defaults.json
        {'default_org': 'NeuroLex Laboratories, Inc.', 'default_shortname': 'NeuroLex', 'default_location': 'Seattle, WA', 'default_website': 'https://neurolex.ai', 'default_country': 'the United States of America', 'default_legal_location': 'Delaware, United States of America', 'default_author': 'Jim Schwoebel', 'default_author_email': 'js@neurolex.co', 'default_email': 'develop@neurolex.ai', 'default_service_statement': True}

This information will now work on all future executions of the license.py file. 

If you'd like to include a service statement, you can in this script through editing the service_statement.txt file in the ../licenses folder. Feel free to edit this to your needs while thinking about the spacing necessary to properly document your code. 

## What licenses are supported 

Currently, we support these licenses with the code base as a default. We plan on updating the library to include more licenses into the future. If you have any recommendations for licenses to add, let us know!  

### Commercial licenses 
* [Trade secret](https://en.wikipedia.org/wiki/Trade_secret)

### Research licenses 
* [Research and academic use license](https://www.audeering.com/research-and-open-source/files/openSMILE-open-source-license.txt)
* [Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)](https://creativecommons.org/licenses/by-nc-nd/3.0/)

### Open-source licenses 
* [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0)
* [MIT License](https://opensource.org/licenses/MIT)
* [3 clause BSD license](https://opensource.org/licenses/BSD-3-Clause)

## references
* [Other opensource licenses](https://choosealicense.com/licenses/)
