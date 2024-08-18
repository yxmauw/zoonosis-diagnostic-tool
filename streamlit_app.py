import streamlit as st
import base64

def reset_button():
    st.session_state["1"] = False
    st.session_state["2"] = False
    st.session_state["3"] = False
    st.session_state["4"] = False
    st.session_state["5"] = False
    st.session_state["6"] = False
    return

def clear_none():
    st.session_state["7"] = False
    return

tab1, tab2 = st.tabs(["Home", "Reference"])

with tab1:
    st.title("🪰 Zoonosis Diagnostic Tool")
    with st.expander("DISCLAIMER: THIS WEBSITE DOES "
                "NOT REPLACE MEDICAL ADVICE"):
        st.write("The information, including but not "
                "limited to, text, graphics, images "
                "and other material contained on this "
                "website are for informational purposes "
                "only. No material on this site is "
                "intended to be a substitute for "
                "professional medical advice, diagnosis "
                "or treatment. Always seek the "
                "advice of a physician or other "
                "qualified health care provider "
                "with any questions you may have regarding "
                "a medical condition or treatment and "
                "before undertaking a new health care "
                "regimen, and never disregard professional "
                "medical advice or delay in seeking it "
                "because of something you have read on "
                "this website.")
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
    st.subheader("Suspect zoonotic infection ...")
    st.write(":blue[**if the patient has:**]")
    with st.expander("Any clinical symptoms ..."):
        clinical_symptoms = st.multiselect("Any clinical symptoms:", 
                    ["fever >= 38°C",
                        "fever more than 1 occasion",
                        "headache", "chills", "myalgia", 
                        "fatigue", "dry cough", 
                        "shortness of breath", 
                        "general malaise", 
                        "None of the above"],
                        placeholder="No symptoms",
                        label_visibility="collapsed")
        if "None of the above" in clinical_symptoms:
            st.write("Please proceed to identify risk factors.")

    st.write(":blue[**AND**]")

    with st.expander("Any risk factors ..."):
        risk_factors.append(st.checkbox("Non-household contact with farm "
                    "animals or wildlife", key="1", on_change=clear_none))
        risk_factors.append(st.checkbox("Employment in agriculture, "
                    "meat processing, dairy or "
                    "veterinary industries", key="2", on_change=clear_none))
        risk_factors.append(st.checkbox("Non-work-related contact with "
                    "animals esp. cattle, sheep, pigs, "
                    "dogs and rodents", key="3", on_change=clear_none))
        risk_factors.append(st.checkbox("Exposure to animal tissues or "
                    "animal products e.g. birth fluids", key="4", on_change=clear_none))
        risk_factors.append(st.checkbox("Involvement in feral pig hunting, "
                    "carcass processing, transporting "
                    "or inspection for export", key="5", on_change=clear_none))
        risk_factors.append(st.checkbox("Tick bites", key="6", on_change=clear_none))
        no_risk_factors = st.checkbox("None of the above", key="7", on_change=reset_button)
        if no_risk_factors or any(risk_factors):
            st.write("Please proceed to exclude other "
                    "possible differential diagnoses.")
        
    st.write(":blue[**AND**]")

    with st.expander("Common differential "
                    "diagnoses not yet excluded ..."):
        exclusion_list.append(st.toggle("Influenza"))
        exclusion_list.append(st.toggle("Urinary tract infection"))
        exclusion_list.append(st.toggle("Cellulitis"))
        if any(exclusion_list):
            st.write("Please perform basic investigations such as "
                    "FBC, EUC, LFTs, CRP, urinalysis, "
                    "influenza rapid test/PCR, "
                    "and if appropriate, blood cultures, CXR to "
                    "exclude diagnosis.")


    if len(clinical_symptoms) > 0 and \
            any(risk_factors) and \
            not any(exclusion_list):
        with st.expander("Next steps:"):
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

        with st.expander("Diagnosis"):

            diseases = ["Q fever", "Brucellosis", "Leptospirosis"]
            all_options = ["Q fever", "Brucellosis", "Leptospirosis", "None of the above"]

            diagnosis = st.radio("Diagnosis is", all_options, index=3, label_visibility="collapsed")

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
            if diagnosis == "Q fever":
                with st.container():
                    st.markdown("""
                    ##### Q fever specific:
                    * Assess chronic Q fever risk (e.g. 
                    underlying heart valve defect, vascular 
                    graft, aneurysm or prosthesis)
                    * Consider echocardiogram.
                    * Continue doxycycline treatment for 14 days
                    even if afebrile, to prevent 5% risk of 
                    developing chronic Q fever due to infectious
                    relapse.
                    ###### :red[If at risk of chronic infection:]
                    * Repeat serology at 3, 6, 12 months.
                    ###### :red[If not at risk:]
                    * Repeat serology at 6, 12 months.
                    ###### If clinical and laboratory evidence of chronic Q fever or endocarditis:
                    * Prolonged combination therapy (with addition
                    of rifampicin or hydrochloroquine) may be required.
                    * Seek expert advice from an infectious diseases physician. 
                    """)
            if diagnosis == "Brucellosis":
                with st.container():
                    st.markdown("""
                    ##### Brucellosis specific:
                    * Ask patient to seek medical assistance if
                    symptoms recur.
                    * Seek expert advice if additional treatment
                    required.
                    """)
            if diagnosis == "Leptospirosis":
                with st.container():
                    st.markdown("""
                    ##### Leptospirosis specific:
                    * Follow-up is not usually required
                    after treatment.
                    """)
            if diagnosis not in diseases:
                st.markdown("##### Next step:")
                st.write("Consult an infectious diseases "
                        "physician for further advice.")
            
    if "None of the above" in clinical_symptoms or \
            no_risk_factors:
        st.subheader("Assessment:")
        st.write("Zoonotic infection is of low probability. "
                "Please consider other differential diagnoses.")

with tab2: 
    def display_pdf(filepath):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    display_pdf("zoonoses.pdf")
    st.markdown("[Reference]")
