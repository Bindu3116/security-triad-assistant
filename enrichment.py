import random

def mock_threat_intel(entity_type, value):
    malicious_samples = ['192.168.1.100', 'bad.com', 'abc123hash']
    if value in malicious_samples:
        return {
            'reputation': 'malicious',
            'details': 'Listed in known threat feeds'
        }
    return {
        'reputation': 'benign',
        'details': 'No threat intel match'
    }

def enrich_entities(entities):
    enriched = {}
    for k, v in entities.items():
        enriched[k] = []
        for item in v:
            info = mock_threat_intel(k, item)
            enriched[k].append({
                'value': item,
                'reputation': info['reputation'],
                'details': info['details']
            })
    return enriched
