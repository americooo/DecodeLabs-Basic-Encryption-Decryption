"""Known-answer, round-trip and command-line checks; no external dependencies."""

import string
import subprocess
import sys
import unittest
from pathlib import Path

from cipher import decrypt, encrypt


class CaesarCipherTests(unittest.TestCase):
    def test_known_answer(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(decrypt("Khoor, Zruog!", 3), "Hello, World!")

    def test_wraparound_and_negative_key(self):
        self.assertEqual(encrypt("XYZ xyz", 3), "ABC abc")
        self.assertEqual(encrypt("ABC abc", -3), "XYZ xyz")

    def test_unchanged_non_ascii_and_empty(self):
        self.assertEqual(encrypt("123 !\n\té O‘zbek 🔐", 26), "123 !\n\té O‘zbek 🔐")
        self.assertEqual(encrypt("é Ў 🔐 123!", 3), "é Ў 🔐 123!")
        self.assertEqual(encrypt("", 3), "")

    def test_all_effective_keys_round_trip(self):
        text = string.ascii_letters + string.digits + string.punctuation + "\né 🔐"
        for shift in range(-52, 53):
            with self.subTest(shift=shift):
                self.assertEqual(decrypt(encrypt(text, shift), shift), text)
        self.assertEqual(encrypt("abc", 1000001), encrypt("abc", 1000001 % 26))

    def run_cli(self, *args, user_input=None):
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("cipher.py")), *args],
            input=user_input, capture_output=True, text=True, check=False,
        )

    def test_cli_encrypt_and_decrypt(self):
        for args in [("--text", "Hello, World!", "--shift", "3"),
                     ("--decrypt", "--text", "Khoor, Zruog!", "--shift", "3")]:
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Encrypted text: Khoor, Zruog!", result.stdout)
            self.assertIn("Decrypted text: Hello, World!", result.stdout)

    def test_interactive_invalid_key_recovers(self):
        result = self.run_cli(user_input="Hello\ninvalid\n3\n")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Invalid key", result.stdout)
        self.assertIn("Encrypted text: Khoor", result.stdout)

    def test_invalid_cli_key(self):
        result = self.run_cli("--text", "hello", "--shift", "invalid")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid int value", result.stderr)


if __name__ == "__main__":
    unittest.main()
