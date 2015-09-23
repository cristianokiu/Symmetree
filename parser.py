from xml.dom.minidom import parseString
from markdown2 import markdown_path

class Node:
    def __init__(self, parent = None):
        self.name = ''
        self.children = []
        self.parent = parent
        self.level = parent.level + 1 if parent else 0

    def __repr__(self):
        return "{0}: {1}".format(self.level, self.name)

def parse_tree(dom_node, parent = None):
    if dom_node.nodeType == dom_node.TEXT_NODE:
        return dom_node.data

    node = parent or Node()
    if dom_node.tagName == 'li':
        node = Node(parent)

    for dom_child in dom_node.childNodes:
        child = parse_tree(dom_child, node)
        if isinstance(child, str):
            node.name += child
        elif child is not node:
            node.children.append(child)

    node.name = node.name.strip()
    return node


dom_root = parseString("<root>{0}</root>".format(
            markdown_path('study.md')
            )).firstChild

tree = parse_tree(dom_root)
