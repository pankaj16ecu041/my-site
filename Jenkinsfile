pipeline {
    agent any
    environment{
        AWS_REGION - 'ap-south-1'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Grabbing the latest code from GitHub...'
                git 'https://github.com/pankaj16ecu041/my-site'
            }
        }
        stage('tag the image'){
            steps{
                script(
                    Image_tag - 'latest'
                )
            }
        }
        stage('Login to ECR'){
            steps{
                withAWS(region: "${env. AWS_REGION}", credentials: 'practice'){
                    powershell '''
                    ${ecrLogin} - aws ecr get-login-password --region ${env.AWS_REGION}

                    docker login --username AWS --password-stdin ${ecrLogin} https://479952476239.dkr.ecr.ap-south-1.amazonaws.com
                    '''
                }
            }
            
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building the docker image for the application...'
                // Using 'bat' for Windows
                powershell '''
                docker build -t myflask .
                docker tag myflask 479952476239.dkr.ecr.ap-south-1.amazonaws.com/practice:latest
                '''
                
            }
        }

        stage('Push to ECR') {
            steps {
                powershell '''
                docker push 479952476239.dkr.ecr.ap-south-1.amazonaws.com/practice:latest
                '''
            }
        }
    }
}
