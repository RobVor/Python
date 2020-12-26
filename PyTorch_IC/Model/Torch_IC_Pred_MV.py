#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:29:56 2020

@author: robertv
"""

from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import shutil

plt.ion()   # interactive mode
#torch.cuda.empty_cache()
#torch.no_grad()
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

dev = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True)
num_ = model.fc.in_features
model.fc = nn.Linear(num_, 3)
crit = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
sched = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

checkpoint = torch.load('/home/robertv/Documents/Torch IC/Output/best_model.pt')
model.load_state_dict(checkpoint['state_dict'], strict=False)
optimizer.load_state_dict(checkpoint['optimizer'])
epoch = checkpoint['epoch']
model = model.to(dev)
model.eval()

dirpath = '/home/robertv/Documents/Torch IC/Input/other/'
img = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
classes = ['nude','safe','sexy']
for c in classes:
    if not os.path.exists(dirpath+c):
        os.makedirs(dirpath+c)

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated

def pred_image(image_path):
    transform = transforms.Compose([
        #transforms.RandomResizedCrop(size=640, scale=(0.8, 1.0)),
        #transforms.RandomRotation(degrees=15),
        transforms.Resize(640),
        transforms.CenterCrop(640),
        #transforms.RandomHorizontalFlip(),
        #transforms.ColorJitter(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    
    image_tensor = ImageFile.Image.open(image_path).convert('RGB')
    image_tensor = transform(image_tensor).float()
    #imshow(image_tensor)
    image_tensor = image_tensor.unsqueeze_(0)
    if torch.cuda.is_available():
        image_tensor.cuda()
        
    input = image_tensor.to(dev)
    output = model(input)
        
    index = output.cpu().data.numpy().argmax()
    return index


for f in img:
    print("Image: ",dirpath+f)
    prediction = pred_image(dirpath+f)
    if prediction == 0:
        imgType = 'nude'
        src = dirpath + f
        dst = dirpath + 'nude/' + f
        shutil.move(src, dst)
    elif prediction == 1:
        imgType = 'safe'
        src = dirpath + f
        dst = dirpath + 'safe/' + f
        shutil.move(src, dst)
    elif prediction == 2:
        imgType = 'sexy'
        src = dirpath + f
        dst = dirpath + 'sexy/' + f
        shutil.move(src, dst)
    else:
        imgType = 'Unknown'
    print("Predicted Class: ", imgType)