from PIL import Image, ImageDraw, ImageFont
import qrcode

NAME = "Nguyễn Văn A"
CLASS_NAME = "Lớp 9A"
YEAR = "Niên khóa 2021–2025"
QR_LINK = "https://your-github-name.github.io/your-repo-name/"

qr = qrcode.make(QR_LINK)
qr = qr.resize((220, 220))

card = Image.new("RGB", (700, 1000), "#FDF6EC")
draw = ImageDraw.Draw(card)

try:
    font_title = ImageFont.truetype("arial.ttf", 48)
    font_text = ImageFont.truetype("arial.ttf", 28)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

draw.text((200, 60), "KỶ YẾU", fill="#3A3A3A", font=font_title)
draw.text((160, 150), NAME, fill="#000000", font=font_title)
draw.text((280, 220), CLASS_NAME, fill="#000000", font=font_text)
draw.text((200, 260), YEAR, fill="#000000", font=font_text)

draw.text(
    (120, 360),
    "Chúc bạn luôn tự tin,\nkiên trì và thành công\ntrên con đường phía trước!",
    fill="#333333",
    font=font_text
)

draw.text((210, 720), "Quét QR để xem kỷ yếu", fill="#000000", font=font_text)
card.paste(qr, (240, 760))

card.save("thiep_ky_yeu.png")
print("Đã tạo thiệp: thiep_ky_yeu.png")
