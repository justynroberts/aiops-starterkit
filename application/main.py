API_TOKEN = "1234"
# ^^^^^^^
# Temporary - Enter API key here for testing


from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# Dummy data for services
SERVICES = [
    {"id": 1, "name": "Service 1", "data": "Some data for Service 1"},
]
RUNNERS = [{"id": 1, "name": "Runner1"}]

# Open external files
with open("configuration/tasks.json", "r") as f:
    TASKS = json.load(f)

services_url = "https://api.pagerduty.com/services"
runners_url = "https://api.pagerduty.com/automation_actions/runners"
payload = ""
headers = {
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Content-Type": "application/json",
    "Authorization": "Token token=" + API_TOKEN,
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the selected services and tasks
        selected_services = request.form.getlist("services")
        selected_tasks = request.form.getlist("tasks")
        selected_runners = request.form.getlist("runners")
        # Do something with the selected services and tasks
        print("Selected services:", selected_services)
        print("Selected tasks:", selected_tasks)
        print("Selected runners:", selected_runners)
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
