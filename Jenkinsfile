pipeline {
    agent any

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Run commands with bash shell to ensure source works
                    sh '''
                    cd MyPythonProject
                    python3 -m venv venv
                    bash -c "source venv/bin/activate && echo 'Virtual environment activated'"
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies within the virtual environment
                    sh '''
                    pwd
                    bash -c "source MyPythonProject/venv/bin/activate && pip install -r MyPythonProject/requirements.txt"
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests within the virtual environment
                    sh '''
                    bash -c "source MyPythonProject/venv/bin/activate && pytest MyPythonProject/tests/test_main.py"
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                // Deactivate the virtual environment after the pipeline runs
                sh '''
                bash -c "source MyPythonProject/venv/bin/activate && deactivate"
                '''
            }
        }
    }
}