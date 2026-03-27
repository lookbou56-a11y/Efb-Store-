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
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #000000, #0f2027, #000000);
            color: white;
            text-align: center;
        }

        .container {
            padding: 60px 20px;
        }

        /* 🔥 BIG FRONT TITLE */
        h1 {
            font-size: 80px;
            font-weight: 900;
            color: #00ffd5;
            text-shadow: 0 0 35px #00ffd5;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 22px;
            color: #ccc;
            margin-bottom: 35px;
        }

        /* BUTTONS */
        .btn {
            display: inline-block;
            margin: 12px;
            padding: 18px 40px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            text-decoration: none;
            transition: 0.3s;
        }

        .btn:hover {
            transform: scale(1.08);
        }

        .whatsapp {
            background: #25D366;
            color: white;
        }

        .contact {
            background: #007bff;
            color: white;
        }

        /* SERVICES */
        .services {
            margin-top: 60px;
        }

        .services h2 {
            font-size: 32px;
            margin-bottom: 20px;
        }

        .card {
            width: 95%;
            margin: 15px auto;
            padding: 25px;
            border-radius: 15px;
            font-size: 22px;

            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(8px);

            box-shadow: 0 0 20px rgba(0,255,200,0.2);
        }

        /* FLOAT BUTTON */
        .float {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #25D366;
            color: white;
            padding: 18px;
            border-radius: 50%;
            font-size: 22px;
            text-decoration: none;
            box-shadow: 0 0 15px #25D366;
        }

    </style>
    </head>

    <body>

    <div class="container">

        <h1>🔥 LOGAN EFB STORE 🔥</h1>

        <div class="subtitle">
            Buy • Sell • Trade • Exchange eFootball Accounts
        </div>

        <!-- WhatsApp Group -->
        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
            Join WhatsApp 🚀
        </a>

        <br>

        <!-- Admin Contact with your styled message -->
        <a class="btn contact" href="https://wa.me/231887935222?text=Hello%20%F0%9F%A4%8D%2C%20I%20came%20across%20your%20EFB%20Store%20%F0%9F%A9%B5%20and%20I%E2%80%99m%20really%20interested%20in%20your%20services%20%F0%9F%A4%97.%20Could%20you%20please%20guide%20me%20on%20how%20to%20get%20started%3F">
            Contact Admin 💬
        </a>

        <div class="services">
            <h2>💰 Our Services</h2>

            <div class="card">✔ Buy Accounts</div>
            <div class="card">✔ Sell Accounts</div>
            <div class="card">✔ Safe Trading</div>
            <div class="card">🔄 Exchange Accounts</div>
        </div>

    </div>

    <!-- Floating WhatsApp -->
    <a class="float" href="https://wa.me/231887935222">💬</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)