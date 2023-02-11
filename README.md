# backend_test_case

You need to design and write a fault-tolerant and scalable REST service 
for storing binary data in any cloud service (S3, Azure Blob Storage, Dropbox, etc.). 
Data is accessed by key-value.

Service requirements:
  - Put, get operations via REST
  - Synchronous writing (data is available via get immediately after the put is completed)
  - You can use any framework except Django

## Installation
Install the dependencies and start the server.


Flask app

```sh
python -m venv venv
pip install -r requirements.txt
python app.py
```

## Get-Test application

```sh
python tests.py
```
