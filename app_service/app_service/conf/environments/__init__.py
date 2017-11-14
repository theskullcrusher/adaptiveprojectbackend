CONFIG_MAP = {
    'prod': 'production',
    'dev': 'development'
}

def get_config(env):
    return '.'.join(['app_service', 'conf', 'environments',
                     CONFIG_MAP.get(env, env), 'Config'])
