import math
import pygame
from Button import Button


def obliczOdleglosc(A,B):
    return math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)

def poleTrojkata(A,B,C):
    return 0.5*math.fabs((B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0]))

def punktTrojkat(A,B,C,P):
    poleABC = poleTrojkata(A,B,C)
    poleAPB = poleTrojkata(A,P,B)
    poleAPC = poleTrojkata(A,P,C)
    poleBPC = poleTrojkata(B,P,C)

    if math.fabs(poleABC - (poleBPC + poleAPC + poleAPB)) < 0.00001:
        return True
    else:
        return False


def punktOdcinek(A, B, P):
    ab = obliczOdleglosc(A, B)
    ap = obliczOdleglosc(A, P)
    bp = obliczOdleglosc(B, P)

    roznica = ab - (ap + bp)
    if math.fabs(roznica) < 0.001:
        return True
    else:
        return False

def punktProsta(A,B,P):
    wyznacznik = B[0]*P[1] + A[0]*B[1] + A[1]*P[0] - (A[1]*B[0] + A[0]*P[1] + B[1]*P[0])

    return wyznacznik

def dwaOdcinki(A,B,C,D):
    w1 = punktProsta(A,B,C)
    w2 = punktProsta(A,B,D)
    w3 = punktProsta(C,D,A)
    w4 = punktProsta(C,D,B)

    if (w1*w2 < 0 and w3*w4 < 0) or punktOdcinek(A,B,C) or punktOdcinek(A,B,D) or punktOdcinek(C,D,A) or punktOdcinek(C,D,B):
        return True
    else:
        return False


def dwaOdcinki(A,B,C,D):
    w1 = punktProsta(A,B,C)
    w2 = punktProsta(A,B,D)
    w3 = punktProsta(C,D,A)
    w4 = punktProsta(C,D,B)

    if (w1*w2 < 0 and w3*w4 < 0) or punktOdcinek(A,B,C) or punktOdcinek(A,B,D) or punktOdcinek(C,D,A) or punktOdcinek(C,D,B):
        return True
    else:
        return False




pygame.init()
okno = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Algorytmy geometryczne")
timer = pygame.time.Clock()
FPS = 60
fontDUZA = pygame.font.SysFont('Comic Sans MS', 34)
fontDUZA.set_underline(True)
fontMALA = pygame.font.SysFont('Comic Sans MS', 22)
fontMALUTKA = pygame.font.SysFont('Comic Sans MS', 14)

