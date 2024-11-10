"""
显示对房屋操作的主菜单
提供对房屋的各种操作(增、删、改、查)
"""

houses = [
{
    "id": 2,
    "name": "tim",
    "tel": "113",
    "addr": "罗湖",
    "rent": 2000,
    "status": True
},
{
    "id": 3,
    "name": "bee",
    "tel": "116",
    "addr": "南山",
    "rent": 3000,
    "status": False
},
]

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


def list_houses():
    """显示房屋列表"""
    print("房屋列表".center(55, "-"))
    print("编号\t房主\t电话\t地址\t月租\t状态（是否出租）")
    for house in houses:
        for value in house.values():
            print(value, end='\t')
        print()