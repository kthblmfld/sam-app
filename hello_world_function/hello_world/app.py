def lambda_handler(event, context):
    print('Version: {' + event['version'] + '}')

    return {
        'status': 'ok'
    }
