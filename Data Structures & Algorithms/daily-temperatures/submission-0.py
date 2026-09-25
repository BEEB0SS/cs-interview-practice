class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                new_temp_index = stack.pop()
                result[new_temp_index] = i - new_temp_index
            stack.append(i)    
        return result



        