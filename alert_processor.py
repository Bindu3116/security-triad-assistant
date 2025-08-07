from enrichment import enrich_entities
from scoring import score_alert
from recommendations import generate_recommendations
from utils import extract_entities

def process_alert(alert):
    # Step 1: Extract entities
    entities = extract_entities(alert)

    # Step 2: Enrich entities (mock threat intel)
    enriched = enrich_entities(entities)

    # Step 3: Score the alert
    risk_score = score_alert(enriched)

    # Step 4: Generate Recommendations
    recs = generate_recommendations(enriched, risk_score)

    return {
        "entities": enriched,
        "risk_score": risk_score,
        "recommendations": recs
    }
