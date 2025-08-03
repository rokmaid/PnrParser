
import requests 
import xml.dom.minidom 
import getReservation
from  getResParser import parsePNR
from  createSession import getSessionToken
from closeSession import closeSession 
from logger import writeLine
from requests import HTTPError ,Timeout
import os 

def main():
   # os.chdir("./PNRParser")
    f = open("logger.txt", "w")
    
    recloc = input("Enter Rec Loc ") 
    
    token=getSessionToken()
    #print(token)
    writeLine(f,"Token retrieved " + token) 

    payload=getReservation.getPayload(token,recloc) 
    #print(payload)
    try:
        url = "https://webservices.cert.platform.sabre.com" ; 
     
        headerData={

            "Content-Type":"text/xml"
        }
        result=requests.post(url,headers=headerData,data=payload)
        doc = xml.dom.minidom.parseString(result.text) 
        
        writeLine(f,"PNR Response "+result.text)
        parsePNR(result.text)

        closeSession(token) 
       

        #print(result.text)

    except HTTPError as err:
         print("Error :{0}".format(err))

def getUrl(token):
  
  # Check if the token is from CERT or Res and return the Url acordingly
  if(token.find("CRT")!=-1):
       return "https://webservices.cert.platform.sabre.com" 
  elif (token.find("RES")!=-1) :
       return "https://webservices.platform.sabre.com"    

  
main()     