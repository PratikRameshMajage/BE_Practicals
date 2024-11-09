def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)

    return matches

# Example usage
text = "abracadabra"
pattern = "abra"
naive_matches = naive_string_matching(text, pattern)
print("Naive String Matching matches at indices:", naive_matches)
