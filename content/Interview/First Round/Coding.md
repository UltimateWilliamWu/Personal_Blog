26.三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
```Python
class Solution:
    def maximumProduct(self, nums):
        # 记录三个最大值与两个最小值
        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")

        for x in nums:
            # 最大三数
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x

            # 最小两数
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x

        return max(max1 * max2 * max3, min1 * min2 * max1)

```