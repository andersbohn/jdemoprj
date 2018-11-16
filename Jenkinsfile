pipeline {
    agent {
        docker { image 'airflow-tools:latest' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'env'
                sh 'ls -l /var'
                sh 'python --version'
                sh 'python3 -m unittest tests/*'
            }
        }
    }
}