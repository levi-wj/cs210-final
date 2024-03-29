'''
Description:
    The spritesheet class reads an image file, slices it, and handles animations

OOP Principles Used:
     Abstraction, encapsulation 

Reasoning:
    This class uses abstraction because it abstracts away the complicated loading and slicing of spritesheets
    This class uses encapsulation because all the data of the sheet is encapsulated in the class
'''

import pygame
from xml.dom import minidom as XML

pygame.init()

class Spritesheet(object):
	def __init__(self, xml_filename: str, fps: int=32, scale: int=1):
		self.frames = {}
		self.spritecount = 0
		self.frame_index = 0
		self.xml_sprites = XML.parse(xml_filename).getElementsByTagName('sprite')
		self.fps = fps
		self.count = 0
		self.playing = False
		self.frame = '<???>'
		self.stopped = False

		for sprite in self.xml_sprites:
			if not self.frames.get(sprite.attributes['name'].value):
				self.frames[sprite.attributes['name'].value] = []
				self.spritecount += 1
				
				for frame in sprite.getElementsByTagName('frame'):
					frame_data = []
					frame_data.append(int(frame.attributes['x'].value))
					frame_data.append(int(frame.attributes['y'].value))
					frame_data.append(int(frame.attributes['w'].value))
					frame_data.append(int(frame.attributes['h'].value))
					frame_data.append(frame.attributes['image'].value)

					self.frames[sprite.attributes['name'].value].append(pygame.transform.scale(self.load_image(frame_data[0], frame_data[1], frame_data[2], frame_data[3], frame_data[4]), (scale, scale)))

	def load_image(self, x, y, w, h, filename):
		image = pygame.image.load(filename).convert_alpha()
		region = [x, y, w, h]

		new_image = pygame.Surface((region[2], region[3]), pygame.SRCALPHA, 32).convert_alpha()
		new_image.blit(image, (0, 0), region)

		return new_image

	def play(self, sprite_name: str, repeat=True):
		for spr_name in self.frames.keys():
			if spr_name == sprite_name:
				if self.frame == sprite_name:
					if self.frame_index < len(self.frames[spr_name]) - 1:
						if self.count < self.fps:
							self.count += 6.0
						else:
							self.count = 0
							self.frame_index += 1
					else:
						if self.count < self.fps:
							self.count += 6.0
						else:
							self.count = 0
							if repeat:
								self.frame_index = 0
				else:
					self.frame = spr_name
					self.frame_index = 0
					self.count = 0

	def image(self):
		if self.frames.get(self.frame) and self.frame_index < len(self.frames[self.frame]):
			return self.frames[self.frame][self.frame_index]

	def get_sprite(self, index):
		return self.frames[list(self.frames)[int(index)]][0]