# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


class Vector2(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


def calc(points, new_x):
	num = len(points)
	result = 0
	for index_j in xrange(num):
		y = points[index_j].y

		result_x = 1
		for index_i in xrange(num):
			if index_i == index_j:
				continue
			result_x *= (new_x - points[index_i].x) / (points[index_j].x - points[index_i].x)

		result += result_x * y
	return result


def test_calc():
	point1 = Vector2(4, 10)
	point2 = Vector2(5, 5.25)
	point3 = Vector2(6, 1)
	points = [point1, point2, point3]
	print calc(points, 18)  # -11


def test_draw():
	point1 = Vector2(-9, 5)
	point2 = Vector2(-4, 2)
	point3 = Vector2(-1, -2)
	point4 = Vector2(7, 9)
	points = [point1, point2, point3, point4]

	step = 1
	x_list = []
	y_list = []
	for x in xrange(-90, 70, step):
		x = x / 10.0
		y = calc(points, x)
		x_list.append(x)
		y_list.append(y)
		print (x, y)

	l1 = plt.plot(x_list, y_list, 'r--', label='type1')
	plt.title('The Lasers in Three Conditions')
	plt.xlabel('row')
	plt.ylabel('column')
	plt.legend()
	plt.show()


def frange(start, stop, step):
	x = start
	while x < stop:
		yield x
	x += step


if __name__ == '__main__':
	test_calc()
	test_draw()
