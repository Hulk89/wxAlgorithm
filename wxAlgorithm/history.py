import wx

class History:
    def __init__(self, sizer):
        self.panels = []
        self.sizer = sizer

    def show(self, *args, **kwargs):
        self.panels[-1].Show()

    def append(self, panel_func, *args, **kwargs):
        if self.panels:
            prev_panel = self.panels[-1]
            prev_panel.Hide()
            self.sizer.Remove(0)
        panel = panel_func(*args, **kwargs)
        self.panels.append(panel)
        self.sizer.Add(panel, 1, wx.EXPAND)
        panel.Show()

    def remove(self):
        if len(self.panels) < 2:
            return
        latest_panel = self.panels.pop()
        latest_panel.Hide()
        self.sizer.Remove(0)
        
        panel = self.panels[-1]
        self.sizer.Add(panel, 1, wx.EXPAND)
        panel.Show()
