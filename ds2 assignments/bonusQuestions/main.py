
import turtle


def permDiff(c, op, j):
  if (len(c) == j + 1):
    return op
  p = []
  cc = c.copy()
  cc.pop(j)
  for i in range(len(cc)):
    g = str(c[j]) + str(cc[i])
    if (g not in op and g not in p):
      p.append(g)
  return permDiff(c, op + p, j + 1)


def permIden(c, op):
  if (len(c) == 0):
    return op
  p = []
  for i in range(1, len(c)):
    g = str(c[0]) + str(c[i])
    if (g not in op and g not in p):
      p.append(g)
  return permIden(c[1:], op + p)


solIdentical = []
solDiff = []


def identicalRec(n, l, c):
  if (n == 1):
    if (c[0] != 1 and c[1] != 1):
      solIdentical.append(l + [c])
    return

  p = permIden(c, [])
  fp = []
  for i in range(len(p)):
    if (str(n) not in p[i]):
      fp.append(p[i])
  for i in range(len(fp)):
    ll = l.copy()
    ll.append([int(fp[i][0]), int(fp[i][1])])
    fc = c.copy()
    fc.remove(int(fp[i][0]))
    fc.remove(int(fp[i][1]))
    ll.append(identicalRec(n - 1, ll, fc))


def diffRec(n, l, c):
  global solDiff
  if (n == 1):
    if (c[0] != 1 and c[1] != 1):
      solDiff.append(l + [c])
      if (c[0] != c[1]):
        solDiff.append(l + [[c[1], c[0]]])
    (solDiff[-1])
    return

  p = permDiff(c, [], 0)
  fp = []
  for i in range(len(p)):
    if (str(n) not in p[i]):
      fp.append(p[i])
  for i in range(len(fp)):
    ll = l.copy()
    ll.append([int(fp[i][0]), int(fp[i][1])])
    fc = c.copy()
    fc.remove(int(fp[i][0]))
    fc.remove(int(fp[i][1]))
    ll.append(diffRec(n - 1, ll, fc))


n = 0


def main():
  global n
  n = int(input("number of cups: "))
  c = []
  for i in range(1, n // 2 + 1):
    c += [i, i]
  identicalRec(n // 2, [], c)
  diffRec(n // 2, [], c)
  print("number of combinations if cups are taken non identical", len(solDiff))
  print("number of combinations if cups are taken identical", len(solIdentical))


main()

colors = ["", "red", "green", "blue", "yellow", "orange",
          "purple", "pink", "brown", "cyan", "magenta"]


def draw(o):
  solutions = o.copy()
  screen = turtle.Screen()
  screen_height = screen.window_height()
  screen.setup(width=1.0, height=1.0)
  screen.bgcolor("white")

  my_turtle = turtle.Turtle()
  my_turtle.speed(0)
  my_turtle.hideturtle()

  my_turtle.penup()
  my_turtle.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
  my_turtle.pendown()

  def draw_rectangle(color, bg, h, w):
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for _ in range(2):
      my_turtle.forward(w)
      my_turtle.right(90)
      my_turtle.forward(h)
      my_turtle.right(90)
    my_turtle.end_fill()

    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.forward(h + 10)

    my_turtle.fillcolor(bg)
    my_turtle.begin_fill()
    for _ in range(2):
      my_turtle.forward(h // 2)
      my_turtle.left(90)
      my_turtle.forward(w)
      my_turtle.left(90)

    my_turtle.end_fill()

  window_width = screen.window_width()
  r = 30 * n
  c = 0
  for solution in solutions:
    for i in range(len(solution)):
      group = solution[i]
      for j in range(2):
        my_turtle.pendown()
        draw_rectangle(colors[group[j]], colors[n // 2 - i], 40, 20)
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(25)
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.right(90)
      my_turtle.penup()
    c += 1
    my_turtle.forward(15)
    if (c >= window_width // (r)):
      c = 0
      my_turtle.goto(-turtle.window_width() / 2,
                     my_turtle.ycor() - 90)
  turtle.update()

  screen.exitonclick()


# draw(solIdentical)
draw(solDiff)
