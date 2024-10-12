###
 # @Author: fuyunyou
 # @Date: 2024-10-12 10:58:40
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-12 11:25:07
 # @Description: 
 # @FilePath: \alien_invasion\AlienAttack\alien_invasion.py
###
import sys
import pygame
from settings import Settings

class AliensInvasion:
    """管理游戏行为和资源的类"""

    def __init__(self):
       """初始化游戏并创建游戏资源""" 
       pygame.init()
       self.settings=Settings()

       #创建并显示游戏窗口
       self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
       pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监视鼠标和键盘事件
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            
            #每次循环结束后都重绘屏幕,控制屏幕颜色
            self.screen.fill(self.settings.bg_color)
            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__=='__main__':
    ai=AliensInvasion()
    ai.run_game()