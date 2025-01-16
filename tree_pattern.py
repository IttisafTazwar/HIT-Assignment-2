
import turtle



def draw_tree(t, branch_length, angle, depth, reduction_factor):
    if depth == 0:
        return

    t.forward(branch_length)

    t.left(angle)
    draw_tree(t, branch_length * reduction_factor, angle, depth - 1, reduction_factor)

    t.right(2 * angle)
    draw_tree(t, branch_length * reduction_factor, angle, depth - 1, reduction_factor)

    t.left(angle)
    t.backward(branch_length)


def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.left(90)
    t.speed(0)
    return t


def main():
    left_angle = float(input("Enter the left branch angle (degrees): "))
    right_angle = float(input("Enter the right branch angle (degrees): "))
    starting_length = float(input("Enter the starting branch length: "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor: "))

    t = setup_turtle()
    t.penup()
    t.goto(0, -200)
    t.pendown()

    draw_tree(t, starting_length, left_angle, recursion_depth, reduction_factor)

    turtle.done()


if __name__ == "__main__":
    main()
