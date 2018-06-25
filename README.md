# make_licenses
Repo for quick access to copy/paste info of licenses into code base.

It's separated into 3 sections: commercial licenses (no redistribution at all), research licenses (restrictions to not use code for commercial use), and open-source licenses (no restrictions). In this way, we can paste such licenses as .txt files inside of all distributions of software and make sure the software is released under the appropriate license. 

## Getting started 

To make a license, run this in the terminal:
        
        cd ~
        git clone git@github.com:jim-schwoebel/make_licenses.git
        cd make_licenses
        python3 license.py

You will then be asked some basic information 

        what type of license? (commercial, research, opensource)? commercial
        what is the name of the repository? nlx-model
        what is the version? (can leave blank for 1.0)
        what does this repo do? this package builds and optimizes machine learning for voice, text, image, and video data.
        what is the link to this repository? https://github.com/NeuroLexDiagnostics/nlx-model
        what is the author(s) name(s)? Jim Schwoebel
        what is the contact author email? js@neurolex.co
        what is the organization name? (leave blank for NeuroLex Laboratories, Inc.) 
        what is the location of the organization? (blank for Seattle, WA)
        what is the website for the organization? (blank for https://neurolex.ai)
        what is the date of publication (e.g. July 2018)? (leave blank for current date) 
        generating default commercial license text
        
You then output a .txt file with the appropriate license terms (output to license.txt).

        ================================================ 
                  NLX-MODEL REPOSITORY                     
        ================================================ 

        repository name: nlx-model 
        repository link: https://github.com/NeuroLexDiagnostics/nlx-model 
        description: this package builds and optimizes machine learning ffor voice, text, image, and video data. 
        license category: commercial 
        license: trade secret 
        organization name: NeuroLex Laboratories, Inc. 
        location: Seattle, WA
        website: https://neurolex.ai 
        release date: 2018-06-25 

        This code (nlx-model) is hereby released under a trade secret license. 

        For more information, check out the license terms below. 

        ================================================ 
                        LICENSE TERMS                      
        ================================================ 

        Copyright (C) NeuroLex Laboratories, Inc. - All Rights Reserved 
        * Unauthorized copying of this file, via any medium is strictly prohibited 
        * Proprietary and confidential 
        * Written by Jim Schwoebel <js@neurolex.co>, 2018-06-25

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

        If you would like to work with us let us know @ js@neurolex.co. 

## What licenses are supported 

Currently, we support these licenses with the code base as a default.

### Commercial licenses 
* [Trade secret]()

### Research licenses 
* [Research and academic use license](https://www.audeering.com/research-and-open-source/files/openSMILE-open-source-license.txt)

### Open-source licenses 
* [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0)


## FUTURE WORK 

Add in these licenses into the code. 

### Commercial license
* [TBA]()

### Research licenses
* [Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported](https://creativecommons.org/licenses/by-nc-nd/3.0/)

### Opensource licenses 
* [MIT License]()
* [3 Clause BSD license]()

## references
* [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
* [MIT License](https://opensource.org/licenses/MIT)
* [Other opensource licenses](https://choosealicense.com/licenses/)
* [Creative Commons](https://creativecommons.org/licenses/by-nc-nd/3.0/)
* [3 clause BSD license](https://opensource.org/licenses/BSD-3-Clause)
