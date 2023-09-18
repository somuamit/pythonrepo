pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'b9771b9f-c525-442e-90b9-c88f7e011706', url: 'https://github.com/somuamit/pythonrepo.git']])
            }
        }
        stage('Build'){
            steps{
               git branch: 'main', credentialsId: 'b9771b9f-c525-442e-90b9-c88f7e011706', url: 'https://github.com/somuamit/pythonrepo.git'
               bat  'python myscript.py'
                
                
            }
        }
        stage('Test'){
            steps{
                echo 'Testing done sucessfully'
            }
        }
    }
}
