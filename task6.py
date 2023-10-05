#Q_1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
max_num=max(lst)
print(max_num)
lst.remove(min(lst))
lst.sort(reverse=True)
print(lst[-1:-5 :-1])
#Q_2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
print(main_lst[0].count("python")+main_lst[2].count("python")+main_lst[3].count("python"))
#Q_3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(my_lst[0].capitalize()+" "+
my_lst[1].capitalize()+" "+
my_lst[2].capitalize()+" "+
my_lst[3].capitalize()+" "+
my_lst[4].capitalize())
#Q_4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst=[]
new_lst.extend(my_lst)
print(new_lst)
#Q_5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2]="Omar"
my_lst[4]=19
print(my_lst)
#Q_6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
#Q_7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
print(tuple1+(9,))
#Q_8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
print(tuple1+tuple2)