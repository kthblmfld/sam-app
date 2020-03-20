import os

ENV_VARS = {
    'SayHelloFeature1': None,
    'DeployedEnv': None
}

for key in ENV_VARS:
    if key in os.environ:
        ENV_VARS[key] = os.environ[key]


def lambda_handler(event, context):
    print(f"DeployedEnv: {ENV_VARS['DeployedEnv']}")
    print(f"SayHelloFeature1: {ENV_VARS['SayHelloFeature1']}")
    print("Hello Piotr")

    # Keep my one and only test happy :(
    return {
        'status': 'ok'
    }