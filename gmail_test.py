import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/mrmatthewrclark/PycharmProjects/TVAlertHandling/client_secret.json"
from google.cloud import pubsub

# Imports the Google Cloud client library
from google.cloud import pubsub_v1

# Instantiates a client
publisher = pubsub_v1.PublisherClient()

# The resource path for the new topic contains the project ID
# and the topic name.
topic_path = publisher.topic_path(
  'ultra-mediator-199301', 'TView2')

# Create the topic.
topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))

