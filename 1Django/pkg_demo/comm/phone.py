class Phone:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    def call(self):
        print('我正在使用%s手机打电话'%(self.brand))
    def takepicture(self):
        print('我正在使用%s手机照相'%(self.brand))


# p = Phone('huawei','white',3000)
# p.call()
# p.takepicture()
