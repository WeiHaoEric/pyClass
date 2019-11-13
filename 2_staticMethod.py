class Some:
    def __init__(self, val):
        self.val = val

    def service(self, num):
        self.val+=num
        print('val is {}'.format(self.val))

    @staticmethod
    def staticCall(num1, num2):
        print("num1 is {}, num2 is {}".format(num1, num2))


# test1: 透過class物件，直接呼叫service
s1 = Some(10)
s1.service(5)

print("===")

# test2: 取得class method-service() 物件，再間接進行呼叫
service = s1.service
service(100)
print("===")

# test3: 取得Some裡面的service method物件，透過傳遞class obj的方式，進行相同功能的呼叫
s2 = Some(20)

service = Some.service
service(s1, 200)
service(s2, 500)

# test 4: 宣告一個不相關的class, 但同樣有self.val
class Other:
    pass

other = Other()
other.val = 100
service(other, 199)

# test5: static method 
## 教學說明: https://blog.csdn.net/handsomekang/article/details/9615239
Some.staticCall(num1=20, num2=40) # <-- See... we can directly call this class method without instance this class obj