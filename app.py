from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3
import json
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        conn = sqlite3.connect("nodes.db")
        cursor = conn.execute("SELECT NODES FROM BLOCKS")
        conn.commit()
        songs_as_dict = []

        for song in cursor.fetchall():

            songs_as_dict.append(song)
        print(songs_as_dict)
        return {'Result': json.dumps(songs_as_dict)}

    def post(self):
        print('I am inside post')
        req_data = request.get_json()
        ip_address = req_data['IP']
        aadhar_number = req_data['Aadhar']
        vote = req_data['Vote']
        print(ip_address,aadhar_number,vote)
        final = ip_address + aadhar_number + vote
        print(final)
        conn = sqlite3.connect("nodes.db")

        # Storing new block
        conn.execute("INSERT INTO BLOCKS VALUES (?,?)", (1,str(final)))
        conn.commit()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)