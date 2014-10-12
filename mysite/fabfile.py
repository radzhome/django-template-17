import os

from boulanger.fabfile import *


# Define Server Topology
env.server_nodes = {
    'web': {
        #'web1': ('<public server address>', '<private ip>'),
    },
    'db': {
        #'db1': ('<public server address>', '<private ip>'),
    },
}

# Auto Generated, Do Not Modify
env.project_name = os.getcwd().split('/')[-1]
env.user = env.project_name + 'team'
env.roledefs = {
    'web': [public_address for public_address, private_address in env.server_nodes['web'].values()],
    'db': [public_address for public_address, private_address in env.server_nodes['db'].values()],
}
