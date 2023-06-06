# - Trong python, tất cả các hàm (function) đều là object, được
#     kế thừa tự động một số phương thức như __call__, ... đều
#     có thể gán nó vào 1 biến và gọi lại sau đó

# 1, Higher oder function là gì?
# - Higher order function (hàm bậc cao) là hàm có tham số truyền
    # vào là một hàm khác
# - Đặc điểm:
    # ~ Một function là một instance của 1 object
    # ~ Có thể lưu trữ function trong 1 biến
    # ~ Có thể truyền 1 function vào tham số của 1 function khác
    # ~ Có thể return về 1 function (Closure function)
    # ~ Có thể lưu trự function trong các kiểu dữ liệu dạng cấu trúc
        # như list, hash tables

# 2, Decorator:
# - Decorator là một kỹ thuật dùng higher order function để trang trí
    # thêm nội dung cho 1 function có sẵn

# Ví dụ:
################### Higher Order Function ###################
# Hàm cha có tham số getMSG là một function
def sayHi(getMsg, msg):
    # Gọi đến hàm getMsg, và truyền tham số cho nó
    print(getMsg(msg))

# Hàm getMsg có một tham số truyền vào
def getMsg(msg):
    return msg + " babipun"
################### Decorator ###################
def deco(func):
    def printer():
        print("***************************")
        func()
        print("***************************")
    return printer

def myfunc():
    print("Babipunsociu")
#################################################
if __name__=='__main__':
    # Gán func vào biến
    msg = getMsg
    sayHi(msg, 'Dũng thiếu hiệp')
    
    #=========================
    # decorator là 1 hàm printer
    decorator = deco(myfunc)
    decorator()