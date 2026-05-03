"""
Project 2: Basic Encryption & Decryption
Batch: 2026 | DecodeLabs
Cybersecurity Analyst - Cryptographic Phase
Caesar Cipher Implementation
"""

import string
import time
from collections import Counter

class CaesarCipher:
    """
    Implementation of Caesar Cipher encryption/decryption.
    Shifts letters by a specified key value with wrap-around using modulo arithmetic.
    """
    
    def __init__(self, shift=3):
        """
        Initialize cipher with shift key
        
        Args:
            shift (int): Number of positions to shift (1-25 recommended)
        """
        self.shift = shift % 26  # Ensure shift is within 0-25
        self.name = "Caesar Cipher"
        
        # Create character mappings
        self.lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    def encrypt_char(self, char):
        """
        Encrypt a single character using Caesar cipher
        
        Math: E_n(x) = (x + n) mod 26
        where x = character position (0-25), n = shift key
        """
        if char in self.lowercase:
            # Get position (0-25), add shift, wrap with modulo 26
            original_pos = ord(char) - ord('a')
            encrypted_pos = (original_pos + self.shift) % 26
            return chr(encrypted_pos + ord('a'))
        
        elif char in self.uppercase:
            original_pos = ord(char) - ord('A')
            encrypted_pos = (original_pos + self.shift) % 26
            return chr(encrypted_pos + ord('A'))
        
        else:
            # Non-alphabetic characters remain unchanged
            return char
    
    def decrypt_char(self, char):
        """
        Decrypt a single character
        
        Math: D_n(x) = (x - n) mod 26
        """
        if char in self.lowercase:
            original_pos = ord(char) - ord('a')
            decrypted_pos = (original_pos - self.shift) % 26
            return chr(decrypted_pos + ord('a'))
        
        elif char in self.uppercase:
            original_pos = ord(char) - ord('A')
            decrypted_pos = (original_pos - self.shift) % 26
            return chr(decrypted_pos + ord('A'))
        
        else:
            return char
    
    def encrypt(self, text):
        """
        Encrypt entire text message
        
        Args:
            text (str): Plaintext message to encrypt
            
        Returns:
            str: Encrypted ciphertext
        """
        if not text:
            return ""
        
        return ''.join(self.encrypt_char(char) for char in text)
    
    def decrypt(self, ciphertext):
        """
        Decrypt entire ciphertext message
        
        Args:
            ciphertext (str): Encrypted message to decrypt
            
        Returns:
            str: Decrypted plaintext
        """
        if not ciphertext:
            return ""
        
        return ''.join(self.decrypt_char(char) for char in ciphertext)
    
    def set_shift(self, new_shift):
        """
        Change the shift key
        """
        self.shift = new_shift % 26
        print(f"✅ Shift key updated to: {self.shift}")
    
    def get_shift(self):
        """
        Get current shift key
        """
        return self.shift


class AdvancedCaesar(CaesarCipher):
    """
    Extended Caesar Cipher with additional security features
    """
    
    def __init__(self, shift=3):
        super().__init__(shift)
        # Add support for numbers and preserve case
        self.digits = string.digits
        
    def encrypt_char_advanced(self, char):
        """Enhanced encryption supporting numbers and symbols"""
        if char in self.lowercase or char in self.uppercase:
            return self.encrypt_char(char)
        elif char in self.digits:
            # Shift digits as well
            original_pos = ord(char) - ord('0')
            encrypted_pos = (original_pos + self.shift) % 10
            return chr(encrypted_pos + ord('0'))
        else:
            # Keep other characters (spaces, punctuation) unchanged
            return char
    
    def decrypt_char_advanced(self, char):
        """Enhanced decryption supporting numbers"""
        if char in self.lowercase or char in self.uppercase:
            return self.decrypt_char(char)
        elif char in self.digits:
            original_pos = ord(char) - ord('0')
            decrypted_pos = (original_pos - self.shift) % 10
            return chr(decrypted_pos + ord('0'))
        else:
            return char
    
    def encrypt_advanced(self, text):
        """Encrypt with advanced character support"""
        if not text:
            return ""
        return ''.join(self.encrypt_char_advanced(char) for char in text)
    
    def decrypt_advanced(self, ciphertext):
        """Decrypt with advanced character support"""
        if not ciphertext:
            return ""
        return ''.join(self.decrypt_char_advanced(char) for char in ciphertext)


