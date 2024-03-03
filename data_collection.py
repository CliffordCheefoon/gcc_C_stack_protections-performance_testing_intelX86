import os
import shutil
import pandas

REPORT_NAME = "r000ue"
TEMP_FILE = "stats.txt"
RUN_GENERATE_REPORT = r""" "C:\Program Files (x86)\Intel\oneAPI\vtune\2024.0\bin64\vtune" -report summary -r r000ue  -format=csv  -csv-delimiter=, """

def run_test(test_case, run_process_cmd):
    collection_df = pandas.DataFrame()


    for counter in range(100):


        os.system(run_process_cmd) 
        os.system(RUN_GENERATE_REPORT + " >  " +  TEMP_FILE) 

        stats = pandas.read_csv(TEMP_FILE)
        stats =  stats.drop(stats.columns[[0]], axis=1)
        stats =stats.T
        stats.columns = stats.iloc[0]
        stats = stats[1:]

        if counter == 0:
            collection_df = stats
        else:
            collection_df = pandas.concat([collection_df,stats], axis=0, ignore_index=True)
            print(collection_df)


        shutil.rmtree(REPORT_NAME)
        os.remove(TEMP_FILE)


    collection_df.to_excel(test_case + ".xlsx")


RUN_PROCESS_WITH_PROFILER_CMD = r""" "C:\Program Files (x86)\Intel\oneAPI\vtune\2024.0\bin64\vtune" -collect uarch-exploration -knob sampling-interval=0.1 -knob collect-memory-bandwidth=true   --app-working-dir=C:\Users\Clifford\repos\securityPaper -- C:\Users\Clifford\repos\securityPaper\REPLACEME.exe 100000 """



a_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "a")
run_test("a", a_cmd)

b_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "b")
run_test("b", b_cmd)

c_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "c")
run_test("c", c_cmd)

d_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "d")
run_test("d", d_cmd)

e_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "e")
run_test("e", e_cmd)

f_cmd = RUN_PROCESS_WITH_PROFILER_CMD.replace("REPLACEME", "f")
run_test("f", f_cmd)