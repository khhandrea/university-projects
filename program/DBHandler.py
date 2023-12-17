import sqlite3
from typing import Tuple

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
    
    def handle(self, data: dict):
        type = data['type']
        target = data['target']

        result = 'None'

        if type == 'get':
            pk = data['pk']
            result = self._get(target, pk)
        elif type == 'insert':
            item = data['item']
            result = self._insert(target, item)
        elif type == 'update':
            pk = data['pk']
            item = data['item']
            result = self._update(target, pk, item)
        elif type == 'delete':
            pk = data['pk']
            result = self._delete(target, pk)
        
        return result
    
    def execute(self, commands: list) -> str:
        for command in commands:
            self.cur.execute(command)
        result = str(self.cur.fetchone())
        return result

    def _get(self, target: str, pk: dict):
        pk_key, pk_value = get_first(pk)

        self.cur.execute(f'SELECT * FROM {target} WHERE {pk_key} = {pk_value}')
        result = str(self.cur.fetchone())

        return result

    def _insert(self, target: str, item: dict) -> str:
        values = []
        for value in item.values():
            if isinstance(value, str):
                value = '"' + value + '"'
            elif isinstance(value, int):
                value = str(value)
            values.append(value)
        values = '(' + ', '.join(values) + ')'

        condition = []
        for key in item:
            if isinstance(item[key], str):
                condition.append(f"{key} = '{item[key]}'")
            else:
                condition.append(f'{key} = {item[key]}')
        condition = ' AND '.join(condition)
        self.cur.execute(f'INSERT INTO {target} VALUES{values}')
        self.cur.execute(f'SELECT * FROM {target} WHERE {condition}')
        result = str(self.cur.fetchone())
        print(result)

        return result

    def _update(self, target: str, pk: dict, item: dict) -> str:
        pk_key, pk_value = get_first(pk)
        key, value = get_first(item)

        if isinstance(pk_value, str):
            pk_value = f"'{pk_value}'"
        
        self.cur.execute(f'UPDATE {target} SET {key} = {value} WHERE {pk_key} = {pk_value}')
        self.cur.execute(f'SELECT * FROM {target} WHERE {pk_key} = {pk_value}')
        result = str(self.cur.fetchone())

        return result

    def _delete(self, target: str, pk: dict) -> str:
        pk_key, pk_value = get_first(pk)

        if isinstance(pk_value, str):
            pk_value = f"'{pk_value}'"
        
        self.cur.execute(f'SELECT * FROM {target} WHERE {pk_key} = {pk_value}')
        result = str(self.cur.fetchone())
        self.cur.execute(f'DELETE FROM {target} WHERE {pk_key} = {pk_value}')

        return result
        