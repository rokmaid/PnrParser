

def getheader(token):

   return  """<soap-env:Header>
		     <eb:MessageHeader xmlns:eb='http://www.ebxml.org/namespaces/messageHeader' eb:version='1.0' soap-env:mustUnderstand='1'>
			 <eb:From>
			 <eb:PartyId eb:type='URI'>123123</eb:PartyId>
			 </eb:From>
			 <eb:To>
			 <eb:PartyId eb:type="URI">99999</eb:PartyId>
			 </eb:To>
			 <eb:CPAId>IPCC</eb:CPAId>
			 <eb:ConversationId>17-07-2019-102345380440037</eb:ConversationId>
			 <eb:Service>getReservationRQ</eb:Service>
			 <eb:Action>getReservationRQ</eb:Action>
			 <eb:MessageData>
			 <eb:MessageId>1691319482893580610</eb:MessageId>
			 <eb:Timestamp>2019-07-17T13:24:51</eb:Timestamp>
			 <eb:RefToMessageId>mid:20001209-133003-2333@clientofsabre.com</eb:RefToMessageId>
			 </eb:MessageData>
		     </eb:MessageHeader>
		     <wsse:Security xmlns:wsse='http://schemas.xmlsoap.org/ws/2002/12/secext'>
		     <wsse:BinarySecurityToken>
             {0}
             </wsse:BinarySecurityToken>
		     </wsse:Security>
     	     </soap-env:Header>""".format(token)

def getBody(locator):

    return """<soap-env:Body>
	<GetReservationRQ xmlns="http://webservices.sabre.com/pnrbuilder/v1_19" xmlns:ns2="http://services.sabre.com/res/or/v1_12" Version="1.19.0">
             <Locator>{0}</Locator>
			<RequestType>Stateful</RequestType>
			<ReturnOptions>
				<SubjectAreas>
					<SubjectArea>PRICE_QUOTE</SubjectArea>
					<SubjectArea>ACCOUNTING_LINE</SubjectArea>
					<SubjectArea>ADDRESS</SubjectArea>
					<SubjectArea>AIR_CABIN</SubjectArea>
					<SubjectArea>AFAX</SubjectArea>
					<SubjectArea>ANCILLARY</SubjectArea>
					<SubjectArea>BAS_EXTENSION</SubjectArea>
					<SubjectArea>CORPORATE_ID</SubjectArea>
					<SubjectArea>CUST_INSIGHT_PROFILE</SubjectArea>
					<SubjectArea>DK_NUMBER</SubjectArea>
					<SubjectArea>DSS</SubjectArea>
					<SubjectArea>EXT_FQTV</SubjectArea>
					<SubjectArea>FARETYPE</SubjectArea>
					<SubjectArea>FQTV</SubjectArea>
					<SubjectArea>GFAX</SubjectArea>
					<SubjectArea>HEADER</SubjectArea>
					<SubjectArea>ITINERARY</SubjectArea>
					<SubjectArea>NAME</SubjectArea>
					<SubjectArea>PASSENGERDETAILS</SubjectArea>
					<SubjectArea>PHONE</SubjectArea>
					<SubjectArea>PRERESERVEDSEAT</SubjectArea>
					<SubjectArea>RECEIVED</SubjectArea>
					<SubjectArea>RECORD_LOCATOR</SubjectArea>
					<SubjectArea>TICKETING</SubjectArea>
					<SubjectArea>REMARKS</SubjectArea>
				</SubjectAreas>
				<ViewName>Simple</ViewName>
				<ResponseFormat>STL</ResponseFormat>
			</ReturnOptions>
		</GetReservationRQ></soap-env:Body>""".format(locator)


def getPayload(token,locator):

    return """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
              {0}
              {1}
              </soap-env:Envelope>""".format(getheader(token),getBody(locator))          