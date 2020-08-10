import os
import torch.nn as nn
from datetime import datetime
from .constant import DATA_DIR

class Model(nn.Module):
    def __init__(self, input_size, hidden_size):
            super(Model, self).__init__()
            self.input_size = input_size
            self.hidden_size  = hidden_size
            self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)
            self.relu = torch.nn.ReLU()
            self.fc2 = torch.nn.Linear(self.hidden_size, 1)
            self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        hidden = self.fc1(x)
        relu = self.relu(hidden)
        output = self.fc2(relu)
        output = self.sigmoid(output)
        return output

def data_loader(filename):
    # load data

    # normalize

    # interpolate

    # change label to one_hot
    pass

if __name__ == '__main__':

    model = Model(input_size=dict_size, output_size=dict_size, hidden_dim=12, n_layers=1)
    # We'll also set the model to the device that we defined earlier (default is CPU)
    model.to(device)

    # Define hyperparameters
    n_epochs = 100
    lr=0.01

    # Define Loss, Optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    fn = ''
    data = data_loader(fn)

    for epoch in range(1, n_epochs + 1):
        for label, d in data:
            optimizer.zero_grad() # Clears existing gradients from previous epoch
            input_seq.to(device)
            output = model(d)
            loss = criterion(output, label)
            loss.backward() # Does backpropagation and calculates gradients
            optimizer.step() # Updates the weights accordingly

        if epoch%10 == 0:
            print('Epoch: {}/{}.............'.format(epoch, n_epochs), end=' ')
            print("Loss: {:.4f}".format(loss.item()))


    now = datetime.now()
    PATH = os.path.join(DATA_DIR,"rnn_{}.pt".format(now))

    # Save
    torch.save(model.state_dict(), PATH)
