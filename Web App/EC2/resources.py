from requestcore import *
from sqlalchemy.sql import *

#Policies:
#-Admin always has full access
#-Owner has full access, if there's such column

#Inherit methods from RequestCore class
class GymWorkout(RequestCore):

    #Policies
    #-Read: Group
    #-Write: Owner
    #-Change: Owner

    #Take any arguments given for the class instance
    def __init__(self, *args, **kwargs):

        #This has to be defined before calling super()
        self.table_name = "gym_workout"
        #self.template_select = "*"

        #Make arguments available for the parent class __init__ function
        #self.__class__ equals to GymWorkout
        super(self.__class__, self).__init__(*args, **kwargs)


class GymExcercise(RequestCore):

    #Policies
    #-Read: All
    #-Write: No allowed
    #-Change: Not allowed

    def __init__(self, *args, **kwargs):

        self.table_name = "gym_excercise"

        super(self.__class__, self).__init__(*args, **kwargs)

class GymMuscleGroup(RequestCore):

    #Policies
    #-Read: All
    #-Write: No allowed
    #-Change: Not allowed

    def __init__(self, *args, **kwargs):

        self.table_name = "gym_musclegroup"

        super(self.__class__, self).__init__(*args, **kwargs)

class GymRoutine(RequestCore):

    #Policies
    #-Read: Group
    #-Write: Owner
    #-Change: Owner

    def __init__(self, *args, **kwargs):

        self.table_name = "gym_routine"

        super(self.__class__, self).__init__(*args, **kwargs)

class GymSection(RequestCore):

    #Policies
    #-Read: Group
    #-Write: Owner
    #-Change: Owner

    def __init__(self, *args, **kwargs):

        self.table_name = "gym_section"

        super(self.__class__, self).__init__(*args, **kwargs)

class GymSet(RequestCore):

    #Policies
    #-Read: Owner
    #-Write: Owner
    #-Change: Owner

    def __init__(self, *args, **kwargs):

        self.table_name = "gym_set"

        super(self.__class__, self).__init__(*args, **kwargs)
