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
    # app.logger.debug(f"Received request: {req}")
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')
    parameters = req.get('queryResult', {}).get('parameters', {})

    if intent == "Salary estimation intent":
        job_title = parameters.get("job_title", "").title()
        if job_title and job_title in salary_data:
            response_text = f"The average salary for a {job_title} is {salary_data[job_title]}."
        else:
            response_text = "I'm sorry, I couldn't find any relevant salary information for that role."
    else:
        response_text = "Sorry, I didn't understand that. Can you please try again"

    # app.logger.debug(f"Response: {response_text}")
    return jsonify({'fulfillmentText': response_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


