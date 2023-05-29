import streamlit as st

knowledge_base = {
    'age': {
        'risk_factor': 2,
        'rules': {
            'age >= 60': 0,
            'age >= 35 and age <= 44': 2
        }
    },
    'multiple_partners': {
        'risk_factor': 2,
        'rules': {
            'multiple_partners == "Yes"': 2
        }
    },
    'early_sexual_activity': {
        'risk_factor': 2,
        'rules': {
            'early_sexual_activity == "Yes"': 2
        }
    },
    'hpv_infection': {
        'risk_factor': 2,
        'rules': {
            'hpv_infection == "Yes"': 2
        }
    },
    'safe_sex': {
        'risk_factor': 2,
        'rules': {
            'safe_sex == "No"': 2
        }
    },
    'smoking': {
        'risk_factor': 2,
        'rules': {
            'smoking == "Yes"': 2
        }
    },
    'weakened_immune_system': {
        'risk_factor': 2,
        'rules': {
            'weakened_immune_system == "Yes"': 2
        }
    },
    'long_term_oral_contraceptives': {
        'risk_factor': 2,
        'rules': {
            'long_term_oral_contraceptives == "Yes"': 2
        }
    },
    'diet': {
        'risk_factor': 2,
        'rules': {
            'diet == "Low in fruits and vegetables, high in processed foods"': 2
        }
    },
    'obesity_overweight': {
        'risk_factor': 2,
        'rules': {
            'obesity_overweight == "Yes"': 2
        }
    },
    'physical_activity': {
        'risk_factor': 2,
        'rules': {
            'physical_activity == "Sedentary"': 2,
            'physical_activity == "Moderately active"': 1,
            'physical_activity == "Regularly active and engage in physical exercise"': 0
        }
    },
    'family_history': {
        'risk_factor': 2,
        'rules': {
            'family_history == "Yes"': 2
        }
    },
    'gene_variations': {
        'risk_factor': 2,
        'rules': {
            'gene_variations == "Yes"': 2
        }
    },
    'lynch_or_cowden_syndrome': {
        'risk_factor': 2,
        'rules': {
            'lynch_or_cowden_syndrome == "Yes"': 2
        }
    },
    'abnormal_bleeding': {
        'risk_factor': 2,
        'rules': {
            'abnormal_bleeding == "Yes"': 2
        }
    },
    'unusual_discharge': {
        'risk_factor': 2,
        'rules': {
            'unusual_discharge == "Yes"': 2
        }
    },
    'pelvic_pain': {
        'risk_factor': 2,
        'rules': {
            'pelvic_pain == "Yes"': 2
        }
    },
    'pain_during_intercourse': {
        'risk_factor': 2,
        'rules': {
            'pain_during_intercourse == "Yes"': 2
        }
    },
    'urinary_problems': {
        'risk_factor': 2,
        'rules': {
            'urinary_problems == "Yes"': 2
        }
    }
}

