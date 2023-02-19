import json

fileName = 'snakes.json'

def readJSON(fileName):
  with open(fileName) as f:
    parameters = json.load(f)
  IDs = parameters['IDs']
  print(IDs)
  return IDs
#   condMapping_original = parameters['conditionMapping_original']
#   condMapping = parameters['conditionMapping_analysis'] #for analysis

readJSON(fileName)

nIDs = len(IDs)

for ID in IDs:
  print(ID)