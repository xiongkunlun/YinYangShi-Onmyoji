#显示当前window的所有句柄
import win32gui

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
            hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update(
            {hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        # method_name(h)
        print(h, t)