class CipherBreaker:
    """
    Demonstrates brute-force attack on Caesar cipher
    Shows why key space matters in cryptography
    """
    
    @staticmethod
    def brute_force_attack(ciphertext):
        """
        Attempt all 25 possible shifts to break the cipher
        """
        print("\n" + "="*60)
        print("🔓 BRUTE FORCE ATTACK SIMULATION 🔓")
        print("="*60)
        print(f"Ciphertext: {ciphertext}")
        print("\nTrying all 25 possible shifts...")
        print("-"*60)
        
        results = []
        for shift in range(1, 26):
            cipher = CaesarCipher(shift)
            decrypted = cipher.decrypt(ciphertext)
            results.append((shift, decrypted))
            print(f"Shift {shift:2d}: {decrypted}")
        
        print("-"*60)
        print("⚠️  Note: Caesar cipher can be broken in seconds!")
        print("    Only 25 possible keys = trivial to brute force")
        return results
    
    @staticmethod
    def frequency_analysis(ciphertext):
        """
        Demonstrate frequency analysis attack
        """
        print("\n" + "="*60)
        print("📊 FREQUENCY ANALYSIS DEMONSTRATION 📊")
        print("="*60)
        
        # Count letter frequencies
        letters_only = [c.lower() for c in ciphertext if c.isalpha()]
        if not letters_only:
            print("No letters to analyze!")
            return
        
        freq = Counter(letters_only)
        
        print("\nLetter frequencies in ciphertext:")
        for letter, count in freq.most_common(10):
            percentage = (count / len(letters_only)) * 100
            bar = '█' * int(percentage)
            print(f"  {letter}: {bar} {percentage:.1f}%")
        
        print("\n💡 In English, 'E' is most common (about 12.7%)")
        print("   Attacker can guess shift by matching most common letters!")


class CryptoVisualizer:
    """
    Visual representation of the Caesar cipher transformation
    """
    
    @staticmethod
    def visualize_shift():
        """Show visual representation of letter shifting"""
        print("\n" + "="*60)
        print("🎨 CAESAR CIPHER VISUALIZATION 🎨")
        print("="*60)
        
        alphabet = string.ascii_lowercase
        shift = 3
        
        print("\nAlphabet mapping (shift=3):")
        print("Plain:  " + ' '.join(alphabet))
        print("        " + ' ' * 2 + '↓' * 26)
        
        shifted = alphabet[shift:] + alphabet[:shift]
        print("Cipher: " + ' '.join(shifted))
        
        print("\nExample: 'A' (pos 0) → shifted by 3 → 'D' (pos 3)")
        print("         'X' (pos 23) → shifted +3 → wrap to 'A' (pos 0)")
        print("\nFormula: Eₙ(x) = (x + n) mod 26")
    
    @staticmethod
    def show_modulo_example():
        """Demonstrate modulo arithmetic for wrap-around"""
        print("\n" + "="*60)
        print("🔄 MODULO ARITHMETIC DEMONSTRATION 🔄")
        print("="*60)
        
        print("\nWhen shifting past 'Z', we wrap back to 'A':")
        print("  'X' (23) + 3 = 26 → 26 mod 26 = 0 → 'A'")
        print("  'Y' (24) + 3 = 27 → 27 mod 26 = 1 → 'B'")
        print("  'Z' (25) + 3 = 28 → 28 mod 26 = 2 → 'C'")
        
        print("\nThis is why modulo 26 is essential for finite alphabet!")


