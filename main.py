
from medicalPrediction import *
from EtlProject import *
from Preprocessing import *


def main():
    medPre = medicalPrediction("momen" , "ألم")
    medPre.medSpecialty()
    fetch = FetchMedicalInno()
    fetch.fetch_table('consultation' , 'consultation.csv')
    fetch.fetch_all()
    fetch.merge_tables()

    fill_na = Preprocessing()
    fill_na.fill_null_values()







if __name__ == '__main__':
    main()
