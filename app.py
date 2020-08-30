import wx
from wxAlgorithm.sorts.bubble import BubblePanel


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, "wxPython")
        bSizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.panel = BubblePanel(self)

        bSizer.Add(self.panel, 1, wx.EXPAND|wx.ALL)
        
        self.statictext = wx.StaticText(self, wx.ID_ANY, "#elements: 5", style=wx.ALIGN_CENTER)
        hSizer.Add(self.statictext, 1, wx.EXPAND|wx.ALL)
        slider = wx.Slider(self, wx.ID_ANY, 5, 2, 10)
        hSizer.Add(slider, 3, wx.EXPAND|wx.ALL)
        bSizer.Add(hSizer, 0, wx.EXPAND|wx.ALL)

        self.SetSizer(bSizer)
        self.Layout()
        slider.Bind(wx.EVT_SLIDER, self.on_slide)

    def on_slide(self, event):
        obj = event.GetEventObject()
        value = obj.GetValue()
        if self.panel.num_elements != value:
            self.panel.set_num_elements(value)
            self.statictext.SetLabel("#elements: {}".format(value))
            self.Layout()
app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