def run_interactive_mode():
    """Interactive mode for user to test encryption/decryption"""
    print("\n" + "="*60)
    print("🎮 INTERACTIVE MODE 🎮")
    print("="*60)
    
    # Get shift key from user
    while True:
        try:
            shift = int(input("\nEnter shift key (1-25, or 0 to exit): "))
            if shift == 0:
                return None
            if 1 <= shift <= 25:
                break
            print("❌ Shift must be between 1 and 25!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    cipher = AdvancedCaesar(shift)
    print(f"\n✅ Cipher initialized with shift: {shift}")
    
    while True:
        print("\n" + "-"*40)
        print("OPTIONS:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Change shift key")
        print("4. Show current shift")
        print("5. Return to main menu")
        print("-"*40)
        
        choice = input("\nYour choice (1-5): ").strip()
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            if message:
                encrypted = cipher.encrypt_advanced(message)
                print(f"\n📝 Original:    {message}")
                print(f"🔒 Encrypted:   {encrypted}")
            else:
                print("❌ Message cannot be empty!")
        
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            if message:
                decrypted = cipher.decrypt_advanced(message)
                print(f"\n🔒 Ciphertext:  {message}")
                print(f"📝 Decrypted:   {decrypted}")
            else:
                print("❌ Message cannot be empty!")
        
        elif choice == '3':
            try:
                new_shift = int(input("Enter new shift (1-25): "))
                if 1 <= new_shift <= 25:
                    cipher.set_shift(new_shift)
                else:
                    print("❌ Shift must be between 1 and 25!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '4':
            print(f"🔑 Current shift key: {cipher.get_shift()}")
        
        elif choice == '5':
            break
        
        else:
            print("❌ Invalid choice!")


def main():
    """
    Main program for Caesar Cipher demonstration
    """
    print("\n" + "="*60)
    print("🔐 DECODELABS CAESAR CIPHER IMPLEMENTATION 🔐")
    print("Cybersecurity Project 2 - Confidentiality Phase")
    print("="*60)
    print("\nThis tool demonstrates:")
    print("• Symmetric encryption with Caesar cipher")
    print("• Mathematical transformation (modulo arithmetic)")
    print("• Brute-force vulnerability demonstration")
    print("• Frequency analysis concepts")
    
    # Default demonstration
    default_cipher = CaesarCipher(3)
    
    while True:
        print("\n" + "-"*60)
        print("MAIN MENU:")
        print("1. 🔐 Run default demonstration")
        print("2. 🎮 Interactive mode (encrypt/decrypt your own messages)")
        print("3. 🔓 Show brute-force attack vulnerability")
        print("4. 📊 Show frequency analysis")
        print("5. 🎨 Show cipher visualization")
        print("6. ❌ Exit")
        print("-"*60)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # Default demonstration
            print("\n" + "="*60)
            print("📚 DEFAULT DEMONSTRATION 📚")
            print("="*60)
            
            test_messages = [
                "Hello World!",
                "The quick brown fox jumps over the lazy dog",
                "Cyber Security @ DecodeLabs 2026"
            ]
            
            for message in test_messages:
                print(f"\n📝 Original:    {message}")
                encrypted = default_cipher.encrypt(message)
                print(f"🔒 Encrypted:   {encrypted}")
                decrypted = default_cipher.decrypt(encrypted)
                print(f"📝 Decrypted:   {decrypted}")
                print(f"✅ Success:     {'✓' if message == decrypted else '✗'}")
        
        elif choice == '2':
            run_interactive_mode()
        
        elif choice == '3':
            print("\n" + "="*60)
            print("🔓 SECURITY VULNERABILITY DEMONSTRATION 🔓")
            print("="*60)
            print("Caesar cipher has only 25 possible keys!")
            print("This makes it vulnerable to brute-force attacks.")
            
            # Take a sample ciphertext
            sample = default_cipher.encrypt("Secret Message")
            print(f"\nSample ciphertext: {sample}")
            
            breaker = CipherBreaker()
            breaker.brute_force_attack(sample)
            
            print("\n⚠️  REAL-WORLD IMPLICATION:")
            print("   Never use Caesar cipher for actual security!")
            print("   Modern encryption uses keys with 2^128+ possibilities.")
        
        elif choice == '4':
            breaker = CipherBreaker()
            # Create a longer ciphertext for analysis
            long_text = "This is a longer message that will be encrypted for frequency analysis demonstration purposes"
            encrypted = default_cipher.encrypt(long_text)
            print(f"\nEncrypted text: {encrypted}")
            breaker.frequency_analysis(encrypted)
        
        elif choice == '5':
            visualizer = CryptoVisualizer()
            visualizer.visualize_shift()
            visualizer.show_modulo_example()
        
        elif choice == '6':
            print("\n👋 Thank you for using DecodeLabs Caesar Cipher!")
            print("Remember: This is for educational purposes only.")
            print("Modern applications use AES, RSA, or other strong algorithms.")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()