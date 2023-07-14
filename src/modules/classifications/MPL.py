# Importando as bibliotecas
import torch
import torch.nn.functional as F
import torch.nn as nn
from torch.autograd import Variable

# Definindo a arquitetura do modelo
class MLP(nn.Module):
    def __init__(self, input_dim, output_dim): #Definindo as componentes
        super(MLP, self).__init__()
        self.layerEntry = nn.Linear(input_dim, 8)
        self.layerHidden1 = nn.Linear(8, 8)
        self.layerHidden2 = nn.Linear(8, 10)
        self.layerHidden3 = nn.Linear(10, 7)
        self.layerHidden4 = nn.Linear(7, 8)
        self.layerHidden5 = nn.Linear(8, 6)
        self.layerHidden6 = nn.Linear(6, 4)
        self.layerOut = nn.Linear(4, output_dim)

    def forward(self, x): # Definindo a sequencia de execução das componentes
        x = F.relu(self.layerEntry(x)) # Função de ativação F.RELU ou F.sigmoid, ...
        x = F.relu(self.layerHidden1(x))
        x = F.relu(self.layerHidden2(x))
        x = F.relu(self.layerHidden3(x))
        x = F.relu(self.layerHidden4(x))
        x = F.relu(self.layerHidden5(x))
        x = F.relu(self.layerHidden6(x))
        x = F.softmax(self.layerOut(x), dim=1)
        return x