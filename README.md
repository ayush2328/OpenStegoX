![License](https://img.shields.io/badge/License-MIT-green.svg)
# OpenStegoX 🔐🖼️

OpenStegoX is a custom **macOS steganography tool** inspired by OpenStego.  
It provides a **GUI-based solution** to hide and extract secret messages inside images using **LSB steganography** combined with **AES encryption**.

This project is designed for **cyber security learning**, **college projects**, and **demonstrating secure data hiding techniques**.

---

## ✨ Features

- 🖼️ Image-based steganography (PNG / JPG)
- 🔐 Password-protected message hiding
- 🔒 AES encryption (via cryptography)
- 🧩 Least Significant Bit (LSB) algorithm
- 🖥️ GUI built using PyQt6
- 🍎 Optimized for macOS
- 🚫 No external tools or VMs required

---

## 🧠 How It Works

1. The secret message is **encrypted using AES**
2. Encrypted data is converted to binary
3. Binary data is embedded into the **LSB of image pixels**
4. The image appears visually unchanged
5. Extraction reverses the process using the same password

---

## 🗂️ Project Structure

```
OpenStegoX/
├── crypto.py      # Encryption & decryption logic
├── stego.py       # LSB steganography engine
├── utils.py       # Helper utilities
├── gui.py         # PyQt6 GUI
├── main.py        # Application entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

- macOS (tested on Apple Silicon)
- Python 3.9+
- PyQt6
- Pillow
- cryptography

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ayush2328/OpenStegoX.git
cd OpenStegoX
```

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python3 main.py
```

---

## 🧪 Usage Guide

### Hide a Message
1. Click **Select Image**
2. Choose a PNG/JPG image
3. Enter the secret message
4. Enter a password
5. Click **Hide Message**
6. Save the encoded image

### Extract a Message
1. Click **Select Image**
2. Choose the encoded image
3. Enter the password
4. Click **Extract Message**

---

## ⚠️ Important Notes

- Use **PNG images** for best results
- Do not resize or recompress encoded images
- Social media platforms destroy steganographic data
- Password is mandatory for extraction

---

## 🛡️ Security Disclaimer

This project is for **educational purposes only**.  
It demonstrates fundamental steganography and encryption concepts and should not be used for malicious activities.

---

## 📌 Future Enhancements

- 📁 Hide files (PDF / ZIP)
- 🖼️ Image preview
- 📊 Capacity analysis
- 🔊 Audio steganography
- 📦 macOS `.app` packaging

---

## 👨‍💻 Author

**Ayush Gupta**  
B.Tech CSE (Cyber Security)  
SRM Institute of Science and Technology

---

## ⭐ Acknowledgements

- Inspired by OpenStego
- PyQt6 Documentation
- Pillow Imaging Library
- Cryptography Library
