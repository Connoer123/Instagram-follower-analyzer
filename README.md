# Instagram-follower-analyzer (Safe ZIP-Based Version)

This script helps you compare your Instagram followers and following without giving your password or logging into any app. All data is handled locally using the ZIP file you download directly from Instagram.

It gives you a .txt file listing the people you follow who don’t follow you back, so you can clean up your following list safely.

---

## Instructions

### 1. Get your data from Instagram

Go to: [https://www.instagram.com/download/request](https://www.instagram.com/download/request)

- Choose **"Some of your information"**
- Select only **"Following and Followers"**
- Format: **JSON**
- Delivery method: **Download to device**

---

### 2. After Instagram sends your data
- Download the ZIP file to your computer

---

### 3. Run the script
- Open 'compare_followers.py' in your Python editor 
- Run the script

When prompted, enter the full path to your Instagram ZIP file:

/Users/yourname/Desktop/instagram-yourname-2025-08-01.zip

The script will generate a file called:not_following_back.txt

---

## Notes
- Instagram’s data export is not real-time, if you recently followed or unfollowed people, wait a few hours before downloading your ZIP.
- No password, login, or API is required. Your data stays local and private on your own device.

