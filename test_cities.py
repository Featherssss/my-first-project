from city_functions import get_info

def test_city_country():
    """测试城市-国家"""
    info = get_info('guangzhou','china')
    assert info == 'Guangzhou,China'
    
def test_city_country_population():
    """测试城市-国家-人口"""
    info = get_info('guangzhou','china',10_000_000)
    assert info == 'Guangzhou,China - Population 10000000'