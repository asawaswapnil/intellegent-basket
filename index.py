#directions=> 0:down, 1:up, 2:right, 3:left
import random,pygame,time
from copy import deepcopy
import matplotlib.pyplot as plt
r=[[0,0,0,100,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
v=deepcopy(r)
N=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
policy=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
pygame.init()
display_w=400
display_h=400
gameDisplay=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("CatchTheApple")
clock=pygame.time.Clock()
crashed=False
cucuImg=pygame.image.load("./pygame/cucu.gif")
cucu=pygame.transform.scale(cucuImg,(display_w/6,display_h/6))
basketImg=pygame.image.load("./pygame/basket.png")

basket=pygame.transform.scale(basketImg,(display_w*7/20,display_h*3/10))
backgroundImg=pygame.image.load("./pygame/background.png")
background=pygame.transform.scale(backgroundImg,(display_w,display_h))
def message_display(text):
    font=pygame.font.Font("freesansbold.ttf",20)
    textsurf=font.render(text,True,(255,0,0))
    textrect=textsurf.get_rect()
    textrect.center=(display_w/2,display_h/10)
    gameDisplay.blit(textsurf,textrect)
#back_rect=background.get_rect()

alpha=1
e=0.0    
offset=3
c=0
i=0
fruit=0

score=0
arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
while i<500:
    
    print e
    #print i
    i+=1
    j=3  
    k=0
    #print score
    while((3<=k+offset<=6)==False):
        global k
        k=int(random.random()*7)
    #print "initially",offset,k -
    #print "fruit",offset+k-3
    while j!=0:    
            v_by_policy=0
            N[j][k]+=1
            d=int(random.random()*3)
            #print "d",d
            lr={0:0,1:1,2:-1}
            explore=random.random()
            gameDisplay.fill((255,255,255))
            gameDisplay.blit(background,(0,0))
            message_display("iteration:"+str(i)+", score:"+str(score))
            gameDisplay.blit(cucu,((offset+k-3)*display_w/4 , (3-j)*display_h/4))
            gameDisplay.blit(basket,(offset*display_w/4 , 2.5*display_h/4))
             pygame.display.update()
            clock.tick(15)
            """if (0<=i<10 or 500<=i<510 or 800<=i<820 or 1000<=i<1100):
                arr[3][offset]=255
                arr[3-j][offset+k-3]=255
                plt.title([i,score])
                plt.imshow(arr, interpolation="none")
                plt.tight_layout()

                 plt.savefig("./apple3_1/"+"%03d.png" % c)
                    
                arr[3][offset]=0
                arr[3-j][offset+k-3]=0"""
            
            #print "d", d
            c+=1
                
             if explore<e :
                step=policy[j][k]
            else:
                step=d
            v_by_policy=v[j][k]
            if  0<=offset-lr[policy[j][k]]<4:
                v_by_policy=v[j][k]+(r[j][k]+(.95*(v[j-1][k+lr[policy[j][k]]])-v[j][k]))/(N[j][k]+1)
            if 0<=offset-lr[step]<4:
                v[j][k]+=(r[j][k]+(.95*(v[j-1][k+lr[step]])-v[j][k]))/(N[j][k]+1)
                k=k+lr[step]
                offset-=lr[step]
                if v_by_policy<v[j][k-lr[step]]:
                    policy[j][k-lr[step]]=d
                    
            j-=1
            #print offset,k,fruit
    if offset==offset+k-3:
        #plt.imshow(arr, interpolation="none", cmap="gray")
        score+=1    
    else:    
        #plt.imshow(arr, interpolation="none")    
        score=0
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(background,(0,0))
    message_display("iteration:"+str(i)+", score:"+str(score))
    gameDisplay.blit(cucu,((offset+k-3)*display_w/4 , (3-j)*display_h/4))
    gameDisplay.blit(basket,(offset*display_w/4 , 2.5*display_h/4))
     pygame.display.update()
    clock.tick(30)
    
    """if( 0<=i<10 or 500<=i<510 or 800<=i<820 or 1000<=i<1100):
        arr[3][offset]=255
        arr[3-j][offset+k-3]=255
        plt.title({"Iteration":i,"Score":score})
        if offset==offset+k-3:
            plt.imshow(arr, interpolation="none", cmap="gray")
            score+=1    
        else:    
            plt.imshow(arr, interpolation="none")    
            score=0
        plt.tight_layout()
         plt.savefig("./apple3_1/"+"%03d.png" % c)
        arr[3][offset]=0
        arr[3-j][offset+k-3]=0    """
    c+=1    
    #print r[j][k],j,k
    global e    
    e=e+0.0025
    global e
    print i, score, e, explore
#ffmpeg -i %03d.png output.gif -vf fps=10
print policy     
print v                
print N    
pygame.quit()
quit()
