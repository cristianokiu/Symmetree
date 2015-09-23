import unittest
from datetime import datetime

from symmetree.serializers import MarkdownSerializer, JSONSerializer
from symmetree.models import Node


class TestMarkdownSerializer(unittest.TestCase):
    def setUp(self):
        self.inpt = \
'''## Study Tree

1. **Foundations**
    - Programming Languages
        + Javascript
        * C++
        + Haskell _(or any other functional language)_
    - Algorithms & Data Structures
    - Mathematics
        * Statistics
        * Linear Algebra

1. **Development**
    - Framework & Applications
        10. Django
        aaaa
        2. React & AngularJS
        2. REST Frameworks
        22. Scrapy
        1. Web Widgets
    - Scalability
        - Queue Systems
            * RabbitMQ
            1. Redis.io
            - Redis Queue'''

    def test_deserializing(self):
        ser = MarkdownSerializer()
        node = ser.deserialize(self.inpt)

        self.assertTrue(len(node.children) == 2)
        self.assertEqual(node.children[1].children[1].
                children[0].children[2].name, 'Redis Queue')
        

class TestJSONSerializer(unittest.TestCase):
    def setUp(self):
        pass

    def test_serializing(self):
        ser = JSONSerializer()
        node = Node(name='Test')
        Node(parent=node, name='Child 1')
        Node(parent=node, name='Child 2')
        json = ser.serialize(node)
        self.assertTrue(len(json) == 210)


if __name__ == "__main__":
    unittest.main()
