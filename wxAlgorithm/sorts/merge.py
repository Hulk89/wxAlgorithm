from wxAlgorithm.sorts.common import StepPanel
from wxAlgorithm.constants import PALLETES

class MergePanel(StepPanel):
    def disable_outrange(self, left, right):
        for i in range(len(self.array)):
            if i < left or i >= right:
                self.colors[i] = 'disabled'

    def merge_sort(self, left, right):
        if right - left <= 1:
            self.disable_outrange(left, right)
            self.colors[left] = 'key'
            yield
        else:
            mid = (left + right) // 2

            yield from self.merge_sort(left, mid)  # left <= arr < mid
            yield from self.merge_sort(mid, right)  # mid <= arr < right
            
            yield from self.merge(left, mid, right)

    def merge(self, left, mid, right):
        self.disable_outrange(left, right)
        for i in range(left, right):
            self.colors[i] = 'candidate'
        x1 = left
        x2 = mid
        new_array = []
        yield

        self.disable_outrange(left, right)
        for i in range(left, right):
            self.colors[i] = 'candidate'
        while x1 < mid and x2 < right:
            if self.array[x1] <= self.array[x2]:
                new_array.append(self.array[x1])
                x1 += 1
            else:
                new_array.append(self.array[x2])
                x2 += 1
        
        while x1 < mid:
            new_array.append(self.array[x1])
            x1 += 1

        while x2 < right:
            new_array.append(self.array[x2])
            x2 += 1
        for i in range(left, right):
            self.array[i] = new_array[i - left]

        yield

    def step_generator(self):
        yield from self.merge_sort(0, len(self.array))  # 0 <= arr < len
