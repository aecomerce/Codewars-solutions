class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
        # Создаем словарь для быстрого поиска соответствий
        self.encoding_map = dict(zip(map1, map2))
        self.decoding_map = dict(zip(map2, map1))
    
    def encode(self, s):
        result = []
        for char in s:
            # Заменяем символ, если он есть в map1, иначе оставляем как есть
            result.append(self.encoding_map.get(char, char))
        return ''.join(result)
    
    def decode(self, s):
        result = []
        for char in s:
            # Аналогично для декодирования
            result.append(self.decoding_map.get(char, char))
        return ''.join(result)
