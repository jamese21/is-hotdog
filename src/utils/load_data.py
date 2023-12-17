import torch
import os
from torchvision import datasets, transforms
from load_config import load_config

def load_data():
    config = load_config().get('data')
    data_dir = config.get('data_dir')
    batch_size = config.get('batch_size')
    num_workers = config.get('num_workers')

    train_transforms = transforms.Compose({transforms.ToTensor()})
    train_image_dataset = datasets.ImageFolder(os.path.join(data_dir, 'train'), train_transforms)
    train_dataloader = torch.utils.data.DataLoader(train_image_dataset, batch_size=batch_size,
                                                    shuffle=True, num_workers=num_workers)
    train_dataset_size = len(train_image_dataset)
    class_names = train_image_dataset.classes

    print(train_image_dataset)
    print(train_dataloader)
    print(train_dataset_size)
    print(class_names)
    return train_dataloader, train_dataset_size, class_names