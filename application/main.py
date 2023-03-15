# For testing
#APIKEY = "YOUR KEY"
#APIKEY_REGION = "US"
# Temporary - Enter API Token here for testing
import os
from flask import Flask, render_template, request, redirect, url_for
import requests
import json
app = Flask(__name__) 
API_TOKEN = os.environ['APIKEY']
APIKEY_REGION = os.environ['API_REGION']
# Dummy data for services
SERVICES = []
RUNNERS = []
with open("configuration/tasks.json", "r") as f:
    TASKS = json.load(f)
payload = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": "Token token=" + API_TOKEN,
}

if APIKEY_REGION="EU":
    services_url = "https://api.eu.pagerduty.com/services"
    automation_url = "https://api.eu.pagerduty.com/automation_actions/actions"
    runners_url = "https://api.eu.pagerduty.com/automation_actions/runners"
else:
    services_url = "https://api.pagerduty.com/services"
    automation_url = "https://api.pagerduty.com/automation_actions/actions"
    runners_url = "https://api.pagerduty.com/automation_actions/runners"

# Main create AA task
def create_action(selected_services,selected_runner,selected_tasks):
    selected_tasks = [int(id) for id in selected_tasks]
    processed_task = [item for item in TASKS if item['id'] in selected_tasks]
    for item in processed_task:
        services_json = []
        for service in selected_services:
            service_json = {"id": service, "type": "service_reference"}
            services_json.append(service_json)
        aa_payload = {"action": {
        "name": item['name'],
        "description": item['description'],
        "action_type": "script",
        "runner": selected_runner[0],
        "action_data_reference": {"script": item['script']},
        "services": services_json
        }}
        response = requests.request("POST", automation_url, json=aa_payload, headers=headers)
    return ()

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        # Get the selected services and tasks
        #API_TOKEN = request.form['text_value'] 
        selected_services = request.form.getlist("services")
        selected_tasks = request.form.getlist("tasks")
        selected_runners = request.form.getlist("runners")  
        # Do something with the selected services and tasks
        create_action(selected_services,selected_runners,selected_tasks)
        message = f"Selected services: {selected_services}\nSelected tasks: {selected_tasks}\nSelected runner: {selected_runners}"
        echo_message = f"{message}"
        # Redirect to the index page
        return redirect(url_for("index", echo_message=echo_message))
    else:
        services_response = requests.request(
            "GET", services_url, data=payload, headers=headers
        )
        services_data = services_response.json()
        runner_response = requests.request(
            "GET", runners_url, data=payload, headers=headers
        )
        runners_data = runner_response.json()
        RUNNERS = []
        SERVICES = []
        for service in services_data["services"]:
            SERVICES.append({"id": service["id"], "name": service["name"]})

        for runners in runners_data["runners"]:
            if runners["runner_type"] == "sidecar":
                RUNNERS.append({"id": runners["id"], "name": runners["name"]})

        echo_message = request.args.get("echo_message", "")
        # Render the template with the services and tasks data and popup message
        return render_template(
            "index.html",
            services=SERVICES,
            tasks=TASKS,
            runners=RUNNERS,
            echo_message=echo_message,
        )
if __name__ == "__main__":
    app.run(debug=True)
