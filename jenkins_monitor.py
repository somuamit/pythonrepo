import requests
import time
import jenkins

# Jenkins Pipeline URL
jenkins_url = 'http://localhost:8080/job/demo1/7/api/json'

# Jenkins API Authentication (if needed)
# username = 'demousr'
# password = 'Password@123'

# Monitor the Jenkins pipeline
while True:
    try:
        # Make an HTTP GET request to the Jenkins API
        response = requests.get(jenkins_url, auth=(username , password) if 'username' in locals() else None)
        response.raise_for_status()  # Raise an exception if the request fails

        # Parse the JSON response
        data = response.json()

        # Extract pipeline status
        result = data['result']
        print(f'Pipeline Status: {result}')

        # Check if the pipeline is completed
        if result not in ['ABORTED', 'NOT_BUILT', 'IN_PROGRESS']:
            break

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    # Wait for a few seconds before checking again
    time.sleep(10)

print('Pipeline monitoring complete.')
