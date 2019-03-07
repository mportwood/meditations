##INCOMPLETE
##This is the code for sending the message via slack
##Currently waiting for slackapp workspace API auth 

##Have to install slackclient. More on that here: https://pypi.org/project/slackclient/
#run this in CLI: 
#pip install slackclient

import os
from slackclient import SlackClient

slack_token = os.environ[""]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  user="portwood",
  text="Hello from Python! :tada:"
)