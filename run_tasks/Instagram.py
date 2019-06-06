from botocore.vendored import requests
import boto3

class Instagram:

    def __init__(self, url, page_id, token, fb_token, database, database_table):
        self.url = url
        self.page_id = page_id
        self.token = token
        self.fb_token = fb_token
        self.database = database
        self.database_table = database_table

    def load_data(self):
        response = requests.post(f'{self.url}',
                                 data={'page_id': f'{self.page_id}',
                                       'fb_token': f'{self.fb_token}'},
                                 headers={'Authorization': f'Token {self.token}'})
        database = boto3.resource(self.database)
        table = database.Table(self.database_table)
        for post in response.json():
            table.put_item(Item=post)
