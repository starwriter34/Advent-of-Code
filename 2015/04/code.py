from hashlib import md5
init = 'ckczppom'

def is_pw(key: str, num: int, leading_zeros: int) -> bool:
    full_key = key + str(num)
    m = md5(full_key.encode())
    target = "0" * leading_zeros
    return m.hexdigest()[0:leading_zeros] == target

def password(init, leading_zeros):
    key = init
    for i in range(100_000_000):
        if is_pw(key, i, leading_zeros):
            return i
    return None

def test():
    key1 = 'abcdef'
    key2 = 'pqrstuv'
    assert password(key1, 5) == 609043
    assert password(key2, 5) == 1048970

test()
print(password(init, 5))
print(password(init, 6))
