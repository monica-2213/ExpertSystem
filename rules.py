import csv

knowledge_base = {
    # Your knowledge base dictionary here...
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
