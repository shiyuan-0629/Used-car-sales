import hashlib

def generate_md5(data: str) -> str:
    md5_hash = hashlib.md5()
    data_bytes = data.encode('utf-8')
    md5_hash.update(data_bytes)
    return md5_hash.hexdigest()

def verify_md5(data: str, known_md5: str) -> bool:
    generated_md5 = generate_md5(data)
    return generated_md5 == known_md5

