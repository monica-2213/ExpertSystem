import streamlit as st


knowledge_base = {
    'age': {
        'risk_factor': 10,
        'rules': {
            'age >= 50': 20,
            'age >= 30': 10
        }
    },
    'multiple_partners': {
        'risk_factor': 10,
        'rules': {
            'multiple_partners == "Yes"': 20
        }
    },
    'early_sexual_activity': {
        'risk_factor': 10,
        'rules': {
            'early_sexual_activity == "Yes"': 10
        }
    },
    'hpv_infection': {
        'risk_factor': 10,
        'rules': {
            'hpv_infection == "Yes"': 15
        }
    },
    'safe_sex': {
        'risk_factor': 10,
        'rules': {
            'safe_sex == "No"': 15
        }
    },
    'smoking': {
        'risk_factor': 10,
        'rules': {
            'smoking == "Yes"': 10
        }
    },
    'weakened_immune_system': {
        'risk_factor': 10,
        'rules': {
            'weakened_immune_system == "Yes"': 10
        }
    },
    'long_term_oral_contraceptives': {
        'risk_factor': 5,
        'rules': {
            'long_term_oral_contraceptives == "Yes"': 5
        }
    },
    'diet': {
        'risk_factor': 10,
        'rules': {
            'diet == "Low in fruits and vegetables, high in processed foods"': 10
        }
    },
    'obesity_overweight': {
        'risk_factor': 10,
        'rules': {
            'obesity_overweight == "Yes"': 10
        }
    },
    'physical_activity': {
        'risk_factor': 0,
        'rules': {
            'physical_activity == "Sedentary"': 10,
            'physical_activity == "Moderately active"': 5,
            'physical_activity == "Regularly active and engage in physical exercise"': 0
        }
    },
    'family_history': {
        'risk_factor': 10,
        'rules': {
            'family_history == "Yes"': 10
        }
    },
    'gene_variations': {
        'risk_factor': 10,
        'rules': {
            'gene_variations == "Yes"': 10
        }
    },
    'lynch_or_cowden_syndrome': {
        'risk_factor': 10,
        'rules': {
            'lynch_or_cowden_syndrome == "Yes"': 10
        }
    },
    'abnormal_bleeding': {
        'risk_factor': 10,
        'rules': {
            'abnormal_bleeding == "Yes"': 10
        }
    },
    'unusual_discharge': {
        'risk_factor': 10,
        'rules': {
            'unusual_discharge == "Yes"': 10
        }
    },
    'pelvic_pain': {
        'risk_factor': 10,
        'rules': {
            'pelvic_pain == "Yes"': 10
        }
    },
    'pain_during_intercourse': {
        'risk_factor': 10,
        'rules': {
            'pain_during_intercourse == "Yes"': 10
        }
    },
    'urinary_problems': {
        'risk_factor': 10,
        'rules': {
            'urinary_problems == "Yes"': 10
        }
    }
}

def calculate_risk_score(answers):
    total_score = 0
    max_score = 0
    for factor, value in answers.items():
        if factor in knowledge_base:
            factor_data = knowledge_base[factor]
            max_score += factor_data['risk_factor']
            for rule, score in factor_data['rules'].items():
                if eval(rule, {'__builtins__': None}, answers):
                    max_score += score
                    total_score += score
    risk_percentage = (total_score / max_score) * 100
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
        # Calculate the risk score
        risk_percentage = calculate_risk_score(answers)
        
        # Display the risk score as a percentage
        st.write('Your risk score for cervical cancer:', f'{risk_percentage:.2f}%')

        if risk_score >= 50:
            st.warning('Based on your risk score, you have a relatively higher risk for cervical cancer. Please consult with your healthcare provider for further evaluation and recommendations.')
        else:
            st.success('Based on your risk score, you have a relatively lower risk for cervical cancer. However, it is still important to attend regular screenings and maintain a healthy lifestyle.')

        # Provide uncertainty estimation
        st.write(f'Uncertainty: High')  # Add appropriate uncertainty measure or explanation

        # Generate explanation
        st.write('Explanation:')
        st.write('Your risk score is calculated based on various risk factors for cervical cancer. The higher the risk score, the higher the probability of developing cervical cancer. The factors that contributed most to your risk score include...')
        # Provide explanation for the factors contributing to the risk score

        # Rule editor (dummy implementation)
        if st.button('Edit Rules'):
            st.write('Rule Editor: (Under development)')  # Provide an interface to edit the rules or add custom rules

if __name__ == '__main__':
    main()
