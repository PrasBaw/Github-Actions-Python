import pandas as pd
import os
import requests
import json

SUBSCRIPTION_ID = os.environment["subscription_id"]
TENANT_ID = os.environment["teanant_id"]
RESOURCE_GROUP_NAME = os.environment["group_name"]
SYNAPSE_WORKSPACE_NAME = os.environment["synapse_workspace_name"]
CLIENT_ID = os.environment["client_id"]
CLIENT_SECRET = os.environment["client_secret"]


def main()
  print("SUBSCRIPTION_ID = ", SUBSCRIPTION_ID)
  print("TENANT_ID = ", TENANT_ID)
  print("RESOURCE_GROUP_NAME = ", RESOURCE_GROUP_NAME)
  print("CLIENT_ID = ", CLIENT_ID)
  print("CLIENT_SECRET = ", CLIENT_SECRET)


if__name__=="__main__":
  main()

  


  
