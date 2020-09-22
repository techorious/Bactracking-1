class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        path = []
        
        self.backtracking(output, candidates, target, 0, path)
        return output
        
    def backtracking(self, output, candidates, target, index, path):
        if(target == 0):
            print(path)
            output.append(deepcopy(path))
            return
        
        elif target < 0:
            print(path)
            return
        
        for i in range(index, len(candidates)):
            path.append(candidates[i])

            self.backtracking(output, candidates, target - candidates[i], i, path)

            path.pop()
