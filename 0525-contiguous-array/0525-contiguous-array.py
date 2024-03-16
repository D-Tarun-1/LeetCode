class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
       #dic={0:1}
       #s=0
       #c=0
       #for i in nums:
           #s+=i
           #r=s%
           #if(r not in dic):
           #    dic[r]=1
           #else:
           #     c+=dic[r]
           #     dic[r]+=1
       #return c
       count = 0
       max_len = 0
       count_map = {0:-1}
       for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count-=1
            if count in count_map:
                max_len = max(max_len,i - count_map[count])
            else:
                count_map[count] = i
       return max_len
