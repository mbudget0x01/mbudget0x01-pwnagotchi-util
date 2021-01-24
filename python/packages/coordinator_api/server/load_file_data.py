def _load_file_data(path:str) -> bytes:
    data = None
    with open(path,'rb') as in_file:
        data = in_file.read()
    return data        