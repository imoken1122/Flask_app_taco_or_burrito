from flask import Flask,request,jsonify
from PIL import Image
from torch.autograd import Variable as V
import torch as th
from torch import nn
from torchvision import transforms, models

class Classifier:
    
    def __init__(self):
        param = th.load("./model/resnet.prm",map_location=lambda x,y:x)
        self.model = self.read_net()
        self.model.load_state_dict(param)
        self.model.eval()
        self.transform = transforms.Compose([
                transforms.Resize((226,226)),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        self.classes = ["Burrito","Taco"]

    def predict(self,img):
        x = self.transform(img)
        x = x.unsqueeze(0) #バッチ処理するからバッチの次元を追加
        o = self.model(V(x))
        pred = o.max(1)[1].data 

        return self.classes[pred]

    def read_net(self):
        model = models.resnet18()
        model.fc = nn.Linear(model.fc.in_features,2)
        return model

