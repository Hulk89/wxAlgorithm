import wx
from wxAlgorithm.sorts import *
from wxAlgorithm.navi_frame import NavigationFrame
from wxAlgorithm.list_panel import ListPanel


lists = [
    ('BubbleSort', BubblePanel),
    ('QuickSort', QuickPanel),
    ('MergeSort', MergePanel)
]


app = wx.App(False)
frame = NavigationFrame(None)
listpanel = ListPanel(frame, lists)
frame.append(listpanel)

frame.Show(True)
app.MainLoop()
