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
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
            }

            h1 {
                font-size: 65px;
                margin-top: 80px;
                color: #00ffc3;
                text-shadow: 0 0 20px #00ffc3;
            }

            p {
                font-size: 20px;
                color: #ccc;
            }

            .btn {
                display: inline-block;
                margin: 15px;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                transition: 0.3s;
                box-shadow: 0 0 10px rgba(0,0,0,0.3);
            }

            .whatsapp {
                background: #25D366;
            }

            .admin {
                background: #0084ff;
            }

            .btn:hover {
                opacity: 0.8;
            }

            .services {
                margin-top: 60px;
            }

            .services h2 {
                font-size: 28px;
                margin-bottom: 20px;
            }

            .card {
                background: #111;
                margin: 15px auto;
                padding: 15px;
                width: 80%;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0,255,195,0.2);
                font-size: 18px;
            }

        </style>
    </head>

    <body>

        <h1>🔥 LOGAN EFB STORE 🔥</h1>
        <p>Buy • Sell • Trade eFootball Accounts</p>

        <!-- Buttons -->
        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
            Join WhatsApp Group 🚀
        </a>

        <br>

        <a class="btn admin" href="https://wa.me/231887935222?text=Hi%20I%20saw%20your%20store%20and%20I%E2%80%99m%20interested%20in%20your%20services.%20Can%20you%20guide%20me%20on%20how%20to%20proceed%3F">
            Contact Admin 💬
        </a>

        <!-- Services Section -->
        <div class="services">
            <h2>💰 Our Services</h2>

            <div class="card">✔ Buy Accounts</div>
            <div class="card">✔ Sell Accounts</div>
            <div class="card">✔ Safe Trading</div>
        </div>

    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)