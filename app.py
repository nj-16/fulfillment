from flask import Flask, request, jsonify

app = Flask(__name__)

salary_data = {
    "Software Engineer": "$150,000 per year",
    "Human Resources": "$70,000 per year",
    "Software Tester": "$120,000 per year",
    "Devops": "$130,000 per year",
    "Data Scientist": "$120,000 per year",
    "Data Analyst": "$85,000 per year"
}

@app.route('/')
def home():
    return jsonify({'student_number': '200582109'})

@app.route('/webhook', methods=['POST'])
def webhook():
    req =  request.get_json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName','')
    parameters = req.get('queryResult', {}).get('parameters', {})

    if intent == "Salary estimation intent":
        job_role = parameters.get('job_role', "").title()
        response_text = f"The average salary for a {job_role} is {salary_data.get(job_role, 'not available at the moment')}."
    else:
        response_text = "Sorry, I didn't understand that. Can you please try again"

    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


