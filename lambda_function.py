from lookup import integrations

def lambda_handler(event, context):
    environment = 'test'
    
    if "queryStringParameters" not in event:
        http_res = {}
        http_res['statusCode'] = 403
        http_res['headers'] = {}
        http_res['headers']['Content-Type'] = 'text/html'

        return http_res
        
    environment = event['queryStringParameters']['environment']
    getDataIntegrationID = event['queryStringParameters']['get-data-integration-id']
    sendDataIntegrationID = event['queryStringParameters']['send-data-integration-id']

    def getRows(integrationID):
        return integration.runLookup(integrationID, None)['data']

    def sendEmail(integrationID, row):
        payload = {
            'Section 1': {}
        }

        for token in row:
            payload['Section 1'][token] = {
                'name': token,
                'value': row[token]
            }

        integration.runLookup(integrationID, payload)

        return
    
    integration = integrations(environment)
    integration.login()

    #get all the references
    rows = getRows(getDataIntegrationID)

    for index in rows:
        sendEmail(sendDataIntegrationID, rows[index])
    
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'text/html'

    return http_res