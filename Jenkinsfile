pipeline {
    agent any
    stages {
        stage('Clone The Repository') {
            steps {
                git 'https://github.com/rajshamz/simple-quiz-app.git'
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'npm install'
            }
        }
        stage('Test Coverage'){
            steps{
                sh 'npm test -- --coverage'
            }
        }
        //stage('SonarQube analysis') {
          //  steps {
              // Run the SonarQube scan
            //  sonarqube(
                // Required parameters
                //credentialsId: 'your-sonarqube-credentials-id',
                //projectKey: 'your-sonarqube-project-key',
                //projectName: 'your-sonarqube-project-name',
                // Optional parameters
                //extraProperties: [
                  // Additional properties to pass to the SonarQube scan
                  //],
                  //failOnError: false,  // Set to true to fail the build if the SonarQube scan fails
                  //maxMemory: '1024m',  // Maximum memory to use for the scan
                  //organization: 'your-sonarqube-organization',  // Set this if you are using the SonarQube Enterprise edition
                  //serverUrl: 'https://your-sonarqube-server.com'  // The URL of your SonarQube server
              //  )
              //}
            //}
          //}
        stage('Build Docker Container') {
            steps {
                script {
                    def app = docker.build("quiz-app:latest", ".")
                }
            }
        }
        stage('Deploy to Docker Desktop') {
            steps {
                script {
                    sh 'docker stop quiz-app || true'
                    sh 'docker rm quiz-app || true'
                    sh 'docker run --name quiz-app -d -p 8099:8080 quiz-app:latest'
                }
            }
        }
     }
}

