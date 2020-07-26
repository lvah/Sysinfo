import hashlib


def get_md5(content):
    """对于字符串进行md5加密"""
    md1 = hashlib.md5(content)
    return md1.hexdigest()
