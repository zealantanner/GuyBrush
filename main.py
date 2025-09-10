import pygame as pg
import functions as f

pg.init()

WIDTH, HEIGHT = 600, 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

img = pg.image.load("assets/YellowFlower.png").convert_alpha()

font = pg.font.Font("assets/HoboStd.otf")

running = True
mouseposlist = []
mousepos = pg.mouse.get_pos()
prevmousepos = mousepos
drawsize = 10

time = 0

while running:
    time += 1
    prevmousepos = mousepos
    mousepos = pg.mouse.get_pos()
    mouseposlist.append(mousepos)
    if pg.mouse.get_pressed()[0]:
        print("left click")
        pg.draw.line(screen,(0,255,0),prevmousepos,mousepos,drawsize*2)
        pg.draw.circle(screen,(255,0,0),mousepos,drawsize)
        pg.draw.circle(screen,(0,0,255),mousepos,drawsize,2)
    if pg.mouse.get_pressed()[2]:
        print("right click")
        pg.draw.line(screen,(mousepos[0]%255,mousepos[1]%255,0),prevmousepos,mousepos,drawsize*2)
        pg.draw.circle(screen,(mousepos[0]%255,mousepos[1]%255,time%255),mousepos,drawsize)
    if pg.mouse.get_pressed()[1]:
        print("middle click")
        pg.draw.line(screen,(0,0,0),prevmousepos,mousepos,drawsize*2)
        pg.draw.circle(screen,(0,0,0),mousepos,drawsize)
    screen.blit(font.render(f"Left/Right click to draw!\nScroll to change size\nTime: {f.Time(time)['min']}:{f.Time(time)['sec']}:{int(f.Time(time)['mill']/10)}",False,(255,255,255),(0,0,0)))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        elif event.type == pg.MOUSEWHEEL:
            print("size change")
            drawsize += event.y
            if drawsize < 1:
                drawsize = 1

    pg.display.flip()


print("end")
pg.quit()