from PySide6.QtWidgets import QTableWidget,QTableWidgetItem
from PySide6.QtCore import QRect,Qt,QDir
from WidgetComponents.Widget_Interface import Widget_Interface


class Files_Table(QTableWidget,Widget_Interface):
    def __init__(self, parent):
        super(Files_Table, self).__init__(parent)
        # 所有的选项
        self.AllItems = []

    pass
    def find_files(self, path):
        self._current_dir = QDir(path)
        self._find_dir = path
        file_name = "*.fbx"

        files = self._current_dir.entryList([file_name],
                QDir.Files | QDir.NoSymLinks)
        self.show_files(files)
        pass

    def show_files(self, files):
        self.setRowCount(0)
        for fn in files:
            # fn = files[fn_i]

            file_name_item = QTableWidgetItem(fn)
            file_name_item.setFlags(file_name_item.flags() ^ Qt.ItemIsEditable)

            row = self.rowCount()
            self.insertRow(row)
            self.setItem(row, 0, file_name_item)
        self.AllItems = files
        n = len(files)
        print(f"{n} file(s) found (Double click on a file to open it)")

    def GetSelectItems(self):
        items_text = []
        for item in self.selectedItems():
            items_text.append(item.text())
        return items_text

    def GetAllItems(self):
        return self.AllItems

    def GetItemsFullPath(self):
        ItemsText = self.GetSelectItems()
        FileFullPaths = []
        if ItemsText == []:
            for i in self.GetAllItems():
                FileFullPaths.append("{}/{}".format(self._find_dir,i))
            pass
        else:
            for i in ItemsText:
                FileFullPaths.append("{}\\{}".format(self._find_dir,i))
            pass
        
        return FileFullPaths

