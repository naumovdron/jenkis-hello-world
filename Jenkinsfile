pipeline {
    agent {
        docker {
            image 'python:3.5.1'
        }
    }
    stages {
        stage('build') {
            steps {
                git url: "https://github.com/naumovdron/jenkis-hello-world"
                sh 'python main.py'
            }
        }
        stage('test') {
            sh "robot test.robot"
            step([$class: 'RobotPublisher',
                disableArchiveOutput: false,
                logFileName: 'log.html',
                otherFiles: '',
                outputFileName: 'output.xml',
                outputPath: '.',
                passThreshold: 100,
                reportFileName: 'report.html',
                unstableThreshold: 0]);
        }
    }
}
