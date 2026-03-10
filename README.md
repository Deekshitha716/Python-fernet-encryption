# Python-fernet-encryption
This project implements a secure password-protected vault in Python that encrypts and decrypts sensitive data using modern cryptographic techniques. The program uses PBKDF2 with SHA-256 to derive a strong encryption key from a user-provided password and Fernet symmetric encryption to securely lock and unlock a secret message.

A random salt is generated to strengthen password security, and the encrypted data is stored in a file (vault.dat). The user must enter the correct password to successfully decrypt and access the stored message, ensuring protection against unauthorized access.

This project demonstrates basic cryptography concepts, secure key derivation, password masking, and file-based encryption, making it a simple example of how secure data storage can be implemented in Python.
