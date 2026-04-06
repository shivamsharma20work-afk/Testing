pipeline{
    agent any

    stages{
        stage("Build") {
            steps {
                sh '''
                docker build -t frontend-image .
                docker build -t backend-image .
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