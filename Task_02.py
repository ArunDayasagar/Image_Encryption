import numpy as np
from PIL import Image
def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)
    decrypted_array = img_array ^ key
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

def generate_key(shape):
    return np.random.randint(0, 256, shape, dtype=np.uint8)

if __name__ == "__main__":
    input_path = 'lion.jpg'
    encrypted_path = 'encrypted_image.png'
    decrypted_path = r'C:\Users\Arun Dayasagar M\OneDrive\Pictures\images\decrypted_image.png'
    img = Image.open(input_path)
    img_array = np.array(img)
    key = generate_key(img_array.shape)
    encrypt_image(input_path, encrypted_path, key)
    decrypt_image(encrypted_path, decrypted_path, key)