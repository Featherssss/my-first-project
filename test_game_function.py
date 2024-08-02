from game_function import get_game_info

def test_name_type_game_info():
    """能否处理Elden Ring-Soulslike这样的游戏信息"""
    game_info = get_game_info('elden ring','soulslike')
    assert game_info == 'Elden Ring-Soulslike'
    
def test_name_type_price_game_info():
    """能否处理Elden Ring-Soulslike-298这样的游戏信息"""
    game_info = get_game_info('elden ring','soulslike',298)
    assert game_info == 'Elden Ring-Soulslike-298'