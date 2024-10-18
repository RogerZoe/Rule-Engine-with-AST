# app.py
from flask import Flask, request, jsonify
from ast_engine import parse_rule, Node
from db_setup import insert_rule, init_db
import sqlite3

app = Flask(__name__)

# Initialize the database when the app starts
init_db()


@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule_string = data['rule_string']

    # Parse the rule string into AST
    root_node = parse_rule(rule_string)

    # Store the rule string in the database
    insert_rule(rule_string)

    return jsonify({"message": "Rule created", "ast": str(root_node)}), 201


@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.json['data']
    rule_string = request.json['rule_string']

    # Parse the rule and evaluate it
    root_node = parse_rule(rule_string)
    result = root_node.evaluate(data)

    return jsonify({"result": result}), 200


if __name__ == '__main__':
    app.run(debug=True)
