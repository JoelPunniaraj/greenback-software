import pandas as pd
import torch
import plotly.graph_objs as plot

file_path = 'C:/Users/joelp/greenback/model/access_model.xlsx'
sheet_name = 'condense-sheets'
data = pd.read_excel(file_path, sheet_name=sheet_name)

features = data[['Year', 'Quarter']].values
target = data['Net Income'].values 

features_tensor = torch.tensor(features, dtype=torch.float32)
target_tensor = torch.tensor(target, dtype=torch.float32)

input_size = features_tensor.shape[1]
output_size = 1
model = torch.nn.Linear(input_size, output_size)

critera = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

num_epochs = 100
for epoch in range(num_epochs):
    outputs = model(features_tensor)
    loss = critera(outputs, target_tensor.view(-1, 1))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

predictions = model(features_tensor).detach().numpy()

figure = plot.Figure()
figure.add_trace(plot.Scatter(x=features[:, 0], y=target, mode='markers', name='Actual'))
figure.add_trace(plot.Scatter(x=features[:, 0], y=predictions.flatten(), mode='lines', name='Predicted'))
figure.update_layout(title='Projection Chart', xaxis_title='Year', yaxis_title='Net Income')
figure.show()
