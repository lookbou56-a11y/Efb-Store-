from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>EFB Store</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(270deg, #0f0c29, #302b63, #24243e);
                background-size: 600% 600%;
                animation: gradient 10s ease infinite;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            @keyframes gradient {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 15px 25px;
                background: #25D366;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>🔥 LOGAN EFB STORE 🔥</h1>
            <p>Buy • Sell • Trade Accounts</p>
            <a href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk?mode=gi_t">
                Join WhatsApp Group 🚀
            </a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()