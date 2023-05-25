import streamlit as st

def calculate_cervical_cancer_risk(answers):
    # Calculate the risk score based on the answers
    risk_score = 0

    if answers['age'] >= 30:
        risk_score += 10

    if answers['multiple_partners'] == 'Yes':
        risk_score += 10

    if answers['early_sexual_activity'] == 'Yes':
        risk_score += 10

    if answers['hpv_infection'] == 'Yes':
        risk_score += 10

    if answers['safe_sex'] == 'No':
        risk_score += 10

    if answers['smoking'] == 'Yes':
        risk_score += 10

    if answers['weakened_immune_system'] == 'Yes':
        risk_score += 10

    if answers['long_term_oral_contraceptives'] == 'Yes':
        risk_score += 5

    if answers['diet'] == 'Low in fruits and vegetables, high in processed foods':
        risk_score += 10

    if answers['obesity_overweight'] == 'Yes':
        risk_score += 10

    if answers['physical_activity'] == 'Sedentary':
        risk_score += 10
    elif answers['physical_activity'] == 'Moderately active':
        risk_score += 5

    if answers['family_history'] == 'Yes':
        risk_score += 10

    if answers['gene_variations'] == 'Yes':
        risk_score += 10

    if answers['lynch_or_cowden_syndrome'] == 'Yes':
        risk_score += 10

    if answers['abnormal_bleeding'] == 'Yes':
        risk_score += 10

    if answers['unusual_discharge'] == 'Yes':
        risk_score += 10

    if answers['pelvic_pain'] == 'Yes':
        risk_score += 10

    if answers['pain_during_intercourse'] == 'Yes':
        risk_score += 10

    if answers['urinary_problems'] == 'Yes':
        risk_score += 10

    # Calculate risk percentage
    risk_percentage = (risk_score / 200) * 100
    return risk_percentage

def main():
    st.title('Cervical Cancer Risk Assessment')
    st.write('Please provide the following information to assess your risk for cervical cancer.')

    questions = {
        'age': 'How old are you?',
        'multiple_partners': 'Have you ever had multiple sexual partners?',
        'early_sexual_activity': 'Did you engage in sexual activity at an early age?',
        'hpv_infection': 'Have you ever been diagnosed with HPV infection?',
        'safe_sex': 'Do you consistently practice safe sex and use condoms?',
        'smoking': 'Do you currently smoke?',
        'weakened_immune_system': 'Do you have a weakened immune system due to a medical condition or immunosuppressant medications?',
        'long_term_oral_contraceptives': 'Have you used oral contraceptives for a long time?',
        'diet': 'How would you describe your diet?',
        'obesity_overweight': 'Do you have obesity or are you overweight?',
        'physical_activity': 'How would you describe your physical activity level?',
        'family_history': 'Are there any close relatives (mother, sister, etc.) who have been diagnosed with cervical cancer?',
        'gene_variations': 'Have you been tested for specific gene variations associated with cervical cancer susceptibility?',
        'lynch_or_cowden_syndrome': 'Have you been diagnosed with Lynch syndrome or Cowden syndrome?',
        'abnormal_bleeding': 'Have you experienced abnormal vaginal bleeding?',
        'unusual_discharge': 'Have you noticed unusual vaginal discharge that is watery, bloody, or has a foul odor?',
        'pelvic_pain': 'Have you been experiencing persistent pelvic pain in the pelvis, lower back, or abdomen?',
        'pain_during_intercourse': 'Do you experience pain during sexual intercourse (dyspareunia)?',
        'urinary_problems': 'Have you experienced urinary problems such as blood in the urine (hematuria), urinary incontinence, or frequent urination?'
    }

    answers = {}

    for key, question in questions.items():
        if key == 'age':
            answers[key] = st.number_input(question, min_value=1, max_value=100, step=1)
        elif key == 'diet':
            answers[key] = st.selectbox(question, [
                'Low in fruits and vegetables, high in processed foods',
                'Balanced and healthy'
            ])
        elif key == 'physical_activity':
            answers[key] = st.selectbox(question, [
                'Sedentary',
                'Moderately active',
                'Regularly active and engage in physical exercise'
            ])
        else:
            answers[key] = st.radio(question, ['Yes', 'No'])

    if st.button('Submit'):
        risk_percentage = calculate_cervical_cancer_risk(answers)

        st.write('Risk Assessment:')
        st.write(f'Your risk score for cervical cancer: {risk_percentage:.2f}%')

        if risk_percentage >= 50:
            st.warning('Based on your risk score, you have a relatively higher risk for cervical cancer. Please consult with your healthcare provider for further evaluation and recommendations.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')

if __name__ == '__main__':
    main()
