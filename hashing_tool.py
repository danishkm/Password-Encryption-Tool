import hashlib

def generate_md5_hash(hashvalue):
  hashtype1=hashlib.md5()
  hashtype1.update(hashvalue.encode())
  return hashtype1.hexdigest()


def generate_sha1_hash(hashvalue):
  hashtype2=hashlib.sha1()
  hashtype2.update(hashvalue.encode())
  return hashtype2.hexdigest()

def generate_sha224_hash(hashvalue):
  hashtype3=hashlib.sha224()
  hashtype3.update(hashvalue.encode())
  return hashtype3.hexdigest()

def main():
    # Prompt user for the string to hash
    hashvalue = input("Enter a string to hash: ")

    # Ask user to choose the hashing algorithm
    print("\nChoose the hashing algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA224")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        hash_result = generate_md5_hash(hashvalue)
        algorithm = "MD5"
    elif choice == "2":
        hash_result = generate_sha1_hash(hashvalue)
        algorithm = "SHA1"
    elif choice == "3":
        hash_result = generate_sha224_hash(hashvalue)
        algorithm = "SHA224"
    else:
        print("Invalid choice.")
        return
    # Display the result
    print(f"\nGenerated {algorithm} hash: {hash_result}")

# Run the main program
if __name__ == "__main__":
    main()
