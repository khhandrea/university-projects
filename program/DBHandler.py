import sqlite3

def get_first(target: dict):
    key = list(target.keys())[0]
    value = list(target.values())[0]
    if isinstance(value, str):
        value = '"' + value + '"'
    return key, value

class DBHandler:
    def __init__(self, location: str):
        if location != None:
            self.con = sqlite3.connect(location, isolation_level=None)
            self.cur = self.con.cursor()

    def execute(self, command):
        self.cur.execute(command)
        result = str(self.cur.fetchone())
        return result
    
    def handle(self, data: dict):
        type = data['type']
        target = data['target']

        result = 'None'

        if type == 'get':
            pk = data['pk']
            result = self._get(target, pk)
        elif type == 'insert':
            item = data['item']
            self._insert(target, item)
        elif type == 'update':
            pk = data['pk']
            item = data['item']
            self._update(target, pk, item)
        elif type == 'delete':
            pk = data['pk']
            self._delete(target, pk)
        
        return result

    def _get(self, target: str, pk: dict):
        pk_key, pk_value = get_first(pk)

        command = f'SELECT * FROM {target} WHERE {pk_key} = {pk_value}'
        result = self.execute(command)
        return result

    def _insert(self, target: str, item: dict):
        values = []
        for value in item.values():
            if isinstance(value, str):
                value = '"' + value + '"'
            elif isinstance(value, int):
                value = str(value)
            values.append(value)
        values = '(' + ', '.join(values) + ')'

        command = f'INSERT INTO {target} VALUES{values}'
        self.execute(command)

    def _update(self, target: str, pk: dict, item: dict):
        pk_key, pk_value = get_first(pk)
        key, value = get_first(item)

        command = f'UPDATE {target} SET {key} = {value} WHERE {pk_key} = {pk_value}'
        result = self.execute(command)
        return result

    def _delete(self, target: str, pk: dict):
        pk_key, pk_value = get_first(pk)

        command = f'DELETE FROM {target} WHERE {pk_key} = {pk_value}'
        self.execute(command)