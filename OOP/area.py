# abstraction

class shape:
    def area(self):
        pass

class square (shape):
    def __init__(self, canh) -> None:
        self.canh = canh

    def area(self):
        return self.canh * self.canh
    
class rectangle (shape):
    def __init__(self, dai, rong) -> None:
        self.chieu_dai = dai
        self.chieu_rong = rong
    
    def area(self):
        return self.chieu_dai * self.chieu_rong
    

vuong = square(5)
chu_nhat = rectangle(5, 10)

def in_dien_tich (shape):
    print("Dien tich cua hinh ", shape.area())

in_dien_tich(vuong)
in_dien_tich(chu_nhat)