from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>LOGAN EFB STORE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
    text-align: center;
}

/* HERO SECTION */
.hero {
    padding: 80px 20px;
}

.hero h1 {
    font-size: 50px;
    color: #00ffd5;
    text-shadow: 0 0 20px #00ffd5;
}

/* BUTTONS */
.btn {
    display: inline-block;
    padding: 15px 25px;
    margin: 10px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}

.whatsapp {
    background: #25D366;
    color: white;
}

.group {
    background: #128C7E;
    color: white;
}

.contact {
    background: #007bff;
    color: white;
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.05);
    margin: 20px;
    padding: 20px;
    border-radius: 15px;
}

/* SECTION */
.section {
    padding: 40px 20px;
}
</style>
</head>

<body>

<div class="hero">
    <h1>🔥 LOGAN EFB STORE 🔥</h1>
    <p>Buy • Sell • Trade • Exchange eFootball Accounts</p>

    <!-- JOIN GROUP BUTTON -->
    <a class="btn group" href="https://chat.whatsapp.com/FnWdfggfsAgJbwDWhwIZuk?mode=gi_t">
        Join WhatsApp Group 🚀
    </a>

    <!-- CONTACT ADMIN -->
    <a class="btn contact" href="https://wa.me/231771896734?text=Hello 🤍, I came across your EFB Store 🩵 and I’m really interested 🤗. Could you guide me?">
        Contact Admin 💬
    </a>
</div>

<!-- PRODUCTS -->
<div class="section">
    <h2>💰 Our Products</h2>

    <div class="card">
        <h3>Pro Account 🔥</h3>
        <p>High rated squad</p>
        <h2>$10</h2>
        <a class="btn whatsapp" href="https://wa.me/231771896734?text=I want to buy Pro Account">
            Buy via WhatsApp 💬
        </a>
    </div>

    <div class="card">
        <h3>Starter Account ⚽</h3>
        <p>Good for beginners</p>
        <h2>$5</h2>
        <a class="btn whatsapp" href="https://wa.me/231771896734?text=I want to buy Starter Account">
            Buy via WhatsApp 💬
        </a>
    </div>

    <div class="card">
        <h3>Coins Package 🪙</h3>
        <p>Cheap eFootball coins</p>
        <h2>$2+</h2>
        <a class="btn whatsapp" href="https://wa.me/231771896734?text=I want to buy coins">
            Buy Coins 💬
        </a>
    </div>
</div>

<!-- ABOUT -->
<div class="section">
    <h2>⚽ ABOUT US</h2>
    <p>🏆 Active eFootball trading market</p>
    <p>👥 Friendly and active members</p>
    <p>⚡ Fast response from admins</p>
    <p>🛡️ Safe marketplace for everyone</p>
</div>

<!-- SERVICES -->
<div class="section">
    <h2>🔥 WHAT WE OFFER</h2>
    <p>🪙 Cheap eFootball coins</p>
    <p>👤 Buy • Sell • Swap accounts</p>
    <p>⚡ Instant delivery</p>
    <p>🛡️ Safe and trusted deals</p>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)