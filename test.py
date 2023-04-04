from flask import Flask, request
from pprint import pprint
app = Flask(__name__)

# --------------------- Send message ----------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        # send the message to the other computer
        pprint(message)
        return 'Message sent: ' + message
    else:
        return '''
            <form method="post">
                <input type="text" name="message">
                <button type="submit">Send</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# --------------------- Upload a file function ----------------------------------
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files['file']
#         # do something with the file, for example save it to disk
#         file.save('uploads/' + file.filename)
#         return 'File uploaded successfully'
#     else:
#         return '''
#             <form method="post" enctype="multipart/form-data">
#                 <input type="file" name="file">
#                 <button type="submit">Upload</button>
#             </form>
#         '''

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)