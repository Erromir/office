board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# 邻居数组为给定的单元格找到8个相邻的单元格
neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

rows = len(board)
cols = len(board[0])

# 创建一个原始板的副本
copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

# 逐个单元地迭代
for row in range(rows):
    for col in range(cols):

        # 对于每个单元计算邻居的数量
        live_neighbors = 0
        for neighbor in neighbors:

            r = (row + neighbor[0])
            c = (col + neighbor[1])

            # 检查相邻细胞的有效性，以及它是否原来是一个活细胞
            # 评估是针对副本进行的，因为它永远不会更新。
            if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                live_neighbors += 1

        # 规则1或规则3
        if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
            board[row][col] = 0
        # 规则4
        if copy_board[row][col] == 0 and live_neighbors == 3:
            board[row][col] = 1

print(board)
结果如下。

# 输入
board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# 输出
board = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]


⑩ Turtle绘图

Turtle模块提供了在二维平面上移动的环境。

Turtle可以实现位置、航向和各种可能的状态和动作。

import turtle as tu

roo = tu.Turtle()  # 创建对象
wn = tu.Screen()  # 屏幕对象
wn.bgcolor("black")  # 屏幕背景
wn.title("分形树")
roo.left(90)  # 移动
roo.speed(20)  # 速度


def draw(l):  # 以长度'l'作为参数的递归函数
    if l < 10:
        return
    else:
        roo.pensize(2)  # 设置画笔大小
        roo.pencolor("yellow")  # 画笔颜色
        roo.forward(l)  # 朝向
        roo.left(30)  # 移动
        draw(3 * l / 4)  # 绘制
        roo.right(60)  # 移动
        draw(3 * l / 4)  # 绘制
        roo.left(30)  # 移动
        roo.pensize(2)
        roo.backward(l)  # 返回初始位置


draw(20)  # 绘制20次

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)


########################################################

def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(3)
        roo.pencolor("lightgreen")  # lightgreen
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan")  # cyan
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)
wn.exitonclick()
绘制时间较长，结果如下，挺好看的。




⑪ 计算器

Kivy是一个免费的开源Python库，可以快速轻松地开发高度交互的跨平台应用程序。

这里我将使用Python中的Kivy包来构建一个计算器GUI。

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class myApp(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        output_label = Label(size_hint_y=0.75, font_size=50)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        clear_button = Button(text='Clear', size_hint_y=None, height=100)
        def print_button_text(instance):
            output_label.text += instance.text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)
        def resize_label_text(label, new_height):
            label.fontsize = 0.5*label.height
        output_label.bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python Syntax error!'
        button_grid.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            output_label.text = " "
        clear_button.bind(on_press=clear_label)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        return root_widget


myApp().run()
