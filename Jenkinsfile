pipeline{
    agent any

    stages{
        stage("Build") {
            steps {
                sh '''
                docker build -t frontend-images ./frontend
                docker build -t backend-images ./backend
                '''
            }
        }
        stage("Test") {
            steps {
                sh '''
                echo "This is Testing stage"
                '''
            }
        }
        stage("Deploy") {
            steps {
                sh '''
                echo "This is Deploy stage"
                '''
            }
        }
    }
}