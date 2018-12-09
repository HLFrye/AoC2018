import re

class NodeGraph:
  def __init__(self):
    self.nodes = {}
    self.in_process = []

  def add_node(self, line):
    def create_node(line):
      m = re.match(r"Step (?P<before>.*) must be finished before step (?P<after>.*) can begin.", line)
      return m.group("after"), m.group("before")
      
    def add_nodes(node, nodes):
        (node_name, node_requires) = node
        if not node_name in nodes:
          nodes[node_name] = []
        nodes[node_name].append(node_requires)
        if not node_requires in nodes:
          nodes[node_requires] = []
    add_nodes(create_node(line), self.nodes)

  def get_next_available(self):
    def are_requirements_met(node_key, nodes):
      for requirements in nodes[node_key]:
        if requirements in nodes:
          return False
      return True
    def cost(key):
      return 61 + (ord(key) - ord('A'))
    
    for key in sorted(self.nodes.keys()):
      if key not in self.in_process:
        if are_requirements_met(key, self.nodes):
          self.in_process.append(key)
          return key, cost(key)
    return None

  def finish(self, key):
    self.in_process.pop(self.in_process.index(key))
    self.nodes.pop(key)

  def has_more_nodes(self):
    return len(self.nodes) > 0

def process(nodes):
  time_counter = 0
  workers = [None] * 5

  def is_available(worker):
    return worker is None

  def is_finished(worker):
    if worker is None:
      return False
    return worker[1] == time_counter

  while nodes.has_more_nodes():
    for i, worker in enumerate(workers):
      if is_finished(worker):
        nodes.finish(worker[0])
        workers[i] = None

    for i, worker in enumerate(workers):
      if is_available(worker):
        next_node = nodes.get_next_available()
        if next_node is not None:
          (node, time) = next_node
          workers[i] = (node, time + time_counter)

    time_counter = time_counter + 1
  
  return time_counter - 1

def main():
  nodes = NodeGraph()
  with open("../input.txt") as input:
    for line in input.readlines():
      nodes.add_node(line)

  print("The total time is {}".format(process(nodes)))

if __name__ == "__main__":
  main()