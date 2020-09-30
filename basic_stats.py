#Name: Quanyue Xie
#Date: 9/29/2020
#Description: import the statistics module
# should return a tuple of three values

import statistics

#define class
class Person():

#constructor, initialization
    def __init__(self, name, age):
        # private
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

#individually defined
def basic_stats(person_list):

    #compute mean median mode given a list of person
    age_list = [p.get_age() for p in person_list]

    # Call the mean median mode of the statistics module respectively
    age_mean = statistics.mean(age_list)
    age_median = statistics.median(age_list)
    age_mode = statistics.mode(age_list)

    return age_mean, age_median, age_mode


if __name__ == "__main__":
    # Instantiate separately
    p1 = Person("Kyoungmin", 73)
    p2 = Person("Mercedes", 24)
    p3 = Person("Avanika", 48)
    p4 = Person("Marta", 24)

    # put person into list
    person_list = [p1, p2, p3, p4]

    # call basic_stats function
    print(basic_stats(person_list))