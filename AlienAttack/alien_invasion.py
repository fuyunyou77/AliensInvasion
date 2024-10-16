###
 # @Author: fuyunyou
 # @Date: 2024-10-12 10:58:40
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-16 18:06:31
 # @Description: 
 # @FilePath: \PythonCode\alien_invasion\AlienAttack\alien_invasion.py
###
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AliensInvasion:
    """管理游戏行为和资源的类"""

    def __init__(self):
       """初始化游戏并创建游戏资源""" 
       pygame.init()
       self.settings=Settings()

       #创建并显示游戏窗口
       self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
       self.settings.screen_width=self.screen.get_rect().width
       self.settings.screen_height=self.screen.get_rect().height
       pygame.display.set_caption("Alien Invasion")

       #创建一个飞船
       self.ship=Ship(self)
       self.bullets=pygame.sprite.Group()
       self.aliens=pygame.sprite.Group()

       self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()
            
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            #向左移动飞船
            self.ship.moving_left=True

        elif event.key==pygame.K_q:
            #要使用英文输入法的q才有效果
            sys.exit()   
        elif event.key==pygame.K_SPACE:
            #按下空格发射一颗子弹
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            #停止向右移动飞船
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            #停止向左移动飞船
            self.ship.moving_left=False

    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets中"""
        if len(self.bullets)<self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置,并消失的的子弹"""
        #更新子弹位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def _create_aliens(self,alien_number,row_number):
        """创建一个外星人并将其放在当前行"""
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size

        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x

        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人向下移,并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
            self.settings.fleet_direction*=-1

    def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人,并计算一行可以容纳多少人
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        #计算一行能容纳多少外星人(需要留出屏幕左右边框边距和外星人之间的间隙)
        available_space_x=self.settings.screen_width-(2*alien_width)
        number_aliens_x=available_space_x//(2*alien_width)

        #计算能容纳几列外星人(同样留出间隙和上下边距)
        ship_height=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
        number_rows=available_space_y//(2*ship_height)

        #创建外星人群
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_aliens(alien_number,row)



    def _update_alien(self):
        """
        检查是否有外星人位于屏幕边缘,
        更新外星人群中所有外星人的位置
        """
        self._check_fleet_edges()
        self.aliens.update()


    def _update_screen(self):
        """每次循环结束后都重绘屏幕,控制屏幕颜色"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()#绘制飞船，先画背景再画飞船，确保飞船显示再背景之上

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__=='__main__':
    ai=AliensInvasion()
    ai.run_game()
    