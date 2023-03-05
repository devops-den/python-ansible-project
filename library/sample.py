from ansible.module_utils.basic import AnsibleModule
import subprocess

class demoClass():
    def __init__(self, p_command):
        self.command = p_command
    
    def execute_command(self):
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output, error
    
def main():
    try:
        module = AnsibleModule(
            argument_spec = dict(
                command = dict(type='str', required=True)
            ),
            supports_check_mode = True
        )

        p_command = module.params.get('command')

        objClass = demoClass(p_command)

        output, error = objClass.execute_command()

        result = dict(
            changed=True,
            message=str(output.decode('ascii').strip()).split("\n")
        )

        # in the event of a successful module execution, you will want to
        # simple AnsibleModule.exit_json(), passing the key/value results
        module.exit_json(**result)

    except Exception as e:
        result = dict(
            changed=False,
            message='Task execution failed with an error.'
        )
        
        module.fail_json(msg=str(e), **result)

if __name__ == '__main__':
    main()