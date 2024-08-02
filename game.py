from game_function import get_game_info

print("任何时候都可以输入'q'来退出程序")
while True:
    name = input('请输入游戏的名字： ')
    if name == 'q':
        break
    type = input('请输入游戏的类型： ')
    if type == 'q':
        break
    
    game_info = get_game_info(name,type)
    print(f"游戏的规范化信息是：{game_info}")