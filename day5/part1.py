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

    def process_vent(self, live_vent):
        if not (line_vent.x1 == line_vent.x2 or line_vent.y1 == line_vent.y2):
            return
        biggest_x = live_vent.x1 if live_vent.x1 > live_vent.x2 else live_vent.x2
        lowest_x = live_vent.x1 if live_vent.x1 < live_vent.x2 else live_vent.x2
        biggest_y = live_vent.y1 if live_vent.y1 > live_vent.y2 else live_vent.y2
        lowest_y = live_vent.y1 if live_vent.y1 < live_vent.y2 else live_vent.y2
        if biggest_x != lowest_x:
            for x in range(lowest_x, biggest_x + 1):
                self.add_point(x, live_vent.y1)
        else:
            for y in range(lowest_y, biggest_y + 1):
                self.add_point(live_vent.x1, y)

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
        print(thermal_vent.num_overlaps)
