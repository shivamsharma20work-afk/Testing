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
        stage("Docker Login") {
            steps {
                withCredentials([usernamePassword('credentialsId': "dockerHubCred" ,
                passwordVariable:"dockerHubPass",
                usernameVariable:"dockerHubUser")]){
                sh '''
                docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}
                echo logged in to DockerHub
                '''
                }
            }
        }
        stage("Test") {
            steps {
                sh '''
                docker run -d -p 3000:3000 --network my-network --name frontend frontend-images
                docker run -d -p 5000:5000 --network my-network --name backend  backend-images

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
