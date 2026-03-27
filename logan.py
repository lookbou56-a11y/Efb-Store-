from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <title>LOGAN EFB STORE</title>

    <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        color: white;
        text-align: center;

        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.9)),
        url('https://i.imgur.com/8Km9tLL.jpeg');

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .container {
        padding: 60px 20px;
    }

    h1 {
        font-size: 55px;
        color: #00ffcc;
        text-shadow: 0 0 25px #00ffcc;
        margin-bottom: 10px;
    }

    p {
        font-size: 18px;
        opacity: 0.9;
    }

    .btn {
        display: inline-block;
        padding: 14px 25px;
        margin: 10px;
        border-radius: 10px;
        text-decoration: none;
        font-size: 16px;
        color: white;
    }

    .whatsapp {
        background: #25D366;
    }

    .contact {
        background: #007BFF;
    }

    .section {
        margin-top: 40px;
    }

    .card {
        background: rgba(0,0,0,0.6);
        padding: 20px;
        margin: 15px auto;
        width: 85%;
        border-radius: 12px;
        box-shadow: 0 0 15