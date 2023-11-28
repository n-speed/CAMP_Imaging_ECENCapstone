from psutil import virtual_memory
from nvsmi import get_available_gpus, get_gpus

import torch

import modeling.LSTM as TSM
from modeling.sequence import train_sequence, test_sequence
from tools.data_import import importing
from tools.formatting import formatting
import graphing

ram_gb = virtual_memory().total / 1e9
print('Runtime has {:.1f} gigabytes of available RAM \n'.format(ram_gb))

input_size = 20
num_layers = 5
hidden_size = 1
output_size = 1

device = TSM.device
model = TSM.LSTMModel(input_size, hidden_size, num_layers).to(device)
loss_fn = torch.nn.MSELoss(reduction = 'mean')
optimzier_obj = torch.optim.Adam(model.parameters(), lr = 1e-3)


raw_data = importing()
train, test = formatting(raw_data,0.75)

i=0
for i in range(4):
	x_train, y_train = train_sequence(train[i])
	x_test, y_test = test_sequence(test[i])

	batch_size = 8
	# Create DataLoader for batch training
	train_dataset = torch.utils.data.TensorDataset(x_train, y_train)
	train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

	# Create DataLoader for batch training
	test_dataset = torch.utils.data.TensorDataset(x_test, y_test)
	test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

	num_epochs = 50
	train_hist =[]
	test_hist =[]
	# Training loop
	for epoch in range(num_epochs):
		total_loss = 0.0

		# Training
		model.train()
		for batch_x, batch_y in train_loader:
			batch_x, batch_y = batch_x.to(device), batch_y.to(device)
			predictions = model(batch_x)
			loss = loss_fn(predictions, batch_y)

			optimzier_obj.zero_grad()
			loss.backward()
			optimzier_obj.step()

			total_loss += loss.item()

		# Calculate average training loss and accuracy
		average_loss = total_loss / len(train_loader)
		train_hist.append(average_loss)

		# Validation on test data
		model.eval()
		with torch.no_grad():
			total_test_loss = 0.0

			for batch_X_test, batch_y_test in test_loader:
				batch_X_test, batch_y_test = batch_X_test.to(device), batch_y_test.to(device)
				predictions_test = model(batch_X_test)
				test_loss = loss_fn(predictions_test, batch_y_test)

				total_test_loss += test_loss.item()

			# Calculate average test loss and accuracy
			average_test_loss = total_test_loss / len(test_loader)
			test_hist.append(average_test_loss)
		if (epoch+1)%5==0:
			print(f'Epoch [{epoch+1}/{num_epochs}] - Training Loss: {average_loss:.4f}, Test Loss: {average_test_loss:.4f}')

	graphing.graphLoss(num_epochs,train_hist,test_hist)

	train_hist.clear() # excessive, but guarantees trash collection of the history arrays
	test_hist.clear()
	print()
