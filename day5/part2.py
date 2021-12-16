class LineVent:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, line):
        line = line.strip()
        parts = line.split("->")
        dot_one = parts[0].replace(" ", "").split(",")
        dot_two = parts[1].replace(" ", "").split(",")
        self.x1 = int(dot_one[0])
        self.y1 = int(dot_one[1])
        self.x2 = int(dot_two[0])
        self.y2 = int(dot_two[1])

class HydrothermalVent:
    all_points = {}
    num_overlaps = 0

    def __init__(self):
        pass

    def process_vent(self, line_vent):
        biggest_x = line_vent.x1 if line_vent.x1 > line_vent.x2 else line_vent.x2
        lowest_x = line_vent.x1 if line_vent.x1 < line_vent.x2 else line_vent.x2
        biggest_y = line_vent.y1 if line_vent.y1 > line_vent.y2 else line_vent.y2
        lowest_y = line_vent.y1 if line_vent.y1 < line_vent.y2 else line_vent.y2

        if abs(line_vent.x1 - line_vent.x2) == abs(line_vent.y1 - line_vent.y2):
            x_points = []
            y_points = []
            steps = abs(line_vent.x1 - line_vent.x2) + 1
            if line_vent.x1 > line_vent.x2:
                for i in range(line_vent.x1, line_vent.x2 - 1, -1):
                    x_points.append(i)
            elif line_vent.x1 == line_vent.x2:                     
                for i in range(steps):
                    x_points.append(line_vent.x2)
            else:
                for i in range(line_vent.x1, line_vent.x2 + 1):
                    x_points.append(i)
            if line_vent.y1 > line_vent.y2:
                for i in range(line_vent.y1, line_vent.y2 - 1, -1):
                    y_points.append(i)
            elif line_vent.y1 == line_vent.y2:
                for i in range(steps):
                    y_points.append(line_vent.y2)
            else:
                for i in range(line_vent.y1, line_vent.y2 + 1):
                    y_points.append(i)
            for i in range(len(x_points)):
                self.add_point(x_points[i], y_points[i])
        elif biggest_x != lowest_x and biggest_y == lowest_y:
            for x in range(lowest_x, biggest_x + 1):
                self.add_point(x, line_vent.y1)
        elif biggest_y != lowest_y and biggest_x == lowest_x:
            for y in range(lowest_y, biggest_y + 1):
                self.add_point(line_vent.x1, y)

    def add_point(self, x, y):
        if x not in self.all_points:
            self.all_points[x] = {y: 1}
        elif y not in self.all_points[x]:
            self.all_points[x][y] = 1
        else:
            self.all_points[x][y] += 1
            if self.all_points[x][y] == 2:
                self.num_overlaps += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        thermal_vent = HydrothermalVent()
        while True:
            file_line = f.readline()
            if not file_line:
                break
            line_vent = LineVent(file_line)
            thermal_vent.process_vent(line_vent)
        f.close()
        print thermal_vent.num_overlaps
