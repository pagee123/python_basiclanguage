score=[96,93,62,90,87,78,65,69,93,97,71,62,77]
excellent=0
for i in score:
    if(i<85):
        continue
    excellent=excellent+1
print(f"認真的學生{excellent}位")