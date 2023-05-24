import torch

model = torch.jit.load("code/traced_linear.pt")

print(model)