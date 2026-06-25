class AttackNode:
    """
    V1.0.1 Graph Node
    """

    def __init__(self, node_id, node_type, target):
        self.node_id = node_id
        self.node_type = node_type
        self.target = target
        self.attributes = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value


class AttackGraph:
    """
    V1.0.1 Attack Graph
    """

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def add_edge(self, from_id, to_id):
        self.edges.append((from_id, to_id))

    def to_dict(self):
        return {
            "nodes": {
                node_id: {
                    "node_id": node.node_id,
                    "type": node.node_type,
                    "target": node.target,
                    "attributes": node.attributes
                }
                for node_id, node in self.nodes.items()
            },
            "edges": self.edges
        }