import turtle;

# def draw_square():
#     window = turtle.Screen();
#     window.bgcolor("red")

#     brad = turtle.Turtle();
#     brad.shape("circle");
#     brad.color("yellow");
#     brad.speed(2);
    
#     brad.forward(100);
#     brad.right(90);
#     brad.forward(100);
#     brad.right(90);
#     brad.forward(100);
#     brad.right(90);
#     brad.forward(100);
#     brad.right(90);

#     window.exitonclick();

# draw_square();

#brad = turtle.Screen();
#brad.bgcolor('red')

def draw_square(sqr):
    for i in range(1,5):
        sqr.fd(100);
        sqr.right(90);

def art():
    window = turtle.Screen()
    window.bgcolor('black');
    
    brad = turtle.Turtle();
    brad.color('green');
    brad.shape('turtle');
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad);
        brad.right(10);
    
    window.exitonclick();

art();
    
# def nameS(lett):
#         lett.bk(100);
#         lett.right(90);
#         lett.fd(100);
#         lett.left(90);
#         lett.fd(100);
#         lett.right(90);
#         lett.fd(100)
#         lett.right(90)
#         lett.fd(100)

# def art():
#         window = turtle.Screen();
#         window.bgcolor('black');

#         brad = turtle.Turtle();
#         brad.color('green');
#         brad.shape('arrow');
#         brad.speed(2)
#         brad.position()
#         nameS(brad);
        
#         window.exitonclick();
        
        
# art();

# def art():
#         window = turtle.Screen();
#         window.bgcolor('black')
#         brad = turtle.Turtle();
#         brad.color('green', 'red')
#         brad.shape('turtle');
#         while True:
#                 brad.forward(200);
#                 brad.left(170);
#                 if abs(brad.pos()) < 1:
#                         break;

#         window.exitonclick();
# art();        