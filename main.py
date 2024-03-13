class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n
  
        total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
        low = 1
        high = n
        while low < high:
            pivot = (low+high)//2
            first_sum = pivot * (pivot + 1) // 2
            second_sum = total_sum - first_sum + pivot
            
            if first_sum == second_sum:
                return pivot
            elif first_sum < second_sum:
                low = pivot + 1
            else:
                high = pivot - 1
        return -1         


        
