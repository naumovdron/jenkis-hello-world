pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                git url: "https://github.com/naumovdron/jenkis-hello-world"
                sh 'python main.py'
            }
        }
        stage('test') {
            steps {
                sh "robot test.robot"
        }
    }
}
