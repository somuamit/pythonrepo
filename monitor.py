from jenkinsapi.jenkins import Jenkins
import time

# Replace with your Jenkins server URL and credentials
jenkins_url = 'http://localhost:8080/job/demo1'
username = 'demousr'
password = 'Reya19072010#'

# Initialize the Jenkins object with your credentials
jenkins = Jenkins(jenkins_url, username=username, password=password)

# Replace 'YourJobName' with the name of your Jenkins pipeline/job
job_name = 'demo1'

# Function to monitor the Jenkins pipeline status
def monitor_pipeline():
    while True:
        job = jenkins[job_name]
        last_build = job.get_last_build()
        
        if last_build.is_running():
            print(f'Pipeline is running (Build #{last_build.get_number()})')
        elif last_build.is_good():
            print(f'Pipeline completed successfully (Build #{last_build.get_number()})')
        else:
            print(f'Pipeline failed (Build #{last_build.get_number()})')

        time.sleep(10)  # Adjust the polling interval as needed

if __name__ == '__main__':
    try:
        monitor_pipeline()
    except KeyboardInterrupt:
        print('Monitoring stopped.')
