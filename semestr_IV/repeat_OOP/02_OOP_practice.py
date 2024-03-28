import random


brands_of_car={
    "BMW":{
        "fuel":60,
        "power":150,
        "volum":12,
    },
    "Volvo":{
        "fuel":60,
        "power":120,
        "volum":10
    },
    "Ferrari":{
        "fuel":80,  #л
        "power":400, #потужніть
        "volum":25 #л/км
    }
}

job_list={
    "Python developer":{
        "salary_for_hour":50,
        "gladness_less":10
    },
    "C# developer": {
        "salary_for_hour":45,
        "gladness_less":25
    },
    "Ruby developer": {
        "salary_for_hour":70,
        "gladness_less":10
    }
}

class Human:
    def __init__(self,name="Human",job=None, home=None, car=None):
        self.name=name
        self.money=100
        self.gladness=50 # %
        self.satiety=50
        self.job=job
        self.home=home
        self.car=car

    def __str__(self) -> str:
        return f"Human: {self.name} has a car {self.car} "
    # встановлення значень властивостей обєкта
    def set_job(self):
        self.job=Job(job_list)

    def set_home(self):
        pass

    def set_car(self):
        self.car=Auto(brands_of_car)

    # отримання значень властивостей обєкта
    def get_job(self):
          pass

    def get_home(self):
        pass

    def get_car(self):
        pass
    

    #дії над обктом => методи
    def eat(self): #їжа
        pass

    #робота
    def work(self, path):
        if self.car!=None:
            if self.car.drive(path):
                self.money+=self.job.salary_for_hour
                self.gladness-=self.job.gladness_less
                self.satiety-=4
            elif self.car.fuel<self.car.volum*path/100:
                self.shopping("fuel",self.car.volum*path/100)

    # здійснення покупок
    def shopping(self):
        pass 

    #відновлення сил (відпочинок)
    def reset(self):
        pass

    #ремонт авто
    #...
    
    # показники персонажу  (людини)
    def live(self,day):  #кількість днів
        pass

    def is_alive():     #живий?
        pass


class Auto:
    def __init__(self,brand_list) -> None:
        self.brand=random.choice(list(brand_list))  #return key
        # print(self.brand)
        self.fuel=brand_list[self.brand]["fuel"]
        self.power=brand_list[self.brand]["power"]
        self.volum=brand_list[self.brand]["volum"]

#100 volum    path=> x
    def drive(self,path):
        if self.fuel>=self.volum*path/100:
            self.fuel=self.fuel-self.volum*path/100  
            return True 
        else:
            print(f"The car cannot move to {path}")
            return False 
    def __str__(self) -> str:
        return self.brand


car=Auto(brands_of_car)
print(car.drive(120))
print(car.drive(120))
print(car.drive(300))


class Job:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary_for_hour=job_list[self.job]["salary_for_hour"]
        #зменшення щастя
        self.gladness_less=job_list[self.job]["gladness_less"]


oleg=Human()
oleg.set_car()
oleg.set_job()
print(oleg.car.brand)
print(oleg.car.fuel)
# print(oleg.job)
print(oleg.money)
print(oleg.satiety)

oleg.work(90)
print(oleg.car.brand)
print(oleg.car.fuel)
# print(oleg.job)
print(oleg.money)
print(oleg.satiety)
print(oleg)