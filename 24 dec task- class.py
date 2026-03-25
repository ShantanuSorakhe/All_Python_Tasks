list_dic_user = [{"id":"1","name":"shantanu","age":18},
                 {"id":"2","name":"sumit","age":19},
                 {"id":"3","name":"rahul","age":20},
                 {"id":"4","name":"abhishek","age":21},
                 {"id":"5","name":"vaibhav","age":22}]

class banking:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
# manually
o1=banking(1,"shantanu","18")
o2=banking(2,"sumit","19")
o3=banking(3,"rahul","20")
o4=banking(4,"abhishek","21")
o5=banking(5,"vaibhav","22")

print(o1.id,o1.name,o1.age)
print(o2.id,o2.name,o2.age)
print(o3.id,o3.name,o3.age)
print(o4.id,o4.name,o4.age)
print(o5.id,o5.name,o5.age)
print("-"*100)

# using loop issue if not used append only last object so using append to add all object in list

all_objects=[]
for oloop in list_dic_user:
    objects=banking(oloop["id"],oloop["name"],oloop["age"])
    all_objects.append(objects)

for print_all_object_list in all_objects:
    print(print_all_object_list.id,print_all_object_list.name,print_all_object_list.age)


