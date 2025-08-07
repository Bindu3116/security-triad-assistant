def score_alert(enriched):
    score = 0
    for entity_type in enriched:
        for entity in enriched[entity_type]:
            if entity['reputation'] == 'malicious':
                score += 20
            elif entity['reputation'] == 'unknown':
                score += 10
    return min(score, 100)
