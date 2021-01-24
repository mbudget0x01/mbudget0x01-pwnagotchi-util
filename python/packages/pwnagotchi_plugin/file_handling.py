def get_file_data(path:str) -> bytes:
    data = None
    with open(path, mode='rb') as stream:
        data = stream.read()
    return data
