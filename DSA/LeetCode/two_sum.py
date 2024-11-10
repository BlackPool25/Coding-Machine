sorted_num = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left<right:
            res = sorted_num[left] + sorted_num[right]
            if res == target:
                return [nums.index(sorted_num[left]), nums.index(sorted_num[right])]
            elif res < target:
                left+=1
            else:
                right -= 1