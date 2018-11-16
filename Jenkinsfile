#!groovy

node {
    stage 'Checkout'
    scmResult = checkout scm
    echo "scm " + scmResult

    stage 'Python test docker'
    agent { docker 'openjdk:8-jre' } 
            steps {
                echo 'Hello, JDK'
                sh 'java -version'
            }
}

