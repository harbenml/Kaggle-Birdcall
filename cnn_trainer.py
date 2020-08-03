import os

from fastai.vision import *
import torchvision
import torch

from data_loader import DataLoader, TrainDataLoader, ValDataLoader

dl = DataLoader()
dl.close()
train_dl = TrainDataLoader(dl)
val_dl = ValDataLoader(dl)
data = ImageDataBunch.create(train_ds=train_dl, valid_ds=val_dl, num_workers=8)
data.normalize()

os.environ["TORCH_HOME"] = "model/pretrained"

learn = create_cnn(data, torchvision.models.resnet18, metrics=accuracy)
learn.loss_func = torch.nn.functional.cross_entropy
learn.fit(10)
