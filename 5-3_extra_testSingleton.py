class SOME:
    __instance = None
    def __new__(cls):
        print('[__new__]: new class {}')

        if not SOME.__instance:#<-- 確認SOME.__instance是否已被宣告
            SOME.__instance = object.__new__(cls)
        return SOME.__instance

    def __init__(self):
        print('[__init__]: init class...')

    def checkID(self):
        myID = id(self)
        print('id={}'.format(id(self)))
        return myID


a = SOME()
a_id = a.checkID()

b = SOME()
b_id = b.checkID()


# if a_id==b_id:
#     print('SOME class因為singleton的設計, 只能有一個instance')
# else:
#     print('oops! 失敗')
        

