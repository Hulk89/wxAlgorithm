import random
import wx
from common import StepPanel
import time


class BubblePanel(StepPanel):
    def step_generator(self):
        for i in range(len(self.array) - 1, 0, -1):
            gray = list(range(i+1, len(self.array)))
            for j in range(i):
                self.color_dicts = {'#00ff00': [j], '#0000ff': [j+1], '#333333': gray}
                yield

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    emp_dict = {'#00ff00': [j+1], '#0000ff': [j]}
                else:
                    emp_dict = {'#555555': [j, j + 1]}
                emp_dict['#333333'] = gray
                self.color_dicts = emp_dict
                yield


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, "wxPython")
        bSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = BubblePanel(self)
        bSizer.Add(self.panel, 1, wx.EXPAND| wx.ALL)
        self.SetSizer(bSizer)
        self.Layout()

app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
