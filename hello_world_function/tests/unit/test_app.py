import pytest

from hello_world_function.hello_world import app


@pytest.fixture()
def event():
    """ Generates EventBridge EC2 Instance Notification Event"""

    return {
        "version": "0",
        "id": "7bf73129-1428-4cd3-a780-95db273d1602",
        "detail-type": "EC2 Instance State-change Notification",
        "source": "aws.ec2",
        "account": "123456789012",
        "time": "2015-11-11T21:29:54Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
        ],
        "detail": {
            "instance-id": "i-abcd1111",
            "state": "pending"
        }
    }


def test_lambda_handler(event):
    result = app.lambda_handler(event, "")
    assert result['status'] == "ok"