#Function for UI
def layout():
    st.title('Cervical Cancer Risk Assessment')
    
    st.markdown('<style>h1, p { color: #003744; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    st.markdown('<style>h2, p { color: #B72552; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    st.markdown('<style>p, p { color: #7F1330; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    
    st.header('Please provide the following information to assess your risk for cervical cancer.')

    # Use beta_expander to collapse and expand sections
    with st.beta_expander('Demographics'):
        st.markdown('#### Age')
        age = st.number_input('How old are you?', min_value=1, max_value=100, step=1)

    with st.beta_expander('Sexual History'):
        st.markdown('#### Multiple Sexual Partners')
        multiple_partners = st.radio('Have you ever had multiple sexual partners?', ['Yes', 'No'])

        st.markdown('#### Early Sexual Activity')
        early_sexual_activity = st.radio('Did you engage in sexual activity at an early age?', ['Yes', 'No'])

        st.markdown('#### HPV Infection')
        hpv_infection = st.radio('Have you ever been diagnosed with HPV infection?', ['Yes', 'No'])

        st.markdown('#### Safe Sex Practices')
        safe_sex = st.radio('Do you consistently practice safe sex and use condoms?', ['Yes', 'No'])

    with st.beta_expander('Lifestyle Factors'):
        st.markdown('#### Smoking')
        smoking = st.radio('Do you currently smoke?', ['Yes', 'No'])

        st.markdown('#### Weakened Immune System')
        weakened_immune_system = st.radio('Do you have a weakened immune system due to a medical condition or immunosuppressant medications?', ['Yes', 'No'])

        st.markdown('#### Long-term Oral Contraceptives')
        long_term_oral_contraceptives = st.radio('Have you used oral contraceptives for a long time?', ['Yes', 'No'])

        st.markdown('#### Diet')
        diet = st.selectbox('How would you describe your diet?', ['Low in fruits and vegetables, high in processed foods', 'Balanced and healthy'])

        st.markdown('#### Obesity or Overweight')
        obesity_overweight = st.radio('Do you have obesity or are you overweight?', ['Yes', 'No'])

        st.markdown('#### Physical Activity')
        physical_activity = st.selectbox('How would you describe your physical activity level?', ['Sedentary', 'Moderately active', 'Regularly active and engage in physical exercise'])

    with st.beta_expander('Family History and Medical Conditions'):
        st.markdown('#### Family History')
        family_history = st.radio('Are there any close relatives (mother, sister, etc.) who have been diagnosed with cervical cancer?', ['Yes', 'No'])

        st.markdown('#### Gene Variations')
        gene_variations = st.radio('Have you been tested for specific gene variations associated with cervical cancer susceptibility?', ['Yes', 'No'])

        st.markdown('#### Lynch or Cowden Syndrome')
        lynch_or_cowden_syndrome = st.radio('Have you been diagnosed with Lynch syndrome or Cowden syndrome?', ['Yes', 'No'])

        st.markdown('#### Abnormal Bleeding')
        abnormal_bleeding = st.radio('Have you experienced abnormal vaginal bleeding?', ['Yes', 'No'])

        st.markdown('#### Unusual Discharge')
        unusual_discharge = st.radio('Have you noticed unusual vaginal discharge that is watery, bloody, or has a foul odor?', ['Yes', 'No'])

        st.markdown('#### Pelvic Pain')
        pelvic_pain = st.radio('Have you been experiencing persistent pelvic pain in the pelvis, lower back, or abdomen?', ['Yes', 'No'])

        st.markdown('#### Pain During Intercourse')
        pain_during_intercourse = st.radio('Do you experience pain during sexual intercourse (dyspareunia)?', ['Yes', 'No'])

        st.markdown('#### Urinary Problems')
        urinary_problems = st.radio('Have you experienced urinary problems such as blood in the urine (hematuria), urinary incontinence, or frequent urination?', ['Yes', 'No'])

    if st.button('Submit'):
        answers = {
            'age': age,
            'multiple_partners': multiple_partners,
            'early_sexual_activity': early_sexual_activity,
            'hpv_infection': hpv_infection,
            'safe_sex': safe_sex,
            'smoking': smoking,
            'weakened_immune_system': weakened_immune_system,
            'long_term_oral_contraceptives': long_term_oral_contraceptives,
            'diet': diet,
            'obesity_overweight': obesity_overweight,
            'physical_activity': physical_activity,
            'family_history': family_history,
            'gene_variations': gene_variations,
            'lynch_or_cowden_syndrome': lynch_or_cowden_syndrome,
            'abnormal_bleeding': abnormal_bleeding,
            'unusual_discharge': unusual_discharge,
            'pelvic_pain': pelvic_pain,
            'pain_during_intercourse': pain_during_intercourse,
            'urinary_problems': urinary_problems
        }

        risk_percentage, factor_scores = calculate_risk_score(answers)
        explanation = generate_explanation(factor_scores)

        st.write('Your risk score for cervical cancer:', f'{risk_percentage:.2f}%')
        if risk_percentage >= 50:
            st.warning('Based on your risk score, you have a relatively higher risk for cervical cancer. Please consult with your healthcare provider for further evaluation and recommendations.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')
        st.write('Your risk score is calculated based on various risk factors for cervical cancer. The higher the risk score, the higher the probability of developing cervical cancer. The factors that contributed most to your risk score include...')
        st.write(explanation)
        
        recommend_medical_tests()
        provide_treatment_recommendations()
        provide_helplines()
        

#Function to calculate the risk score/percentage
def calculate_risk_score(answers):
    total_score = 0
    max_score = 0
    factor_scores = {}

    for factor, value in answers.items():
        if factor in knowledge_base:
            factor_data = knowledge_base[factor]
            max_score += factor_data['risk_factor']
            for rule, score in factor_data['rules'].items():
                if eval(rule, {'__builtins__': None}, answers):
                    total_score += factor_data['risk_factor']
                    factor_scores[factor] = factor_scores.get(factor, 0) + factor_data['risk_factor']

    risk_percentage = (total_score / max_score) * 100
    return risk_percentage, factor_scores


def generate_explanation(factor_scores):
    explanation = "Factors contributing to your risk score:\n"
    for factor, score in factor_scores.items():
        explanation += f"- {factor}: {score}\n"
    return explanation

def recommend_medical_tests():
    st.header('Recommended Medical Tests and Screenings')
    st.markdown('- Pap test: Recommended for all individuals with a cervix, starting at the age of 21 or within 3 years of becoming sexually active. It should be repeated every 3 years for individuals aged 21-65 who have a normal result.')
    st.markdown('- HPV testing: In addition to the Pap test, HPV testing may be recommended for individuals aged 30 and above as part of cervical cancer screening. Talk to your healthcare provider for more information about HPV testing and its frequency.')

def provide_treatment_recommendations():
    st.header('Treatment Recommendations')
    st.markdown('- If your risk score indicates a higher risk for cervical cancer, it is important to consult with your healthcare provider for further evaluation and recommendations.')
    st.markdown('- Treatment options for cervical cancer may include surgery, radiation therapy, chemotherapy, or a combination of these approaches. The choice of treatment depends on the stage of cancer, overall health, and individual preferences. Your healthcare provider will guide you through the treatment decision-making process.')

def provide_helplines():
    st.header('Helplines (Malaysia)')
    st.markdown('- Cancer Helpline: 1-800-88-1000')
    st.markdown('- National Population and Family Development Board (LPPKN): 03-7953 6655')
    st.markdown('- Malaysian AIDS Council: 03-4047 7000')
    st.markdown('- Talian Kasih: 15999 (24-hour helpline for survivors of domestic violence, sexual abuse, and other related issues)')

    
def main():
    layout()
    
if __name__ == '__main__':
    main()
