from flask import Flask, render_template, request, send_file
import qrcode
import io
import base64
from urllib.parse import urlparse

app = Flask(__name__)


def normalize_input_as_url(text):
    """
    If text already has a scheme and netloc, return as-is.
    If it looks like a domain (contains a dot) but no scheme, prepend https://.
    Otherwise return None (treat as plain text).
    """
    if not text:
        return None
    text = text.strip()
    parsed = urlparse(text)
    # Case 1: already absolute (scheme + netloc)
    if parsed.scheme and parsed.netloc:
        return text
    # Case 2: looks like a domain (e.g. "google.com" or "www.google.com")
    if '.' in text and ' ' not in text:
        return 'https://' + text
    # Otherwise it's probably plain text, not a link
    return None


@app.route('/')
def home():
    return "This is a Test"


@app.route('/about')
def ab():
    return render_template('about.html')


@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/qr', methods=['GET', 'POST'])
def qr():
    qr_img = None
    qr_data = None
    normalized_url = None

    if request.method == 'POST':
        qr_data = request.form.get('qr_text')
        normalized_url = normalize_input_as_url(qr_data)
        to_encode = normalized_url if normalized_url else qr_data
        if qr_data:
            qr_img = qrcode.make(qr_data)
            buf = io.BytesIO()
            qr_img.save(buf, 'PNG')
            buf.seek(0)

            if request.form.get('action') == 'download':
                return send_file(
                    buf,
                    mimetype='image/png',
                    as_attachment=True,
                    download_name='QR.png'
                )

            qr_img = base64.b64encode(buf.getvalue()).decode('UTF-8')

    # data = "https://www.google.com"
    # IMG = qrcode.make(data)
    # BUFFER = io.BytesIO()
    # IMG.save(BUFFER, 'PNG')
    # BUFFER.seek(0)

    # QR_IMG = base64.b64encode(BUFFER.getvalue()).decode('UTF-8')

    return render_template('qr.html', qr_data=qr_data, QR_IMG=qr_img, qr_url=normalized_url)


if __name__ == '__main__':
    app.run(debug=True)
