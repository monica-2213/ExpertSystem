import streamlit as st

def calculate_cervical_cancer_risk(answers):
    risk_score = 0
    
    if answers['sexual_partners'] == 'Multiple':
        risk_score += 1
    
    if answers['sexual_activity_age'] == 'Early':
        risk_score += 1
    
    if answers['hpv_infection']:
        risk_score += 1
    
    if answers['safe_sex']:
        risk_score -= 1
    
    if answers['smoker']:
        risk_score += 1
    
    if answers['weakened_immune_system']:
        risk_score += 1
    
    if answers['contraceptive_use'] == 'Long-term':
        risk_score += 0.5
    
    if answers['diet'] == 'Unhealthy':
        risk_score += 1
    
    if answers['weight'] == 'Obese':
        risk_score += 1
    
    if answers['exercise']:
        risk_score -= 1
    
    if answers['gene_variations']:
        risk_score += 1
    
    if answers['family_history'] == 'Close relatives':
        risk_score += 0.5
    
    if answers['inherited_conditions']:
        risk_score += 1
    
    if answers['abnormal_bleeding']:
        st.warning('Abnormal vaginal bleeding is present. Consider the possibility of cervical cancer.')
    
    if answers['unusual_discharge']:
        st.warning('Unusual vaginal discharge is present. Consider the possibility of cervical cancer.')
    
    if answers['pelvic_pain']:
        st.warning('Persistent pelvic pain is reported. Consider the possibility of advanced cervical cancer.')
    
    if answers['pain_during_intercourse']:
        st.warning('Pain during sexual intercourse (dyspareunia) is reported. Consider the possibility of cervical cancer.')
    
    if answers['urinary_problems']:
        st.warning('Urinary problems are present. Consider the possibility of advanced cervical cancer.')
    
    return risk_score

# Streamlit app
def main():
    st.title('GynoCare - Cervical Cancer Risk Assessment')
    st.write('Answer the following questions to assess your risk for cervical cancer.')

    # Questions
    questions = {
        'sexual_partners': 'How many sexual partners have you had?',
        'sexual_activity_age': 'At what age did you first engage in sexual activity?',
        'hpv_infection': 'Have you ever had an HPV infection?',
        'safe_sex': 'Do you consistently practice safe sex and use condoms?',
        'smoker': 'Do you smoke?',
        'weakened_immune_system': 'Do you have a weakened immune system due to a medical condition or medications?',
        'contraceptive_use': 'What is the duration of your long-term oral contraceptive use?',
        'diet': 'How would you describe your diet?',
        'weight': 'What is your current weight status?',
        'exercise': 'Do you engage in regular physical activity?',
        'gene_variations': 'Do you have any known gene variations associated with cervical cancer susceptibility?',
        'family_history': 'Is there a family history of cervical cancer among close relatives?',
        'inherited_conditions': 'Do you have a known diagnosis of Lynch syndrome or Cowden syndrome?',
        'abnormal_bleeding': 'Are you experiencing abnormal vaginal bleeding?',
        'unusual_discharge': 'Are you experiencing unusual vaginal discharge (watery, bloody, or foul odor)?',
        'pelvic_pain': 'Are you experiencing persistent pelvic pain?',
        'pain_during_intercourse': 'Are you experiencing pain during sexual intercourse?',
        'urinary_problems': 'Are you experiencing urinary problems (blood in urine, urinary incontinence, frequent urination)?'
    }

    answers = {}

    # Display questions and collect answers
    for key, question in questions.items():
        answers[key] = st.radio(question, ['No', 'Yes'])

    # Calculate risk score
    risk_score = calculate_cervical_cancer_risk(answers)

    # Display risk assessment
    st.subheader('Risk Assessment')
    st.write(f'Your risk score for cervical cancer: {risk_score}')

    # Provide recommendations based on risk score
    st.subheader('Recommendations')
    if risk_score >= 3:
        st.warning('Based on your risk score, it is recommended to consult with a healthcare professional for further evaluation and screening.')
    else:
        st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')

if __name__ == '__main__':
    main()
