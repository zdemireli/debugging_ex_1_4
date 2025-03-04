Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\user> py
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import csv
>>> import numpy as np
>>> from typing import Set,Tuple, List
>>> import torch
>>> import torch.utils
>>> import torch.utils.data
>>> import torch.nn as nn
>>> import torchvision
>>> NoneType = type(None)
>>> import matplotlib.pyplot as plt
>>> from IPython.display import display, clear_output
>>> from PIL import Image
>>> import torchvision.transforms.functional as TF
>>> from torchvision.models import vgg11
>>> from torchvision.models import mobilenet_v2
>>> import torchvision.transforms as transforms
>>> import time
>>> class Generator(nn.Module):
...     def __init__(self):
...             super().__init__()
...             self.model=nn.Sequential(nn.Linear(100, 256),nn.ReLU(),nn.Linear(256, 512),nn.ReLU(),nn.Linear(512, 1024),nn.ReLU(),nn.Linear(1024, 784),nn.Tanh(),)
...     def forward(self,x):
...             output=self.model(x)
...             output=output.view(x.size(0),1,28,28)
...             return output
...
>>> class Discriminator(nn.Module):
...     def __init__(self):
...             super().__init__()
...             self.model = nn.Sequential(nn.Linear(784, 1024),nn.ReLU(),nn.Dropout(0.3),nn.Linear(1024, 512),nn.ReLU(),nn.Dropout(0.3),nn.Linear(512, 256),nn.ReLU(),nn.Dropout(0.3),nn.Linear(256, 1),nn.Sigmoid(),)
...     def forward(self,x):
...             x=x.view(x.size(0),784)
...             output=self.model(x)
...             return output
...
>>> def train_gan(batch_size: int = 32, num_epochs: int = 100, device: str = "cuda:0" if torch.cuda.is_available() else "cpu"):
...     transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
...     try:
...             train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
...     except:
...             print("Failed to download MNIST, retrying with different URL")
...             torchvision.datasets.MNIST.resources = [('https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz','f68b3c2dcbeaaa9fbdd348bbdeb94873'),('https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz','d53e105ee54ea40749a09fcbcd1e9432'),('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz','9fb629c4189551a2d022fa330f9573f3'),('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz','ec29112dd5afa0611ce80d1b7f02629c')]
...             train_set=torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
...     train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
...     real_samples, mnist_labels = next(iter(train_loader))
...     fig = plt.figure()
...     for i in range(16):
...             sub = fig.add_subplot(4, 4, 1 + i)
...             sub.imshow(real_samples[i].reshape(28, 28), cmap="gray_r")
...             sub.axis('off')
...     fig.tight_layout()
...     fig.suptitle("Real images")
...     display(fig)
...     time.sleep(3)
...     discriminator = Discriminator().to(device)
...     generator = Generator().to(device)
...     lr=0.0001
...     loss_function = nn.BCELoss()
...     optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
...     optimizer_generator = torch.optim.Adam(generator.parameters(), lr=lr)
...     for epoch in range(num_epochs):
...             for n, (real_samples, mnist_labels) in enumerate(train_loader):
...                     real_samples = real_samples.to(device=device)
...                     real_batch_size=real_samples.size(0)
...                     real_samples_labels=torch.ones((real_batch_size,1)).to(device=device)
...                     latent_space_samples = torch.randn((real_batch_size, 100)).to(device=device)
...                     generated_samples = generator(latent_space_samples)
...                     generated_samples = generated_samples.view(real_batch_size, -1)
...                     generated_samples_labels = torch.zeros((real_batch_size, 1)).to(device=device)
...                     all_samples = torch.cat((real_samples.view(real_batch_size, -1), generated_samples))
...                     all_samples_labels = torch.cat((real_samples_labels, generated_samples_labels))
...                     discriminator.zero_grad()
...                     output_discriminator = discriminator(all_samples)
...                     loss_discriminator = loss_function(output_discriminator, all_samples_labels)
...                     loss_discriminator.backward()
...                     optimizer_discriminator.step()
...                     latent_space_samples = torch.randn((real_batch_size, 100)).to(device=device)
...                     generator.zero_grad()
...                     generated_samples = generator(latent_space_samples)
...                     generated_samples = generated_samples.view(real_batch_size, -1)
...                     output_discriminator_generated = discriminator(generated_samples)
...                     loss_generator = loss_function(output_discriminator_generated, real_samples_labels)
...                     loss_generator.backward()
...                     optimizer_generator.step()
...                     if n %100==0:
...                             name = f"Generate images\n Epoch: {epoch} Loss D.: {loss_discriminator:.2f} Loss G.: {loss_generator:.2f}"
...                             generated_samples = generated_samples.detach().cpu().numpy()
...                             fig = plt.figure()
...                             for i in range(16):
...                                     sub = fig.add_subplot(4, 4, 1 + i)
...                                     sub.imshow(generated_samples[i].reshape(28, 28), cmap="gray_r")
...                                     sub.axis('off')
...                             fig.suptitle(name)
...                             fig.tight_layout()
...                             clear_output(wait=True)
...                             display(fig)
...
>>> train_gan(batch_size=32, num_epochs=100)
Figure(640x480)
Figure(640x480)
Figure(640x480)
Figure(640x480)
Figure(640x480)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 46, in train_gan
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<stdin>", line 7, in forward
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\container.py", line 250, in forward
    input = module(input)
            ^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
>>>
