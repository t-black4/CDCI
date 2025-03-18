#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

PROJECT_NAME="MyPythonProject"

# Create project directories
mkdir -p "$PROJECT_NAME/src"
mkdir -p "$PROJECT_NAME/tests"

# Create main Python file
cat > "$PROJECT_NAME/src/main.py" <<EOL
# Main Python File
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
EOL

# Create test Python file
cat > "$PROJECT_NAME/tests/test_main.py" <<EOL
# Test File
import unittest
import sys
import os

# Ensure the src directory is included in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import main

class TestMain(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
EOL

# Create a requirements file
cat > "$PROJECT_NAME/requirements.txt" <<EOL
# Add dependencies here
EOL

# Create a virtual environment
python3 -m venv "$PROJECT_NAME/venv"

# Create a Jenkinsfile for CI/CD
cat > "$PROJECT_NAME/Jenkinsfile" <<EOL
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the code...'
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'source venv/bin/activate && python -m unittest discover tests'
                }
            }
        }
    }
}
EOL

echo "Project setup complete!"
