
#Mengelompokkan nilai mahasiswa ke dalam beberapa Grade
nilai_mahasiswa = [90, 78, 70, 75, 68, 40, 45, 80, 98, 60, 54, 75, 83, 63, 40]
for nilai in nilai_mahasiswa:
    if nilai >= 85:
        Grade = "A" 
    elif nilai >= 75:
        Grade = "B"
    elif nilai >= 65:
        Grade = "C"
    elif nilai >= 50:
        Grade = "D"
    else: Grade = "E"
    print (f"Nilai {nilai} -> Grade {Grade}")

#Distribusi masing-masing Grade 
nilai_mahasiswa = [90, 78, 70, 75, 68, 40, 45, 80, 98, 60, 54, 75, 83, 63, 40]

distribusi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

for nilai in nilai_mahasiswa:
    if nilai >= 85: #Untuk setiap nilai yang di atas 85
        distribusi["A"] += 1 #tambahkan 1 pada key "A"
    elif nilai >= 75: #ibid
        distribusi["B"] += 1 
    elif nilai >= 65: #ibid
        distribusi["C"] += 1
    elif nilai >= 50: #ibid
        distribusi["D"] += 1
    else: distribusi["E"] += 1

print (f"Distribusi berdasarkan grade: \n {distribusi}")


#Mengelompokkan nilai dan menghitung total mahasiswa berdasarkan kriteria Lulus/Tidak Lulus
Lulus = []
Tidak_Lulus = []

for nilai in nilai_mahasiswa:
    if nilai >= 65:
        Lulus.append(nilai) #memasukkan nilai di atas 65 ke dalam list Lulus
    else: Tidak_Lulus.append(nilai)  #memasukkan nilai di bawah 65 ke dalam list Tidak_Lulus

print (f"Nilai Lulus:\n{Lulus}")
print (f"Nilai Tidak Lulus:\n{Tidak_Lulus}")

Total_Lulus = len(Lulus) #menghitung total anggota dalam list Lulus
Total_Tidak_Lulus = len(Tidak_Lulus) #menghitung total anggota dalam list Tidak_Lulus

print (f"Total Lulus: {Total_Lulus}")
print (f"Total Tidak Lulus: {Total_Tidak_Lulus}")

# Melihat nilai tertinggi, nilai terendah, dan rata2 nilai (menggunakan max, min, sum, len)
nilai_mahasiswa = [90, 78, 70, 75, 68, 40, 45, 80, 98, 60, 54, 75, 83, 63, 40]
tinggi= max(nilai_mahasiswa)
print (f"Nilai tertingginya adalah:  {tinggi}")
rendah= min(nilai_mahasiswa)
print (f"Nilai terendahnya adalah:  {rendah}")
rata2= sum(nilai_mahasiswa)/len(nilai_mahasiswa)
print (f"Nilai reratanya adalah:  {rata2}")

# Nilai Rata-Rata (menggunakan For Loops)
Total = 0
for x in nilai_mahasiswa:
    Total += x #Tambahkan setiap nilai pada list ke dalam "Total"
print (Total)
print (Total/len(nilai_mahasiswa)) #Total nilai mahasiswa dibagi jumlah nilai pada list nilai mahasiswa
#Nilai Terbesar dan Nilai Terendah (Menggunakan for loops dan conditional statement)
nilai_tertinggi = nilai_mahasiswa[0]  #mengambil nilai pertama pada list sebagai pembanding
nilai_terendah = nilai_mahasiswa[0] #mengambil nilai pertama pada list sebagai pembanding

for nilai in nilai_mahasiswa:
    if nilai > nilai_tertinggi: #membandingkan setiap nilai pada list dengan nilai pertama
        nilai_tertinggi = nilai #apabila tidak lebih tinggi abaikan, apabila lebih tinggi "nilai tertinggi" akan berubah

    if nilai < nilai_terendah: #ibid
        nilai_terendah = nilai

print(f"Nilai terendahnya adalah: {nilai_terendah}")
print(f"Nilai tertingginya adalah: {nilai_tertinggi}")





    
    



