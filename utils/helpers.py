def dict_helper(objlist):
    result = [item.serialize() for item in objlist]
    return result