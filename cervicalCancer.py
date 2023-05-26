import streamlit as st

# Define color theme
primaryColor = "#E694FF"
backgroundColor = "#00172B"
secondaryBackgroundColor = "#0083B8"
textColor = "#C6CDD4"
font = "sans-serif"

# Apply the color theme to Streamlit
st.set_page_config(
    page_title="Cervical Cancer Risk Assessment",
    page_icon=":female_sign:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Set the CSS style
st.markdown(
    f"""
    <style>
        body {{
            color: {textColor};
            background-color: {backgroundColor};
            font-family: {font};
        }}
        .stButton button,
        .stTextInput input,
        .stTextArea textarea,
        .stNumberInput input,
        .stSelectbox select,
        .stRadio input,
        .stCheckbox input {{
            color: {textColor};
            background-color: {secondaryBackgroundColor};
            font-family: {font};
        }}
        .stNumberInput input {{
            color: {textColor};
            background-color: {secondaryBackgroundColor};
            border-color: {primaryColor};
        }}
        .stButton button {{
            background-color: {primaryColor};
        }}
        .stTitle {{
            color: {primaryColor};
        }}
        .stWarning {{
            color: {primaryColor};
        }}
        .stSuccess {{
            color: {primaryColor};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

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
        'risk_factor': 0,
        'rules': {
            'safe_sex == "No"': 0
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
        'risk_factor': 0,
        'rules': {
            'physical_activity == "Sedentary"': 0,
            'physical_activity == "Moderately active"': 0,
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

# Define the layout using Streamlit's layout components
def layout():
    st.title('Cervical Cancer Risk Assessment')
    st.write('Please provide the following information to assess your risk for cervical cancer.')

    # Use columns to display questions and answers side by side
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

    # Use a container to group questions and answers
    with st.beta_container():
        col1, col2 = st.beta_columns(2)
        with col1:
            answers = {}
            for key, question in questions.items():
                if key == 'age':
                    answers[key] = st.number_input(question, min_value=1, max_value=100, step=1)
                elif key == 'diet':
                    answers[key] = st.selectbox(question, ['Low in fruits and vegetables, high in processed foods', 'Balanced and healthy'])
                elif key == 'physical_activity':
                    answers[key] = st.selectbox(question, ['Sedentary', 'Moderately active', 'Regularly active and engage in physical exercise'])
                else:
                    answers[key] = st.radio(question, ['Yes', 'No'])
        
        with col2:
            if st.button('Submit'):
                risk_percentage, factor_scores = calculate_risk_score(answers)
                explanation = generate_explanation(factor_scores)

                st.write('Your risk score for cervical cancer:', f'{risk_percentage:.2f}%')
                if risk_percentage >= 50:
                    st.warning('Based on your risk score, you have a relatively higher risk for cervical cancer. Please consult with your healthcare provider for further evaluation and recommendations.')
                else:
                    st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')
                st.write('Your risk score is calculated based on various risk factors for cervical cancer. The higher the risk score, the higher the probability of developing cervical cancer. The factors that contributed most to your risk score include...')
                st.write(explanation)
                
#Function to calculate risk score
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
                    max_score += score
                    total_score += score
                    factor_scores[factor] = factor_scores.get(factor, 0) + score

    risk_percentage = (total_score / max_score) * 100
    return risk_percentage, factor_scores


def generate_explanation(factor_scores):
    explanation = "Factors contributing to your risk score:\n"
    for factor, score in factor_scores.items():
        explanation += f"- {factor}: {score}\n"
    return explanation


def main():
    layout()
    
            
if __name__ == '__main__':
    main()
