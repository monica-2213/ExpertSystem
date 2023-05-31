import streamlit as st

st.set_page_config(page_icon="https://w7.pngwing.com/pngs/583/500/png-transparent-cervical-cancer-screening-cervix-prevent-cancer.png")

# Add custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #08565E;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .colorful-button {
        background-color: #FFFFFF;
        color: #08565E;
    }
    
    .colorful-button: hover{
        background-color: #08565E;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)


knowledge_base = {
    'age': {
        'risk_factor': 2,
        'description': 'Age: Your age can impact your risk for cervical cancer. The risk increases with age.',
        'rules': {
            'age >= 60': 0,
            'age >= 35 and age <= 44': 2
        }
    },
    'multiple_partners': {
        'risk_factor': 2,
        'description': 'Multiple Sexual Partners: Having multiple sexual partners increases the risk of cervical cancer.',
        'rules': {
            'multiple_partners == "Yes"': 2
        }
    },
    'early_sexual_activity': {
        'risk_factor': 2,
        'description': 'Early Sexual Activity: Engaging in sexual activity at a young age is associated with a higher risk of cervical cancer.',
        'rules': {
            'early_sexual_activity == "Yes"': 2
        }
    },
    'hpv_infection': {
        'risk_factor': 2,
        'description': 'HPV Infection: Human papillomavirus (HPV) infection is the most significant risk factor for cervical cancer.',
        'rules': {
            'hpv_infection == "Yes"': 2
        }
    },
    'safe_sex': {
        'risk_factor': 2,
        'description': 'Unsafe Sexual Practices: Not practicing safe sex, such as not using condoms, increases the risk of cervical cancer.',
        'rules': {
            'safe_sex == "No"': 2
        }
    },
    'smoking': {
        'risk_factor': 2,
        'description': 'Smoking: Smoking tobacco can increase the risk of developing cervical cancer.',
        'rules': {
            'smoking == "Yes"': 2
        }
    },
    'weakened_immune_system': {
        'risk_factor': 2,
        'description': 'Weakened Immune System: Having a weakened immune system due to conditions like HIV/AIDS or immunosuppressive therapy can increase the risk of cervical cancer.',
        'rules': {
            'weakened_immune_system == "Yes"': 2
        }
    },
    'long_term_oral_contraceptives': {
        'risk_factor': 2,
        'description': 'Long-term Oral Contraceptives: Taking oral contraceptives for an extended period may slightly increase the risk of cervical cancer.',
        'rules': {
            'long_term_oral_contraceptives == "Yes"': 2
        }
    },
    'diet': {
        'risk_factor': 2,
        'description': 'Diet: A diet low in fruits and vegetables and high in processed foods may increase the risk of cervical cancer.',
        'rules': {
            'diet == "Low in fruits and vegetables, high in processed foods"': 2
        }
    },
    'obesity_overweight': {
        'risk_factor': 2,
        'description': 'Obesity/Overweight: Being overweight or obese is associated with an increased risk of cervical cancer.',
        'rules': {
            'obesity_overweight == "Yes"': 2
        }
    },
    'physical_activity': {
        'risk_factor': 2,
        'description': 'Physical Activity: Being sedentary or having low levels of physical activity may increase the risk of cervical cancer.',
        'rules': {
            'physical_activity == "Sedentary"': 2,
            'physical_activity == "Moderately active"': 1,
            'physical_activity == "Regularly active and engage in physical exercise"': 0
        }
    },
    'family_history': {
        'risk_factor': 2,
        'description': 'Family History: Having a family history of cervical cancer may increase the risk of developing the disease.',
        'rules': {
            'family_history == "Yes"': 2
        }
    },
    'gene_variations': {
        'risk_factor': 2,
        'description': 'Gene Variations: Certain genetic variations or mutations may increase the susceptibility to cervical cancer.',
        'rules': {
            'gene_variations == "Yes"': 2
        }
    },
    'lynch_or_cowden_syndrome': {
        'risk_factor': 2,
        'description': 'Lynch or Cowden Syndrome: Having Lynch syndrome or Cowden syndrome increases the risk of cervical cancer.',
        'rules': {
            'lynch_or_cowden_syndrome == "Yes"': 2
        }
    },
    'abnormal_bleeding': {
        'risk_factor': 2,
        'description': 'Abnormal Bleeding: Experiencing abnormal vaginal bleeding, such as between periods or after intercourse, may indicate an increased risk of cervical cancer.',
        'rules': {
            'abnormal_bleeding == "Yes"': 2
        }
    },
    'unusual_discharge': {
        'risk_factor': 2,
        'description': 'Unusual Discharge: Having unusual vaginal discharge, such as a strong odor or unusual color, may be a sign of an increased risk of cervical cancer.',
        'rules': {
            'unusual_discharge == "Yes"': 2
        }
    },
    'pelvic_pain': {
        'risk_factor': 2,
        'description': 'Pelvic Pain: Persistent pelvic pain or discomfort may indicate an increased risk of cervical cancer.',
        'rules': {
            'pelvic_pain == "Yes"': 2
        }
    },
    'pain_during_intercourse': {
        'risk_factor': 2,
        'description': 'Pain During Intercourse: Experiencing pain or discomfort during sexual intercourse may be a sign of an increased risk of cervical cancer.',
        'rules': {
            'pain_during_intercourse == "Yes"': 2
        }
    },
    'urinary_problems': {
        'risk_factor': 2,
        'description': 'Urinary Problems: Having urinary problems, such as frequent urination or pain during urination, may indicate an increased risk of cervical cancer.',
        'rules': {
            'urinary_problems == "Yes"': 2
        }
    }
}


# Function to calculate the risk score/percentage
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
    return risk_percentage, factor_scores, total_score


# Function to generate the explanation based on user answers
def generate_explanation(answers):
    explanation = []
    
    for factor, value in answers.items():
        if factor in knowledge_base:
            factor_data = knowledge_base[factor]
            factor_description = factor_data['description']
            
            for rule, score in factor_data['rules'].items():
                if eval(rule, {'__builtins__': None}, answers):
                    explanation.append(f"{factor_description}\n")
    
    return explanation


#Function for UI
def layout():
    st.title('Cervical Cancer Risk Assessment')
    
    st.markdown('<style>h1, p { color: #fcfaf2; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    st.markdown('<style>h2, p { color: #fcfbf5; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    st.markdown('<style>p, p { color: #ffffff; font-family: "Arial", sans-serif;}</style>', unsafe_allow_html=True)
    
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
    
    if st.button("Submit", class="colorful-button"):
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
        
        risk_percentage, factor_scores, total_score = calculate_risk_score(answers)
        
        # Color and font size styling
        if risk_percentage >= 50:
            risk_color = 'red'
        else:
            risk_color = 'green'

        risk_style = f"font-size: 24px; color: {risk_color}; font-weight: bold;"

        # Display risk percentage with styling
        st.write('Your risk score for cervical cancer:', f'<span style="{risk_style}">{risk_percentage:.2f}%</span>', unsafe_allow_html=True)
        
        if risk_percentage >= 50:
            st.warning('Based on your risk score, you have a relatively higher risk for cervical cancer. Please consult with your healthcare provider for further evaluation and recommendations.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')
        st.header('Factors that Contribute to Your Risk Score: ')
       
        # Generate and display the explanation
        explanation = generate_explanation(answers)
        st.write('\n'.join(explanation))
        
        recommend_medical_tests()
        provide_treatment_recommendations()
        provide_helplines()
        
    
def recommend_medical_tests():
    st.header('Recommended Medical Tests and Screenings')
    st.write('Pap test: Recommended for all individuals with a cervix, starting at the age of 21 or within 3 years of becoming sexually active. It should be repeated every 3 years for individuals aged 21-65 who have a normal result.')
    st.write('HPV testing: In addition to the Pap test, HPV testing may be recommended for individuals aged 30 and above as part of cervical cancer screening. Talk to your healthcare provider for more information about HPV testing and its frequency.')

def provide_treatment_recommendations():
    st.header('Treatment Recommendations')
    st.write('If your risk score indicates a higher risk for cervical cancer, it is important to consult with your healthcare provider for further evaluation and recommendations.')
    st.write('Treatment options for cervical cancer may include surgery, radiation therapy, chemotherapy, or a combination of these approaches. The choice of treatment depends on the stage of cancer, overall health, and individual preferences. Your healthcare provider will guide you through the treatment decision-making process.')

def provide_helplines():
    st.header('Helplines (Malaysia)')
    st.write('Cancer Helpline: 1-800-88-1000')
    st.write('National Population and Family Development Board (LPPKN): 03-7953 6655')
    st.write('Malaysian AIDS Council: 03-4047 7000')
    st.write('Talian Kasih: 15999 (24-hour helpline for survivors of domestic violence, sexual abuse, and other related issues)')

    
def main():
    layout()
    
if __name__ == '__main__':
    main()
