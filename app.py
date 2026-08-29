from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CodSoft DevOps Task 1</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f4f4f4;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
            }

            h1 {
                color: #333;
            }

            p {
                font-size: 18px;
                color: #555;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Dockerized Web Application</h1>
            <p>CodSoft DevOps Internship - Git & GitHub Workflow</p>
            <p>Merge conflict successfully resolved!</p>
            <p>Application successfully managed using Git and GitHub!</p>
            <p>CI/CD Pipeline deployed with GitHub Actions</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)