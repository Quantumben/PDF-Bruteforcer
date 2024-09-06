from PyPDF2 import PdfReader
import time
import os

def unlock_pdf(pdf_file, password_list_file):
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf)
        
        if not reader.is_encrypted:
            print("The PDF is not encrypted.")
            return
        
        with open(password_list_file, 'r') as passwords:
            for line in passwords:
                password = line.strip()
                try:
                    if reader.decrypt(password):
                        print(f"Success! The password is: {password}")
                        return
                    else:
                        print(f"Attempt with password {password} failed.")
                except Exception as e:
                    print(f"Error with password {password}: {str(e)}")
            print("Password not found in the file.")

# Example usage
current_directory = os.getcwd()
pdf_file = os.path.join(current_directory, 'Statement-604XXXX345-030920240643164316-288338.pdf')  # PDF file in the current directory
password_list_file = os.path.join(current_directory, 'possible_phone_numbers.txt')  # Password file in the current directory

start_time = time.time()
unlock_pdf(pdf_file, password_list_file)
end_time = time.time()

print(f"Time taken: {end_time - start_time:.2f} seconds")
