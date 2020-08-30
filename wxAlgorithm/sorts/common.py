import random

import wx

class ArrayPanel(wx.Panel):
    """array를 받아서 그림을 그려주는 panel."""
    def __init__(self, parent, array):
        super().__init__(parent, wx.ID_ANY)
        self.set(array, {})

        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def set(self, array, color_dicts):
        self.array = array
        self.color_dicts = color_dicts
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

        max_val = max(array)
        el_width = canvas_w / len(array)

        for i, el in enumerate(array):
            el_height = int(el / max_val * canvas_h)

            for k, v in self.color_dicts.items():
                if i in v:
                    dc.SetBrush(wx.Brush(k))
                    break
            else:
                dc.SetBrush(wx.Brush("#71dcf4"))
            dc.DrawRectangle(i * el_width,
                             canvas_h - el_height,
                             el_width,
                             el_height)


class StepPanel(wx.Panel):
    """step, reset button을 추가한 panel"""
    def __init__(self, parent, num_elements=5):
        super().__init__(parent, wx.ID_ANY)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = ArrayPanel(self, [])
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
        self.color_dicts = {}
        self.panel.set(self.array, self.color_dicts)
        self.next.Enable()

    def step_generator(self):
        raise NotImplementedError
    
    def on_reset_clicked(self, event):
        self.reset_data()

    def on_next_clicked(self, event):
        try:
            next(self.step_gen)
            self.panel.set(self.array, self.color_dicts)
        except StopIteration:
            self.panel.set(self.array, {'#333333': range(len(self.array))})
            self.next.Disable()
