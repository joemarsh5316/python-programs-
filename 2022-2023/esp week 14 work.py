import turtle

window = turtle.Screen()
window.bgcolor("sky blue")
turtle.done

tree = turtle.Turtle()
tree.color("forest green")

def make_tree_segment(size, top_position):
    tree.begin_fill()
    tree.setposition(0, top_position)
    tree.setposition(size, top_position - size)
    tree.setposition(-size, top_position - size)
    tree.setposition(0, top_position)
    tree.end_fill()


make_tree_segment(50, 20)
make_tree_segment(80, 0)
make_tree_segment(120, -30)
make_tree_segment(150, -60)
