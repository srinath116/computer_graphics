import pygame 
import sys

pygame.init()

size = width, height = 1300, 720
screen = pygame.display.set_mode(size)
black = [0,0,0]
white = [255, 255, 255]

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
my=[193,189,182]
mid=[105,60,36]

screen.fill(white)

def draw_gate():

	while 1:	
		top=pygame.draw.polygon(screen,my,[(152, 190), (152, 230), (1056, 230),(1056, 190)],0)
		# screen.blit(font.render('Hello!', True, (255,0,0)), (200, 100))

		pygame.draw.polygon(screen,mid,[(573, 235), (617, 235), (617, 462), (573, 462)],0)

		pygame.draw.polygon(screen,white,[(573, 300), (573, 320),(617, 320), (617, 300)],0)

		pygame.draw.polygon(screen,black,[(207, 325), (207, 463), (326, 463), (326, 325)],True)
		pygame.draw.polygon(screen,mid,[(206, 325), (206, 463), (242, 463), (242, 325)],0)
		pygame.draw.polygon(screen,black,[(253, 390), (253, 430), (320, 430), (320, 390)],True)

		pygame.draw.polygon(screen,black,[(327, 325), (389, 344), (389, 450), (327, 460)],True)
		
		pygame.draw.polygon(screen,black,[(870, 325), (996, 325), (996, 472), (870, 472)],True)
		pygame.draw.polygon(screen,mid,[(958, 325), (958, 472), (1000, 472), (1000, 325	)],0)
		pygame.draw.polygon(screen,black,[(873, 390), (873, 430), (930, 430), (930, 390)],True)
		
		pygame.draw.polygon(screen,black,[(871, 323), (871, 463), (810, 453), (810, 344)],True)
	
		pygame.draw.polygon(screen,black,[(279, 233), (326, 233), (326, 325), (279, 325)],True)
		pygame.draw.polygon(screen,black,[(326, 325), (334, 327), (334, 237), (326, 233)],True)

		pygame.draw.polygon(screen,black,[(870, 233), (923, 233), (923, 325), (870, 325)],True)
		pygame.draw.polygon(screen,black,[(870, 325), (863, 327), (863, 237), (870, 233)],True)

		pygame.draw.polygon(screen,black,[(152, 230), (251, 272)],True)
		pygame.draw.polygon(screen,black,[(251, 272), (276, 272)],True)
		pygame.draw.polygon(screen,black,[(335, 272), (573, 272)],True)
		pygame.draw.polygon(screen,black,[(619, 272), (865, 272)],True)
		pygame.draw.polygon(screen,black,[(926, 272), (940, 272)],True)
		pygame.draw.polygon(screen,black,[(940, 272), (1056, 230)],True)

		pygame.draw.polygon(screen,black,[(384, 272), (384, 342), (345, 330), (345, 272)],True)
		pygame.draw.polygon(screen,black,[(812, 272), (812, 342), (856, 328), (856, 272)],True)

		pygame.draw.polygon(screen,black,[(328, 390), (328, 458), (430, 458), (430, 390)],True)
		
		pygame.draw.polygon(screen,black,[(351, 390), (351, 458)],True)
		pygame.draw.polygon(screen,black,[(354, 390), (354, 458)],True)

		pygame.draw.polygon(screen,black,[(371, 390), (371, 458)],True)
		pygame.draw.polygon(screen,black,[(374, 390), (374, 458)],True)

		pygame.draw.polygon(screen,black,[(391, 390), (391, 458)],True)
		pygame.draw.polygon(screen,black,[(394, 390), (394, 458)],True)

		pygame.draw.polygon(screen,black,[(411, 390), (411, 458)],True)
		pygame.draw.polygon(screen,black,[(414, 390), (414, 458)],True)


		pygame.draw.polygon(screen,black,[(490, 379), (490, 440), (563, 460), (563, 391)],True)

		pygame.draw.polygon(screen,black,[(500, 382), (500, 440)],True)
		pygame.draw.polygon(screen,black,[(503, 382), (503, 440)],True)

		pygame.draw.polygon(screen,black,[(520, 386), (520, 448)],True)
		pygame.draw.polygon(screen,black,[(523, 386), (523, 448)],True)

		pygame.draw.polygon(screen,black,[(535, 388), (535, 452)],True)
		pygame.draw.polygon(screen,black,[(538, 388), (538, 452)],True)

		pygame.draw.polygon(screen,black,[(550, 390), (550, 458)],True)
		pygame.draw.polygon(screen,black,[(553, 390), (553, 458)],True)


		pygame.draw.polygon(screen,black,[(626, 389), (626, 464)],True)

		pygame.draw.polygon(screen,black,[(627, 458), (744, 458), (744, 390), (627, 390)],True)

		pygame.draw.polygon(screen,black,[(647, 390), (647, 458)],True)
		pygame.draw.polygon(screen,black,[(650, 390), (650, 458)],True)

		pygame.draw.polygon(screen,black,[(667, 390), (667, 458)],True)
		pygame.draw.polygon(screen,black,[(670, 390), (670, 458)],True)

		pygame.draw.polygon(screen,black,[(692, 390), (692, 458)],True)
		pygame.draw.polygon(screen,black,[(695, 390), (695, 458)],True)

		pygame.draw.polygon(screen,black,[(718, 390), (718, 458)],True)
		pygame.draw.polygon(screen,black,[(721, 390), (721, 458)],True)

		
		pygame.draw.polygon(screen,black,[(760, 371), (760, 435), (861, 460), (861, 391)],True)

		pygame.draw.polygon(screen,black,[(766, 372), (766, 438)],True)
		pygame.draw.polygon(screen,black,[(769, 372), (769, 438)],True)

		pygame.draw.polygon(screen,black,[(787, 375), (787, 440)],True)
		pygame.draw.polygon(screen,black,[(790, 375), (790, 440)],True)

		pygame.draw.polygon(screen,black,[(805, 378), (805, 444)],True)
		pygame.draw.polygon(screen,black,[(808, 378), (808, 444)],True)

		pygame.draw.polygon(screen,black,[(830, 382), (830, 450)],True)
		pygame.draw.polygon(screen,black,[(833, 382), (833, 450)],True)

		#pygame.draw.polygon(screen,red,[(861, 392), (863, 463), (871, 464), (871, 392)],True)

		pygame.draw.polygon(screen,black,[(326, 461), (0, 595)],True)
		pygame.draw.polygon(screen,black,[(864, 472), (1246, 574)],True)

		pygame.draw.polygon(screen,black,[(205, 465), (3, 529)],True)
		pygame.draw.polygon(screen,black,[(999, 471), (1204, 511)],True)


		pygame.draw.polygon(screen,black,[(560, 472), (510, 694)],True)
		pygame.draw.polygon(screen,black,[(630, 472), (700, 694)],True)

		pygame.draw.polygon(screen,black,[(520, 195), (520, 220)],True)
		pygame.draw.polygon(screen,black,[(525, 195), (525, 220)],True)

		pygame.draw.polygon(screen,black,[(550, 195), (550, 220)],True)
		pygame.draw.polygon(screen,black,[(555, 195), (555, 220)],True)

		pygame.draw.polygon(screen,black,[(570, 195), (570, 220)],True)
		pygame.draw.polygon(screen,black,[(575, 195), (575, 220)],True)

		pygame.draw.polygon(screen,black,[(600, 200), (600, 220)],True)
		pygame.draw.polygon(screen,black,[(605, 200), (605, 220)],True)
		pygame.draw.polygon(screen,black,[(585, 195), (585,200),(625, 200),(625,195)],True)

		pygame.display.flip()
		
	


draw_gate()

