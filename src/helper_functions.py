def get_key_file():
    with open('../riotApiKey.txt', 'r') as k:
        key_file = k.read()
        return key_file.strip()
