from typing import Dict, List, Any


class AttackNode:
    """
    Represents a single attack surface node in the security graph.
    """

    def __init__(self, node_id: str, node_type: str, target: str):
        self.node_id = node_id
        self.node_type = node_type
        self.target = target

        self.attributes: Dict[str, Any] = {}
        self.edges: List[str] = []

    def add_attribute(self, key: str, value: Any):
        self.attributes[key] = value

    def add_edge(self, target_node_id: str):
        if target_node_id not in self.edges:
            self.edges.append(target_node_id)


class AttackGraph:
    """
    Core Attack Surface Graph for V1.0 framework.

    This replaces list-based attack surface modeling with a graph-based structure.
    """

    def __init__(self):
        self.nodes: Dict[str, AttackNode] = {}

    def add_node(self, node: AttackNode):
        self.nodes[node.node_id] = node

    def add_edge(self, from_id: str, to_id: str):
        if from_id in self.nodes:
            self.nodes[from_id].add_edge(to_id)

    def get_node(self, node_id: str):
        return self.nodes.get(node_id)

    def to_dict(self):
        """
        Serialize graph for reporting layer.
        """
        return {
            "nodes": {
                node_id: {
                    "type": node.node_type,
                    "target": node.target,
                    "attributes": node.attributes,
                    "edges": node.edges
                }
                for node_id, node in self.nodes.items()
            }
        }