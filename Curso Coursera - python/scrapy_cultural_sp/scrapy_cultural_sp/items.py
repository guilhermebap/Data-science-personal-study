# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from  scrapy.item import Item, Field


class Atracao(Item):
    cidade =  Field()
    endereço =  Field()
    dia =  Field()
    hora =  Field()
    artista =  Field()
