import os
from flask import Flask, render_template, request, redirect, url_for,jsonify
import requests
import json
app = Flask(__name__) 
services_url=""
runners_url=""
automation_url=""
API_KEY=""

with open("configuration/tasks.json", "r") as f:
    TASKS = json.load(f)

RUNNERS = []
SERVICES = []



def updateservices():
  services_response = requests.request(
            "GET", services_url, data=payload, headers=headers
        )
  services_data = services_response.json()
  print (services_data)
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

def create_action(selected_services,selected_runner,selected_tasks):
    print ("deploying....")
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
    return (response)

@app.route('/update_api_key_and_region', methods=['POST'])
def update_api_key_and_region():
    API_KEY = request.form.get('api_key')
    APIKEY_REGION = request.form.get('region')
    payload = ""
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Token token=" + API_KEY,}

    if APIKEY_REGION == "EU":

        services_url = "https://api.eu.pagerduty.com/services"
     
        automation_url = "https://api.eu.pagerduty.com/automation_actions/actions"

        runners_url = "https://api.eu.pagerduty.com/automation_actions/runners"
    else:
        services_url = "https://api.pagerduty.com/services"
      
        automation_url = "https://api.pagerduty.com/automation_actions/actions"
     
        runners_url = "https://api.pagerduty.com/automation_actions/runners"
        
   
    services_response = requests.request(
                "GET", services_url, data=payload, headers=headers
            )
    services_data = services_response.json()
    runner_response = requests.request(
                "GET", runners_url, data=payload, headers=headers
            )
    runners_data = runner_response.json()
    for service in services_data["services"]:
        SERVICES.append({"id": service["id"], "name": service["name"]})

    for runners in runners_data["runners"]:
        if runners["runner_type"] == "sidecar":
          RUNNERS.append({"id": runners["id"], "name": runners["name"]})

    return jsonify({
        'services': SERVICES,
        'runners': RUNNERS,
    })

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_services = request.form.getlist("services")
        selected_tasks = request.form.getlist("tasks")
        selected_runners = request.form.getlist("runners")  
        create_action(selected_services,selected_runners,selected_tasks)
        message = f"Selected services: {selected_services}\nSelected tasks: {selected_tasks}\nSelected runner: {selected_runners}"
        create_action(selected_services,selected_runners,selected_tasks)
        return redirect(url_for("index", echo_message=echo_message))

    else:
        echo_message = request.args.get("echo_message", "")
        return render_template(
            "index.html",
            services=SERVICES,
            tasks=TASKS,
            runners=RUNNERS,
            echo_message=echo_message,
        )
if __name__ == "__main__":

    app.run(host="0.0.0.0",port=5001,debug=True)

