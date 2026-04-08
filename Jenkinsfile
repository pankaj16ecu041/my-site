pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Step 1: Grabbing the latest code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Step 2: Building the TeachMe application...'
                // Using 'bat' for Windows
                bat 'echo "The build is running!"'
            }
        }

        stage('Test') {
            steps {
                echo 'Step 3: Checking if the code has errors...'
                // CHANGED: used 'bat' instead of 'sh' 
                // CHANGED: used 'python' instead of 'python3'
                bat 'python --version'
            }
        }
    }
}
