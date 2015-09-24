#encoding: utf-8
import os
import pygame
import json
from pygame.locals import *
os_char='gb18030'
# pygame.init()

# text = u"我爱你"
# font = pygame.font.SysFont('SimHei', 14)
# ftext = font.render(text, True, (0, 0, 0), (255, 255, 255))
# pygame.image.save(ftext, "C:/mypython/t.jpg")


jsonStr = '[{"0":"1","id":"1","1":"\u53cb\u90bb\u7535\u5b50\u5546\u52a1","name":"\u53cb\u90bb\u7535\u5b50\u5546\u52a1","2":"\u5f20\u4e09","link_man":"\u5f20\u4e09","3":"130123456782","mobile":"130123456782"},{"0":"2205","id":"2205","1":"\u8d1e\u94ed\u7eba\u7ec7\u6709\u9650\u516c\u53f8","name":"\u8d1e\u94ed\u7eba\u7ec7\u6709\u9650\u516c\u53f8","2":"\u90d1\u654f","link_man":"\u90d1\u654f","3":"18862252131","mobile":"18862252131"},{"0":"2","id":"2","1":"\u5317\u4eac\u53cb\u90bb\u7535\u5b50\u5546\u52a1\u79d1\u6280\u6709\u9650\u516c\u53f8","name":"\u5317\u4eac\u53cb\u90bb\u7535\u5b50\u5546\u52a1\u79d1\u6280\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"3","id":"3","1":"\u4e1c\u839e\u5e02\u521b\u5fc6\u5851\u80f6\u539f\u6599\u6709\u9650\u516c\u53f8","name":"\u4e1c\u839e\u5e02\u521b\u5fc6\u5851\u80f6\u539f\u6599\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"4","id":"4","1":"\u5b81\u6ce2\u5e02\u6c5f\u4e1c\u5174\u4e30\u94dc\u5236\u6709\u9650\u516c\u53f8","name":"\u5b81\u6ce2\u5e02\u6c5f\u4e1c\u5174\u4e30\u94dc\u5236\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"5","id":"5","1":"\u6df1\u5733\u5e02\u4fe1\u8bfa\u8fbe\u7535\u5b50\u79d1\u6280\u6709\u9650\u516c\u53f8","name":"\u6df1\u5733\u5e02\u4fe1\u8bfa\u8fbe\u7535\u5b50\u79d1\u6280\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"6","id":"6","1":"\u676d\u5dde\u7ea6\u62ff\u6469\u64e6\u6750\u6599\u6709\u9650\u516c\u53f8","name":"\u676d\u5dde\u7ea6\u62ff\u6469\u64e6\u6750\u6599\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"7","id":"7","1":"\u6df1\u5733\u534e\u8054\u53d1\u8d38\u6613\u6709\u9650\u516c\u53f8","name":"\u6df1\u5733\u534e\u8054\u53d1\u8d38\u6613\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"8","id":"8","1":"\u5317\u4eac\u5723\u8f69\u5efa\u7b51\u88c5\u9970\u6709\u9650\u516c\u53f8","name":"\u5317\u4eac\u5723\u8f69\u5efa\u7b51\u88c5\u9970\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""},{"0":"9","id":"9","1":"\u4e0a\u6d77\u897f\u535a\u601d\u6d41\u4f53\u63a7\u5236\u6709\u9650\u516c\u53f8","name":"\u4e0a\u6d77\u897f\u535a\u601d\u6d41\u4f53\u63a7\u5236\u6709\u9650\u516c\u53f8","2":"","link_man":"","3":"","mobile":""}]'

deJson = json.dumps(jsonStr)
# deJson = repr(jsonStr)

decodeStr = json.loads(deJson)
# print map(decode)

print decodeStr
# print decode



