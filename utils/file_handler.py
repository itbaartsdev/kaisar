from utils.logger import logger
import os

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        logger(f"Error membaca file {filename}: {str(e)}", 'error')
        return []

def save_to_file(filename, data):
    """Fungsi untuk menyimpan data ke file"""
    try:
        # Pastikan folder config ada
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Tulis data ke file
        with open(filename, 'a') as f:
            f.write(data)
        logger(f"Data berhasil disimpan ke {filename}", 'success')
    except Exception as e:
        logger(f"Error menyimpan ke file {filename}: {str(e)}", 'error') 