# Caesar-Cipher-Encryption

# Caesar Cipher Encryption Tool

This project is a simple Caesar Cipher encryption and decryption tool with both command-line and GUI implementations using Python and Tkinter.

## Features
- Encrypt and decrypt text using the Caesar Cipher algorithm.
- Simple command-line implementation (`caesar_cipher_encryption.py`).
- User-friendly GUI implementation (`gui.py`) built with Tkinter.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/caesar-cipher-tool.git
   cd caesar-cipher-tool
   ```
2. Ensure you have Python installed (Python 3.x recommended).
3. Install dependencies (if any, Tkinter is included with Python by default).

## Usage

### Command-line Version
Run the `caesar_cipher_encryption.py` script:
```sh
python caesar_cipher_encryption.py
```

### GUI Version
Run the `gui.py` script:
```sh
python gui.py
```

## File Structure
```
caesar-cipher-tool/
│── caesar_cipher_encryption.py  # Core logic for encryption and decryption
│── gui.py  # Tkinter-based GUI for easy use
│── README.md  # Project documentation
```

## How It Works
- The program takes a text input and a shift value.
- It shifts each letter in the input text forward (encryption) or backward (decryption) by the specified shift value.
- The GUI version provides a graphical interface to input text and view results.

## Example
**Encryption Example**:
```
Input:  HELLO
Shift:  3
Output: KHOOR
```
**Decryption Example**:
```
Input:  KHOOR
Shift:  3
Output: HELLO
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements!

## License
This project is licensed under the MIT License.

---
**Author**: Your Name

