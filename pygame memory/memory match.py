## importing pygame package and initializing pyagme
## importing random and time 
import pygame,random
import time as ti
pygame.init()

## this function is used to display(blit) images according to the level
## level(1)-->white image(not the real imgae back side) only
## level(2)-->3 different images and white image 
def visibleimg(lvl,imgs):
    lvl2image=0
    bgload=[]
    gameimage4=pygame.image.load("step0003.png")
    bgload.append(gameimage4)

    if lvl==1:
        for i in range(4):
            for j in range(3):
                screen.blit(bgload[0],(i*120+45,j*120+60))
                pygame.display.update()
    else:
        for i in range(4):
            for j in range(3):
                screen.blit(imgs[lvl2image],(i*120+45,j*120+60))
                lvl2image+=1
                pygame.display.update()
        pygame.time.delay(8000)
        for i in range(4):
            for j in range(3):
                screen.blit(bgload[0],(i*120+45,j*120+60))
                pygame.display.update()

## this function keep track of time and display it
def time():
    time1=60-(ti.time()-s_time)
    pygame.draw.rect(screen,sea_blue,(672,90,45,26))
    timedis=font.render("Time:" + str(round(time1)), True,black)
    screen.blit(timedis,(610, 90))
    return time1
## this function display the socre            
def score(points):
    pygame.draw.rect(screen,sea_blue,(682,55,75,28))
    scoredis=font.render("Score:" + str(points), True,black)
    screen.blit(scoredis,(610, 60))
## load 3 different images to a list and multiply it by 4 and shuffle it  
def mainimgs():
    imgload=[]
    gameimage1=pygame.image.load("facewithout.PNG")
    gameimage2=pygame.image.load("rollingthefloor.png")
    gameimage3=pygame.image.load("yawning.png")
    
    imgload.append(gameimage1)
    imgload.append(gameimage2)
    imgload.append(gameimage3)
    imgload*=4
    random.shuffle(imgload)
    return(imgload)

## this function is used to find whether selected images match
def match_ch(images,flip):
    if images[flip[0]]==images[flip[1]]:
        return True
## finds whether first selected image have a match previously diplayed image(match known) 
def match_ch2(images1,flip1,count1):
    if images1[fliped[0]]==images1[flip1[count1]]:
        return True
    else:
        return False

## get the current mouse position and convert to a grid number(eg-(2,1),(1,1))
def imglocation():
    mouselocation=pygame.mouse.get_pos()
    imagex=int((mouselocation[0]-45)/120)
    imagey=int((mouselocation[1]-60)/120)
    image=imagex,imagey
    return(image)

## this is the main game loop funtion
def main(memrun,c,points):
    while memrun==True:
            score(points)
            current_time=time()
            # if time goes to 0 game will close
            if round(current_time)==0:
                memrun=False
                return memrun
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    memrun=False
                    return memrun
                if event.type==pygame.MOUSEBUTTONDOWN:
                    imagelocation=imglocation()
                    # grid loction is converted to list index number to be called from the loaded image list
                    imagelistindex =(imagelocation[0]*3)+imagelocation[1]
                    if imagelistindex not in fliped and imagelistindex not in found:
                        # this list contain current two images that have been displayed
                        fliped.append(imagelistindex)
                        pygame.draw.rect(screen,sea_blue,(25,20,180,34))
                        pygame.display.update()
                        #k_imgs is the known image list
                        k_imgs.append(imagelistindex)
                        # if there are two images in k_imgs below loop is triggered to find if there is match known and if so diplay the message 
                        if len(k_imgs)>=2:
                            for a in range(len(k_imgs)-1):
                                if fliped[0]==k_imgs[a]:
                                    continue
                                else:
                                    c=match_ch2(imgs,k_imgs,a)
                                    if c==True:
                                           screen.blit(top_text,(25,20))
                                           pygame.display.update()                        
                        # if fliped have 2 or less imgaes display revlevent image
                        if len(fliped)<=2:
                            if len(fliped)==1:
                                f_flip=imagelocation
                            screen.blit(imgs[imagelistindex],(120*imagelocation[0]+45,120*imagelocation[1]+60))
                            pygame.display.update()
                            pygame.time.delay(500)
                        # after the two images have been displayed checks whether they are the same
                        if len(fliped)==2:
                            match=match_ch(imgs,fliped)
                            s_flip=imagelocation
                            if match==True:
                                # adding points if it is correct
                                points+=20
                                # remove the list index of found imgaes and currently displayed images from k_imgs list
                                for item in k_imgs[:]:
                                    for x in found:
                                        if item==x:
                                            k_imgs.remove(item)
                                    if item==fliped[0] or item==fliped[1]:
                                        k_imgs.remove(item)
                                # background color is dislpaed again to get disappearing affect       
                                screen.blit(gameimage5,(120*f_flip[0]+45,120*f_flip[1]+60))
                                screen.blit(gameimage5,(120*s_flip[0]+45,120*s_flip[1]+60))
                                found.append(fliped[0])
                                found.append(fliped[1])
                                c=None
                                del fliped[0:]
                                pygame.display.update()
                            else:
                                # if the images dont match checks if the first clicked image have known match using match_ch2 function
                                for a in range(len(k_imgs)-1):
                                    if fliped[0]==k_imgs[a]:
                                        continue
                                    else:
                                        c=match_ch2(imgs,k_imgs,a)
                                        if c==True:
                                            break
                                # if first clicked image had a known match points are reduced
                                if c==True:
                                    penalty_count=k_imgs.count(fliped[0])
                                    points-=penalty_count*5
                                gameimage4=pygame.image.load("step0003.png")
                                # display the white image
                                screen.blit(gameimage4,(120*f_flip[0]+45,120*f_flip[1]+60))
                                screen.blit(gameimage4,(120*s_flip[0]+45,120*s_flip[1]+60))
                                pygame.display.update()
                                del fliped[0:]   
                # if all the images have been found below lines triggerd to dispaly level end screen
                if len(found)==12:
                    load_screen=True
                    points+=round(current_time)
                    # rendering all the necessary text
                    levelend_sc1=font.render("level complete!", True,black)
                    levelend_sc2=font.render("You scored  " + str(points), True,black)
                    levelend_sc3=font.render("bonus  "+ str(round(current_time)), True,black)
                    while load_screen==True:
                        mouselocation=pygame.mouse.get_pos()
                        click=pygame.mouse.get_pressed()
                        for event in pygame.event.get():
                            screen.fill(white)
                            screen.blit(levelend_sc1,(300,150))
                            screen.blit(levelend_sc2,(190,250))
                            screen.blit(levelend_sc3,(435,250))
                            pygame.draw.rect(screen,c_green,(100,400,175,50))
                            pygame.draw.rect(screen,red,(600,400,100,50))
                            screen.blit(play_again_text,(125,415))
                            screen.blit(exit_text,(627,415))
                            # if mouse is on top of button light color and bright color is displayed to get a button affect
                            if 275 > mouselocation[0]>100 and 450> mouselocation[1]> 400:
                                pygame.draw.rect(screen,bright_c_green,(100,400,175,50))
                                screen.blit(play_again_text,(125,415))
                                pygame.display.update()
                                if click[0]==1:
                                    load_screen=False
                                    memrun=False
                                    return points
                            if 700 > mouselocation[0]>600 and 450> mouselocation[1]> 400:
                                pygame.draw.rect(screen,bright_red,(600,400,100,50))
                                screen.blit(exit_text,(627,415))
                                pygame.display.update()
                                if click[0]==1:
                                    pygame.quit()
                        pygame.display.update()
                        del k_imgs[0:]
