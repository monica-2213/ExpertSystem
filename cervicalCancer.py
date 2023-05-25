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

def calculate_cervical_cancer_risk(answers):
    # Calculate the risk score based on the answers
    risk_score = 0

    for key, value in answers.items():
        if key in knowledge_base:
            risk_factor = knowledge_base[key]['risk_factor']
            if value in knowledge_base[key]['rules']:
                rule_score = knowledge_base[key]['rules'][value]
                risk_score += rule_score

    # Calculate risk percentage
    risk_percentage = (risk_score / sum([factor['risk_factor'] for factor in knowledge_base.values()])) * 100
    return risk_percentage

def main():
    st.title('Cervical Cancer Risk Assessment')
    st.write('Please provide the following information to assess your risk for cervical cancer.')

    questions = {
        'age': 'How old are you?',
        'multiple_partners': 'Have you ever had multiple sexual partners?',
        # Add more questions here
    }

    answers = {}

    for key, question in questions.items():
        answers[key] = st.radio(question, ['Yes', 'No'])

    if st.button('Submit'):
        risk_percentage = calculate_cervical_cancer_risk(answers)

        st.write('Risk Assessment:')
        st.write(f'Your risk score for cervical cancer: {risk_percentage:.2f}%')

        if risk_percentage >= 50:
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
