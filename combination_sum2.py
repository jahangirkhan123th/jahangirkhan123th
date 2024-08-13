class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
        # Base case: if target is met, add the current path to the result
            if target == 0:
                result.append(path)
                return
            # Traverse through the candidates
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current candidate is greater than the target, no need to continue (since the list is sorted)
                if candidates[i] > target:
                    break
                # Recurse with the next candidate, reducing the target
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        # Sort candidates to facilitate skipping duplicates and pruning
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result

#    Example usage:
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
solution=Solution()
print(solution.combinationSum2(candidates, target))
