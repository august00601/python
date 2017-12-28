def docstring_test():
    """この関数はdocstringのテストです"""
    return True

#以下の2つは同じとみなされます
def spam():
    """マルチライン
    ドックストリング"""
    return True

def eggs():
    """
    マルチライン
    ドックストリング
    """
    return True

