pipeline {
    // 1. Where should this run? 'any' means any available computer/node.
    agent any

    // 2. The sequence of events
    stages {

        // Stage 1: Getting the code
        stage('Checkout') {
            steps {
                echo 'Step 1: Grabbing the latest code from GitHub...'
                checkout scm
            }
        }

        // Stage 2: Simulating a build
        stage('Build') {
            steps {
                echo 'Step 2: Building the TeachMe application...'
                // For now, we just print a message to see it work
                sh 'echo "The build is running!"'
            }
        }

        // Stage 3: Running a test
        stage('Test') {
            steps {
                echo 'Step 3: Checking if the code has errors...'
                sh 'python3 --version'
            }
        }
    }
}