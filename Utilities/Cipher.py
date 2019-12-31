import base64
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


if __name__ == '__main__':
    message = 'test'
    encoded = Cipher.encrypt(message)
    print(encoded)
    print(Cipher.decrypt(encoded))