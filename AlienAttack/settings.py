###
 # @Author: fuyunyou
 # @Date: 2024-10-12 11:17:45
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-16 17:36:00
 # @Description: 
 # @FilePath: \PythonCode\alien_invasion\AlienAttack\settings.py
###
class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed=1.5

        #子弹设置
        self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=5

        #外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction=1