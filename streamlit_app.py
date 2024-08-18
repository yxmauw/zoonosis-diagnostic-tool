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

if len(clinical_symptoms) > 0 and \
        any(risk_factors) and \
        not any(exclusion_list):
    st.subheader("Next steps:")
    st.write("Commence doxycycline (100mg po bd) "
             "as empirical treatment immediately, "
             "before test results are available. "
             "Alternative: cotrimoxazole")
    st.write("Request tests for 3 diseases in parellel. "
             "5mL clotted blood is needed for **each** "
             "antibody (serology) test, plus an additional "
             "5mL for PCR test.")
    st.markdown("""
        **Q fever**
        * Request _Coxiella burnetii_ PCR testing and 
                serology. 

        **Brucellosis**
        * For people who had contact with feral pigs
        * IgM and IgG of _Brucella_ species on initial
            serum sample.
        * Send another serum sample 5-7 days later
            and ask for serological testing for
            _Brucella spp._ in parallel with earlier
            sample.
                
        **Leptospirosis**
        * IgM and IgG for _Leptospira spp._ on initial
            serum sample.
        * Send another serum sample 5-7 days later
            and ask for serological testing for 
            _Leptospira spp._ in parellel with earlier
            sample.
    """)

st.header("Diagnosis is:")

diseases = ["Q fever", "Brucellosis", "Leptospirosis"]
all_options = ["Q fever", "Brucellosis", "Leptospirosis", "None of the above"]

diagnosis = st.radio("Diagnosis is", all_options, label_visibility="collapsed")

if diagnosis in diseases:
    st.subheader("Management steps:")
    st.markdown("""
                * Treat according to Therapeutic Guidelines: 
                Antibiotic
                * Consult infectious diseases physician in
                all suspected or confirmed cases where diagnosis 
                and treatment are complicated.
                * Consult pathology for advice on intepreting 
                serology.
                * Brucellosis treatment includes 6 weeks rifampicin.
    """)