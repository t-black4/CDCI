pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the code...'
                    // Checkout the code from version control
                    checkout scm
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment...'
                    // Change directory to MyPythonProject
                    dir('MyPythonProject') {
                        // Create virtual environment and install dependencies
                        sh '''
                        /usr/bin/python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    // Change directory to MyPythonProject
                    dir('MyPythonProject') {
                        // Run the tests with the virtual environment activated
                        sh '''
                        source venv/bin/activate
                        python -m unittest discover tests
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Clean up the virtual environment (optional)
            dir('MyPythonProject') {
                sh 'rm -rf venv'
            }
        }
    }
}
