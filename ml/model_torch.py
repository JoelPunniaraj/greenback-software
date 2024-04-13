import pandas as pd
import plotly as pl
import torch as tr

file_path = 'C:/Users/joelp/greenback/model/access_model.xlsx'
sheet_name = 'condense-sheets'

data = pd.read_excel(file_path, sheet_name=sheet_name)
data = data.transpose()

column_names = data.iloc[0]
available_metrics = [metric for metric in column_names[1:] if pd.notnull(metric)]

print("\nAvailable Metrics: \n")
for metric in available_metrics:
    if metric != "Reported Quarter":
        print(metric)

def select_metric():
    while True:
        selected_metric = input("\nEnter Metric: ")
        if selected_metric.lower() == 'exit' or 'quit':
            break
        
        if selected_metric in available_metrics:
            column_index = column_names.tolist().index(selected_metric)
            metric_data = data.iloc[1:, column_index].values.reshape(-1, 1)
            print(metric_data)
        else:
            print("Invalid! Try Again")

select_metric()







