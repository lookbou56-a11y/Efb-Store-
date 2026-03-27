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
                font-family: Arial;
                text-align: center;
                color: white;
                height: 100vh;

                background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1e3c72);
                background-size: 400% 400%;
                animation: gradientBG 10s ease infinite;
            }

            @keyframes gradientBG {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            h1 {
                font-size: 55px;
                margin-top: 100px;
                font-weight: bold;
            }

            p {
                font-size: 22px;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                padding: 15px 30px;
                margin: 10px;
                font-size: 18px;
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

            .payment {
                background: #6