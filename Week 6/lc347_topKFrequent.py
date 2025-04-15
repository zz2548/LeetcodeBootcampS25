class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given: array: nums
        # Return: k most frequen elements

        # What we can do
        # 1. Create a max heap where key is number of occurences
        #    Heapify is O(n)
        # 2. Pop from max heap k times

        # Alternatively
        # Use hashmap to count occurences
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # O(n)