import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the rules for risk assessment
lifestyle_rules = [
    ("Multiple sexual partners", "higher"),
    ("Early sexual activity", "higher"),
    ("History of HPV infection", "higher"),
    ("Practices safe sex with condoms", "lower"),
    ("Smoker", "higher"),
    ("Weakened immune system", "higher"),
    ("Long-term oral contraceptive use", "slightly higher"),
    ("Unhealthy diet", "higher"),
    ("Obesity or overweight", "higher"),
    ("Healthy lifestyle", "lower")
]

family_history_rules = [
    ("Presence of specific gene variations", "higher"),
    ("Family history of cervical cancer", "slightly higher"),
    ("Diagnosis of Lynch syndrome or Cowden syndrome", "higher"),
    ("No genetic predisposition, familial clustering, or inherited conditions", "lower")
]

symptoms_rules = [
    ("Abnormal vaginal bleeding", "possible"),
    ("Unusual vaginal discharge", "possible"),
    ("Persistent pelvic pain", "possible"),
    ("Pain during sexual intercourse", "possible"),
    ("Urinary problems", "possible")
]

# Define the fuzzy input variables
age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
age['young'] = fuzz.trimf(age.universe, [20, 20, 40])
age['middle_aged'] = fuzz.trimf(age.universe, [20, 40, 60])
age['old'] = fuzz.trimf(age.universe, [40, 60, 80])

lifestyle = ctrl.Antecedent(np.arange(0, 11, 1), 'lifestyle')
lifestyle.automf(3)

family_history = ctrl.Antecedent(np.arange(0, 11, 1), 'family_history')
family_history.automf(3)

symptoms = ctrl.Antecedent(np.arange(0, 11, 1), 'symptoms')
symptoms.automf(3)

# Define the fuzzy output variable
risk = ctrl.Consequent(np.arange(0, 11, 1), 'risk')
risk['low'] = fuzz.trimf(risk.universe, [0, 0, 5])
risk['medium'] = fuzz.trimf(risk.universe, [0, 5, 10])
risk['high'] = fuzz.trimf(risk.universe, [5, 10, 10])

# Define the fuzzy membership functions and rules
rule1 = ctrl.Rule(age['young'] & lifestyle['low'] & family_history['low'] & symptoms['low'], risk['low'])
rule2 = ctrl.Rule(age['middle_aged'] & lifestyle['average'] & family_history['average'] & symptoms['average'], risk['medium'])
rule3 = ctrl.Rule(age['old'] & lifestyle['high'] & family_history['high'] & symptoms['high'], risk['high'])

# Create the fuzzy control system
risk_assessment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
risk_assessment = ctrl.ControlSystemSimulation(risk_assessment_ctrl)

# Streamlit app
st.title("GynoCare - Cervical Cancer Diagnosis and Treatment Recommendations")
st.subheader("Please answer the following questions to assess your risk of cervical cancer.")

# Age question
st.header("Age")
age_input = st.slider("Select your age:", 20, 80)

# Lifestyle questions
st.header("Lifestyle Factors")
lifestyle_input = {}
for i, (question, _) in enumerate(lifestyle_rules):
    answer = st.radio(f"{i+1}. {question}?", ("Yes", "No"))
    if answer == "Yes":
        lifestyle_input[i] = 1
    else:
        lifestyle_input[i] = 0

# Family history questions
st.header("Family History")
family_history_input = {}
for i, (question, _) in enumerate(family_history_rules):
    answer = st.radio(f"{i+1}. {question}?", ("Yes", "No"))
    if answer == "Yes":
        family_history_input[i] = 1
    else:
        family_history_input[i] = 0

# Symptoms questions
st.header("Symptoms")
symptoms_input = {}
for i, (question, _) in enumerate(symptoms_rules):
    answer = st.radio(f"{i+1}. {question}?", ("Yes", "No"))
    if answer == "Yes":
        symptoms_input[i] = 1
    else:
        symptoms_input[i] = 0

# Add a submit button
submit_button = st.button("Submit")

# Execute when the submit button is clicked
if submit_button:
    # Set the input values for fuzzy reasoning
    risk_assessment.input['age'] = age_input
    risk_assessment.input['lifestyle'] = sum(lifestyle_input.values())
    risk_assessment.input['family_history'] = sum(family_history_input.values())
    risk_assessment.input['symptoms'] = sum(symptoms_input.values())

    # Perform fuzzy reasoning
    risk_assessment.compute()

    # Get the final risk assessment result
    final_risk = risk_assessment.output['risk']

    # Display the risk assessment result
    st.subheader("Risk Assessment Result")
    st.write(f"Your preliminary risk of cervical cancer is: {final_risk:.2f} out of 10")

    # Display additional information or recommendations based on the risk level
    if final_risk < 3:
        st.subheader("Recommendations")
        st.write("Based on your risk assessment, your risk of cervical cancer is low. However, it is still important to maintain regular screenings and follow preventive measures such as HPV vaccination. Please consult with your healthcare provider for further guidance.")
    elif final_risk >= 3 and final_risk < 7:
        st.subheader("Recommendations")
        st.write("Based on your risk assessment, your risk of cervical cancer is moderate. It is recommended to schedule regular screenings, such as Pap tests and HPV testing, as advised by your healthcare provider. Additionally, maintaining a healthy lifestyle and following safe sex practices can further reduce your risk.")
    else:
        st.subheader("Recommendations")
        st.write("Based on your risk assessment, your risk of cervical cancer is high. It is crucial to consult with your healthcare provider for further evaluation and follow their recommended screenings, tests, and treatment options. Lifestyle changes, such as quitting smoking and adopting a healthy diet, can also be beneficial.")

    # Perform further actions or calculations if needed
    # (Add code for further actions or calculations)
