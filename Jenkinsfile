pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: 'SECONDS')
        ansiColor('xterm')
    }
    stages {
        stage('Ansible playbook invoke') {
            steps {
                ansiblePlaybook(
                    playbook: 'playbook.yml',
                    inventory: 'inventory.yml',
                    credentialsId: 'devops-ansible',
                    colorized: true)
            }
        }
    }
}