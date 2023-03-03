from PySide6.QtWidgets import QWidget



# 仅能QWidget 继承
class Widget_Interface(object):
    def __init__(self) -> None:
        print("接口初始化")
        # 所有实例化过的子类 都装这里面
        self.AllChildsWidget = []
        pass

    def __init_subclass__(cls) -> None:
        print("子类初始化:{}".format(cls))
        pass

    # 初始化期间不要调用 = -=
    # Ui_MainWindow() 初始化完成之后才可调用
    def GetMainWindowUI(this):
        from Window.MainWindow import MainWindow
        
        assert isinstance(this, QWidget)
        __MainWindow = this.topLevelWidget()
        assert isinstance(__MainWindow, MainWindow)
        return __MainWindow.ui
    pass