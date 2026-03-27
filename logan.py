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

                /* YOUR BACKGROUND IMAGE */
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)),
                url('https://i.imgur.com/8Km9tLL.jpeg');
                
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }

            h1 {
                font-size: 60px;
                margin-top: 100px;
                color: #00ffcc;
                text-shadow: 0 0 25px #00ffcc;
            }

            p {
                font-size: 20px;
                color: #ddd;
            }

            .btn {
                display: inline-block;
                margin: 10px;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                transition: 0.3s;
            }

            .whatsapp {
                background: #25D366;
            }

            .admin {
                background: #007bff;
            }

            .btn:hover {
                transform: scale(1.05);
            }

            .services {
                margin-top: 60px;
            }

            .services h2 {
                font-size: 30px;
                margin-bottom: 20px;
            }

            .box {
                background: rgba(0,0,0,0.6);
                margin: 10px auto;
                padding: 15px;
                width: 80%;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,255,200,0.3);
            }
        </style>
    </head>

    <body>

        <h1>🔥 LOGAN EFB STORE 🔥</h1>

        <p>Buy • Sell • Trade • Exchange eFootball Services</p>

        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk?mode=gi_t">
            Join WhatsApp Group 🚀
        </a>

        <br>

        <a class="btn admin" href="https://wa.me/231887935222?text=Hello%20🤍,%20I%20came%20across%20your%20EFB%20Store%20🩵%20and%20I’m%20really%20interested%20in%20your%20services%20🤗.%20Could%20you%20please%20guide%20me%20on%20how%20to%20get%20started?">
            Contact Admin 💬
        </a>

        <div class="services">
            <h2>💰 Our Services</h2>

            <div class="box">✔ Buy eFootball Accounts</div>
            <div class="box">✔ Sell eFootball Accounts</div>
            <div class="box">✔ Safe Trading</div>
            <div class="box">✔ Exchange Accounts</div>
            <div class="box">✔ Buy eFootball Coins 💰</div>
            <div class="box">✔ Account Upgrade Services 🚀</div>
            <div class="box">✔ Squad Building Help ⚽</div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)