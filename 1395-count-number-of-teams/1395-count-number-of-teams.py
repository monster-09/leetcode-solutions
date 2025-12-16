class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        # Fix the middle soldier j
        for j in range(1, n - 1):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0

            # Count soldiers on the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            # Count soldiers on the right of j
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_smaller += 1

            # Add valid increasing and decreasing teams
            teams += left_smaller * right_greater
            teams += left_greater * right_smaller

        return teams
