import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
from torchvision import models
from load_config import load_config

def load_model():
    config = load_config().get('model')
    # model_name = config.get('model_name')
    model = models.resnet50(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 2)
    return model
