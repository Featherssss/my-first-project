def get_game_info(name,type,price=None):
    """获得游戏信息"""
    if price:
        formatted_info = f"{name}-{type}-{price}"
    else:
        formatted_info = f"{name}-{type}"
    return formatted_info.title()