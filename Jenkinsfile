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
                docker run -d -p 3000:3000 --network my-network frontend-images
                docker run -d -p 5000:5000 --network my-network backend-images
                
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