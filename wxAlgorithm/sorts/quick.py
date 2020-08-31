import random
import wx
from wxAlgorithm.sorts.common import StepPanel
from wxAlgorithm.constants import PALLETES

class QuickPanel(StepPanel):
    def disable_outrange(self, left, right):
        for i in range(len(self.array)):
            if i < left or i >= right:
                self.colors[i] = 'disabled'

    def quick(self, left, right):
        self.disable_outrange(left, right)
        if right - left == 0:
            yield
        elif right - left == 1:
            self.colors[left] = 'key'
            yield
        else:
            pivot = self.array[left]
            self.colors[left] = 'key'
            yield

            self.disable_outrange(left, right)
            greater = [e for e in self.array[left + 1:right] if e > pivot]
            less = [e for e in self.array[left + 1:right] if e <= pivot]

            new_arr = less + [pivot] + greater
            for i, e in enumerate(new_arr):
                self.array[left + i] = e
                self.colors[left + i] = 'candidate'
            self.colors[left + len(less)] = 'key'
            yield

            yield from self.quick(left, left + len(less))
            yield from self.quick(left + len(less) + 1, right)

    def step_generator(self):
        yield from self.quick(0, len(self.array))  # 0 <= arr < len
