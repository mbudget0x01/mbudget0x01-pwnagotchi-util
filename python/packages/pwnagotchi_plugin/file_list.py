import os
import json

def generate_file_list(path:str) -> []:
    resp = []
    for file in os.listdir(path):
        if file.endswith(".pcap"):
            resp.append(file)
    return resp

def generate_file_list_json(path:str) -> str:
    return json.dumps(generate_file_list(path))