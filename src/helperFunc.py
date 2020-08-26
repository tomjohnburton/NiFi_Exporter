import requests
import json


def getCluster(url):
    response = requests.get(url, verify=False)
    # logger.debug( response.text)
    jData = json.loads(response.text)
    return jData['cluster']['nodes']


def convertStatus(status):
    if status == 'CONNECTED':
        return 1
    else:
        return 0


def getFlow(url):
    response = requests.get(url, verify=False)
    jData = json.loads(response.text)
    return jData['controllerStatus']


def about(url):
    response = requests.get(url, verify=False)
    jData = json.loads(response.text)
    return jData['about']


def getProcessorFlow(url):
    response = requests.get(url, verify=False)
    jData = json.loads(response.text)
    return jData['processGroups']


def getRetryCount(url):
    response = requests.get(url, verify=False)
    jData = json.loads(response.text)
    return jData['status']['aggregateSnapshot']['flowFilesQueued']
