# List (Daftar berurutan)
prompts = ["Buatkan email", "Ringkas teks ini", "Terjemahkan ke Inggris", "Generate ke Dokumen"]

# Dictionary (Pasangan Key-Value — Mirip format JSON API)
user_data = {
    "id": 101,
    "name": "Ilham",
    "role": "Guru",
    "is_active": True
}
print(prompts[0])
print(user_data["name"])
print(user_data["role"])

for teacher in prompts:
    print(">", teacher)