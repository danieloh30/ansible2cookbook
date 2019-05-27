#!/usr/bin/python 

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
 'status': ['preview'],
 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: hello_module

short_description: This is my custom module

version_added: "1.0"

description:
    - "my first module to print hello"

options:
    name:
        description:
            - TBM
        required: true
'''

EXAMPLES = '''
- name: Print instant messages
  hello_module:
    name: hello
'''

RETURN = '''
message:
    description: The message that the module prints
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    
    module_args = dict(
        name=dict(type='str', required=False, default=False)
    )

    result = dict(
        changed=True,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    result['message'] = 'hello'
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
