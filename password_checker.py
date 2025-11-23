import math
import re

def password_entropy(password):
    charset = 0
    
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32
    
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def estimate_time(entropy):
    guesses = 2 ** entropy
    seconds = guesses / (10**8)  # 100M guesses per second
    return seconds

def rate_strength(entropy):
    if entropy < 28:
        return "Very Weak"
    if 28 <= entropy < 36:
        return "Weak"
    if 36 <= entropy < 60:
        return "Reasonable"
    if 60 <= entropy < 128:
        return "Strong"
    return "Very Strong"

def main():
    password = input("Enter password to analyze: ")
    ent = password_entropy(password)
    crack_time = estimate_time(ent)
    
    print(f"Entropy: {ent} bits")
    print(f"Estimated brute-force time: {crack_time:.2e} seconds")
    print(f"Strength rating: {rate_strength(ent)}")

if __name__ == "__main__":
    main()
