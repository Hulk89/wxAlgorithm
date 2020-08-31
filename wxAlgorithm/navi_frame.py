import wx

class NavigationFrame(wx.Frame): 
    """Navigation이 가능한 frame. append로 panel을 넣고, back_button으로 이전 panel로 돌아간다.
    """
    def __init__(self, parent, size=wx.Size(800, 600)):
        super().__init__(parent,
                         id=wx.ID_ANY,
                         title=wx.EmptyString,
                         pos=wx.DefaultPosition,
                         size=size,
                         style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.panels = []

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.back_button = wx.Button(self, wx.ID_ANY, "<")
        self.sizer.Add(self.back_button, 0, wx.EXPAND|wx.ALL)

        self.SetSizer(self.sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        self.back_button.Bind(wx.EVT_BUTTON, self.on_back)
        self.back_button.Hide()

    def append(self, panel):
        if self.panels:
            prev_panel = self.panels[-1]
            prev_panel.Hide()
            self.sizer.Remove(1)
        self.panels.append(panel)
        self.sizer.Add(panel, 1, wx.EXPAND)
        panel.Show()

        self.Layout()

    def on_back(self, event):
        if len(self.panels) < 2:
            return
        latest_panel = self.panels.pop()
        latest_panel.Hide()
        self.sizer.Remove(1)
        
        panel = self.panels[-1]
        self.sizer.Add(panel, 1, wx.EXPAND)
        panel.Show()

        self.Layout()


    def Layout(self):
        if len(self.panels) >= 2:
            self.back_button.Show()
        else:
            self.back_button.Hide()
        super().Layout()

