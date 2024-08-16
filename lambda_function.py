from lookup import integrations
import time

def lambda_handler(event, context):
    start = time.time()

    environment = 'test'
    
    #basic validations
    if "queryStringParameters" not in event:        
        return 'Invalid parameters'
        
    environment = event['queryStringParameters']['environment']
    integrationIDs = event['queryStringParameters']['integrationIDs']

    conditions = None
    if 'conditions' in event['queryStringParameters']:
        conditions = event['queryStringParameters']['conditions']

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

        def checkConditions(conditions, integrationID, row):
            if conditions is not None:
                if integrationID in conditions:
                    for token in row:
                        if token == conditions[integrationID]['token']:
                            if conditions[integrationID]['value'] != row[token]:
                                return False
            return True

        for i in rows:
            for integrationID in integrationIDs[index]:
                #check if the integration needs running
                valid = checkConditions(conditions, integrationID, rows[i])

                if not valid:
                    continue

                newRows = callIntegration(integrationID, rows[i])

                if (len(integrationIDs) > index + 1):
                    newIndex = index + 1
                    recursiveSomething(newIndex, newRows)
    
    #integrations initialisation
    integration = integrations(environment)
    integration.login()

    #start
    recursiveSomething()

    time_lapsed = time.time() - start

    return {
        "result": "All good",
        "time_lapsed": round(time_lapsed, 2)
    }