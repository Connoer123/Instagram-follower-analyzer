import zipfile
import os
import json

# Ask for the ZIP file 
zip_path = input("Enter the full path to your Instagram ZIP file: ").strip()
extract_to = "unzipped_instagram_data"

# Extract the ZIP file 
print("Unzipping the data...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

# Locate followers and following JSON files 
followers_file = os.path.join(extract_to, "connections/followers_and_following/followers_1.json")
following_file = os.path.join(extract_to, "connections/followers_and_following/following.json")

# Load the JSON data 
with open(followers_file, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open(following_file, "r", encoding="utf-8") as f:
    following_data = json.load(f)

# STEP 5: Extract usernames 
followers_usernames = {
    entry["string_list_data"][0]["value"]
    for entry in followers_data
    if "string_list_data" in entry and entry["string_list_data"]
}

following_usernames = {
    entry["string_list_data"][0]["value"]
    for entry in following_data["relationships_following"]
    if "string_list_data" in entry and entry["string_list_data"]
}

# Find people who don't follow you back 
not_following_back = sorted(following_usernames - followers_usernames)

# STEP 7: Save results
output_path = "not_following_back.txt"
with open(output_path, "w") as f:
    for user in not_following_back:
        f.write(user + "\n")

print(f"\nDone! {len(not_following_back)} users do not follow you back.")
print(f"Check the file in your folder: {output_path}")
