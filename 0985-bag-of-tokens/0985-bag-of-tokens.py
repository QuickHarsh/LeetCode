class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N = len(tokens)
        tokens.sort()
        left, right = 0, N-1
        score = max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)

            elif score >= 1:
                power += tokens[right]
                right -= 1
                score -= 1

            else:
                break
        return max_score
            