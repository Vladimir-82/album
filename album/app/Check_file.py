def checker(file):

    if str(file).lower().endswith(('png', 'jpg', 'jpeg')):
        return True
    else:
        raise Exception('Unsupported file')

