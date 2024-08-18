import streamlit as st

st.title("🎈 Zoonosis Scoring App")
st.write(
    "The algorithm for the diagnosis " 
    "and management of common zoonoses has " 
    "been developed, incorporating the advice and "
    "comments of GPs and laboratory and infectious "
    "disease specialists."
)
st.subheader("Limitations of the algorithm")
st.markdown("""
* non-exhaustive
* many medical conditions can present with signs
    and symptoms that mimic zoonoses
* Individual variability in the presentations 
    of zoonotic illness
* GPs urged to consult infectious disease specialists
    and medical microbiologists for further guidance
"""
)

st.subheader("Suspect zoonotic infection if the patient has:")
st.multiselect("Any of the following clinical symptoms:", 
               ["fever >= 38°C",
                "fever more than 1 occasion",
                "headache", "chills", "myalgia", 
                "fatigue", "dry cough", 
                "shortness of breath", 
                "general malaise"])
st.multiselect("Any of the following risk factors:", 
               ["Non-household contact with farm "
                "animals or wildlife", 
                "Employment in agriculture, "
                "Meat processing, dairy or "
                "veterinary industries", 
                "Non-work-related contact with "
                "animals esp. cattle, sheep, pigs, "
                "dogs and rodents", 
                "Exposure to animal tissues or "
                "animal products e.g. birth fluids",
                "Involvement in feral pig hunting, "
                "carcass processing, transporting "
                "or inspection for export",
                "Tick bites"])

