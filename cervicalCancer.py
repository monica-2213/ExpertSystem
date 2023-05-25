import streamlit as st

def calculate_cervical_cancer_risk(answers):
    risk_score = 0
    
    if answers['sexual_partners'] == 'Yes':
        risk_score += 1
    
    if answers['sexual_activity_age'] == 'Yes':
        risk_score += 1
    
    if answers['hpv_infection'] == 'Yes':
        risk_score += 1
    
    if answers['safe_sex'] == 'Yes':
        risk_score -= 1
    
    if answers['smoker'] == 'Yes':
        risk_score += 1
    
    if answers['weakened_immune_system'] == 'Yes':
        risk_score += 1
    
    if answers['contraceptive_use'] == 'Yes':
        risk_score += 0.5
    
    if answers['diet'] == 'Low in fruits and vegetables, high in processed foods':
        risk_score += 1
    
    if answers['weight'] == 'Yes':
        risk_score += 1
    
    if answers['exercise'] == 'Regularly active and engage in physical exercise':
        risk_score -= 1
    
    if answers['gene_variations'] == 'Yes':
        risk_score += 1
    
    if answers['family_history'] == 'Yes':
        risk_score += 0.5
    
    if answers['abnormal_bleeding'] == 'Yes':
        st.warning('Abnormal vaginal bleeding is present. Consider the possibility of cervical cancer.')
    
    if answers['unusual_discharge'] == 'Yes':
        st.warning('Unusual vaginal discharge is present. Consider the possibility of cervical cancer.')
    
    if answers['pelvic_pain'] == 'Yes':
        st.warning('Persistent pelvic pain is reported. Consider the possibility of advanced cervical cancer.')
    
    if answers['pain_during_intercourse'] == 'Yes':
        st.warning('Pain during sexual intercourse (dyspareunia) is reported. Consider the possibility of cervical cancer.')
    
    if answers['urinary_problems'] == 'Yes':
        st.warning('Urinary problems are present. Consider the possibility of advanced cervical cancer.')
    
    risk_percentage = (risk_score / 12) * 100
    return risk_percentage

# Streamlit app
def main():
    st.title('GynoCare - Cervical Cancer Risk Assessment')
    st.write('Answer the following questions to assess your risk for cervical cancer.')

    # Questions
    questions = {
        'age': 'How old are you?',
        'sexual_partners': 'Have you ever had multiple sexual partners?',
        'sexual_activity_age': 'Did you engage in sexual activity at an early age?',
        'hpv_infection': 'Have you ever been diagnosed with HPV infection?',
        'safe_sex': 'Do you consistently practice safe sex and use condoms?',
        'smoker': 'Do you currently smoke?',
        'weakened_immune_system': 'Do you have a weakened immune system due to a medical condition or immunosuppressant medications?',
        'contraceptive_use': 'Have you used oral contraceptives for a long time?',
        'diet': 'How would you describe your diet?',
        'weight': 'Do you have obesity or are you overweight?',
        'exercise': 'How would you describe your physical activity level?',
        'family_history': 'Are there any close relatives who have been diagnosed with cervical cancer?',
        'gene_variations': 'Have you been tested for specific gene variations associated with cervical cancer susceptibility?',
        'abnormal_bleeding': 'Have you experienced abnormal vaginal bleeding?',
        'unusual_discharge': 'Have you noticed unusual vaginal discharge that is watery, bloody, or has a foul odor?',
        'pelvic_pain': 'Have you been experiencing persistent pelvic pain in the pelvis, lower back, or abdomen?',
        'pain_during_intercourse': 'Do you experience pain during sexual intercourse (dyspareunia)?',
        'urinary_problems': 'Have you experienced urinary problems such as blood in the urine (hematuria), urinary incontinence, or frequent urination?'
    }

    answers = {}

    # Display questions and collect answers
    for key, question in questions.items():
        if key == 'age':
            answers[key] = st.number_input(question, min_value=0, max_value=100)
        else:
            answers[key] = st.radio(question, ['No', 'Yes'])

    if st.button('Submit'):
        # Calculate risk score
        risk_percentage = calculate_cervical_cancer_risk(answers)

        # Display risk assessment
        st.subheader('Risk Assessment')
        st.write(f'Your risk score for cervical cancer: {risk_percentage:.2f}%')

        # Provide recommendations based on risk score
        st.subheader('Recommendations')
        if risk_percentage >= 30:
            st.warning('Based on your risk score, it is recommended to consult with a healthcare professional for further evaluation and screening.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')

if __name__ == '__main__':
    main()
