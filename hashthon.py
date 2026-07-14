import getpass

import bcrypt


def hashfunction():
    """an hashtable mechanism aka a password generator"""
    new_pw = getpass.getpass("Login: ")
    # password = getpass.getpass("password: ")
    print(new_pw)
    hash_pw = bcrypt.hashpw(new_pw.encode("utf-8"), bcrypt.gensalt())
    reverse = hash_pw.decode()
    print(hash_pw)
    print(reverse)
    print(reverse.encode())


if __name__ == "__main__":
    hashfunction()
