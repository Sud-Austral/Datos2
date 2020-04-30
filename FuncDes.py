from cryptography.fernet import Fernet

def desPass(key = b'nPfJPTrWOr2NDiQsjacW9aj7VCHuukKNLa9y1Py2ZS0='):
    cipher_suite = Fernet(key)
    ciphered_text = b'gAAAAABeq0WdC2DyURsZI0Cu_o3OqBHuZbUAYC-a3EuS_Yko4n0O5CNhV6aGElpvR7KVelmsT10zBLMcxvTEpItdyDoV2-ya1g=='
    unciphered_text = (cipher_suite.decrypt(ciphered_text))
    return unciphered_text