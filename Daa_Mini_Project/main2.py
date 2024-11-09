def rabin_karp(text, pattern, q=101):
    d = 256  # Number of characters in the input alphabet
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q  # The highest power of d
    p = 0  # Hash value for the pattern
    t = 0  # Hash value for the text
    occurrences = []

    # Preprocessing: Calculate the hash value of the pattern and the first window of the text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):
        if p == t:
            # Check for characters one by one
            if text[i:i + m] == pattern:
                occurrences.append(i)

        # Calculate hash value for the next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return occurrences

# Example usage
text = "abracadabra"
pattern = "abra"

# Run the Rabin-Karp Algorithm
rabin_karp_matches = rabin_karp(text, pattern)
print("Rabin-Karp Matches:", rabin_karp_matches)

