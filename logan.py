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

                background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.9)),
                url('https://images.unsplash.com/photo-1555949963-aa79dcee981c');

                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }

            /* HERO SECTION (FULL SCREEN) */
            .hero {
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
            }

            h1 {
                font-size: 70px;
                margin: 0;
                color: #00ffe1;
                text-shadow: 0 0 20px #00ffe1, 0 0 40px #00ffe1;
            }

            p {
                font-size: 22px;
                margin: 15px 0;
                color: #ccc;
            }

            .btn {
                margin: 10px;
                padding: 15px 35px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                display: inline-block;
                transition: 0.3s;
            }

            .whatsapp {
                background: #25D366;
            }

            .admin {
                background: #007bff;
            }

            .btn:hover {
                transform: scale(1.1);
            }

            /* SERVICES SECTION */
            .services {
                padding: 40px 0;
                text-align: center;
            }

            .services h2 {
                font-size: 30px;
                margin-bottom: 20px;
            }

            .box {
                background: rgba(0,0,0,0.6);
                margin: 10px auto;
                padding: 15px;
                width: 85%;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,255,200,0.3);
                font-size: 18px;
            }
        </style>
    </head>

    <body>

        <!-- BIG FIRST VIEW -->
        <div class="hero">
            <h1>🔥 LOGAN EFB STORE 🔥</h1>
            <p>Buy • Sell • Trade • Exchange eFootball Services</p>

            <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk?mode=gi_t">
                Join WhatsApp 🚀
            </a>

            <a class="btn admin" href="https://wa.me/231887935222?text=Hello%20🤍,%20I%20came%20across%20your%20EFB%20Store%20🩵%20and%20I’m%20really%20interested%20in%20your%20services%20🤗.%20Could%20you%20please%20guide%20me%20on%20how%20to%20get%20started?">
                Contact Admin 💬
            </a>
        </div>

        <!-- SERVICES BELOW -->
        <div class="services">
            <h2>💰 Our Services</h2>

            <div class="box">✔ Buy Accounts</div>
            <div class="box">✔ Sell Accounts</div>
            <div class="box">✔ Safe Trading</div>
            <div class="box">✔ Exchange Accounts</div>
            <div class="box">✔ Buy Coins 💰</div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)