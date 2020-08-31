import random
import wx
from wxAlgorithm.sorts.common import StepPanel
from wxAlgorithm.constants import PALLETES


class BubblePanel(StepPanel):
    def step_generator(self):
        for i in range(len(self.array) - 1, 0, -1):
            for j in range(i):
                # color before step
                for k in range(i+1, len(self.array)):
                    self.colors[k] = 'disabled'
                self.colors[j] = 'key'
                self.colors[j+1] = 'candidate'

                yield
                # color after step
                for k in range(i+1, len(self.array)):
                    self.colors[k] = 'disabled'

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.colors[j+1] = 'key'
                    self.colors[j] = 'candidate'

                else:
                    self.colors[j] = self.colors[j+1] = 'candidate'

                yield

