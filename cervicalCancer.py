import streamlit as st

knowledge_base = {
    'multiple_partners': {
        'risk_factor': 1,
        'rules': {
            'multiple_partners == "Yes"': 1
        }
    },
    'early_sexual_activity': {
        'risk_factor': 1,
        'rules': {
            'early_sexual_activity == "Yes"': 1
        }
    },
    'hpv_infection': {
        'risk_factor': 1,
        'rules': {
            'hpv_infection == "Yes"': 1
        }
    },
    'safe_sex': {
        'risk_factor': 1,
        'rules': {
            'safe_sex == "No"': 1
        }
    },
    'smoking': {
        'risk_factor': 1,
        'rules': {
            'smoking == "Yes"': 1
        }
    },
    'weakened_immune_system': {
        'risk_factor': 1,
        'rules': {
            'weakened_immune_system == "Yes"': 1
        }
    },
    'long_term_oral_contraceptives': {
        'risk_factor': 0.5,
        'rules': {
            'long_term_oral_contraceptives == "Yes"': 0.5
        }
    },
    'diet': {
        'risk_factor': 1,
        'rules': {
            'diet == "Low in fruits and vegetables, high in processed foods"': 1
        }
    },
    'obesity_overweight': {
        'risk_factor': 1,
        'rules': {
            'obesity_overweight == "Yes"': 1
        }
    },
    'physical_activity': {
        'risk_factor': 1,
        'rules': {
            'physical_activity == "Sedentary"': 1
        }
    },
    'family_history': {
        'risk_factor': 0.5,
        'rules': {
            'gene_variations == "Yes"': 0.5
        }
    },
    'gene_variations': {
        'risk_factor': 0.5,
        'rules': {
            'family_history == "Yes"': 0.5
        }
    },
    'lynch_or_cowden_syndrome': {
        'risk_factor': 1,
        'rules': {
            'lynch_or_cowden_syndrome == "Yes"': 1
        }
    },
    'abnormal_bleeding': {
        'risk_factor': 1,
        'rules': {
            'abnormal_bleeding == "Yes"': 1
        }
    },
    'unusual_discharge': {
        'risk_factor': 1,
        'rules': {
            'unusual_discharge == "Yes"': 1
        }
    },
    'pelvic_pain': {
        'risk_factor': 1,
        'rules': {
            'pelvic_pain == "Yes"': 1
        }
    },
    'pain_during_intercourse': {
        'risk_factor': 1,
        'rules': {
            'pain_during_intercourse == "Yes"': 1
        }
    },
    'urinary_problems': {
        'risk_factor': 1,
        'rules': {
            'urinary_problems == "Yes"': 1
        }
    }
}

def calculate_risk_score(answers):
    max_score = 0
    total_score = 0

    for factor, response in answers.items():
        if factor in knowledge_base:
            factor_data = knowledge_base[factor]
            for rule, score in factor_data['rules'].items():
                if eval(rule, {}, answers):
                    max_score += factor_data['risk_factor']
                    total_score += factor_data['risk_factor'] * score

    return (total_score / max_score) * 100

def main():
    st.title("Cervical Cancer Risk Calculator")

    questions = {
        'multiple_partners': 'Have you had multiple sexual partners?',
        'early_sexual_activity': 'Did you engage in sexual activity at an early age?',
        'hpv_infection': 'Do you have a history of HPV infection?',
        'safe_sex': 'Do you practice safe sex and consistently use condoms?',
        'smoking': 'Are you a smoker?',
        'weakened_immune_system': 'Do you have a weakened immune system due to a medical condition or immunosuppressant medications?',
        'long_term_oral_contraceptives': 'Do you have a long-term history of oral contraceptive use?',
        'diet': 'Do you follow a diet low in fruits and vegetables and high in processed foods?',
        'obesity_overweight': 'Do you have obesity or are overweight?',
        'physical_activity': 'Do you maintain a healthy weight through regular physical activity and a balanced diet?',
        'family_history': 'Is there a family history of cervical cancer among close relatives?',
        'gene_variations': 'Is there a presence of specific gene variations associated with cervical cancer susceptibility?',
        'lynch_or_cowden_syndrome': 'Do you have a known diagnosis of Lynch syndrome or Cowden syndrome?',
        'abnormal_bleeding': 'Do you experience abnormal vaginal bleeding?',
        'unusual_discharge': 'Do you experience unusual vaginal discharge (watery, bloody, or foul odor)?',
        'pelvic_pain': 'Do you experience persistent pelvic pain located in the pelvis, lower back, or abdomen?',
        'pain_during_intercourse': 'Do you experience pain during sexual intercourse (dyspareunia)?',
        'urinary_problems': 'Do you have urinary problems such as blood in the urine, urinary incontinence, or frequent urination?'
    }

    answers = {}

    for key, question in questions.items():
        if key == 'diet':
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
        risk_score = calculate_risk_score(answers)
        st.write('Your risk score: {:.2f}%'.format(risk_score))
        if risk_score > 75:
            st.write('Based on your risk score, you have a high risk of cervical cancer. Please consult a healthcare professional for further evaluation.')
        elif risk_score > 50:
            st.write('Based on your risk score, you have a moderate risk of cervical cancer. It is recommended to monitor your health and consider preventive measures.')
        else:
            st.write('Based on your risk score, you have a low risk of cervical cancer. However, it is still important to prioritize regular check-ups and healthy lifestyle habits.')

        st.write('Uncertainty estimation and explanation are still under development.')

if __name__ == '__main__':
    main()
