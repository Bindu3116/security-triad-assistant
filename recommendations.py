def generate_recommendations(enriched, score):
    recs = []

    if score >= 60:
        recs.append("Investigate and block malicious IP/domain.")
        recs.append("Isolate affected endpoints.")
    elif 30 <= score < 60:
        recs.append("Monitor the entities for suspicious activity.")
        recs.append("Escalate to Tier 2 analyst.")
    else:
        recs.append("Mark as low priority.")
    
    return recs
