import requests 
import xml.dom.minidom 
from requests import HTTPError ,Timeout
import json


def getHeader(epr,password,pcc):

    return """<SOAP-ENV:Header>
     <eb:MessageHeader SOAP-ENV:mustUnderstand="1" eb:version="1.0">
        <eb:From>
           <eb:PartyId type="urn:x12.org:IO5:01">999999</eb:PartyId>
        </eb:From>
        <eb:To>
           <eb:PartyId type="urn:x12.org:IO5:01">123123</eb:PartyId>
        </eb:To>
        <eb:CPAId>IPCC</eb:CPAId>
        <eb:ConversationId>Python parser</eb:ConversationId>
        <eb:Service eb:type="OTA">ServiceSession</eb:Service>
        <eb:Action>SessionCreateRQ</eb:Action>
        <eb:MessageData>
           <eb:MessageId>mid:20001209-133003-2333@clientofsabre.com1</eb:MessageId>
           <eb:Timestamp>2014-12-29T16:06:031</eb:Timestamp>
        </eb:MessageData>
     </eb:MessageHeader>
     <wsse:Security xmlns:wsse="http://schemas.xmlsoap.org/ws/2002/12/secext" xmlns:wsu="http://schemas.xmlsoap.org/ws/2002/12/utility">
        <wsse:UsernameToken>
           <wsse:Username>{0}</wsse:Username>
           <wsse:Password>{1}</wsse:Password>
           <Organization>{2}</Organization>
           <Domain>DEFAULT</Domain>
        </wsse:UsernameToken>
     </wsse:Security>
  </SOAP-ENV:Header>""".format(epr,password,pcc)

def getBody():
      return """<SOAP-ENV:Body>
              <SessionCreateRQ returnContextID="true"/>
              </SOAP-ENV:Body>"""

def getPayload(epr,password,pcc):

    return """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:eb="http://www.ebxml.org/namespaces/messageHeader" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsd="http://www.w3.org/1999/XMLSchema">
             {0}
             {1}
           </SOAP-ENV:Envelope>""" .format(getHeader(epr,password,pcc),getBody()) 

def createSession(epr,password,pcc):

    url ="https://sws-crt.cert.havail.sabre.com" 

    try:
        
        headerData={

            "Content-Type":"text/xml"
        }
        with open('config.json') as f:
         JSONdata = json.load(f)
        epr=JSONdata['epr']
        password=JSONdata['pass']
        pcc=JSONdata['pcc']


        payload = getPayload(epr,password,pcc)
        result=requests.post(url,headers=headerData,data=payload)
        doc = xml.dom.minidom.parseString(result.text) 
        #print(result.text)
        # Check invalid credentials  
        
        if checkErrors(doc)==False:
           token = doc.getElementsByTagName("wsse:BinarySecurityToken")[0].firstChild.nodeValue 
           return token 

    except HTTPError as err:
         print("Error :{0}".format(err))

def checkErrors(doc):

  error_list= doc.getElementsByTagName("soap-env:Fault")
  if len(error_list)>0:
      error_code=error_list[0].getElementsByTagName("StackTrace")[0].firstChild.nodeValue 
      print(error_code)
      return True

  return False 

def getSessionToken():
    
    with open('config.json') as f:
        JSONdata = json.load(f)
        epr=JSONdata['epr']
        password=JSONdata['pass']
        pcc=JSONdata['pcc']
        #print(epr+ "  "+ password+" "+pcc) 
        token =createSession(epr,password,pcc)

        return token ;   
 