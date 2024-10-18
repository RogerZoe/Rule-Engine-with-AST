

# Rule Engine Application

## Overview
This is a 3-tier rule engine application that determines user eligibility based on various attributes such as age, department, income, and experience. It uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic rule creation, combination, and evaluation.

The application includes:

- A **Flask API** for rule creation and evaluation.
- A **SQLite database** for storing the rule strings.
- A **Node-based AST structure** to represent and evaluate the rules.

## Features
- Create and store rules in a structured AST format.
- Evaluate rules dynamically based on user data.
- Combine rules for more complex logic.
- SQLite for persistent storage of rule strings.

## API Endpoints
### 1. POST /create_rule
This endpoint takes a rule string, parses it into an AST, and stores it in the database.

**Request:**
```json
{
  "rule_string": "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)"
}
```
**Response:**
```json
{
  "message": "Rule created",
  "ast": "<AST representation>"
}
```

### 2. POST /evaluate_rule
This endpoint evaluates a given rule string against user data to determine if the user meets the conditions.

**Request:**
```json
{
  "rule_string": "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)",
  "data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
  }
}
```
**Response:**
```json
{
  "result": true
}
```

## Setup Instructions
### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd rule_engine
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install flask sqlite3
   ```

4. **Set up the database:** Initialize the SQLite database by running:
   ```bash
   python db_setup.py
   ```

## Running the Application
Start the Flask server:
```bash
python app.py
```
The application will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Example Usage
### Create a rule using Postman or curl:
```bash
curl -X POST http://127.0.0.1:5000/create_rule \
-H "Content-Type: application/json" \
-d '{"rule_string": "(age > 30 AND department = \"Sales\") OR (age < 25 AND department = \"Marketing\") AND (salary > 50000)"}'
```

### Evaluate a rule:
```bash
curl -X POST http://127.0.0.1:5000/evaluate_rule \
-H "Content-Type: application/json" \
-d '{
    "data": {"age": 35, "department": "Sales", "salary": 60000, "experience": 3},
    "rule_string": "(age > 30 AND department = \"Sales\") OR (age < 25 AND department = \"Marketing\") AND (salary > 50000)"
}'
```

## Database Structure
The database uses SQLite to store rule strings.

### Schema:
- **Table:** rules
  - `id`: Auto-incremented primary key.
  - `rule_string`: The rule expression stored as a string.
  - `ast`: (Optional) Serialized representation of the AST.

### Sample Data:
```sql
INSERT INTO rules (rule_string) VALUES ("(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)");
```

## Test Cases
1. **Create Individual Rules:** Create rule (age > 30 AND department = 'Sales'). Verify the AST representation matches the rule logic.
2. **Combine Rules:** Combine two rules and verify the AST reflects the combined logic.
3. **Evaluate Rules:** Test sample data to see if users meet the eligibility based on the rules.
4. **Error Handling:** Test invalid rule strings and missing operators. Test evaluation with incomplete user data.

## Non-Functional Considerations
- **Security:** Add input validation and sanitize rule inputs to prevent injection attacks.
- **Performance:** Efficient parsing of rules and AST combination strategies to reduce redundant evaluations.
- **Scalability:** Ensure the system can handle a growing number of rules and evaluations efficiently.
- **Logging:** Implement logging for requests and errors to facilitate debugging and monitoring.

## Codebase Structure
The codebase follows a structured format for better maintainability:
```
rule_engine/
│
├── app.py                   # Flask application
├── db_setup.py              # Database initialization script
├── models/                  # Contains models for database interactions
│   └── rule.py              # Rule model for AST representation
├── services/                # Business logic layer
│   ├── rule_service.py      # Contains rule creation and evaluation logic
├── utils/                   # Utility functions
│   └── ast_parser.py        # AST parsing and evaluation
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## Sample Input/Output
### Sample Rule 1:
`(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)`

#### Test Case 1:
**Input:**
```json
{
    "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    },
    "rule_string": "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)"
}
```
**Expected Output:**
```json
{
    "result": true
}
```
**Explanation:** The user's age is 35 (which is greater than 30) and their department is 'Sales'. This satisfies the first part of the rule. Thus, the result is true.

#### Test Case 2:
**Input:**
```json
{
    "data": {
        "age": 23,
        "department": "Marketing",
        "salary": 60000,
        "experience": 1
    },
    "rule_string": "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000)"
}
```
**Expected Output:**
```json
{
    "result": true
}
```
**Explanation:** The user's age is 23 (less than 25) and their department is 'Marketing', and their salary is 60000 (which is greater than 50000). This satisfies the second part of the rule, so the result is true.


