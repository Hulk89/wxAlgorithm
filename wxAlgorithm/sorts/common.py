import random

import wx
from wxAlgorithm.constants import PALLETES

class ArrayPanel(wx.Panel):
    """array를 받아서 그림을 그려주는 panel."""
    def __init__(self, parent, array, colors):
        super().__init__(parent, wx.ID_ANY)
        self.set(array, colors)

        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def set(self, array, colors):
        self.array = array
        for color in colors:
            if color not in PALLETES.keys():
                raise ValueError("{} are not in PALLETES".format(color))
        self.colors = colors
        self.Refresh()

    def on_size(self, event):
        event.Skip()
        self.Refresh()

    def on_paint(self, event):
        canvas_w, canvas_h = self.GetClientSize()

        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush('white'))
        dc.Clear()

        array = self.array
        colors = self.colors

        max_val = max(array)
        el_width = canvas_w / len(array)

        for i, (el, color) in enumerate(zip(array, colors)):
            el_height = int(el / max_val * canvas_h)
            dc.SetBrush(wx.Brush(PALLETES[color]))

            dc.DrawRectangle(i * el_width,
                             canvas_h - el_height,
                             el_width,
                             el_height)


class StepPanel(wx.Panel):
    """step, reset button을 추가한 panel"""
    def __init__(self, parent, num_elements=5):
        super().__init__(parent, wx.ID_ANY)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = ArrayPanel(self, [], [])
        bSizer.Add(self.panel, 1, wx.EXPAND| wx.ALL)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.reset = wx.Button(self, wx.ID_ANY, "reset")
        self.next = wx.Button(self, wx.ID_ANY, "next")
        hSizer.Add(self.next, 1, wx.EXPAND)
        hSizer.Add(self.reset, 1, wx.EXPAND)
        bSizer.Add(hSizer, 0, wx.EXPAND|wx.ALL)

        self.SetSizer(bSizer)
        self.Layout()

        self.reset.Bind(wx.EVT_BUTTON, self.on_reset_clicked)
        self.next.Bind(wx.EVT_BUTTON, self.on_next_clicked)
        
        # not GUI
        self.num_elements = num_elements
        self.reset_data()

    def set_num_elements(self, num_elements):
        self.num_elements = num_elements
        self.reset_data()

    def reset_data(self):
        self.array = [i + 1 for i in range(self.num_elements)]
        random.shuffle(self.array)

        self.step_gen = self.step_generator()
        self.colors = ['default' for _ in self.array]
        self.panel.set(self.array, self.colors)
        self.next.Enable()

    def step_generator(self):
        raise NotImplementedError
    
    def on_reset_clicked(self, event):
        self.reset_data()

    def on_next_clicked(self, event):
        try:
            self.colors = ['default' for _ in self.array]
            next(self.step_gen)
            self.panel.set(self.array, self.colors)
        except StopIteration:
            self.panel.set(self.array, ['disabled' for _ in self.array])
            self.next.Disable()
