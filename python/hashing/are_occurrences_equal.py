from collections import defaultdict

def are_occurrences_equal(s):
    counts = defaultdict(int)

    for i in range(len(s)):
        counts[s[i]] += 1

    ans_set =  set()
    for letter in counts:
        ans_set.add(counts[letter])

    return len(ans_set) == 1

def are_occurrences_equal_2(s):
    counts = defaultdict(int)

    for i in range(len(s)):
        counts[s[i]] += 1

    frecuencies = counts.values()
    print(frecuencies)

    return len(set(frecuencies)) == 1

print(are_occurrences_equal_2("aabbccee"))