import json

from xml.dom.minidom import parseString
from markdown2 import markdown
from abc import ABCMeta, abstractmethod
from .models import Node


class Serializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, node, *args, **kwargs):
        pass

    @abstractmethod
    def deserialize(self, inpt, *args, **kwargs):
        pass

    @staticmethod
    def to_dict(node):
        dic = {'name': node.name,
               'begin': node.begin.isoformat(),
               'spent': node.spent.total_seconds()}

        if node.children:
            dic['children'] = [Serializer.to_dict(c)
                               for c in node.children]

        return dic

    @staticmethod
    def from_dict(dic):
        raise NotImplementedError()


class MarkdownSerializer(Serializer):
    def serialize(self, node):
        raise NotImplementedError()

    def deserialize(self, inpt):
        dom_root = parseString("<root>{0}</root>".
                               format(markdown(inpt))).firstChild

        return self._parse_tree(dom_root)

    def _parse_tree(self, dom_node, parent=None):
        if dom_node.nodeType == dom_node.TEXT_NODE:
            return dom_node.data

        node = parent or Node()
        if dom_node.tagName == 'li':
            node = Node(parent)

        for dom_child in dom_node.childNodes:
            child = self._parse_tree(dom_child, node)
            if isinstance(child, str):
                node.name += child

        node.name = node.name.strip()
        return node


class JSONSerializer(Serializer):
    def serialize(self, node, pretty=False):
        return json.dumps(Serializer.to_dict(node),
                          indent=2 if pretty else None)

    def deserialize(self, inpt):
        raise NotImplementedError()
