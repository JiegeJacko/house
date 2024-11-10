"""
程序的执行入口
根据用户的选择，调用相应的函数完成功能
"""

from house_operation import *

if __name__ == "__main__":
    while True:
        main_menu()
        key = input("请选择(1~6): ")
        match key:
            case "1":
                pass
            case "2":
                print("2 hahaa")
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case _:
                break
    print("你退出了程序\n欢迎下次使用")