import streamlit as st

def calculate_cervical_cancer_risk(answers):
    risk_score = 0
    
    # Calculate risk score based on answers
    if answers['sexual_partners'] == 'Yes':
        risk_score += 10

    if answers['early_sexual_activity'] == 'Yes':
        risk_score += 5

    if answers['hpv_infection'] == 'Yes':
        risk_score += 15

    if answers['safe_sex'] == 'Yes':
        risk_score -= 5

    if answers['smoking'] == 'Yes':
        risk_score += 10

    if answers['weakened_immune_system'] == 'Yes':
        risk_score += 10

    if answers['long_term_contraceptive_use'] == 'Yes':
        risk_score += 5

    if answers['diet'] == 'Low in fruits and vegetables, high in processed foods':
        risk_score += 10

    if answers['obesity'] == 'Yes':
        risk_score += 10

    if answers['physical_activity'] == 'Sedentary':
        risk_score += 10
    elif answers['physical_activity'] == 'Moderately active':
        risk_score -= 5

    if answers['family_history'] == 'Yes':
        risk_score += 5

    if answers['gene_testing'] == 'Yes':
        risk_score += 10

    if answers['lynch_or_cowden_syndrome'] == 'Yes':
        risk_score += 15

    if answers['abnormal_bleeding'] == 'Yes':
        risk_score += 5

    if answers['unusual_discharge'] == 'Yes':
        risk_score += 5

    if answers['pelvic_pain'] == 'Yes':
        risk_score += 5

    if answers['pain_during_intercourse'] == 'Yes':
        risk_score += 5

    if answers['urinary_problems'] == 'Yes':
        risk_score += 5

    # Convert risk score to percentage
    risk_percentage = (risk_score / 120) * 100

    return risk_percentage

def main():
    st.title('GynoCare: Cervical Cancer Risk Assessment')
    st.subheader('Answer the following questions to assess your risk for cervical cancer.')

    questions = {
        'age': 'How old are you?',
        'sexual_partners': 'Have you ever had multiple sexual partners?',
        'early_sexual_activity': 'Did you engage in sexual activity at an early age?',
        'hpv_infection': 'Have you ever been diagnosed with HPV infection?',
        'safe_sex': 'Do you consistently practice safe sex and use condoms?',
        'smoking': 'Do you currently smoke?',
        'weakened_immune_system': 'Do you have a weakened immune system due to a medical condition or immunosuppressant medications?',
        'long_term_contraceptive_use': 'Have you used oral contraceptives for a long time?',
        'diet': 'How would you describe your diet?',
        'obesity': 'Do you have obesity or are you overweight?',
        'physical_activity': 'How would you describe your physical activity level?',
        'family_history': 'Are there any close relatives (mother, sister, etc.) who have been diagnosed with cervical cancer?',
        'gene_testing': 'Have you been tested for specific gene variations associated with cervical cancer susceptibility?',
        'lynch_or_cowden_syndrome': 'Have you been diagnosed with Lynch syndrome or Cowden syndrome?',
        'abnormal_bleeding': 'Have you experienced abnormal vaginal bleeding?',
        'unusual_discharge': 'Have you noticed unusual vaginal discharge that is watery, bloody, or has a foul odor?',
        'pelvic_pain': 'Have you been experiencing persistent pelvic pain in the pelvis, lower back, or abdomen?',
        'pain_during_intercourse': 'Do you experience pain during sexual intercourse (dyspareunia)?',
        'urinary_problems': 'Have you experienced urinary problems such as blood in the urine (hematuria), urinary incontinence, or frequent urination?'
    }

    answers = {}
    for key, question in questions.items():
        if key == 'diet':
            options = ['Low in fruits and vegetables, high in processed foods', 'Balanced and healthy']
            answers[key] = st.selectbox(question, options)
        elif key == 'physical_activity':
            options = ['Sedentary', 'Moderately active', 'Regularly active and engage in physical exercise']
            answers[key] = st.selectbox(question, options)
        else:
            answers[key] = st.radio(question, ['Yes', 'No'])

    if st.button('Submit'):
        risk_percentage = calculate_cervical_cancer_risk(answers)
        st.subheader('Risk Assessment:')
        st.write(f'Your risk score for cervical cancer: {risk_percentage:.2f}%')

        if risk_percentage >= 50:
            st.warning('Your risk score indicates a higher risk for cervical cancer. We recommend consulting with a healthcare professional for further evaluation and screening.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')

if __name__ == '__main__':
    main()
