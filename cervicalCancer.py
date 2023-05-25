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

family_history = ctrl.Antecedent(np.arange(0, 11, 1), 'family_history')
family_history['low'] = fuzz.trimf(family_history.universe, [0, 0, 5])
family_history['medium'] = fuzz.trimf(family_history.universe, [0, 5, 10])
family_history['high'] = fuzz.trimf(family_history.universe, [5, 10, 10])

# Define the fuzzy output variable
risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')
risk['low'] = fuzz.trimf(risk.universe, [0, 0, 25])
risk['medium'] = fuzz.trimf(risk.universe, [0, 25, 75])
risk['high'] = fuzz.trimf(risk.universe, [25, 75, 100])

# Define the fuzzy membership functions and rules
rule1 = ctrl.Rule(age['young'] | age['middle_aged'], risk['low'])
rule2 = ctrl.Rule(age['old'], risk['medium'])

rule3 = ctrl.Rule(family_history['low'], risk['low'])
rule4 = ctrl.Rule(family_history['medium'], risk['medium'])
rule5 = ctrl.Rule(family_history['high'], risk['high'])

# Create the fuzzy control system
risk_assessment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
risk_assessment = ctrl.ControlSystemSimulation(risk_assessment_ctrl)

# Streamlit app
st.title("Cervical Cancer Risk Assessment")
st.subheader("Please answer the following questions to assess your risk of cervical cancer.")

# Age question
st.header("Demographics")
age_input = st.slider("Select your age:", 20, 80)

# Family history question
st.header("Family History")
family_history_input = st.radio("Do you have any family history of cervical cancer?", ("Yes", "No"))

# Set the inputs for fuzzy reasoning
risk_assessment.input['age'] = age_input
if family_history_input == "Yes":
    risk_assessment.input['family_history'] = 5  # Assign a medium value for family history
else:
    risk_assessment.input['family_history'] = 0  # Assign a low value for no family history

# Lifestyle questions
st.header("Lifestyle Factors")
for i, (question, _) in enumerate(lifestyle_rules):
    answer = st.radio(f"{i+1}. {question}?", ("Yes", "No"))
    if answer == "Yes":
        # Update the fuzzy risk assessment based on the lifestyle factor
        risk_assessment.compute()

# Symptoms questions
st.header("Symptoms")
for i, (question, _) in enumerate(symptoms_rules):
    answer = st.radio(f"{i+1}. {question}?", ("Yes", "No"))
    if answer == "Yes":
        # Update the fuzzy risk assessment based on the symptoms factor
        risk_assessment.compute()

# Add a submit button
submit_button = st.button("Submit")

# Execute when the submit button is clicked
if submit_button:
    # Perform fuzzy reasoning based on user inputs
    risk_assessment.compute()

    # Get the final risk assessment result
    final_risk = risk_assessment.output['risk']

    # Display the risk assessment result
    st.subheader("Risk Assessment Result")
    st.write(f"Your preliminary risk of cervical cancer is: {final_risk:.2f}%")

    # Display additional information or recommendations based on the risk level if desired
    # (Add code to display additional information or recommendations)

    # Perform further actions or calculations if needed
    # (Add code for further actions or calculations)