import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets this automatically
    app.run(host="0.0.0.0", port=port)
# (Use the exact Flask script I gave above)
