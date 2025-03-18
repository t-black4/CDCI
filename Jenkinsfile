pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Setup environment, create virtualenv, install dependencies
                    sh 'cd MyPythonProject'
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the unit tests
                    
                    sh 'source venv/bin/activate && python -m unittest discover -s tests'
                }
            }
        }
    }

    post {
        always {
            // Clean up
            sh 'deactivate'
        }
    }
}
