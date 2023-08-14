             #TIME ( 21:15:30 )

class Time :

    def __init__ ( self , sec , min , h ) :
        #properties
        self.seconds = sec
        self.minuts = min
        self.hour = h 

    #methods
    def time_to_second ( self ) :
        ...

    def add ( self , time1 , time2 ) :
        ...

    def subtraction ( self , time1 , time2 ) :
        ...

    def rest_of_the_day ( self , time ) :      #zaman baqi munde az ruz
        ...

    def day_position ( self , time ) :          #sobh,zohr,shab,.....
        ...