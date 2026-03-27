from flask import Flask

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
                margin-top: 120px;
                font-weight: bold;
            }

            p {
                font-size: 22px;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                padding: 16px 35px;
                margin: 10px;
                font-size: 20px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                transition: 0.3s;
            }

            .whatsapp {
                background: #25D366;
            }

            .contact {
                background: #007BFF;
            }

            .btn:hover {
                transform: scale(1.1);
                opacity: 0.9;
            }
        </style>
    </head>

    <body>

        <h1>🔥 LOGAN EFB STORE 🔥</h1>
        <p>Buy • Sell • Trade Accounts</p>

        <a class="btn whatsapp"
        href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
        Join WhatsApp Group 🚀
        </a>

        <br>

        <a class="btn contact"
        href="https://wa.me/231887935222?text=Hi%2C%20I%20saw%20your%20store%20and%20I%E2%80%99m%20interested%20in%20your%20services.%20Can%20you%20guide%20me%20on%20how%20to%20proceed%3F">
        Contact Admin 💬
        </a>

    </body>
    </html>
    '''

app.run(host="0.0.0.0", port=3000)