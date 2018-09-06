#!python3
#-*-coding:utf-8-*-

'Core module of ProjectReborn, contains it\'s core'

__author__ = 'FallenXtar'


class AreaMap(object):
    def getCordinate(self): 
        pass
    
    def getAround(self, parameter_list): 
        pass

    def getTerrian(self, parameter_list):
        pass

    def getHydration(self, parameter_list):
        pass

    def getAltitude(self, parameter_list):
        pass
    
    def getDiscribe(self, parameter_list):
        pass
    
    def getLandform(self, parameter_list):
        pass


class Act(object):
    def playerLogin(self, parameter_list):
        pass

    def playerLogout(self, parameter_list):
        pass
    

    def lookAround(self,parameter_list):
        pass

    def moveTo(self, parameter_list):
        pass

    def checkInventory(self, parameter_list):
        pass
    
    def checkAttribute(self,parameter_list):
        pass
    
    def checkStatus(self, parameter_list):
        pass
    
    def checkSkills(self, parameter_list):
        pass
    
    def checkASS(self, parameter_list):
        pass
    



class Charater(Act):
    def __init__ (self,id,nickname):
        self.id = id
        self.nickname = nickname
    


# 定义 角色 类
# 角色 的属性有 id（唯一）、nickname显示名称 等

