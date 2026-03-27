from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>EFB Store</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                font-family: Arial;
                background: linear-gradient(135deg, #0f0f0f, #1a0033);
                color: white;
                text-align: center;
            }

            .hero {
                padding: 80px 20px;
            }

            .hero h1 {
                font-size: 50px; /* BIG TEXT 🔥 */
                margin-bottom: 10px;
                color: #00ffcc;
            }

            .hero p {
                font-size: 18px;
                color: #ccc;
            }

            .btn {
                display: inline-block;
                padding: 14px 25px;
                background: #25D366;
                color: white;
                text-decoration: none;
                border-radius: 12px;
                margin-top: 20px;
                font-size: 18px;
                transition: 0.3s;
            }

            .btn:hover {
                background: #1ebd5a;
                transform: scale(1.1);
            }

            .section {
                padding: 40px 20px;
            }

            .cards {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
            }

            .card {
                background: #1a1a1a;
                padding: 20px;
                margin: 10px;
                border-radius: 15px;
                width: 250px;
                box-shadow: 0 0 15px rgba(0,255,200,0.2);
            }

            footer {
                margin-top: 30px;
                padding: 15px;
                background: #111;
                color: gray;
            }
        </style>
    </head>

    <body>

        <!-- HERO SECTION -->
        <div class="hero">
            <h1>🔥 LOGAN EFB STORE 🔥</h1>
            <p>Buy • Sell • Trade eFootball Accounts</p>

            <a class="btn" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
                Join WhatsApp 🚀
            </a>
        </div>

        <!-- SERVICES -->
        <div class="section">
            <h2>💰 Our Services</h2>
            <div class="cards">
                <div class="card">✔ Buy Accounts</div>
                <div class="card">✔ Sell Accounts</div>
                <div class="card">✔ Safe Trading</div>
                <div class="card">✔ Account Upgrade</div>
            </div>
        </div>

        <!-- FEATURES -->
        <div class="section">
            <h2>🔥 Why Choose Us?</h2>
            <div class="cards">
                <div class="card">⚡ Fast Deals</div>
                <div class="card">🔒 Trusted Community</div>
                <div class="card">🌍 Worldwide Access</div>
                <div class="card">💬 24/7 Support</div>
            </div>
        </div>

        <!-- CALL TO ACTION -->
        <div class="section">
            <h2>📲 Join Our Group Now</h2>
            <p>Don’t miss deals and updates</p>

            <a class="btn" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
                Enter WhatsApp Group 🔥
            </a>
        </div>

        <footer>
            © 2026 Logan EFB Store | Built by You 😎
        </footer>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)