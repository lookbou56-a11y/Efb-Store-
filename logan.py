from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Logan EFB Store</title>

        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0a0f1f, #111827, #1f2937);
                color: white;
                text-align: center;
            }

            h1 {
                font-size: 75px;
                margin-top: 80px;
                font-weight: 900;
                letter-spacing: 2px;
                color: #00ffc3;
                text-shadow: 0 0 25px #00ffc3, 0 0 40px rgba(0,255,195,0.4);
            }

            p {
                font-size: 20px;
                color: #cbd5e1;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                margin: 10px;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 12px;
                text-decoration: none;
                color: white;
                transition: 0.3s;
                box-shadow: 0 5px 15px rgba(0,0,0,0.4);
            }

            .whatsapp {
                background: #25D366;
            }

            .admin {
                background: #3b82f6;
            }

            .btn:hover {
                transform: scale(1.05);
                opacity: 0.9;
            }

            .services {
                margin-top: 70px;
            }

            .services h2 {
                font-size: 30px;
                margin-bottom: 20px;
                color: #facc15;
            }

            .card {
                background: rgba(255,255,255,0.05);
                margin: 12px auto;
                padding: 15px;
                width: 80%;
                border-radius: 14px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 20px rgba(0,255,195,0.1);
                font-size: 18px;
            }

        </style>
    </head>

    <body>

        <h1>🔥 LOGAN EFB STORE 🔥</h1>
        <p>Buy • Sell • Trade • Exchange eFootball Accounts</p>

        <!-- Buttons -->
        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
            Join WhatsApp Group 🚀
        </a>

        <br>

        <a class="btn admin" href="https://wa.me/231887935222?text=Hi%20I%20saw%20your%20store%20and%20I%E2%80%99m%20interested%20in%20your%20services.%20Can%20you%20guide%20me%20on%20how%20to%20proceed%3F">
            Contact Admin 💬
        </a>

        <!-- Services -->
        <div class="services">
            <h2>💰 Our Services</h2>

            <div class="card">✔ Buy Accounts</div>
            <div class="card">✔ Sell Accounts</div>
            <div class="card">✔ Safe Trading</div>
            <div class="card">🔄 Exchange Accounts</div>
        </div>

    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)