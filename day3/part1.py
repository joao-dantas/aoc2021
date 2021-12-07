class ControlLists:
  def __init__(self, zeros_list, ones_list):
      pass
  zeros_list =zeros_list
  ones_list = ones_list
  most_common = -1

  def process(self, lines, idx):
      for line in lines:
          if line[idx] == "0":
              self.zeros_list.append(line)
          else:
              self.ones_list.append(line)
      if len(zeros_list) > len(ones_list):
          self.most_common = 0
      else:
          self.most_common = 1
      ControlLists()

if __name__ == '__main__':
    with open('example_input.txt') as f:
        ones_list = []
        zeros_list = []
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line[0] == "0":
                zeros_list.append(line)
            else:
                ones_list.append(line)

        for line in zeros_list:


        print ones_list
        print zeros_list
        f.close()

