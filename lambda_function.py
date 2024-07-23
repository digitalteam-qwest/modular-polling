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

    #for each given row, call the next integration in the list
    def something(index, rows):
        if (rows is not None):
            for i in rows:
                newRows = callIntegration(integrationIDs[index], rows[i])

                if (len(integrationIDs) > index + 1):
                    newIndex = index + 1
                    #
                    something(newIndex, newRows)
        else:
            newRows = callIntegration(integrationIDs[index], None)

            if (len(integrationIDs) > index + 1):
                newIndex = index + 1
                something(newIndex, newRows)
    
    integration = integrations(environment)
    integration.login()

    #start with the first integration in the list
    something(0, None)

    return 'All good'
    

# test code
#event = {
#    "queryStringParameters": {
#        "environment": 'test',
#        "integrationIDs": ['669f586074915','669f58853d1f4','669f58d9c5804']
#    }
#}

#lambda_handler(event,None)