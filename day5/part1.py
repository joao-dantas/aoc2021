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

    def __str__(self):
        return "x1: " + str(self.x1) + ", x2: " + str(self.x2) + ", y1: " + str(self.y1) + ", y2: " + str(self.y2)


class HydrothermalVent:
    all_points = {}
    num_overlaps = 0

    def __init__(self):
        pass

    def process_vent(self, live_vent):
        if not (line_vent.x1 == line_vent.x2 or line_vent.y1 == line_vent.y2):
            return
        if live_vent.x2 > live_vent.x1:
            for i in range(live_vent.x1, live_vent.x2 + 1):
                if i not in self.all_points:
                    self.all_points[i] = {live_vent.y1: 1}
                elif live_vent.y1 not in self.all_points[i]:
                    self.all_points[i][live_vent.y1] = 1
                else:
                    self.all_points[i][live_vent.y1] += 1
                    if self.all_points[i][live_vent.y1] == 2:
                        self.num_overlaps += 1
        elif live_vent.x1 > live_vent.x2:
            for i in range(live_vent.x2, live_vent.x1 + 1):
                if i not in self.all_points:
                    self.all_points[i] = {live_vent.y1: 1}
                elif live_vent.y1 not in self.all_points[i]:
                    self.all_points[i][live_vent.y1] = 1
                else:
                    self.all_points[i][live_vent.y1] += 1
                    if self.all_points[i][live_vent.y1] == 2:
                        self.num_overlaps += 1

        elif live_vent.y2 > live_vent.y1:
            for i in range(live_vent.y1, live_vent.y2 + 1):
                if live_vent.x1 not in self.all_points:
                    self.all_points[live_vent.x1] = {live_vent.y1: 1}
                elif i not in self.all_points[live_vent.x1]:
                    self.all_points[live_vent.x1][i] = 1
                else:
                    self.all_points[live_vent.x1][i] += 1
                    if self.all_points[live_vent.x1][i] == 2:
                        self.num_overlaps += 1
        else:
            for i in range(live_vent.y2, live_vent.y1 + 1):
                if live_vent.x1 not in self.all_points:
                    self.all_points[live_vent.x1] = {live_vent.y1: 0}
                elif i not in self.all_points[live_vent.x1]:
                    self.all_points[live_vent.x1][i] = 1
                else:
                    self.all_points[live_vent.x1][i] += 1
                    if self.all_points[live_vent.x1][i] == 2:
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
        print thermal_vent.all_points
        print thermal_vent.num_overlaps
