"""
显示对房屋操作的主菜单
提供对房屋的各种操作(增、删、改、查)
"""

houses = [
{
    "id": 998,
    "name": "tim",
    "tel": "113",
    "addr": "罗湖",
    "rent": 2000,
    "status": True
},
{
    "id": 999,
    "name": "bee",
    "tel": "116",
    "addr": "南山",
    "rent": 3000,
    "status": False
},
]
_id = 1

def main_menu():
    """
    显示主菜单
    让用户选择
    """
    print()
    print(" 房屋出租系统菜单 ".center(60, "="))
    print("1. 新增房源")
    print("2. 删除房屋")
    print("3. 修改房屋")
    print("4. 查找房屋")
    print("5. 列出房屋")
    print("6. 退出")


def add_house():
    """添加房屋"""
    print("添加房屋".center(55, "-"))

    global _id
    new_house = {
    "id": _id,
    "name": None,
    "tel": None,
    "addr": None,
    "rent": None,
    "status": None
    }
    
    new_house["name"] = input("姓名: ")        
    new_house["tel"] = input("电话: ")        
    new_house["addr"] = input("地址: ")        
    new_house["rent"] = input("月租: ")        

    while True:
        tmp = input("是否出租（y 或 n）: ")        
        if tmp.upper() in ["Y", "YES"]:
            new_house["status"] = True
            break
        elif tmp.upper() in ["N", "NO"]:
            new_house["status"] = False
            break
        else:
            continue
    houses.append(new_house)
    _id += 1


def del_houses():
    """删除房屋"""
    print("删除房屋".center(55, "-"))

    while True:
        id = input("编号: ")
        try:
            id = int(id)
        except ValueError:
            print("请正确输入编号")
            continue

        for house in houses:
            if id == house["id"]:
                break
        else:
            print("编号不存在，请重新输入")
            continue
        break
    
    while True:
        tmp = input("是否删除该房屋（y 或 n）: ")        
        if tmp.upper() in ["Y", "YES"]:
            houses.remove(house)
            break
        elif tmp.upper() in ["N", "NO"]:
            break
        else:
            continue


def find_house():
    """根据id查找房屋"""
    print("查找房屋".center(55, "-"))
    while True:
        id = input("编号: ")
        try:
            id = int(id)
        except ValueError:
            print("请正确输入编号")
            continue
        print("编号\t房主\t电话\t地址\t月租\t状态（是否出租）")
        for house in houses:
            if house["id"] == id:
                for value in house.values():
                    print(value, end='\t')
                print()
                break
        else:
            print("编号不存在，请重新输入")
            continue
        break


def list_houses():
    """显示房屋列表"""
    print("房屋列表".center(55, "-"))
    print("编号\t房主\t电话\t地址\t月租\t状态（是否出租）")
    for house in houses:
        for value in house.values():
            print(value, end='\t')
        print()