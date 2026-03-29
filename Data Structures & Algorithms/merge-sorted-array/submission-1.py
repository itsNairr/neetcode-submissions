class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[len(nums1)-m:] = nums1[0:m]
        i = len(nums1)-m
        j = 0
        k = 0

        while j < len(nums2):
            print(nums1)
            if i == len(nums1) or nums2[j] < nums1[i]:
                nums1[k] = nums2[j]
                j+=1
                k += 1
            else:
                nums1[k] = nums1[i]
                k += 1
                i +=1

        