import sys
print("sys.path Homedire")
print(sys.path)

sys.path.append("PythonPath")

print("\nModified sys.path:")
print(sys.path)
sys.path.remove("PythonPath")
print("\nRestored sys.path:")
print(sys.path)