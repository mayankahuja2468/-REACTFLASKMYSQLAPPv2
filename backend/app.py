from flask import Flask, request, send_file, jsonify, Response
from flask_cors import CORS
import mysql.connector
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)



@app.route('/calculate', methods=['POST'])
def test_response():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'database',
        'port': '3306',
        'database': 'commics'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    file = request.files['file']
    name = request.form.get('name')
    power = request.form.get('power')
    image = file.read()
    cursor.execute('''INSERT INTO dc (name,power,image) VALUES (%s,%s,%s)''', (name,power,image))
    cursor.execute('SELECT * FROM dc')
    results = [{'name1':name1,'power1':power1,'image1':image1} for (name1,power1,image1) in cursor]
    cursor.close()
    connection.close()
    # JSONify response
    str1 = "Listed Powers are " + str(len(results)) + " "
    files = [] 
    for item in results:
        #name1_string = item['name1']
        power1_string = str(item['power1'])
        str1 = str1 + power1_string
        #file1 = converitem['image1'],mimetype='image/jpeg')
        #files.append(file1)
        files.append(item['image1'])
    
    

    # Add Access-Control-Allow-Origin header to allow cross-site request
    #str = results[0]['Lancelot'] + ""

    # Mozilla provides good references for Access Control at:
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

    #image.write(files[0])
    image1 = Image.open(BytesIO(files[0]))
    type1 = str(type(image1))
    str1 = str1 + " " + type1

    return Response(files[0], mimetype='image/jpeg')

app.run()