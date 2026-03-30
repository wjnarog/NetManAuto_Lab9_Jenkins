pipeline {
    agent any

    environment {
        QUAL_GATE = 5
        SCRIPT_TO_TEST = 'netman_netconf_obj2.py'
        TEST_SCRIPT = 'unit_tests.py'
        EMAIL = 'root@localhost'
    }
    
    stages {
        stage('Update/Install packages') {
            steps {
                echo 'Updating and Installing required packages'
                sh 'pip install --upgrade -r requirements.txt'
            }
        }
        stage('Checking and fixing violations') {
            steps {
                echo 'Checking for PEP8 violations'
                sh 'pylint ${SCRIPT_TO_TEST} --fail-under=5'
            }
        }
        stage('Running application') {
            steps {
                echo 'Running ${SCRIPT_TO_TEST} script'
                sh 'python3 ${SCRIPT_TO_TEST} | tee output.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                echo 'Testing ${SCRIPT_TO_TEST} against unit tests'
                sh 'python3 ${TEST_SCRIPT}'
            }
        }
    }
    post {
            success {
                mail to: "${EMAIL}",
                    subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Build #${env.BUILD_NUMBER} succeeded"
            }
            failure {
                mail to: "${EMAIL}",
                    subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Build #${env.BUILD_NUMBER} failed"
            }
        }
}