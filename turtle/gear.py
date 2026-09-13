import turtle
t = turtle
t.speed(0)

for x in range(180):
	t.width(7)
	t.forward(2)
	t.right(2)
	if(x%10==0):
		t.left(90)
		t.forward(10)
		t.write(x)
		t.backward(10)
		t.width(1)
		t.right(90)

t.done()