import torch
from tensorflow.python.client import device_lib
# device_lib = device_lib()
print(device_lib.list_local_devices())
print(torch.cuda.is_available())
print(torch.__version__)