import os

# Folders jisme __init__.py banana hai
folders = ["config", "database", "handlers", "utils"]

for folder in folders:
    path = os.path.join(folder, "__init__.py")
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("# Auto-generated init file\n")
        print(f"✅ Created {path}")
    else:
        print(f"⚡ Already exists: {path}")
