pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    stages {
        stage('Ansible playbook invoke') {
            steps {
                ansiblePlaybook(
                    playbook: 'playbook.yml',
                    inventory: 'inventory.yml',
                    credentialsId: 'devops-ansible',
                    colorized: true,
                    hostKeyChecking: false)
            }
        }
    }
}