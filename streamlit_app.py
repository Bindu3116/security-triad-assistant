import streamlit as st
import json
from alert_processor import process_alert

st.set_page_config(page_title="Security Alert Triage Assistant", layout="centered")

st.title("🔐 Security Alert Triage Assistant")
st.markdown("Paste a raw JSON alert or upload a `.json` file to begin analysis.")

# Alert input area
uploaded_file = st.file_uploader("Upload a JSON alert file", type="json")
raw_json = st.text_area("Or paste alert JSON here", height=200)

alert = None

if uploaded_file:
    alert = json.load(uploaded_file)
elif raw_json:
    try:
        alert = json.loads(raw_json)
    except Exception as e:
        st.error("Invalid JSON. Please check your formatting.")

if alert:
    st.subheader("🧠 Parsed Alert")
    st.json(alert)

    if st.button("🚀 Process Alert"):
        with st.spinner("Processing..."):
            result = process_alert(alert)

        st.success("Triage complete!")

        st.subheader("🔍 Extracted Entities")
        for entity_type, values in result["entities"].items():
            st.markdown(f"**{entity_type.upper()}**")
            for v in values:
                st.markdown(f"- `{v['value']}` → {v['reputation'].upper()} – _{v['details']}_")

        st.subheader("⚖️ Risk Score")
        risk = result["risk_score"]
        risk_color = "green" if risk < 30 else "orange" if risk < 60 else "red"
        st.markdown(f"<h2 style='color:{risk_color}'>{risk} / 100</h2>", unsafe_allow_html=True)

        st.subheader("✅ Recommendations")
        for r in result["recommendations"]:
            st.markdown(f"- {r}")
