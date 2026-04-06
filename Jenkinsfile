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
                docker login -u ${dockerHubUser} -p ${dockerHubPass}
                docker tag 5ada0d13d7eb shivam011/frontend-images:latest
                docker tag dccc93e88dfa shivam011/backend-images:latest
                docker push shivam011/frontend-images
                docker push shivam011/backend-images

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
