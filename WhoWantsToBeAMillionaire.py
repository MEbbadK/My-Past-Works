# Who Whants To Be A Millionaire
# Ebbad Khalid
# ICS 201 Mrs.Hwang
# January 10, 2017

import turtle

canvas = turtle.Screen()
canvas.bgcolor("blue")
t = turtle.Turtle() 
t.speed(10)
t.pencolor("red")

t.shape("circle")
t.shapesize(16,20,8)
t.fillcolor("yellow")

turtle.pencolor("yellow")
turtle.setpos(-190,0)
turtle.pencolor("blue")
turtle.write("Who Wants To Be A Millionaire", move=False , align="left" , font=("Arial", 20, "normal"))

#d and f are to create the bills in turtle

d = turtle.Turtle()

d.pencolor("green")
d.penup()
d.setpos(-360,-150)
d.shape("square")
d.shapesize(15,10,8)
d.fillcolor("green")

f = turtle.Turtle()

f.pencolor("green")
f.penup()
f.setpos(360,-150)
f.shape("square")
f.shapesize(15,10,8)
f.fillcolor("green")

#everything from g to bd is to create my coins

g = turtle.Turtle()
g.penup()
g.setpos(-360,150)
g.left(90)
g.pendown
g.shape("circle")
g.shapesize(5,2,2)
g.fillcolor("yellow")


y = turtle.Turtle()
y.penup()
y.setpos(-360,160)
y.left(90)
y.pendown
y.shape("circle")
y.shapesize(5,2,2)
y.fillcolor("yellow")


gx = turtle.Turtle()
gx.penup()
gx.setpos(-360,170)
gx.left(90)
gx.pendown
gx.shape("circle")
gx.shapesize(5,2,2)
gx.fillcolor("yellow")


gd = turtle.Turtle()
gd.penup()
gd.setpos(-360,180)
gd.left(90)
gd.pendown
gd.shape("circle")
gd.shapesize(5,2,2)
gd.fillcolor("yellow")


ge = turtle.Turtle()
ge.penup()
ge.setpos(-360,190)
ge.left(90)
ge.pendown
ge.shape("circle")
ge.shapesize(5,2,2)
ge.fillcolor("yellow")

gw = turtle.Turtle()
gw.penup()
gw.setpos(-360,200)
gw.left(90)
gw.pendown
gw.shape("circle")
gw.shapesize(5,2,2)
gw.fillcolor("yellow")

gq = turtle.Turtle()
gq.penup()
gq.setpos(-360,210)
gq.left(90)
gq.pendown
gq.shape("circle")
gq.shapesize(5,2,2)
gq.fillcolor("yellow")

gr = turtle.Turtle()
gr.penup()
gr.setpos(-360,220)
gr.left(90)
gr.pendown
gr.shape("circle")
gr.shapesize(5,2,2)
gr.fillcolor("yellow")

gb = turtle.Turtle()
gb.penup()
gb.setpos(-360,230)
gb.left(90)
gb.pendown
gb.shape("circle")
gb.shapesize(5,2,2)
gb.fillcolor("yellow")

gc = turtle.Turtle()
gc.penup()
gc.setpos(-360,240)
gc.left(90)
gc.pendown
gc.shape("circle")
gc.shapesize(5,2,2)
gc.fillcolor("yellow")

bt = turtle.Turtle()
bt.penup()
bt.setpos(360,150)
bt.left(90)
bt.pendown
bt.shape("circle")
bt.shapesize(5,2,2)
bt.fillcolor("yellow")



br = turtle.Turtle()
br.penup()
br.setpos(360,160)
br.left(90)
br.pendown
br.shape("circle")
br.shapesize(5,2,2)
br.fillcolor("yellow")

be = turtle.Turtle()
be.penup()
be.setpos(360,170)
be.left(90)
be.pendown
be.shape("circle")
be.shapesize(5,2,2)
be.fillcolor("yellow")

bw = turtle.Turtle()
bw.penup()
bw.setpos(360,180)
bw.left(90)
bw.pendown
bw.shape("circle")
bw.shapesize(5,2,2)
bw.fillcolor("yellow")

bq = turtle.Turtle()
bq.penup()
bq.setpos(360,190)
bq.left(90)
bq.pendown
bq.shape("circle")
bq.shapesize(5,2,2)
bq.fillcolor("yellow")

