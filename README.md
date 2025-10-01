# 🔐 Password Generator (Python)

A simple yet powerful **Password Generator** built with Python.
This script generates strong, random passwords using lowercase letters, uppercase letters, digits, and symbols.
It also supports saving generated passwords (with purpose & account name) to a text file, and automatically copies them to the clipboard for easy use.

---

## ✨ Features

* Generate strong, random passwords of custom length.
* Ensures at least one lowercase, uppercase, digit, and symbol in every password.
* Save generated passwords with:

  * **Purpose** (e.g., Gmail, GitHub, Netflix)
  * **Account/Username**
* Stores all saved passwords in `passwords.txt`.
* Auto-copies generated password to clipboard.

---

## 🛠️ Requirements

* Python 3.7+
* Install dependencies:

```bash
pip install pyperclip
```

---

## 🚀 Usage

Run the script:

```bash
python password_generator.py
```

Example flow:

```
Enter the desired password length (minimum 4): 12
The password is: 9A!xVh5#YkLq
✅ Password copied to clipboard!
Do you want to save the password? (yes/no): yes
Enter the purpose of the password (e.g., email, social media): Gmail
Enter the account/username associated with this password: abd@gmail.com
Password saved to passwords.txt
```

---

## 📂 Saved Passwords

Passwords are stored in `passwords.txt` like this:

```
Gmail | abd@gmail.com | 9A!xVh5#YkLq
GitHub | abd123 | &F7hT!kXrQ
```

---

## 📌 Future Improvements

* Encrypt stored passwords for extra security.
* Add a password retrieval system.
* GUI version using Tkinter or PyQt.

---

## 👨‍💻 Author

Made with Python by **ABD** 🚀
