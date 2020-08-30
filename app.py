import wx
from wxAlgorithm.sorts.bubble import BubblePanel
from wxAlgorithm.history import History


class Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent,
                         id=wx.ID_ANY)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        back = wx.Button(self, wx.ID_ANY, "back")
        bSizer.Add(back, 0, wx.EXPAND|wx.ALL)
        self.panel = BubblePanel(self)
        bSizer.Add(self.panel, 1, wx.EXPAND|wx.ALL)
        
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.statictext = wx.StaticText(self, wx.ID_ANY, "#elements: 5", style=wx.ALIGN_CENTER)
        hSizer.Add(self.statictext, 1, wx.EXPAND|wx.ALL)
        slider = wx.Slider(self, wx.ID_ANY, 5, 2, 10)
        hSizer.Add(slider, 3, wx.EXPAND|wx.ALL)
        bSizer.Add(hSizer, 0, wx.EXPAND|wx.ALL)

        self.SetSizer(bSizer)
        self.Layout()

        slider.Bind(wx.EVT_SLIDER, self.on_slide)
        back.Bind(wx.EVT_BUTTON, self.on_back)
        self.Bind(wx.EVT_SIZE, self.on_resize)

    def on_resize(self, event):
        event.Skip()
        self.Layout()
        self.Refresh()

    def on_slide(self, event):
        obj = event.GetEventObject()
        value = obj.GetValue()
        if self.panel.num_elements != value:
            self.panel.set_num_elements(value)
            self.statictext.SetLabel("#elements: {}".format(value))
            self.Layout()

    def on_back(self, event):
        parent = self.GetParent()
        parent.back()

class ListPanel(wx.Panel):
    def __init__(self, parent, lists):
        super().__init__(parent, wx.ID_ANY)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        listbox = wx.ListBox(self, wx.ID_ANY,
                             wx.DefaultPosition, wx.DefaultSize,
                             [l[0] for l in lists], 0 )
        listbox.Bind(wx.EVT_LISTBOX_DCLICK, self.clicked)
        self.lists = lists
        bSizer.Add(listbox, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer(bSizer)
        self.Layout()

    def clicked(self, event):
        index = event.GetSelection()
        parent = self.GetParent()
        parent.append(self.lists[index][1], parent)

lists = [
    ('BubbleSort', Panel)
]

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent,
                         id=wx.ID_ANY,
                         title=wx.EmptyString,
                         pos=wx.DefaultPosition,
                         size=wx.Size(800, 600),
                         style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.history = History(sizer)
        self.append(ListPanel, self, lists)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def Show(self, *args, **kwargs):
        super().Show(*args, **kwargs)
        self.history.show()

    def append(self, *args, **kwargs):
        self.history.append(*args, **kwargs)
        self.Layout()

    def back(self):
        self.history.remove()
        self.Layout()


app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
