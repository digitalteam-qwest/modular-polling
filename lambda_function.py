from lookup import integrations

def lambda_handler(event, context):

    environment = 'test'
    
    #basic validations
    if "queryStringParameters" not in event:        
        return 'Invalid parameters'
        
    environment = event['queryStringParameters']['environment']
    integrationIDs = event['queryStringParameters']['integrationIDs']

    #call the given integration and pass the given row as the payload
    def callIntegration(integrationID, row):
        payload = {
            'Section 1': {}
        }

        #translate the row into payload
        if (row is not None):
            for token in row:
                payload['Section 1'][token] = {
                    'name': token,
                    'value': row[token]
                }

        return integration.runLookup(integrationID, payload)['data']

    #for each given row, call the given integration
    def recursiveSomething(index = 0, rows = {'0': None}):
        for i in rows:
            newRows = callIntegration(integrationIDs[index], rows[i])

            if (len(integrationIDs) > index + 1):
                newIndex = index + 1
                recursiveSomething(newIndex, newRows)
    
    #integrations initialisation
    integration = integrations(environment)
    integration.login()

    #start
    recursiveSomething()

    return 'All good'