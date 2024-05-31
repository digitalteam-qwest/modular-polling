import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from lookup import integrations


#get emails from integrations
#run integrations against them

def lambda_handler(event, context):
    environment = 'test'
    
    if "queryStringParameters" not in event:
        http_res = {}
        http_res['statusCode'] = 403
        http_res['headers'] = {}
        http_res['headers']['Content-Type'] = 'text/html'

        return http_res
        
    environment = event['queryStringParameters']['environment']
    databaseIntegrationID = event['queryStringParameters']['database-integration-id']
    emailIntegrationID = event['queryStringParameters']['email-integration-id']

    def getRows(integrationID):
        return integration.runLookup(integrationID, None)['data']

    def sendEmail(integrationID, row):
        payload = {
            'Section 1': {}
        }

        for token in row:
            payload[token] = {
                'name': token,
                'value': row[token]
            }

        integration.runLookup(integrationID, payload)

        return
    
    integration = integrations(environment)
    integration.login()

    #get all the references
    rows = getRows(databaseIntegrationID)

    for index in rows:
        sendEmail(emailIntegrationID, rows[index])
    
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'text/html'

    return http_res
    
event = {
  "queryStringParameters": {
    "environment": "test",
    "database-integration-id": "663206b4dac66",
    "email-integration-id": "663206b4dac66"
  }
}

lambda_handler(event, None)