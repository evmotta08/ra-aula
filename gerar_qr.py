"""Gera o QR code da página.
Uso: python gerar_qr.py https://seu-site.netlify.app
Cria qr_aula.png (preto no branco, grande, bom para projetor)."""
import sys
import qrcode

if len(sys.argv) != 2:
    sys.exit("Informe a URL: python gerar_qr.py https://seu-site.netlify.app")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=24, border=4)
qr.add_data(sys.argv[1])
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("qr_aula.png")
print("Salvo: qr_aula.png")
