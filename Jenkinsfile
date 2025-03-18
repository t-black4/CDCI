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
                    // Change directory to MyPythonProject and create virtual environment
                    dir('MyPythonProject') {
                        sh '''
                        # Create virtual environment
                        /usr/bin/python3 -m venv venv
                        # Activate virtual environment and install dependencies
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
                    // Change directory to MyPythonProject and run tests
                    dir('MyPythonProject') {
                        sh '''
                        # Activate virtual environment
                        . venv/bin/activate
                        # Run your test command here, e.g., pytest
                        pytest
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
