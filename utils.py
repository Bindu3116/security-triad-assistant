import re

def extract_entities(alert):
    text = str(alert)
    entities = {
        "ip": re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text),
        "domain": re.findall(r'\b(?:[a-z0-9-]+\.)+[a-z]{2,6}\b', text),
        "file_hash": re.findall(r'\b[a-fA-F0-9]{32,64}\b', text),
        "username": re.findall(r'"user"\s*:\s*"([^"]+)"', text),
        "process": re.findall(r'"process"\s*:\s*"([^"]+)"', text)
    }
    return entities
