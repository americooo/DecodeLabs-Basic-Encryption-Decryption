# Basic Encryption & Decryption

**DecodeLabs Cyber Security Internship - Project 2 | Batch 2026**

A Python command-line application that encrypts user text with a Caesar cipher,
decrypts it with the same key, and displays both results.

## Features

- Interactive input or command-line arguments.
- User-selected integer shift, including negative and large keys.
- Uppercase and lowercase ASCII letters keep their case and wrap around A-Z/a-z.
- Spaces, numbers, punctuation, and non-ASCII characters remain unchanged.
- Decrypt existing ciphertext with `--decrypt`.
- No third-party packages or network access required.

## Requirements

Python 3.9 or newer.

## Run

```bash
git clone https://github.com/americooo/DecodeLabs-Basic-Encryption-Decryption.git
cd DecodeLabs-Basic-Encryption-Decryption
python3 cipher.py
```

Enter your text and an integer shift key when prompted. Invalid interactive keys
are rejected with a retry prompt. Ctrl+C or end-of-input cancels the program.

### Encrypt and decrypt a message

```bash
python3 cipher.py --text "Hello, World!" --shift 3
```

```text
Shift key: 3 (effective shift: 3)
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

### Decrypt existing ciphertext

```bash
python3 cipher.py --decrypt --text "Khoor, Zruog!" --shift 3
```

This displays the supplied encrypted text and the recovered `Hello, World!`.

## How it works

Each ASCII letter is mapped to an index from 0 to 25. With key `k`:

```text
Encryption: (letter_index + k) mod 26
Decryption: (letter_index - k) mod 26
```

For example, with key 3, `A -> D`, `Z -> C`, and `a -> d`. Decryption applies
the opposite shift. Keys are equivalent modulo 26; key 26 leaves text unchanged.

## Verify

```bash
python3 -m unittest -v
```

Tests cover known ciphertext, alphabet wraparound, negative/large keys, empty
input, Unicode preservation, round trips across all effective shifts, both CLI
modes, and invalid key handling.

## Project requirements

| DecodeLabs requirement | Implementation |
| --- | --- |
| Encrypt user text using basic logic | `encrypt()` uses a Caesar shift |
| Decrypt encrypted text | `decrypt()` reverses the shift |
| Display encrypted and decrypted output | Both CLI modes print both results |

## Security limitations

This is an educational classical cipher, not protection for real secrets.
There are only 26 possible shifts, and letter patterns remain visible. Do not
use it for passwords, confidential files, or secure communications. Production
systems need vetted authenticated encryption and proper key management.

## Files

- `cipher.py` - cipher functions and command-line interface.
- `test_cipher.py` - automated checks using Python's standard library.
- `.github/workflows/tests.yml` - automated tests on GitHub.

## Author

[Amirbek Raxmatullayev](https://github.com/americooo)

Project 1: [Password Strength Checker](https://github.com/americooo/DecodeLabs-Password-Strength-Checker)