punktOdcinekB = Button('aquamarine3','aquamarine','black',"PUNKT - ODCINEK",45)
punktProstaB = Button('aquamarine3','aquamarine','black',"PUNKT - PROSTA",45)
punktTrojkatB = Button('aquamarine3','aquamarine','black',"PUNKT - TRÓJKĄT",45)
dwaOdcinkiB = Button('aquamarine3','aquamarine','black',"DWA ODCINKI",55)
punktFiguraB = Button('aquamarine3','aquamarine','black',"PUNKT FIGURA",55)
koniecB = Button('aquamarine3','aquamarine','black',"ZAMKNIJ",85)
menuB = Button('aquamarine3','aquamarine','black',"POWRÓT",45)
TRYB = 0
run = True
WIERZCHOŁKI = []
P = []
K = []
punktyWspolne = 0
WIERZCHOŁKI.append([300,300])
rysowanie = 1
while run:
    timer.tick(FPS)
    okno.fill('azure3')
    klawisze = pygame.key.get_pressed()
    myszPozycja = pygame.mouse.get_pos()
    myszKlik = pygame.mouse.get_pressed()


    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            run = False

    if klawisze[pygame.K_ESCAPE]: run = False
    if TRYB == 0:
        okno.blit(fontDUZA.render("Wizualizacja algorytmów geometrycznych", True, 'black'),(60,20))
        okno.blit(fontMALUTKA.render("Informatyka rozszerzona                    Zespół Szkół Energetycznych w Rzeszowie                                      Paweł Łapiński", True, 'black'),(10,580))

        punktOdcinekB.render(okno,250,100,300,50)
        punktProstaB.render(okno,250,170,300,50)
        punktTrojkatB.render(okno,250,240,300,50)
        dwaOdcinkiB.render(okno,250,310,300,50)
        punktFiguraB.render(okno,250,380,300,50)
        koniecB.render(okno,250,510,300,50)

        if punktOdcinekB.clik():
            TRYB = 1
        if punktProstaB.clik():
            TRYB = 2
        if punktTrojkatB.clik():
            TRYB = 3
        if dwaOdcinkiB.clik():
            TRYB = 4
        if punktFiguraB.clik():
            czasRysowania = pygame.time.get_ticks()
            WIERZCHOŁKI = []
            P = []
            K = []
            punktyWspolne = 0
            WIERZCHOŁKI.append([300, 300])
            rysowanie = 1
            TRYB = 5
        if koniecB.clik():
            run = False

    if TRYB in (1,2,3,4,5):
        okno.fill('white')
        menuB.render(okno,585,540,200,50)
        if menuB.clik():
            TRYB = 0

    if TRYB == 1:
        A = [300,500]
        B = [600,250]
        P = [myszPozycja[0],myszPozycja[1]]
        okno.blit(fontDUZA.render("Algorytm punkt - odcinek", True, 'black'),(10,10))
        pygame.draw.line(okno,'black',A,B,3)
        pygame.draw.line(okno,'red',(myszPozycja),B,1)
        pygame.draw.line(okno,'red',A,(myszPozycja),1)
        pygame.draw.circle(okno,'black',A,3)
        pygame.draw.circle(okno,'black',B,3)
        pygame.draw.circle(okno,'red',(myszPozycja),3)
        okno.blit(fontMALA.render("A", True, 'black'),A)
        okno.blit(fontMALA.render("B", True, 'black'),B)
        okno.blit(fontMALA.render("P", True, 'red'),(myszPozycja[0]-20,myszPozycja[1]-20))
        okno.blit(fontMALA.render("Długość AB: " + str(round(obliczOdleglosc(A,B),1)), True, 'black'), (20, 70))
        if punktOdcinek(A,B,P):
            okno.blit(fontMALA.render("Punkt P znajduje się NA odcinku AB", True, 'blue'), (350, 70))
        else:
            okno.blit(fontMALA.render("Punkt P znajduje się POZA odcinkiem AB", True, 'blue'), (350, 70))
        okno.blit(fontMALA.render("Długość AP: " + str(round(obliczOdleglosc(A,P),1)), True, 'black'), (20, 100))
        okno.blit(fontMALA.render("Długość BP: " + str(round(obliczOdleglosc(B,P),1)), True, 'black'), (20, 130))
        okno.blit(fontMALA.render("Suma AP + BP: " + str(round(obliczOdleglosc(B,P)+ obliczOdleglosc(A,P),1)), True, 'red'), (20, 160))
        okno.blit(fontMALA.render("Różnica AB - (AP + BP): " + str(math.fabs(round(obliczOdleglosc(A,B) - (obliczOdleglosc(B,P)+ obliczOdleglosc(A,P)),4))), True, 'black'), (20, 190))


    if TRYB == 2:
        okno.blit(fontDUZA.render("Algorytm punkt - prosta", True, 'black'),(10,10))
        A = [200, 500]
        B = [600, 100]
        P = [myszPozycja[0], myszPozycja[1]]
        pygame.draw.line(okno, 'black', (100,600), (700,0), 3)
        pygame.draw.circle(okno, 'black', A, 3)
        pygame.draw.circle(okno, 'black', B, 3)
        pygame.draw.circle(okno, 'red', (myszPozycja), 3)
        okno.blit(fontMALA.render("A", True, 'black'), A)
        okno.blit(fontMALA.render("B", True, 'black'), B)
        okno.blit(fontMALA.render("P", True, 'red'), (myszPozycja[0] - 20, myszPozycja[1] - 20))
        okno.blit(fontMALA.render("Punkt P (" + str(P[0])+","+ str(P[1]) + ")", True, 'red'), (20, 70))
        okno.blit(fontMALA.render("Wyznacznik: " + str(punktProsta(A,B,P)), True, 'black'), (20, 100))
        okno.blit(fontMALA.render("Punkt P leży:", True, 'black'), (20, 130))
        if punktProsta(A,B,P) < 0:
            okno.blit(fontMALA.render("Po LEWEJ stronia prostej AB", True, 'blue'), (30, 160))
        elif punktProsta(A, B, P) > 0:
            okno.blit(fontMALA.render("Po PRAWEJ stronia prostej AB", True, 'blue'), (30, 160))
        if punktProsta(A, B, P) == 0:
            okno.blit(fontMALA.render("IDEALNIE na prostej AB", True, 'blue'), (30, 160))
    if TRYB == 3:
        okno.blit(fontDUZA.render("Algorytm punkt - trójkąt", True, 'black'),(10,10))
        A = [200, 500]
        B = [600, 500]
        C = [400, 250]
        P = [myszPozycja[0], myszPozycja[1]]
        pygame.draw.line(okno, 'black', A, B, 3)
        pygame.draw.line(okno, 'black', A, C, 3)
        pygame.draw.line(okno, 'black', C, B, 3)
        pygame.draw.circle(okno, 'black', A, 3)
        pygame.draw.circle(okno, 'black', B, 3)
        pygame.draw.circle(okno, 'red', (myszPozycja), 3)
        okno.blit(fontMALA.render("A", True, 'black'), (180,500))
        okno.blit(fontMALA.render("C", True, 'black'), (390,220))
        okno.blit(fontMALA.render("B", True, 'black'), B)
        okno.blit(fontMALA.render("P", True, 'red'), (myszPozycja[0] - 20, myszPozycja[1] - 20))
        pygame.draw.line(okno, 'red', A, P, 1)
        pygame.draw.line(okno, 'red', B, P, 1)
        pygame.draw.line(okno, 'red', C, P, 1)

        okno.blit(fontMALA.render("Pole Δ ABC = " + str(round(poleTrojkata(A,B,C),0)), True, 'black'), (20, 70))
        okno.blit(fontMALA.render("Suma ΔABC+ΔABP+ΔBPC = " + str(round(poleTrojkata(A,B,P)+poleTrojkata(A,P,C)+poleTrojkata(B,P,C),0)), True, 'black'), (300, 70))
        okno.blit(fontMALA.render("Pole Δ ABP = " + str(round(poleTrojkata(A,B,P),0)), True, 'red'), (20, 100))
        okno.blit(fontMALA.render("Pole Δ APC = " + str(round(poleTrojkata(A,P,C),0)), True, 'red'), (20, 130))
        okno.blit(fontMALA.render("Pole Δ BPC = " + str(round(poleTrojkata(B,P,C),0)), True, 'red'), (20, 160))

        if punktTrojkat(A,B,C,P):
            okno.blit(fontMALA.render("Punkt P leży WEWNĄTRZ Δ ABC ", True, 'blue'), (20, 190))
        else:
            okno.blit(fontMALA.render("Punkt P leży POZA Δ ABC ", True, 'blue'), (20, 190))


    if TRYB == 4:
        A = [300, 500]
        B = [500, 300]
        C = [300, 300]
        D = [myszPozycja[0], myszPozycja[1]]
        pygame.draw.line(okno, 'black', A, B, 3)
        pygame.draw.line(okno, 'black', C, D, 3)
        pygame.draw.circle(okno, 'black', A, 3)
        pygame.draw.circle(okno, 'black', B, 3)
        pygame.draw.circle(okno, 'black', C, 3)
        pygame.draw.circle(okno, 'black', (myszPozycja), 3)

        okno.blit(fontMALA.render("A", True, 'black'), A)
        okno.blit(fontMALA.render("C", True, 'black'), (C[0]-20,C[1]))
        okno.blit(fontMALA.render("B", True, 'black'), B)
        okno.blit(fontMALA.render("D", True, 'red'), (myszPozycja[0] - 20, myszPozycja[1]))
        okno.blit(fontMALA.render("Punkt A (" + str(A[0]) + "," + str(A[1]) + ")", True, 'black'), (20, 70))
        okno.blit(fontMALA.render("WYZNACZNIK AB + C = " + str(punktProsta(A,B,C))  , True, 'cyan4'), (400, 70))
        okno.blit(fontMALA.render("WYZNACZNIK AB + D = " + str(punktProsta(A,B,D))  , True, 'cyan4'), (400, 100))
        okno.blit(fontMALA.render("WYZNACZNIK CD + A = " + str(punktProsta(C,D,A))  , True, 'chartreuse4'), (400, 130))
        okno.blit(fontMALA.render("WYZNACZNIK CD + B = " + str(punktProsta(C,D,B))  , True, 'chartreuse4'), (400, 160))
        okno.blit(fontMALA.render("Punkt B (" + str(B[0]) + "," + str(B[1]) + ")", True, 'black'), (20, 100))
        okno.blit(fontMALA.render("Punkt C (" + str(C[0]) + "," + str(C[1]) + ")", True, 'black'), (20, 130))
        okno.blit(fontMALA.render("Punkt D (" + str(D[0]) + "," + str(D[1]) + ")", True, 'red'), (20, 160))
        if dwaOdcinki(A,B,C,D):
            okno.blit(fontMALA.render("Odcinki MAJĄ punkt wspólny", True, 'blue'), (20, 190))
        else:
            okno.blit(fontMALA.render("Odcinki NIE MAJĄ punktu wspólnego ", True, 'blue'), (20, 190))

        okno.blit(fontDUZA.render("Algorytm dwa odcinki", True, 'black'),(10,10))

    if TRYB == 5:
        okno.blit(fontDUZA.render("Algorytm punkt - figura", True, 'black'), (10, 10))
        if rysowanie < 3:
            okno.blit(fontMALA.render("Punkt W1:(300,300)", True, 'black'), (20, 70))
            okno.blit(fontMALA.render("MYSZ:("+str(myszPozycja[0])+","+str(myszPozycja[1])+")", True, 'black'), (20, 100))
        for i in range(len(WIERZCHOŁKI)-1):
            pygame.draw.line(okno, 'black', WIERZCHOŁKI[i], WIERZCHOŁKI[i+1], 3)
            okno.blit(fontMALA.render("W"+str(i+1), True, 'black'), WIERZCHOŁKI[i])
            pygame.draw.circle(okno, 'black', (WIERZCHOŁKI[i][0], WIERZCHOŁKI[i][1]), 4)
        if rysowanie == 1:
            okno.blit(fontMALA.render("Narysuj figurę klikając LPM lub PPM(koniec)", True, 'black'), (300, 70))

            pygame.draw.line(okno,'black',WIERZCHOŁKI[-1],myszPozycja,3)
            if myszKlik[0] and pygame.time.get_ticks() - czasRysowania > 300:
                czasRysowania = pygame.time.get_ticks()
                WIERZCHOŁKI.append(myszPozycja)
            if myszKlik[2] and pygame.time.get_ticks() - czasRysowania > 300:
                WIERZCHOŁKI.append(WIERZCHOŁKI[0])
            if len(WIERZCHOŁKI) > 1 and WIERZCHOŁKI[0][0] == WIERZCHOŁKI[-1][0] and WIERZCHOŁKI[0][1] == WIERZCHOŁKI[-1][1]:
                rysowanie = 2
        if rysowanie == 2:
            okno.blit(fontMALA.render("Umieść punkt P klikając LPM", True, 'black'), (300, 70))
            if myszKlik[0] and pygame.time.get_ticks() - czasRysowania > 300:
                czasRysowania = pygame.time.get_ticks()
                P.append(myszPozycja[0])
                P.append(myszPozycja[1])
                rysowanie = 3
        if rysowanie == 3:
            maxX = WIERZCHOŁKI[0][0]
            for punkt in WIERZCHOŁKI:
                if punkt[0] > maxX:
                    maxX = punkt[0]

            K.append(maxX + 50)
            K.append(P[1])

            for i in range(len(WIERZCHOŁKI) - 1):
                if dwaOdcinki(P, K, WIERZCHOŁKI[i], WIERZCHOŁKI[i + 1]):
                    punktyWspolne += 1

            if dwaOdcinki(P, K, WIERZCHOŁKI[0], WIERZCHOŁKI[-1]):
                punktyWspolne += 1

            rysowanie = 4
        if rysowanie == 4:
            pygame.draw.circle(okno, 'red', (P[0], P[1]), 4)
            okno.blit(fontMALA.render("P", True, 'red'), (P[0], P[1]))
            pygame.draw.circle(okno, 'red', (K[0], K[1]), 4)
            okno.blit(fontMALA.render("K", True, 'red'), (K[0], K[1]))
            okno.blit(fontMALA.render("Punkt P:(" + str(P[0]) + "," + str(P[1]) + ")", True, 'red'),(20, 70))
            okno.blit(fontMALA.render("Punkt K:(" + str(K[0]) + "," + str(K[1]) + ")", True, 'red'),(20, 100))
            okno.blit(fontMALA.render("Ilość punktów przecięcia: " + str(punktyWspolne) , True, 'black'),(20, 130))
            pygame.draw.line(okno, 'red', P, K, 3)

            if punktyWspolne % 2 == 1:
                okno.blit(fontMALA.render("Punkt P leży WEWNĄTRZ figury", True, 'blue'), (20, 160))
            else:
                okno.blit(fontMALA.render("Punkt P leży POZA figurą ", True, 'blue'), (20, 160))

    pygame.display.update()

pygame.quit()