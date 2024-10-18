# ast_engine.py
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' for AND/OR, 'operand' for condition
        self.value = value  # condition for operand nodes
        self.left = left  # left child (Node)
        self.right = right  # right child (Node)

    def evaluate(self, data):
        """Evaluate this node based on user data"""
        if self.type == "operator":
            if self.value == "AND":
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == "OR":
                return self.left.evaluate(data) or self.right.evaluate(data)
        elif self.type == "operand":
            # Example of handling comparison logic
            attribute, operator, val = self.value.split(" ")
            attribute_value = data.get(attribute)

            # Handle different comparison operators
            if operator == ">":
                return attribute_value > int(val)
            elif operator == "<":
                return attribute_value < int(val)
            elif operator == "=":
                return attribute_value == val.strip("'")
        return False

def parse_rule(rule_string):
    """Parse a rule string into an AST"""
    # This is a basic parser. You may extend it for complex parsing.
    if "AND" in rule_string:
        left, right = rule_string.split(" AND ", 1)
        return Node("operator", "AND", parse_rule(left), parse_rule(right))
    elif "OR" in rule_string:
        left, right = rule_string.split(" OR ", 1)
        return Node("operator", "OR", parse_rule(left), parse_rule(right))
    else:
        # This is a simple condition like age > 30
        return Node("operand", rule_string)
