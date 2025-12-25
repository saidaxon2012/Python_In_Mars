# with 

text = input("Soz kiriting: ")

with open("file.txt", "a", encoding="utf-8") as f:
    f.write(text)
    
print("Faylga yozildi.")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    
lines = [
    'First line',
    'Second line',
    'Third line',
    'Fourth line',
    'Fifth line'
]
with open("lines.txt", "w", encoding="utf-8") as f:
    for i in lines:
        f write(i + '\n')
        
with open("lines.txt", "r", encoding="utf-8") as f:
    resul = f.read(.splitlines())
    
print(result
      
      )