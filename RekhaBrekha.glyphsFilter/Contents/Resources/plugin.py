# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class RekhaBrekha(FilterWithoutDialog):
	supportedScripts = ("gurmukhi","devanagari","bengali")

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'RekhaBrekha',
			'de': 'RäckhaBräckha',
			'fr': 'RékhaBrékha',
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		decomposeIndexes = []
		for i, component in enumerate(layer.components):
			glyph = component.component
			shouldDecompose = all((
				glyph.export,
				glyph.script in self.supportedScripts,
				glyph.category == "Letter",
				))
			if shouldDecompose:
				decomposeIndexes.append(i)

		for i in reversed(sorted(decomposeIndexes)):
			layer.components[i].decompose()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
