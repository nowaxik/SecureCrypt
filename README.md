# SecureCrypt
SecureCrypt is a simple application for encrypting and decrypting files using a symmetric key. The program uses the Cryptography library to generate keys and encrypt files.

The application consists of two functions: encrypt_file() and decrypt_file(), which are responsible for encrypting and decrypting files, respectively. The function encrypt_file() generates a random key, writes it to the file "key.txt", and then encrypts the contents of the selected file and saves it in the same file. The decrypt_file() function reads the key from the "key.txt" file, decrypts the contents of the selected file and writes it to the same file.

The program also has a function select_file(), which opens a file selection dialog box and returns the path of the selected file. This function is used in the encrypt() and decrypt() functions to select a file to encrypt or decrypt.

The program's graphical interface consists of two buttons on the left side of the window for encrypting and decrypting files. After selecting a file and pressing the "Encrypt file" or "Decrypt file" button, the program performs the corresponding operation and displays a message with the result of the operation.

On the right side of the window is the program's image and its name, displayed in an "image_frame". The program icon is loaded from the "icon.png" file, and the program name is displayed with the program_name label.

The entire graphical interface is created using the Tkinter library. The program window is 500x200 pixels in size and uses two frames: button_frame and image_frame, which are used to place buttons and the program image, respectively.
