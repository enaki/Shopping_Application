import base64
import hashlib

from cryptography.fernet import Fernet

key = 'my deep darkest secret is secure'
alternate_encoded_key = b'bXkgZGVlcCBkYXJrZXN0IHNlY3JldCBpcyBzZWN1cmU='


class Cipher:
    @staticmethod
    def encrypt(message_text: str) -> bytes:
        key_encoded = base64.urlsafe_b64encode(key.encode())
        f = Fernet(key_encoded)
        return f.encrypt(message_text.encode())

    @staticmethod
    def decrypt(message_code: bytes) -> str:
        key_encoded = base64.urlsafe_b64encode(key.encode())
        f = Fernet(key_encoded)
        return f.decrypt(message_code).decode()


users = {
    'marin': 'moisii',
    'alex': 'ilioi0',
    'maria': 'mesina',
    'mihai': 'heghea',
    'petru': 'petrica',
    'andrei': 'dorcu0',
    'anisoara': 'i_like_to_destroy_things',
    'alinutza': 'apple_is_my_life',
    'enaki': 'vasile'
}


def get_hash(password : str) -> str:
    return hashlib.md5(password.encode('utf8')).hexdigest()


if __name__ == '__main__':
    message = 'test123!@#$%^&*('
    #encoded = Cipher.encrypt(message)
    #print(encoded)
    #print(Cipher.decrypt(encoded))

    for user, password in users.items():
        hashpass = get_hash(password)
        print("{} -> {}".format(user, hashpass))
