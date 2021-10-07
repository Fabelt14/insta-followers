
import os
from multiprocessing import Pool,pool
processes = ( "main.sh", " h.sh" )


def run_process(process):

     os.system(f'bash {process}')
if __name__ =="__main__":
     pool = Pool(processes=2)
     pool.map(run_process,processes)
