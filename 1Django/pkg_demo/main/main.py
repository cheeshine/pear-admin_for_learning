import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# main.py abspath
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# 将当前目录设置为系统目录
sys.path.append(base_dir)

from comm.phone import Phone
from math1.math import MyMath

phone = Phone('huawei','black',5000)
phone.call()
phone.takepicture()

print(MyMath.add(10,20))
print(MyMath.sub(10,20))
print(MyMath.mul(10,20))
print(MyMath.div(10,20))
    
