#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, os
class Fish:
        def __init__(self):(self.x, self.y, self.step) = random.randrange(11), random.randrange(11), (1, -1)
        def move(self):
                if random.randrange(2):self.x += random.choice(self.step)
                else:self.y += random.choice(self.step)
                if self.x < 0:self.x = -self.x
                elif self.x > 10:self.x = 20 - self.x
                if self.y < 0:self.y = -self.y
                elif self.y > 10:self.y = 20 - self.y
        def get(self):return (self.x, self.y)
class Turtle(Fish):
        def __init__(self):super().__init__();(self.step, self.energy) = (2, 1, -1, -2), 100
        def eat(self):self.energy += 20
        def move(self):super().move();self.energy -= 1
(fish, turtle, times) = [Fish() for i in range(10)], Turtle(), 0
while True:
        (empty, axis) = list(), list()
        for i in range(11):empty.append([0] * 11)
        if not len(fish):print('鱼都被吃光了!');break
        if not turtle.energy:print('乌龟的体力耗尽了!');break
        for i in fish[:]:
                i.move()
                if i.get() == turtle.get():turtle.eat();fish.remove(i);continue
                axis.append(i.get())
        turtle.move()
        times += 1
        for i in axis:empty[10 - i[1]][i[0]] = 1
        ttaxis = turtle.get()
        empty[10 - ttaxis[1]][ttaxis[0]] = 2
        os.system('cls')
        print('步数: %d\n体力: %d\n剩余鱼数: %d' % (times, turtle.energy, len(fish)))
        for i in empty:
                for j in i:
                        if j == 1:print('*', end = '')
                        elif j == 2:print('0', end = '')
                        else:print(' ', end = '')
                print()
        time.sleep(0.3)
os.system('pause')
