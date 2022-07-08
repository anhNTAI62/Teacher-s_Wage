from fileinput import close
import sqlite3
from unicodedata import name
luonggv_db = sqlite3.connect("Wage.sqlite")
contro = luonggv_db.cursor()
huy_bang = """DROP TABLE IF EXISTS Wage"""
tao_bang = """CREATE TABLE Wage(
    Name text,
    Hours float,
    Rate float,
    Total float,
    Tax float
)"""
chen_vao_bang = """INSERT INTO Wage(Name, Hours, Rate, Total, Tax) VALUES(?,?,?,?,?)"""
contro.execute(huy_bang)
contro.execute(tao_bang)
du_lieu = open("Database.txt")
dem_dong = 0
tong_dong = du_lieu.readlines()
for dong in tong_dong:
    dem_dong += 1
    if dem_dong > 2:
        du_lieu_xu_li = dong.strip().split()
        Name = du_lieu_xu_li[0]
        Hours = du_lieu_xu_li[1]
        Rate = du_lieu_xu_li[2]
        Total = float(Hours)*float(Rate)
        if Total >=2000000:
            Tax = Total*0.1
        else:
            Tax = float(0)
        contro.execute(chen_vao_bang,(Name,Hours,Rate,Total,Tax))
hien_thi_du_lieu = "SELECT * FROM Wage WHERE Hours > 5 ORDER BY Hours ASC"
contro.execute(hien_thi_du_lieu)
du_lieu_dau_ra = contro.fetchall()
print("Lecturer List: \n")
print("{0:^5}{1:^5}{2:^10}{3:^10}{4:^10}".format("Name","Hours","Rate","Total","Tax"))
for hang in du_lieu_dau_ra:
    print("{0:^5}{1:^7}{2:^10}{3:^10}{4:^10}".format(hang[0],hang[1],hang[2],hang[3],hang[4]))

luonggv_db.close()
#LƯU Ý CÁC LỆNH VỚI SQLITE PHẢI CÓ ĐÓNG MỞ NGOẶC (), LƯU Ý ĐÓNG ĐÚNG VỊ TRÍ NGOẶC BAO ĐÓNG KẺO ĐÓNG NHẦM BAO ĐÓNG SANG BÊN KHÁC.
        
            



