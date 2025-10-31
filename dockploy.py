# Install the requests library if not already installed
# pip install requests

import requests

API_URL = "http://98.70.29.85:3000//api/project.all"
api_key = "YbktZhWbSGoxWyeJsWCQtCmJKPDxevYGbvgqzuQMywXYijAFIHiqYLJIvtGwZanB"
app_name = "job-portal-backend-2amhuw"


def get_application_id():
    """Fetch Application ID for a given app name"""
    headers = {
        "accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        response = requests.get(API_URL, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Safely iterate and find the requested application by name
        for project in data or []:
            environments = project.get("environments", [])
            for env in environments:
                applications = env.get("applications", [])
                for app in applications:
                    if app.get("appName") == app_name:
                        print(app.get("applicationId"))
                        return app.get("applicationId")

    except requests.RequestException as e:
        print(f"Error fetching application ID: {e}")


# Call the function
get_application_id()
