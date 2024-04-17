
# Written By Joel Punniaraj 
# Last Updated : 4/14/2024

from sklearn.linear_model import LinearRegression
import pandas as pd

def view_regression():

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
    
    while True:
        selected_metric = input("\nEnter Metric: ")
        if selected_metric.lower() in ['exit', 'quit']:
            break
        
        if selected_metric in available_metrics:
            column_index = column_names.tolist().index(selected_metric)
            metric_data = data.iloc[1:, column_index].values
            non_zero_values = [value for value in metric_data if value != 0]
            
            print()
            for value in non_zero_values:
                rounded_value = round(value, 3)
                print([rounded_value])
            
            if non_zero_values:
                x = [[i] for i in range(len(non_zero_values), 0, -1)]  
                y = [[value] for value in non_zero_values]  
                
                model = LinearRegression()
                model.fit(x, y)
                
                projected = model.predict([[len(non_zero_values) + 1]])
                rounded_projected = round(projected[0][0])
                projected = model.predict([[len(non_zero_values) + 1]])

                change = rounded_projected - non_zero_values[0]
                print("\nProjected Value:", [rounded_projected])
                print("Change:", [change])

            else:
                print("\nInsufficient Data")
        else:
            print("Invalid Metric! Try Again")


user = input("\nView Regression Model? ")
if user == 'yes':
    view_regression()
elif user == 'no':
    exit()
    















