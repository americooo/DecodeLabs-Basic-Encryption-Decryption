"""DecodeLabs Project 2: an educational Caesar cipher (not secure encryption)."""

import argparse


def encrypt(text: str, shift: int) -> str:
    """Shift ASCII letters, preserving case and all other characters."""
    result = []
    for char in text:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            result.append(char)
            continue
        result.append(chr(base + (ord(char) - base + shift) % 26))
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """Reverse the Caesar shift using the same key."""
    return encrypt(text, -shift)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Text to encrypt; prompts when omitted")
    parser.add_argument("--shift", type=int, help="Integer key; prompts when omitted")
    parser.add_argument("--decrypt", action="store_true", help="Treat input as ciphertext")
    args = parser.parse_args()
    try:
        text = args.text if args.text is not None else input("Enter text: ")
        shift = args.shift
        while shift is None:
            try:
                shift = int(input("Enter shift key (integer, e.g. 3): "))
            except ValueError:
                print("Invalid key. Please enter an integer.")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return 130

    if args.decrypt:
        encrypted = text
        decrypted = decrypt(text, shift)
    else:
        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)
    print(f"Shift key: {shift} (effective shift: {shift % 26})")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
