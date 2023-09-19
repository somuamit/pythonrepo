import jenkins
import time

# Replace with your Jenkins server URL and credentials
jenkins_url = 'http://localhost:8080'
username = 'demousr'
password = 'Reya19072010#'

# Initialize the Jenkins server connection
server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Replace 'YourJobName' with the name of your Jenkins pipeline/job
job_name = 'demo1'

# Function to monitor the Jenkins pipeline status
def monitor_pipeline():
    while True:
        job_info = server.get_job_info(job_name)
        last_build = job_info['lastBuild']

        if last_build is not None:
            build_number = last_build['number']
            build_info = server.get_build_info(job_name, build_number)

            if build_info['building']:
                print(f'Pipeline is running (Build #{build_number})')
            elif build_info['result'] == 'SUCCESS':
                print(f'Pipeline completed successfully (Build #{build_number})')
            else:
                print(f'Pipeline failed (Build #{build_number})')

        time.sleep(10)  # Adjust the polling interval as needed

if __name__ == '__main__':
    try:
        monitor_pipeline()
    except KeyboardInterrupt:
        print('Monitoring stopped.')
