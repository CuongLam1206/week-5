import random
docker_compose = {
    "version": "3.8",
    "services": {
        "app": {
            "image": "python:3.10-slim",
            "command": "python app.py",
            "volumes": "./app:/app",
            "restart": "always",
            "ports": "5000:5000",
            "depends_on": "db"
        }
    }
}


print("Original docker-compose content:")
print(docker_compose)

docker_compose["version"] = "3.10"
print("After updating version:")
print(docker_compose)

image_value = docker_compose["services"]["app"]["image"]
print("Image:", image_value)

docker_compose["services"]["app"]["environment"] = ["PYTHONUNBUFFERED=1"]
print("After adding environment:")
print(docker_compose)

if "volumes" in docker_compose["services"]["app"]:
    print("Key 'volumes' exists in 'app'.")
else:
    print("Key 'volumes' does not exist in 'app'.")

del docker_compose["services"]["app"]["depends_on"]
print("After deleting 'depends_on':")
print(docker_compose)

total_keys = len(docker_compose)
print("Total number of keys in docker_compose:", total_keys)

values_list = list(docker_compose.values())
print("List of all values in dictionary:", values_list)

found = False
for key, value in docker_compose.items():
    if isinstance(value, dict):  # Kiểm tra trong các dictionary con
        for sub_key, sub_value in value.items():
            if sub_value == "always":
                found = True
                break
    elif value == "always":  
        found = True
        break

if found:
    print("'always' exists as a value in the dictionary.")
else:
    print("'always' does not exist as a value in the dictionary.")

new_key = input("Enter a new key: ")
new_value = input(f"Enter the value for key '{new_key}': ")
docker_compose[new_key] = new_value
print("After adding new key:")
print(docker_compose)
