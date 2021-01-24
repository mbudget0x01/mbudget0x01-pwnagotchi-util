# API Definition

Short overwiew over the api and how the requests work.

## Requests

The requests have multiple elements. The first element is the application identifier.
This is ```mbudget0x01-pwnagotchi-util-coordinator```. The second element is the request itself, followd by the additional data. The last element is the Servers acknoledgement.

All the parts are separated by a ```:```. \
As example ```mbudget0x01-pwnagotchi-util-coordinator:REQ_COORDINATER_AVIABLE:0.0.0.0:OK```

A special case is the ```DATA_SEGMENT``` this holds the size of the following raw data. The raw data will just be received.
