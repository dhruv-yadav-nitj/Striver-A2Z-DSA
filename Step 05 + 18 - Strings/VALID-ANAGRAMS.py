def validAnagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)
