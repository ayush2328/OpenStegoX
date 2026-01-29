# stego.py
from PIL import Image

END_MARKER = "1111111111111110"

def to_bits(data: bytes) -> str:
    return ''.join(format(b, '08b') for b in data) + END_MARKER

def from_bits(bits: str) -> bytes:
    bytes_out = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == END_MARKER[:8]:
            break
        bytes_out.append(int(byte, 2))
    return bytes(bytes_out)

def hide_data(image_path, data: bytes, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    bits = to_bits(data)
    w, h = img.size
    idx = 0

    for y in range(h):
        for x in range(w):
            if idx >= len(bits):
                img.save(output_path)
                return
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(bits[idx])
            pixels[x, y] = (r, g, b)
            idx += 1

    raise ValueError("Image too small")

def extract_data(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    bits = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            if bits.endswith(END_MARKER):
                return from_bits(bits)

    raise ValueError("No hidden data found")
