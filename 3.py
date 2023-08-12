                #DATE ( 1402/05/21 )

class Date :

    def __init__ ( self , ruz , mah , sal ) :
        #properties
        self.day = ruz
        self.month = mah
        self.year = sal
        self.joda_konande = "/"

    #methods
    def season ( self , date ) :                         #che mahi az sal
        ...

    def age ( self , bith_date , today ) :               #sen afrad
        ...

    def ruzaye_zendegi ( self , birth_date , today ) :   #ta emruz chand ruz az zendegit gozashte
        ...

    def week_day ( self , date ) :                       #che ruzi az hafte
        ...

    def count_down ( self , date ) :                     #chand ruz az sal baqi mande
        ...

    def reminder ( self , birth_date , today ) :         #chand ruz ta tavalod ya yek ruz khas baqi mande
        ...

    def symbol ( self , year ) :                         #namade un sal chie
        ...

    def kabise ( self , year ) :                         #aya sal kabise hast
        ...

    def miladi ( self , date ) :                         #tabdil shamsi b miladi
        ...

    def qamari ( self , date ) :                         #tabdil shamsi b qamari
        ...