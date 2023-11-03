from lessons.CQ07.point import Point

point: Point = Point(20.0, 50.0)

point.scale_by(2)

new_point: Point = point.scale(5)

print(new_point.x)