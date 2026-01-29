# utils.py
def read_text_file(path):
    with open(path, "r") as f:
        return f.read()

def save_text_file(path, text):
    with open(path, "w") as f:
        f.write(text)
