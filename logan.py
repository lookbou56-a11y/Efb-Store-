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
                font-size: 50px;
                margin-top: 100px;
                color: #00ffc3;
            }

            p {
                font-size: 18px;
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
        </style>
    </head>

    <body>

        <h1>🔥 LOGAN EFB STORE 🔥</h1>
        <p>Buy • Sell • Trade eFootball Accounts</p>

        <!-- WhatsApp Group -->
        <a class="btn whatsapp" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk">
            Join WhatsApp Group 🚀
        </a>

        <br>

        <!-- Admin Contact -->
        <a class="btn admin" href="https://wa.me/231887935222?text=Hi%20I%20saw%20your%20store%20and%20I%E2%80%99m%20interested%20in%20your%20services.%20Can%20you%20guide%20me%20on%20how%20to%20proceed%3F">
            Contact Admin 💬
        </a>

    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)