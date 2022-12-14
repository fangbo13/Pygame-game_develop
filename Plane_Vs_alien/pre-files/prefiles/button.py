"""author  =  Haibo """


import pygame


pygame.init()




def draw_button(window,x,y,width,height,bgcolor,title,text_color=(255,255,255),font_size=30):
    pygame.draw.rect(window,bgcolor,(x,y,width,height))
    font = pygame.font.Font('E:\Pygame-game_develop\Plane_Vs_alien\wordfIle\wordfile.ttf',font_size)
    text = font.render(title,True,text_color)
    t_w, t_h = text.get_size()
    window.blit(text,(x+width/2-t_w/2,y+height/2-t_h/2))


    
class Button:
    def __init__(self,title,pos,size,bg_color,text_color = Color.random_color(),font_size=20):
        self.title = title
        self.pos = pos
        self.size = size
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = font_size
        self.old_color = bg_color



width = 400
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("haibo")
window.fill((255,255,255))

font = pygame.font.Font('E:\Pygame-game_develop\Plane_Vs_alien\wordfIle\wordfile.ttf',30)


True_Button  = Button('Yes',(100,100),(100, 50),(255,0,0,),(255,255,255))
True_Button.draw(window)



pygame.display.update()

while True:
    for event in pygame.event.get():
        if pygame.event.type == pygame.QUIT:
            exit()
