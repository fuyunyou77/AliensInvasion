###
 # @Author: fuyunyou
 # @Date: 2024-10-13 22:56:30
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-13 23:18:41
 # @Description: 外星人类:包含外星人的一些基本行为和信息
 # @FilePath: \ai_game_project\AlienAttack\alien.py
###
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen=ai_game.screen

        #加载外星人图像并设置其rect属性
        self.image=pygame.image.load('../images/alien.bmp')
        self.rect=self.image.get_rect()
        
        #每个外星人最初都在左上角生成
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #存储外星人的精确水平位置
        self.x=float(self.rect.x)
        