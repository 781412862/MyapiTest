import yaml
import os
with open ('./cfg.yml','r') as cf:
    #读取到的配置信息赋值给configInfor

    cofigInfor = yaml.load(cf)
