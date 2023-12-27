from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resumes():
    job_description = request.form['job_description']
    with open("/Users/nitin/Documents/IBAB/techfest/job_des.txt", "w") as file:
        file.write(job_description)
    print("Job description saved.")

    # Handle uploaded files
    destination_folder = "resumes"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file in request.files.getlist('resumes'):
        file_path = os.path.join(destination_folder, file.filename)
        file.save(file_path)
        print(f"Uploaded: {file_path}")

    return "Files uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)
