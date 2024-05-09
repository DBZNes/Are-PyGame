import pygame, sys
from settings import *
from level import Level
from button import Button

class Game:
	def get_font(size):
		return pygame.font.Font("../graphics/font/font.ttf", size)

	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Are PyGame')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_TAB:
						self.level.toggle_menu()
			self.screen.fill(WATER_COLOR)
			self.level.run()

			pygame.display.update()
			self.clock.tick(FPS)
	
	def main_menu(self):
		BG = pygame.image.load("../graphics/menu/bg.png")
		while True:
			self.screen.blit(BG, (0,0))

			menu_mouse_pos = pygame.mouse.get_pos()

			menu_text = Game.get_font(100).render("MAIN MENU", True, "black")
			menu_rect = menu_text.get_rect(center=(640, 100))

			play_button = Button(image=pygame.image.load("../graphics/menu/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=Game.get_font(75), base_color="#d7fcd4", hovering_color="White")
			quit_button = Button(image=pygame.image.load("../graphics/menu/Quit Rect.png"), pos=(640, 450), 
                            text_input="QUIT", font= Game.get_font(20), base_color="#d7fcd4", hovering_color="White")
			
			self.screen.blit(menu_text, menu_rect)
			for button in [play_button, quit_button]:
				button.changeColor(menu_mouse_pos)
				button.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if play_button.checkForInput(menu_mouse_pos):
						Game.run(self)
					if quit_button.checkForInput(menu_mouse_pos):
						pygame.quit()
						sys.exit()
			pygame.display.update()
			self.clock.tick(FPS)
            

if __name__ == '__main__':
	game = Game()
	game.main_menu()