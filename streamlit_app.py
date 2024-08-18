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
risk_factors = []
exclusion_list = []
st.subheader("Suspect zoonotic infection if the patient has:")
clinical_symptoms = st.multiselect("Any of the following clinical symptoms:", 
               ["fever >= 38°C",
                "fever more than 1 occasion",
                "headache", "chills", "myalgia", 
                "fatigue", "dry cough", 
                "shortness of breath", 
                "general malaise"])

st.write("AND")
st.markdown("Any of the following risk factors:")
risk_factors.append(st.checkbox("Non-household contact with farm "
            "animals or wildlife"))
risk_factors.append(st.checkbox("Employment in agriculture, "
            "meat processing, dairy or "
            "veterinary industries"))
risk_factors.append(st.checkbox("Non-work-related contact with "
            "animals esp. cattle, sheep, pigs, "
            "dogs and rodents"))
risk_factors.append(st.checkbox("Exposure to animal tissues or "
            "animal products e.g. birth fluids"))
risk_factors.append(st.checkbox("Involvement in feral pig hunting, "
            "carcass processing, transporting "
            "or inspection for export"))
risk_factors.append(st.checkbox("Tick bites"))

st.write("AND")

st.markdown("Other common causes of fever excluded such as:")
exclusion_list.append(st.toggle("Influenza"))
exclusion_list.append(st.toggle("Urinary tract infection"))
exclusion_list.append(st.toggle("Cellulitis"))
st.write("through basic investigations such as "
         "FBC, EUC, LFTs, CRP, urinalysis, "
         "influenza rapid test/PCR, "
         "if appropriate, blood cultures, CXR")


