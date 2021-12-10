# trick solution
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(c.lower() for c in licensePlate if c.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)
