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

'''

####################################################################
##                    IMPORT STATEMENTS                           ##
####################################################################

import os, datetime, json

# set current directory (if for some reason deleted, make this directory)
curdir=os.getcwd()

try:
    os.chdir(curdir+'/licenses')
except:
    os.mkdir(curdir+'/licenses')
    os.chdir(curdir+'/licenses')

# set defaults (loaded after you run set_defaults.py)
if 'defaults.json' not in os.listdir():
    os.chdir(curdir)
    os.system('python3 set_defaults.py')
    os.chdir(curdir+'/licenses')

data=json.load(open('defaults.json'))
default_org=data['default_org']
default_shortname=data['default_shortname']
default_location=data['default_location']
default_website=data['default_website']
default_country=data['default_country']
default_legal_location=data['default_legal_location']
default_author=data['default_author']
default_author_email=data['default_author_email']
default_email=data['default_email']

####################################################################
##                      HELPER FUNCTIONS                          ##
####################################################################

def header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date):
    one='================================================ \n'
    two='          %s REPOSITORY                     \n'%(rname.upper())
    three='================================================ \n'
    space='\n'
    four='repository name: %s \n'%(rname)
    five='repository version: %s \n'%(rversion)
    six='repository link: %s \n'%(rlink)
    seven='author: %s \n'%(author)
    eight='author contact: %s \n'%(author_email)
    nine='description: %s \n'%(description)
    ten='license category: %s \n'%(lcategory)
    eleven='license: %s \n'%(ltype)
    twelve='organization name: %s \n'%(organization)
    thirteen='location: %s \n'%(location)
    fourteen='website: %s \n'%(website)
    fifteen='release date: %s \n\n'%(date)
    sixteen='This code (%s) is hereby released under a %s license. \n\n'%(rname, ltype)
    seventeen= 'For more information, check out the license terms below. \n\n'
    eighteen='================================================ \n'
    nineteen='                LICENSE TERMS                      \n'
    twenty='================================================ \n\n'
    
    return one+two+three+space+four+five+six+seven+eight+nine+ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen+twenty

def trade_secret(organization, email, date):
    ## this is for generating text indicating the confidentiality of a code base as a trade secret 
    one='Copyright (C) %s - All Rights Reserved \n'%(organization)
    two='* Unauthorized copying of this file, via any medium is strictly prohibited \n'
    three ='* Proprietary and confidential \n'
    four= '* Written by %s <%s>, %s'%(author, email, date)
    five = '\n'
    
    return one+two+three+four+five


def research_license(default_shortname, organization, default_country,default_legal_location, email):
    # this is for code released under a research license 
    text=("This %s Research License Agreement (license, license agreement,\n"%(default_shortname)+
        "or agreement in the ongoing), is a legal agreement between you \n"+
        "and %s ('%s' or we) for the software \n "%(organization,default_shortname)+
        "or data mentioned above, which may include source code, \n"+
        "and any associated materials, text or speech files, \n"+
        'associated media and "on-line" or electronic documentation \n'+
        '(all together called the "Software"). \n\n'+
        "By installing, copying, or otherwise using this Software, \n"+
        "you agree to be bound by the terms in this license. \n"+
        "If you do not agree, you must not install copy or use the Software. \n"+
        "The Software is protected by copyright and other intellectual \n"+
        "property laws and is licensed, not sold. \n\n"+
        "This license grants you the following rights: \n\n" +
        ## main license clause - what you can use 
        "A. You may use, copy, reproduce, and distribute this Software \n"+
        "for any non-commercial purpose, subject to the restrictions \n"+
        "set out below. Some purposes which can be non-commercial are teaching, \n"+
        "academic research, public demonstrations and personal experimentation \n"+
        "or personal home use. You may also distribute this Software with \n"+
        "books or other teaching materials, or publish the Software on websites, \n"+
        "that are intended to teach the use of the Software for academic or \n"+
        "other non-commercial purposes. \n\n"+
        ## main license clause - what you cannot use 
        "You may NOT use or distribute this Software or any derivative works \n"+
        "in any form for commercial purposes, except those outlined in (B). \n"+
        "Examples of commercial purposes are running business operations, \n"+
        "licensing, leasing, or selling the Software, distributing the \n"+
        "Software for use with commercial products (no matter whether free or paid), \n"+
        "using the Software in the creation or use of commercial products or any \n"+
        "other activity which purpose is to procure a commercial gain to you or \n"+
        "others (except for conditions set out in (B)).\n\n"+
        # part B.
        "B. Further, you may use the software for commercial research, which meets \n"+
        "the following conditions: commercial research which is not directly \n"+
        "associated with product development and has the primary purpose of \n"+
        "publishing and sharing results with the academic world; pre-product \n"+
        "evaluations of algorithms and methods, as long as these evaluations \n"+
        "are more of an evaluatory, planning, and research nature than of a product development nature. \n"+
        "Any further commercial use requires you to obtain a commercial \n"+
        "license or written approval from %s which grants \n"%(default_shortname)+
        "you extended usage rights for this software. In particular any direct \n"+
        "(software) or indirect (models, features extracted with the software) \n"+
        "use of the software, parts of the software, or derivatives in a \n"+
        "product (no matter whether free or paid), is not allowed without \n"
        "an additional commercial license.\n\n"
        "C. If the software includes source code or data, you may create \n"+
        "derivative works of such portions of the software and distribute the \n"+
        "modified software for non-commercial purposes, as provided herein.\n"+
        "If you distribute the software or any derivative works of the Software, \n"+
        "you must distribute them under the same terms and conditions as in this \n"+
        "license, and you must not grant other rights to the software or \n"+
        "derivative works that are different from those provided by this license agreement. \n"+
        "If you have created derivative works of the software, and distribute \n"+
        "such derivative works, you will cause the modified files to carry \n"+
        "prominent notices so that recipients know that they are not receiving \n"+
        "the original software. Such notices must state: \n"+
        "(i) that you have altered the software; \n"+
        "and (ii) the date of any changes as well as your name. \n\n"+
        "In return for the above rights, you agree to: \n\n"
        "1. That you will not remove any copyright or other notices (authors \n"+
        "and citing information, for example) from the software. \n\n"+
        "2. That if any of the software is in binary format, you will not attempt \n"+
        "to modify such portions of the software, or to reverse engineer or \n"+
        "decompile them, except and only to the extent authorized by applicable law. \n\n"+
        "3. That the copyright holders (NeuroLex) are granted back, \n"+
        "without any restrictions or limitations, a non-exclusive, perpetual, \n"+
        "irrevocable, royalty-free, assignable and sub-licensable license, \n"+
        "to reproduce, publicly perform or display, install, use, modify, post, \n"+
        "distribute, make and have made, sell and transfer your modifications \n"+
        "to and/or derivative works of the software source code or data, \n"+
        "for any purpose. \n\n"+
        "4. That any feedback about the software provided by you to us is voluntarily \n"+
        "given, and NeuroLex shall be free to use the feedback \n"+
        "as they see fit without obligation or restriction of any kind, \n"+
        "even if the feedback is designated by you as confidential. \n\n"+
        '5. THAT THE SOFTWARE COMES "AS IS", WITH NO WARRANTIES. \n'+
        "THIS MEANS NO EXPRESS, IMPLIED OR STATUTORY WARRANTY, INCLUDING \n"+
        "WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A \n"+
        "PARTICULAR PURPOSE, ANY WARRANTY AGAINST INTERFERENCE WITH YOUR \n"+
        "ENJOYMENT OF THE SOFTWARE OR ANY WARRANTY OF TITLE OR NON-INFRINGEMENT.\n"+
        "THERE IS NO WARRANTY THAT THIS SOFTWARE WILL FULFILL ANY OF YOUR \n"+
        "PARTICULAR PURPOSES OR NEEDS. ALSO, YOU MUST PASS THIS DISCLAIMER ON \n"+
        "WHENEVER YOU DISTRIBUTE THE SOFTWARE OR DERIVATIVE WORKS. \n\n"+
        "6. THAT NEITHER NEUROLEX NOR ANY AUTHOR OR CONTRIBUTOR TO THE \n"+
        "SOFTWARE WILL BE LIABLE FOR ANY DAMAGES RELATED TO THE SOFTWARE OR THIS \n"+
        "LICENSE, INCLUDING DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL OR INCIDENTAL \n"+
        "DAMAGES, TO THE MAXIMUM EXTENT THE LAW PERMITS, NO MATTER WHAT LEGAL \n"+
        "THEORY IT IS BASED ON. ALSO, YOU MUST PASS THIS LIMITATION OF LIABILITY \n"+
        "ON WHENEVER YOU DISTRIBUTE THE SOFTWARE OR DERIVATIVE WORKS.\n\n"+
        "7. That we have no duty of reasonable care or lack of negligence, \n"+
        "and we are not obligated to (and will not) provide technical support for the Software. \n\n"+
        "8. That if you breach this license agreement or if you sue anyone over \n"+
        "patents that you think may apply to or read on the software or anyone's \n"+
        "use of the software, this license agreement (and your license and rights \n"+
        "obtained herein) terminate automatically. Upon any such termination, \n"+
        "you shall destroy all of your copies of the software immediately. \n"
        "Sections 3, 4, 5, 6, 7, 10 and 11 of this license agreement shall survive \n"+
        "any termination of this license agreement.\n\n"+
        "9. That the patent rights, if any, granted to you in this license agreement \n"+
        "only apply to the software, not to any derivative works you make.\n\n"+
        "10.That the software may be subject to %s export or import laws or such \n"%(default_country)+
        "laws in other places. You agree to comply with all such laws and regulations \n"+
        "that may apply to the software after the delivery of the software to you. \n\n"+
        "11.That all rights not expressly granted to you in this license agreement \n"+
        "are reserved by %s. \n\n"%(default_shortname)+
        "12.That this license agreement shall be construed and controlled by the laws \n"+
        "of %s, without regard to conflicts of law. \n"%(default_legal_location)+
        "If any provision of this license agreement shall be deemed unenforceable \n"+
        "or contrary to law, the rest of this license agreement shall remain in \n"+
        "full effect and interpreted in an enforceable manner that most closely \n"+
        "captures the intent of the original language. \n\n"+
        "++ For other, such as commercial, licensing options, \n"+
        "please contact NeuroLex at %s ++ \n\n"%(email)+
        "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \n"+
        "``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT \n"+
        "LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR \n"+
        "A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR \n"+
        "CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, \n"+
        "EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, \n"+
        "PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR \n"+
        "PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF \n"+
        "LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING \n"+
        "NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS \n"+
        "SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. \n")

    return text

def cc_research():
    
    one="You are free to: \n\n"
    two="* Share — copy and redistribute the material in any medium or format \n\n"
    three="The licensor cannot revoke these freedoms as long as you follow the license terms.\n\n"
    four="Under the following terms: \n\n"
    five="* Attribution — You must give appropriate credit, provide a link to the license, and \n"
    six="indicate if changes were made. You may do so in any reasonable manner, \n"
    seven="but not in any way that suggests the licensor endorses you or your use. \n\n"
    eight="* NonCommercial — You may not use the material for commercial purposes.\n\n"
    nine="* NoDerivatives — If you remix, transform, or build upon the material, you \n"
    ten="may not distribute the modified material.\n\n"
    eleven="No additional restrictions — You may not apply legal terms or technological measures \n"
    twelve="that legally restrict others from doing anything the license permits. \n\n"
    thirteen='Notices: \n\n'
    fourteen='You do not have to comply with the license for elements of the material \n' 
    fifteen='in the public domain or where your use is permitted by an applicable exception or limitation. \n\n'
    sixteen='No warranties are given. The license may not give you all of the permissions \n' 
    seventeen='necessary for your intended use. For example, other rights such as publicity, \n'
    eighteen='privacy, or moral rights may limit how you use the material. \n\n'
    nineteen='This is a human-readable summary of (and not a substitute for) the license. \n'
    twenty='The license can be read here (https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode) \n'

    text=one+two+three+four+five+six+seven+eight+nine+ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen+twenty

    return text 

def apache_license(date, default_org):
    # this is for code released under the Apache 2.0 license
    year=date[0:4]
    one="Copyright %s %s \n"%(year, default_org)
    two='Licensed under the Apache License, Version 2.0 (the "License"); \n'
    three='you may not use this file except in compliance with the License. \n'
    four='You may obtain a copy of the License at \n\n'
    five='     http://www.apache.org/licenses/LICENSE-2.0 \n\n'
    six='Unless required by applicable law or agreed to in writing, software \n'
    seven='distributed under the License is distributed on an "AS IS" BASIS, \n'
    eight='WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. \n'
    nine='See the License for the specific language governing permissions and \n'
    ten='limitations under the License. \n'

    text=one+two+three+four+five+six+seven+eight+nine+ten
    
    return text

def mit_license(date, default_org):

    year=date[0:4]
    one="Copyright %s %s \n\n"%(year, default_org)
    two="Permission is hereby granted, free of charge, to any person obtaining a copy \n"
    three='of this software and associated documentation files (the "Software"), to deal \n'
    four="in the Software without restriction, including without limitation the rights \n"
    five="to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \n"
    six="copies of the Software, and to permit persons to whom the Software is furnished \n"
    seven="to do so, subject to the following conditions:\n\n"
    eight="The above copyright notice and this permission notice shall be included in all \n"
    nine="copies or substantial portions of the Software.\n\n"
    ten='THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,\n'
    eleven="INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A \n"
    twelve="PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT \n"
    thirteen="HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN \n"
    fourteen="ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION \n"
    fifteen="WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. \n"

    text=one+two+three+four+five+six+seven+eight+nine+ten+eleven+twelve+thirteen+fourteen+fifteen

    return text 

def bsd3_license(date, default_org):

    year=date[0:-4]
    one="Copyright %s %s \n\n"%(year, default_org)
    two='Redistribution and use in source and binary forms, with or without modification,\n'
    three='are permitted provided that the following conditions are met: \n\n'
    four='1. Redistributions of source code must retain the above copyright notice, this \n'
    five='list of conditions and the following disclaimer.\n\n'
    six='2. Redistributions in binary form must reproduce the above copyright notice, this \n'
    seven='list of conditions and the following disclaimer in the documentation and/or \n'
    eight='other materials provided with the distribution.\n\n'
    nine='3. Neither the name of the copyright holder nor the names of its contributors \n'
    ten='may be used to endorse or promote products derived from this software without \n'
    eleven='specific prior written permission.\n\n'
    twelve='THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" \n'
    thirteen='AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, \n'
    fourteen='THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR \n'
    fifteen='PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR \n'
    sixteen='CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, \n'
    seventeen='EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, \n'
    eighteen='PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; \n'
    nineteen='OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, \n'
    twenty='WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE \n'
    twentyone='OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, \n'
    twentytwo='EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n'

    text=one+two+three+four+five+six+seven+eight+nine+ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen+twenty+twentyone+twentytwo

    return text 

def service_statement(email):
    
    one='\n================================================ \n'
    two='                SERVICE STATEMENT                    \n'
    three='================================================ \n\n'
    four='If you are using the code written for a larger project, we are \n'
    five='happy to consult with you and help you with deployment. Our team \n'
    six='has >10 world experts in kafka distributed architectures, microservices \n'
    seven='built on top of Node.JS / python / docker, and applying machine learning to \n'
    eight='model speech and text data. \n\n'
    nine='We have helped a wide variety of enterprises - small businesses, \n' 
    ten='researchers, enterprises, and/or independent developers. \n\n'
    eleven="If you would like to work with us let us know @ %s. \n"%(default_email)
    twelve="We're happy to help - even if its an opensource project. :) "
    
    return one+two+three+four+five+six+seven+eight+nine+ten+eleven


####################################################################
##                      MAIN CODE BASE                            ##
####################################################################

## Get input from user initially
lcategory= input('what type of license? (commercial, research, opensource)? ')

while lcategory not in ['c','r','o','commerical','research','opensource', 'open source']:
    print('input not recognized')
    lcategory= input('what type of license? (commercial, research, opensource)? ')
if lcategory in ['c','r','o']:
    if lcategory=='c':
        lcategory='commercial'
    elif lcategory=='r':
        lcategory='research'
    elif lcategory in ['o','open source']:
        lcategory='opensource'
        
rname= input('what is the name of the repository? ')
rversion = input('what is the version? (can leave blank for 1.0)')
if rversion in ['', ' ']:
    rversion='1.0'
description = input('what does this repo do? ')
if description in ['', ' ']:
    description='n/a'
rlink= input('what is the link to this repository? ' )
if rlink in ['', ' ']:
    rlink='n/a'
author = input('what is the author(s) name(s)? (blank for %s) '%(default_author))
if author in ['', ' ']:
    author=default_author
author_email = input('what is the contact author email? (blank for %s) '%(default_author_email))
if author_email in ['',' ']:
    author_email=default_author_email
organization = input('what is the organization name? (leave blank for %s) '%(default_org))
if organization in [' ','']:
    organization=default_org
location=input('what is the location of the organization? (blank for %s)'%(default_location))
if location in ['', ' ']:
    location=default_location
website=input('what is the website for the organization? (blank for %s)'%(default_website))
if website in ['', ' ']:
    website=default_website
date = input('what is the date of publication (e.g. July 2018)? (leave blank for current date) ')
if date in [' ','']:
    date=str(datetime.datetime.now())[0:10]

## Now generate licenses based on some supplemental information
filename=rname+'_license.txt'
ltext=open(filename,'w')

if lcategory in ['c','commercial']:
    print('generating commercial license')
    ltype='trade secret'
    ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
    ltext.write(trade_secret(organization, author_email, date))
    ltext.write(service_statement(default_email))

    
elif lcategory in ['r','research']:
    ltype=input('what type of research license would you like? Options are %s and cc. (leave blank to default to %s) '%(default_shortname, default_shortname)).lower()
    while ltype not in ['', ' ', default_shortname.lower(), 'cc']:
        ltype=input('what type of research license would you like? Options are %s and cc. (leave blank to default to %s) '%(default_shortname, default_shortname)).lower()
    if ltype in ['', ' ']:
        ltype = default_shortname.lower()
    if ltype == default_shortname.lower():
        print('generating %s research license'%(default_shortname))
        ltype='%s research license'%(default_shortname)
        ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
        ltext.write(research_license(default_shortname, organization, default_country, default_legal_location, default_email))
        ltext.write(service_statement(default_email))
    elif ltype == 'cc':
        print('generating cc license...')
        ltype = 'Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)'
        ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
        ltext.write(cc_research())
        ltext.write(service_statement(default_email))

elif lcategory in ['o','opensource','open source']:
    ltype=input('what type of opensource license would you like? Options are apache, mit, or 3bsd. (leave blank to default to apache 2.0 license) ').lower()
    while ltype not in ['', ' ', 'apache', 'mit', '3bsd']:
        ltype=input('what type of opensource license would you like? Options are apache, mit, or 3bsd. (leave blank to default to apache 2.0 license) ').lower()
    if ltype in ['',' ']:
        ltype='apache'
    if ltype == 'apache':
        print('generating apache 2.0 license')
        ltype='Apache 2.0 license'
        ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
        ltext.write(apache_license(date, default_org))
        ltext.write(service_statement(default_email))
    elif ltype == 'mit':
        print('generating mit license')
        ltype='MIT License'
        ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
        ltext.write(mit_license(date, default_org))
        ltext.write(service_statement(default_email))
    elif ltype == '3bsd':
        print('generating 3 clause BSD license')
        ltype='3-Clause BSD License'
        ltext.write(header(author, author_email, rname, rversion, description, lcategory, ltype, rlink, organization, location, website, date))
        ltext.write(bsd3_license(date, default_org))
        ltext.write(service_statement(default_email)) 

ltext.close()
# open file when it is finished automatically 
os.system('open %s'%(filename))
    
