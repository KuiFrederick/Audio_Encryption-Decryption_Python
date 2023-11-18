from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt_audio_file(input_file, output_file, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create the AES cipher object with the provided key and mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Pad the plaintext to match the block size of AES (i.e., 16 bytes)
    padded_plaintext = pad(plaintext, 16)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the IV and ciphertext to the output file
    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)

# Example usage
input_file = './Recorded_Audio/gametheme.mp3'

output_directory = os.path.join('Encrypted_Audio')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
output_file = os.path.join(output_directory, 'encrypted_audio.bin')
key = b'ksh9827cryptions'

encrypt_audio_file(input_file, output_file, key)