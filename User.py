from datetime import date,datetime


class Users:

    all_posts={}

    def __init__(self, name, age, email, phone, username):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        self.username=username
        self.user_posts=[]
        Users.all_posts[name]=[]

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def contact_info(self):
        return f"{self.name}'s contact information is: phone number: {self.phone}, email: {self.email}."

    def user_post(self, str):
        today_date = date.today().strftime("%B %d, %Y")
        time=datetime.now().strftime("%d/%m/%Y %H:%M")
        post=f"{self.username} posted {str} on {today_date} at {time}."
        self.user_posts.append(post)
        Users.all_posts[self.name].append(post)
        return post
    
    def remove_user_post(self,str):
        for post in self.user_posts:
            if str in post:
                self.user_posts.remove(post)
        for post in Users.all_posts[self.name]:
            if str in post:
                Users.all_posts[self.name].remove(post)
                


robert= Users("Robert", 31, "robert@random.com", "555-555-1111", "Roarin_Robert")
alisha=Users("Alisha", 31, "alisha@email.com", "557-775-1234", "gemini_elegance")
mike=Users("Mike", 55, "mike@dares.com", "554-445-1234", "mike_dares")

test= alisha.user_post("I had chic-fil-a today for lunch, it was delicious!")
test2=alisha.user_post("Live,Laugh,Love!")
test3=robert.user_post("I'm amazing at coding!")

# print(robert)
# print(alisha.contact_info())
print(test)
print(alisha.user_posts)
print(robert.user_posts)
print(Users.all_posts)
alisha.remove_user_post("Live,Laugh,Love!")
print(alisha.user_posts)
print(Users.all_posts)
