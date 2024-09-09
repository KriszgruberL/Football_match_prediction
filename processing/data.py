import pandas as pd
df = pd.read_csv('/Users/alexjones/Desktop/CSV_SQL/Football_match_prediction/data/csv/dataset.csv')

df.columns = df.columns.str.replace('<', '_less_than_').str.replace('>', '_greater_than_').str.replace('.', '_')

output_file_path = '/Users/alexjones/Desktop/CSV_SQL/Football_match_prediction/data/csv/modified2.csv'
df.to_csv(output_file_path, index=False)

