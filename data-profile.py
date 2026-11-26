import os 
import sys
choice = sys.argv[1]
if os.path.exists("a") and os.path.exists("b"):
    os.rename("data","c")
elif os.path.exists("b") and os.path.exists("c"):
    os.rename("data","a")
elif os.path.exists("a") and os.path.exists("c"):
    os.rename("data","b")
if choice == 'a':
    os.rename("a","data")
elif choice == 'b':
    os.rename("b","data")
elif choice == 'c':
    os.rename("c","data")
