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
            text-align: center;
            color: white;
            background: linear-gradient(135deg, #0f2027, #203a43, #000000);
        }

        .container {
            padding: 40px 20px;
        }

        h1 {
            font-size: 60px;
            font-weight: bold;
            color: #00ffcc;
            text-shadow: 0 0 25px #00ffcc;
            margin-bottom: 10px;
        }

        p {
            font-size: 20px;
            color: #ccc;
        }

        .btn {
            display: inline-block;
            margin: 15px;
            padding: 15px 30px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }

        .whatsapp {
            background: #25D366;
            color: white;
        }

        .contact {
            background: #007bff;
            color: white;
        }

        h2 {
            margin-top: 50px;
            font-size: 28px;
        }

        .service {
            width: 90%;
            margin: 15px auto;
            padding: 20px;
            background: #111;
            border-radius: 12px;
            font-size: 20px;
            box-shadow: 0 0 15px rgba(0,255,204,0.3);
        }

    </style>
    </head>

    <body>

    <div class="container">
        <h1>🔥 LOGAN EFB STORE 🔥</h1>
        <p>Buy • Sell • Trade • Exchange eFootball Accounts</p>

        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
            Join WhatsApp 🚀
        </a>

        <br>

        <a class="btn contact" href="https://wa.me/231887935222?text=Hi%20I%20saw%20your%20store%20and%20I%E2%80%99m%20interested%20in%20your%20services.%20Can%20you%20guide%20me%20on%20how%20to%20proceed%3F">
            Contact Admin 💬
        </a>

        <h2>💰 Our Services</h2>

        <div class="service">✔ Buy Accounts</div>
        <div class="service">✔ Sell Accounts</div>
        <div class="service">✔ Safe Trading</div>
        <div class="service">🔄 Exchange Accounts</div>

    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)