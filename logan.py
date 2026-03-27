from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>LOGAN EFB STORE</title>

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                text-align: center;
                color: white;
                height: 100vh;

                background: linear-gradient(-45deg, #1e3c72, #2a5298, #00c6ff, #0072ff);
                background-size: 400% 400%;
                animation: bgMove 10s ease infinite;
            }

            @keyframes bgMove {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            h1 {
                font-size: 60px;
                margin-top: