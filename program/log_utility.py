from json import dumps

def make_log_data(message: str):
    data = {
        'type': 'insert',
        'target': 'log',
        'item': {
            'message': message
        }
    }
    data = dumps(data)
    return data