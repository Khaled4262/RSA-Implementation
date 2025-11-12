**RSA Implementation in Python**

This repository contains a Python implementation of RSA encryption and decryption, featuring key generation with hardcoded large primes, encryption, and decryption using the Chinese Remainder Theorem (CRT) for optimization.

**Features**

- RSA key pair generation (public and private keys)
- Encryption of plaintext messages
- Decryption using CRT optimization for faster computation
- Simple demonstration in the main() method
  
**Requirements**

- Python 3.X
- gmpy2 library for efficient large number arithmetic
    To install dependencies run: pip install gmpy2
  
**Usage**

Clone the repository and run the script: python RSAFunctions.py
This will output:
- Original message
- Encrypted message 
- Decrypted message

**Notes**

The primes used in this implementation are hardcoded for educational purposes only.
For real-world security, you should generate secure random large primes dynamically.
This implementation focuses on illustrating the RSA algorithm and CRT optimization rather than production-grade security.

**License**

This project is open-source and available under the MIT License.
