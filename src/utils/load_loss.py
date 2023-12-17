import torch.nn as nn
import torch.backends.cudnn as cudnn
from utils.load_config import load_config, save_config

def load_loss_function():
    loss_func_name = load_config().get('loss_function')

    try: 
        if loss_func_name == "CrossEntropyLoss":
            loss_func = nn.CrossEntropyLoss()
        elif loss_func_name == "NLLLoss":
            loss_func = nn.NLLLoss()

    except:
        print('Error: Could not find loss function. Please check loss function name.')
        exit(1)
    return loss_func