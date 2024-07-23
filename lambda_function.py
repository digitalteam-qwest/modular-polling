from lookup import integrations

def lambda_handler(event, context):
    environment = 'test'
    
    if "queryStringParameters" not in event:        
        return 'Invalid parameters'
        
    environment = event['queryStringParameters']['environment']
    integrationIDs = event['queryStringParameters']['integrationIDs']

    def callIntegration(integrationID, row):
        payload = {
            'Section 1': {}
        }

        if (row is not None):
            for token in row:
                payload['Section 1'][token] = {
                    'name': token,
                    'value': row[token]
                }

        return integration.runLookup(integrationID, payload)['data']

    def something(index, rows):
        if (rows is not None):
            for i in rows:
                newRows = callIntegration(integrationIDs[index], rows[i])

                if (len(integrationIDs) > index + 1):
                    newIndex = index + 1
                    something(newIndex, newRows)
        else:
            newRows = callIntegration(integrationIDs[index], None)

            if (len(integrationIDs) > index + 1):
                newIndex = index + 1
                return something(newIndex, newRows)
    
    integration = integrations(environment)
    integration.login()

    something(0, None)

    return 'All good'
    

# test code
#event = {
#    "queryStringParameters": {
#        "environment": 'test',
#        "integrationIDs": ['669f586074915','669f58853d1f4','669f58d9c5804']
#    }
#}
#
#lambda_handler(event,None)