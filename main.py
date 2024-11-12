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
                add_house()
            case "2":
                del_houses()
            case "3":
                pass
            case "4":
                find_house()
            case "5":
                list_houses()
            case "6":
                print("你退出了程序\n欢迎下次使用")
                break
            case _:
                print("请正确输入选项！！！")
                continue