ba = turtle.Turtle()
ba.penup()
ba.setpos(360,200)
ba.left(90)
ba.pendown
ba.shape("circle")
ba.shapesize(5,2,2)
ba.fillcolor("yellow")

bd = turtle.Turtle()
bd.penup()
bd.setpos(360,210)
bd.left(90)
bd.pendown
bd.shape("circle")
bd.shapesize(5,2,2)
bd.fillcolor("yellow")




#See, making it so that you can only continue by clicking on the turtle screen is a design choice. It is done with intent.

turtle.penup()
turtle.setpos(-150,-210)
turtle.pencolor("red")
turtle.write("Click only on the screen ", move=False , align="left" , font=("Arial", 20, "normal"))
turtle.setpos(-70,-230)
turtle.write("to continue", move=False , align="left" , font=("Arial", 20, "normal"))
canvas.exitonclick()

#Now this is where the regular coding begins


print("Welcome To Who Wants To Be A Millionaire.")

print("Test your knowledge and win.")

name = input("Now tell us player, what is the name you would like to go by this game?")

import random
num = random.randint(1,4)

#My code would be much cleaner if I could've made the guess's make a variable equal yes or no
#and then turn use it to ask the next questions but
#I ran into an error when I tried something like that and I couldn't solve
#it so I just copied and pasted when I needed to.

