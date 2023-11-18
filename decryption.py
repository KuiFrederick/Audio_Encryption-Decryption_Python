from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_audio_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    # Extract the IV from the ciphertext
    iv = ciphertext[:16]

    # Create the AES cipher object with the provided key and mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext[16:])

    # Unpad the plaintext
    plaintext = unpad(padded_plaintext, 16)

    # Write the decrypted audio to the output file
    with open(output_file, 'wb') as file:
        file.write(plaintext)

# Example usage
input_file = './Encrypted_Audio/encrypted_audio.bin'
output_directory = os.path.join('frontend', 'public', 'record_audio')

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
# Save the decrypted audio file in the output directory
output_file = os.path.join(output_directory, 'decrypted_audio.wav')
# Your code to save the decrypted audio file goes here
key = b'ksh9827cryptions'

decrypt_audio_file(input_file, output_file, key)