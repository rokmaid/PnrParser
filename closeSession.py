from requests import HTTPError ,Timeout
import json
import requests 
from logger import writeLine


def getBody(pcc):

    return """
      <SOAP-ENV:Body>
    <SessionCloseRQ>
	<POS>
		<Source PseudoCityCode="{0}"/>
	</POS>
    </SessionCloseRQ>
    </SOAP-ENV:Body>""".format(pcc)

def getHeader(token): 

    return """  <SOAP-ENV:Header>
     <eb:MessageHeader SOAP-ENV:mustUnderstand="1" eb:version="1.0">
        <eb:From>
           <eb:PartyId type="urn:x12.org:IO5:01">999999</eb:PartyId>
        </eb:From>
        <eb:To>
           <eb:PartyId type="urn:x12.org:IO5:01">123123</eb:PartyId>
        </eb:To>
        <eb:CPAId>IPCC</eb:CPAId>
        <eb:ConversationId>SessionCochaMobile</eb:ConversationId>
        <eb:Service eb:type="OTA">ServiceSession</eb:Service>
        <eb:Action>SessionCreateRQ</eb:Action>
        <eb:MessageData>
           <eb:MessageId>mid:20001209-133003-2333@clientofsabre.com1</eb:MessageId>
           <eb:Timestamp>2014-12-29T16:06:031</eb:Timestamp>
        </eb:MessageData>
     </eb:MessageHeader>
     <wsse:Security xmlns:wsse="http://schemas.xmlsoap.org/ws/2002/12/secext" xmlns:wsu="http://schemas.xmlsoap.org/ws/2002/12/utility">
     	<wsse:BinarySecurityToken>
         {0}
	</wsse:BinarySecurityToken>
     </wsse:Security>
  </SOAP-ENV:Header>""".format(token)

def getPayload(token,pcc):

    return """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:eb="http://www.ebxml.org/namespaces/messageHeader" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsd="http://www.w3.org/1999/XMLSchema">
            {0}
            {1}
            </SOAP-ENV:Envelope>""".format(getHeader(token),getBody(pcc)) 


def closeSession(token):
   
    with open('config.json') as f:
     JSONdata = json.load(f)
     pcc = JSONdata['pcc']

    payload = getPayload(token,pcc)
    try:
     url ="https://sws-crt.cert.havail.sabre.com" 
     headerData={

            "Content-Type":"text/xml"
    }
     result=requests.post(url,headers=headerData,data=payload)
     #print(result.text)
     with  open("logger.txt", "a") as l :
      writeLine(l,"Session Closed "+ result.text)
   
    except HTTPError as err:
         print("Error :{0}".format(err))
