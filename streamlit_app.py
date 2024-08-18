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

st.write("AND")
st.markdown("Any of the following risk factors:")
st.checkbox("Non-household contact with farm "
            "animals or wildlife")
st.checkbox("Employment in agriculture, "
            "meat processing, dairy or "
            "veterinary industries")
st.checkbox("Non-work-related contact with "
            "animals esp. cattle, sheep, pigs, "
            "dogs and rodents")
st.checkbox("Exposure to animal tissues or "
            "animal products e.g. birth fluids")
st.checkbox("Involvement in feral pig hunting, "
            "carcass processing, transporting "
            "or inspection for export")
st.checkbox("Tick bites")

st.write("AND")

st.markdown("Other common causes of fever excluded such as:")
st.toggle("Influenza")
st.toggle("Urinary tract infection")
st.toggle("Cellulitis")
st.write("through basic investigations such as "
         "FBC, EUC, LFTs, CRP, urinalysis, "
         "influenza rapid test/PCR, "
         "if appropriate, blood cultures, CXR")

