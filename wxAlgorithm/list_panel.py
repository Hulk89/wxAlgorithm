""" Algorithm List Panel
"""
import wx
from wxAlgorithm.navi_frame import NavigationFrame

class ListPanel(wx.Panel):
    def __init__(self, parent, lists):
        """
        Parameters
        ----------
        parent: NavigationFrame
                navigation이 가능한 Frame
        lists:  tuple(str, wx.Panel)
                list에 보일 이름, parent만을 argument로 갖는 wx.Panel
        """
        super().__init__(parent, wx.ID_ANY)
        assert isinstance(parent, NavigationFrame), "parent must be NavigationFrame"

        bSizer = wx.BoxSizer(wx.VERTICAL)
        listbox = wx.ListBox(self, wx.ID_ANY,
                             wx.DefaultPosition, wx.DefaultSize,
                             [l[0] for l in lists], 0 )
        listbox.Bind(wx.EVT_LISTBOX_DCLICK, self.clicked)
        bSizer.Add(listbox, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer(bSizer)
        self.Layout()

        self.lists = lists

    def clicked(self, event):
        """listbox에서 어떤 항목을 클릭하면 불립
        """
        index = event.GetSelection()
        parent = self.GetParent()
        parent.append(self.lists[index][1](parent))