if num == 1:
    print("For the thousand dolllar question,")
    print("What is the actual name of the rapper who goes by the name of Slim Shady?")
    guess1=int(input("Press 1 if Marshall Mathers, press 2 if Jay Park, press 3 if Shawn Carter, press 4 if Robert Winkle"))
    if guess1 ==int(1):
        print("Correct, now let's move on to the $100,000 question")
        num2 = random.randint(1,3)
        if num2==1:
            print("Which part of the body is absolutle useless?")
            guess2=int(input("1, the kidney, 2, the spleen, 3, cytoplasm, 4, the appendix"))
            if guess2==4:
                print("Correct, now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            #Now this is an easy question if you know your stuff.
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
                
            else :
                print("Incorrect, please play again.")
        elif num2==2:
            #This is a homage to a classic Who Wants To Be A Millionaire question and
            #you can find it easily on the internet if you do some digging
            print("What is the Pokemon mascot?")
            guess2=int(input("1, Clefairy, 2, Frodo, 3, Wartortle, 4, Pikachu?"))
            if guess2 == int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
        elif num2==3:
            print("What is the movie that has grossed the most money in the")
            print("box office worldwide adjusted for infation?")
            guess2=int(input("1, Star Wars, 2, Avatar, 3, Titanic, 4, Gone With The Wind?"))
            if guess2==int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")    
        
    else:
        print("Incorrect, please play again.")
        
    
elif num == 2:
    print("For the thousand dolllar question,")
    print("Who was the scientist who once yelled Eureka when he made a discovery?")
    guess1=int(input("Press 1 if Albert Einstein, Press 2 if Isaac Newton, press 3 if Galileo Galilei, press 4 if Archimedes"))
    if guess1 == int(4):
        print("Correct, now let's move on to the $100,000 question")
        num2 = random.randint(1,3)
        if num2==1:
            print("Which part of the body is absolutle useless?")
            guess2=int(input("1, the kidney, 2, the spleen, 3, cytoplasm, 4, the appendix"))
            if guess2==4:
                print("Correct, now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
                
            else :
                print("Incorrect, please play again.")
        elif num2==2:
            print("What is the Pokemon mascot?")
            guess2==int(input("1, Clefairy, 2, Frodo, 3, Wartortle, 4, Pikachu"))
            if guess2 == int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                        print("Who was the only US President to get impeached before Bill Clinton?")
                        guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                        if guess3==int(3):
                            print("Correct, now let's move on to the final, $1,000,000 question.")
                            num4 = random.randint(1,2)
                            if num4 == 1:
                                print("For $1,000,000 dollars,")
                                print("who was the 18th president of the USA?")
                                guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                                if guess4== int(1):
                                    print("Congratulations, you have won the game and $1,000,000.")
                                    print("Please play again whenever you feel like.")
                                else:
                                    print("Incorrect, please play again.")
                            elif num4 == 2:
                                print("For $1,000,000,")
                                print("What is the capital city of Sweden?")
                                guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                                if guess4==int(3):
                                    print("Congratulations, you have won the game and $1,000,000.")
                                    print("Please play again whenever you feel like.")
                                else:
                                    print("Incorrect, please play again.")
                        else:
                            print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
        elif num2==3:
            print("What is the movie that has grossed the most money in the")
            print("box office worldwide adjusted for infation?")
            guess2=int(input("1, Star Wars, 2, Avatar, 3, Titanic, 4, Gone With The Wind"))
            if guess2==int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
            
    else:
        print("Incorrect, please play again.")

elif num == 3:
    print("For the thousand dolllar question,")
    print("What was the name of the famous billionaire who was one  of the")
    print("first to invest in Pixar")
    guess1=int(input("1, if Steve Jobs, 2, Bill Gates, 3, Mark Zuckerberg, 4, if Warren Buffet"))
    if guess1 == 1:
        print("Correct, now let's move on to the $100,000 question")
        num2 = random.randint(1,3)
        if num2==1:
            print("Which part of the body is absolutle useless")
            guess2=int(input("1, the kidney, 2, the spleen, 3, cytoplasm, 4, the appendix"))
            if guess2==4:
                print("Correct, now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
        elif num2==2:
            print("What is the Pokemon mascot")
            guess2=int(input("1, Clefairy, 2, Frodo, 3, Wartortle, 4, Pikachu"))
            if guess2==int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
        elif num2==3:
            print("What is the movie that has grossed the most money in the")
            print("box office worldwide adjusted for infation?")
            guess2=int(input("1, Star Wars, 2, Avatar, 3, Titanic, 4, Gone With The Wind"))
            if guess2==int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
    else:
        print("Incorrect, please play again.")

elif num == 4:
    print("For the thousand dolllar question,")
    print("Is E=MC squared used to find?")
    guess1=int(input("1, speed, 2, energy, 3, mass, 4, height"))
    if guess1 == int(2):
        print("Correct, now let's move on to the $100,000 question")
        num2 = random.randint(1,3)
        if num2==1:
            print("Which part of the body is absolutle useless?")
            guess2=int(input("a, the kidney, b, the spleen, c, cytoplasm, d, the appendix"))
            if guess2==4:
                print("Correct, now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
        elif num2==2:
            print("What is the Pokemon mascot?")
            guess2=int(input("1, Clefairy, 2, Frodo, 3, Wartortle, 4, Pikachu"))
            if guess2 == int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")           
        elif num2==3:
            print("What is the movie that has grossed the most money in the")
            print("box office worldwide adjusted for infation?")
            guess2=int(input("1, Star Wars, 2, Avatar, 3, Titanic, 4, Gone With The Wind"))
            if guess2==int(4):
                print("Correct now let's move on to the $500,000 question.")
                num3 = random.randint(1,2)
                if num3 == 1:
                    print("Who was the superhero to have the first live-action suerhero movie ever made after them?")
                    guess3=int(input("1, Spider-man, 2, Batman, 3, Superman, 4, Darkman"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                elif num3 == 2:
                    print("Who was the only US President to get impeached before Bill Clinton?")
                    guess3=int(input("1, George Bush, 2, Thoedore Roosevelt, 3, Andrew Johnson, 4, Jimmy Carter"))
                    if guess3==int(3):
                        print("Correct, now let's move on to the final, $1,000,000 question.")
                        num4 = random.randint(1,2)
                        if num4 == 1:
                            print("For $1,000,000 dollars,")
                            print("who was the 18th president of the USA?")
                            guess4=int(input("1, Ulysses Grant, 2, Abraham Lincoln, 3, Theodore Roosevelt, 4, Andrew Johnson"))
                            if guess4== int(1):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                        elif num4 == 2:
                            print("For $1,000,000,")
                            print("What is the capital city of Sweden?")
                            guess4=int(input("1,England , 2, Gothenburg, 3, Stockholm, 4, Copenhagen"))
                            if guess4==int(3):
                                print("Congratulations, you have won the game and $1,000,000.")
                                print("Please play again whenever you feel like.")
                            else:
                                print("Incorrect, please play again.")
                    else:
                        print("Incorrect, please play again.")
            else :
                print("Incorrect, please play again.")
    else:
        print("Incorrect, please play again.")    
    




#Thank you for making it to the end of my culminating assignment,
#and have a great day.





