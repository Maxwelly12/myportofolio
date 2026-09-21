Nama    : Maxwelly F.H. Simatupang
NPM     : 2506584294
Kelas   : PBP F

Website portofolio pribadi yang menampilkan profil diri (About Me), riwayat pengalaman (Experience), dan lain
sebagainya. Proyek ini dibuat sebagai media untuk memperkenalkan diri secara profesional.

📋 Fitur
About Me     - Perkenalan singkat, deskripsi diri, dan keahlian (skills)

Experience   - Daftar pengalaman kerja, volunter, atau organisasi yang pernah diikuti

Model Experience didefinisikan di main/models.py dengan field berikut:
-id (UUIDField) : primary key unik.
-title (CharField) : .
-description (TextField) : deskripsi/keterangan pengalaman kerja.
-category (CharField dengan choices) : jenis jenjang pekerjaan, seperti, interneship, volunteer, research, dan lain sebagainya.
-thumbnail(URLField)
-started_at (DateTimeField, default hari ini) : tanggal mulai pekerjaan.
-ended_at (DateTimeField, opsional) — tanggal selesai pekerjaan. 
-is_ongoing (property) — otomatis bernilai True jika ended_at masih kosong. 

Education    - Riwayat pendidikan diri dan disajikan dalam bentuk timeline dengan pengalaman atau pengetahuan yang didapatkan 
dari pendidikan tersebut. 

Model Education didefinisikan di main/models.py dengan field berikut:
-id (UUIDField) : primary key unik.
-institution_name (CharField) : nama institusi pendidikan.
-description (TextField) : deskripsi/keterangan pendidikan.
-category (CharField dengan choices) : jenis jenjang pendidikan, middle, high_school, bachelor.
-started_at (DateTimeField, default hari ini) : tanggal mulai pendidikan.
-ended_at (DateTimeField, opsional) — tanggal selesai pendidikan. 
-is_ongoing (property) — otomatis bernilai True jika ended_at masih kosong. 

Selama proses pengembangan fitur education, saya menggunakan Artificial Intelligence, seperti Gemini, Claude, dan lain
sebagainya, sebagai sarana Debugging dan membantu grid timeline.

Testimony    - Testimoni seseorang terhadap saya, baik mengenai pengalaman kerjasama ataupun feedback yang dapat diberikan kepada saya sebagai sarana pandangan orang terhadap saya.

Model Testimony didefinisikan di main/models.py dengan field berikut:
-id (UUIDField) : primary key unik.
-name (CharField) : nama pemberi testimoni.
-description (TextField) : testimoni seseorang terhadap saya.
-message_date (DateTimeField, default hari ini) : tanggal pemberian testimoni

Selama proses pengembangan fitur testimony, saya menggunakan Artificial Intelligence, seperti Gemini, Claude, dan lain
sebagainya, sebagai sarana Debugging.

Prompt yang digunakan dalam pengembangan fitur: 
1. "Bantu saya dalam membuat grid timeline pada section education dan beri saya penjelasan mengenai kode yang diberikan
dalam membantu modifikasi kode di masa  yang akan datang"
2. "Bantu  saya dalam debugging dimana ketika saat saya menjalankan python manage.py shell dan error pada 
Education.object.get(institution_name  =  "Universitas Indonesia")"
3. "Bantu saya dalam debugging dimana testimony yang diberikan tidak masuk kedalam sebuah website tersebut berikanlah beberapa possible masalah"

*Penggunaan AI difokuskan pada  pemahaman kode lebih lanjut yang berguna dalam proses modifikasi kedepannya.*