############################################################################################################################################################################################################################################

## declaration of some of the variables
width=760
height=640
black=(0,0,0)
gameimage4=None
points=0
load_screen=True
## declaration of all the colours used in the game
sea_blue=(5,102,141)
m_seaweed=(2,128,144)
c_green=(2,195,154)
bright_c_green=(2,230,154)
red=(200,0,0)
bright_red=(250,0,0)
white=(255,255,255)
## assigning the fonts and rendering all the text used in the game 
font=pygame.font.SysFont('freesans.ttf',35)
font1=pygame.font.SysFont('freesansbold.ttf',65)
load_screen_text=font1.render("MEMORY PAIRS",True,black)
top_text=font.render("Match Known",True,black)
play_text=font.render("Play",True,black)
exit_text=font.render("Exit",True,black)
play_again_text=font.render("Play Again",True,black)
                
##start of the game
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Memory Pairs")
##main menu/load screen 
while load_screen==True:
    mouselocation=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    for event in pygame.event.get():
        screen.fill(white)
        pygame.draw.rect(screen,c_green,(100,400,100,50))
        pygame.draw.rect(screen,red,(600,400,100,50))
        screen.blit(load_screen_text,(225,145))
        screen.blit(play_text,(125,415))
        screen.blit(exit_text,(627,415))
        if 200 > mouselocation[0]>100 and 450> mouselocation[1]> 400:
            pygame.draw.rect(screen,bright_c_green,(100,400,100,50))
            screen.blit(play_text,(125,415))
            pygame.display.update()
            if click[0]==1:
                load_screen=False
        if 700 > mouselocation[0]>600 and 450> mouselocation[1]> 400:
            pygame.draw.rect(screen,bright_red,(600,400,100,50))
            screen.blit(exit_text,(627,415))
            pygame.display.update()
            if click[0]==1:
                pygame.quit()
        pygame.display.update()


############ start of level 1
memrun=True
screen.fill(sea_blue)
found=[]
fliped=[]
imgs=[]
k_imgs=[]
imgs=mainimgs()
visibleimg(1,None)
gameimage5=pygame.image.load("sea blue bg.png")
count=0
c=False
s_time=ti.time()
stat=main(memrun,c,points,)
if stat==False:
    pygame.quit()
#### end of level 1
    
############ start of level 2
memrun=True
screen.fill(sea_blue)
found=[]
fliped=[]
imgs=[]
k_imgs=[0,1,2,3,4,5,6,7,8,9,10,11]
imgs=mainimgs()
visibleimg(2,imgs)
count=0
c=False
points=stat
s_time=ti.time()
stat=main(memrun,c,points)
if stat==False:
    pygame.quit()
#### end of level 2

