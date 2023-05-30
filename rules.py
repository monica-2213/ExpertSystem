import csv

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

def create_csv_file(data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Factor', 'Risk Factor', 'Rules'])

        for factor, factor_data in data.items():
            risk_factor = factor_data['risk_factor']
            rules = factor_data['rules']

            for rule, score in rules.items():
                writer.writerow([factor, risk_factor, rule])

# Specify the file path for the CSV file
csv_file_path = 'knowledge_base.csv'

# Call the function to create the CSV file
create_csv_file(knowledge_base, csv_file_path)
