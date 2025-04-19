from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Skyhome - Tạo Tin Đăng</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f6f6f6; }
        input, textarea { width: 100%; padding: 8px; margin-top: 5px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #ccc; }
        label { font-weight: bold; }
        button { padding: 10px 20px; background: #3490dc; color: white; border: none; border-radius: 8px; cursor: pointer; }
        .container { background: white; padding: 30px; border-radius: 12px; max-width: 800px; margin: auto; }
        pre { background: #eee; padding: 15px; border-radius: 8px; white-space: pre-wrap; }
    </style>
</head>
<body>
<div class="container">
    <h2>Tạo Mẫu Tin Đăng Cho Thuê - Skyhome</h2>
    <form method="post">
        <label>Khu vực:</label><input name="ten_khu_vuc">
        <label>Loại phòng:</label><input name="loai_phong">
        <label>Diện tích (m²):</label><input name="dien_tich">
        <label>Địa chỉ:</label><input name="dia_chi">
        <label>Nội thất:</label><textarea name="noi_that"></textarea>
        <label>Ưu điểm:</label><textarea name="uu_diem"></textarea>
        <label>Tiện ích xung quanh:</label><textarea name="tien_ich"></textarea>
        <label>Tên sale:</label><input name="ten_sale">
        <label>SĐT:</label><input name="sdt">
        <button type="submit">Tạo Tin</button>
    </form>
    {% if tin_dang %}
    <h3>Tin Đăng Được Tạo:</h3>
    <pre>{{ tin_dang }}</pre>
    {% endif %}
</div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    tin_dang = ""
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        tin_dang = tao_tin_dang(**data)
    return render_template_string(HTML_FORM, tin_dang=tin_dang)

def tao_tin_dang(ten_khu_vuc, loai_phong, dien_tich, gia_thue, dia_chi, noi_that, uu_diem, tien_ich, ten_sale, sdt):
    tieu_de = f"\U0001f3e1 {loai_phong} | Full NT | {ten_khu_vuc}"
    
    thong_tin = (
        f"**\U0001f4cd Vị trí: {dia_chi}\n"
        f"**\U0001f3e1 Loại phòng: {loai_phong}\n"
        f"**📐 Diện tích: {dien_tich}m²\n"
    )

    noi_dung = (
        f"**✅ Nội thất: {noi_that}\n"
        f"**🌟 Ưu điểm: {uu_diem}\n"
        f"**🏙 Tiện ích: {tien_ich}\n"
        f"\n📞 Liên hệ: {ten_sale} – Skyhome\n"
        f"📲 Zalo/call: {sdt} - Hoặc inbox trực tiếp để được tư vấn\n"
        f"📸 Có video thực tế – hỗ trợ xem nhà nhanh"
    )

    return tieu_de + "\n\n" + thong_tin + "\n" + noi_dung

if __name__ == '__main__':
    app.run(debug=True)
