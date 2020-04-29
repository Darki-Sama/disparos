import pygame
import random

ANCHO=1200
ALTO=800
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y= (ALTO-self.rect.height) - 10
        self.velx=0
        self.vely=0
        self.bloques=None

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.bloques,False)
        for b in ls_col:
            ls_col=pygame.sprite.spritecollide(self,self.bloques,False)
            for b in ls_col:
                    if j.velx > 0:
                        if self.rect.right > b.rect.left:
                            self.rect.right = b.rect.left
                            self.velx=0
                    else:
                        if self.rect.left < b.rect.right:
                            self.rect.left = b.rect.right
                            self.velx=0

            ls_col=pygame.sprite.spritecollide(self,self.bloques,False)
            for b in ls_col:
                    if j.vely > 0:
                        if self.rect.bottom > b.rect.top:
                            self.rect.bottom = b.rect.top
                            self.vely=0
                    else:
                        if self.rect.top < b.rect.bottom:
                            self.rect.top = b.rect.bottom
                            self.vely=0
        self.rect.y+=self.vely

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, d_an, d_al, cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    fondo=pygame.image.load('skyfalls.png')
    info= fondo.get_rect()
    limv_an=950
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j=Jugador([300,200])
    jugadores.add(j)

    '''b=Bloque([300,200],200,120)
    bloques.add(b)

    b1=Bloque([500,400],100,250,AMARILLO)
    bloques.add(b1)
    '''

    j.bloques=bloques
    f_posx=0
    f_velx=0

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx= -5
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.vely= -5
                    j.velx=0
                if event.key == pygame.K_DOWN:
                    j.vely= 5
                    j.velx=0

            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0
                f_velx = -5
        #Control

        if j.rect.x > limv_an:
            j.rect.x = limv_an
            j.velx = 0
            f_velx = -5

        #Colision

        #Limpieza de memoria

        #Refresco
        jugadores.update()
        bloques.update()
        #ventana.fill(NEGRO)
        ventana.blit(fondo,[f_posx,0])
        jugadores.draw(ventana)
        bloques.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
        f_posx+=f_velx
