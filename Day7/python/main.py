import re

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

def are_requirements_met(node_key, nodes):
  for requirements in nodes[node_key]:
    if requirements in nodes:
      return False
  return True

def get_order(nodes):
  can_execute = None
  def get_next():
    for key in sorted(nodes.keys()):
      if are_requirements_met(key, nodes):
        nodes.pop(key)
        return key
    return None
  next = get_next()
  while next is not None:
    yield next
    next = get_next()

def main():
  nodes = {}
  with open("../input.txt") as input:
    for line in input.readlines():
      add_nodes(create_node(line), nodes)

  order = ""
  for item in get_order(nodes):
    order = order + item

  print("The code is : {}".format(order))
  for key, value in nodes.items():
    print("nodes[{}] = {}".format(key, value))

if __name__ == "__main__":
  main()