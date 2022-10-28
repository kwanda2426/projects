import pandas as pd
import streamlit as st
import time
import plotly.express as px
from plotly.subplots import make_subplots

from PIL import Image


@st.cache(allow_output_mutation=True)

###############################################################################################################################
def temp_5():
    df_5 = pd.read_csv('data_Prof/JR5134/JR5134_temparature(-5).csv')
    return df_5

def temp5():
    df5 = pd.read_csv('data_Prof/JR5134/JR5134_temparature(5).csv')
    return df5
def temp20():
    df20 = pd.read_csv('data_Prof/JR5134/JR5134_temparature(20).csv')
    return df20

def temp40():
    df40 = pd.read_csv('data_Prof/JR5134/JR5134_temparature(40).csv')
    return df40
def temp55():
    df55 = pd.read_csv('data_Prof/JR5134/JR5134_temparature(55).csv')
    return df55
#
def FatiqueTest():
    FatiqueTest = pd.read_csv('data_Prof/JR5134/FatiqueTest.csv')
    return FatiqueTest

def ShearFatigue():
    ShearFatigue = pd.read_csv('data_Prof/JR5134/ShearFatigue.csv')
    return ShearFatigue

################################################################################################JR6242


def BeamFatigue():
    BeamFatigue = pd.read_csv('data_Prof/JR6242/BeamFatigue.csv')
    return BeamFatigue

# def DynamicModulusample():
#     DynamicModulusample = pd.read_csv('data_Prof/JR6242/DynamicModulus.csv')
#     return DynamicModulusample

def HamburgWheelTrackingTest():
    HamburgWheelTrackingTest = pd.read_csv('data_Prof/JR6242/HamburgWheel.csv')
    return HamburgWheelTrackingTest

def Lot596():
    Lot596 = pd.read_csv('data_Prof/JR6242/Lot596.csv')
    return Lot596
def Lot597():
    Lot597 = pd.read_csv('data_Prof/JR6242/Lot597.csv')
    return Lot597

def Lot594():
    Lot594 = pd.read_csv('data_Prof/JR6242/Lot594.csv')
    return Lot594

def Lot592():
    Lot5962 = pd.read_csv('data_Prof/JR6242/Lot592.csv')
    return Lot592


def Lot593():
    Lot593 = pd.read_csv('data_Prof/JR6242/Lot593.csv')
    return Lot593


################################################################################

def sample():
    sample = pd.read_csv('data_Prof/soilJR6136/SAMPLEDESCRIPTION.csv')
    return sample

def sieve():
    sieve = pd.read_csv('data_Prof/soilJR6136/SIEVEANALYSIS1.csv')
    return sieve
#

def sieve1():
    sieve1 = pd.read_csv('data_Prof/soilJR6136/SIEVEANALYSISn.csv')
    return sieve1
########################################################################################################


def ATTERBERG():
    ATTERBERG = pd.read_csv('data_Prof/soilJR6034/ATTERBERGRESULTS.csv')
    return ATTERBERG

def COMPACTIONS():
    COMPACTIONS = pd.read_csv('data_Prof/soilJR6034/COMPACTIONS.csv')
    return COMPACTIONS

def SAMPLE1():
    SAMPLE1 = pd.read_csv('data_Prof/soilJR6034/SAMPLEDESCRIPTION.csv')
    return SAMPLE1

def SIEVE2():
    SIEVE2 = pd.read_csv('data_Prof/JR6242/COMPACTIONS.csv')
    return SIEVE2

###########################################################################
###blinders
#
# def Before30():
#     Before30 = pd.read_csv('data_Prof/blinders/30_Before RTFO Ageing.csv')
#     return Before30
# def After30():
#     After30 = pd.read_csv('data_Prof/blinders/30After RTFO Ageing.csv')
#     return After30
# def After50():
#     After50 = pd.read_csv('data_Prof/blinders/50After  RTFO.xlsx')
#     return After50
# def Before50():
#     Before50 = pd.read_csv('data_Prof/blinders/50Before RTFO.csv')
#     return Before50








################################################################################################



def main():

############################################################### JR5134
    temperature_5 = temp_5()
    temperature5 = temp5()
    temperature20 = temp20()
    temperature40 = temp40()
    temperature55 = temp55()
    ShearFatigue1 = ShearFatigue()
    FatiqueTest1 = FatiqueTest()
#################################################################JR6242

    # DynamicModulusamplen = DynamicModulusample()
    HamburgWheelTrackingTestn = HamburgWheelTrackingTest()
    BeamFatiguen = BeamFatigue()
    Lot596n = Lot596()
    Lot594n = Lot594()
    Lot592n = Lot592()
    Lot593n = Lot593()
    Lot597n = Lot597()


###############################################################################################
    # ##soilsssssssssss
    sieven = sieve()
    sieve1n = sieve1()
    samplen = sample()

    # ATTERBERGn = ATTERBERG()
    # COMPACTIONSn = COMPACTIONS()
    # SAMPLE1n = SAMPLE1()
    # SIEVE2n = SIEVE2()
###############################################################################################
    # ###blindeeeeeeerrrrrrrrrr
    # Before30n = Before30()
    # Before50n = Before50()
    # After50n = After50()
    # After50n = After30()
#################################################################################################

    text = """
    ## Note: ##
    ---------------------
    **This is a dashboard to show an interactive report in an app.**\n

    ---------------------
    """
    st.sidebar.markdown(text)

    # Checkbox
    st.sidebar.subheader("Summary")

    st.sidebar.checkbox("Desctription of the data")
########################################################################################


    st.sidebar.subheader("Exploration")
    # df = load_data()
    # st.header('Overall Performance')
    status = st.sidebar.selectbox("Asphalt:", ["Asphalt_JR5134", "Asphalt_JR6242"
                                               ,'Soil_JR6034', 'Soil_JR6136'])
    # status1 = st.sidebar.selectbox("Soils:", ["JR6034", "JR6136", 'Binder'])
    # status_binder = st.sidebar.selectbox("Binder:", ['Binder'])
    # status_concrete = st.sidebar.selectbox("Concrete:", ["JR5134", "JR6242"])
    # status_aggregat = st.sidebar.selectbox("Aggregat:", ["JR5134", "JR6242"])


    if status == "Asphalt_JR5134":


        ##########################################################################################

        st.title('Date Reported:  1/17/2012')
        st.title('JR No: 5134')

        st.subheader("Shear and Fatigue test speciment densities")
        st.table(ShearFatigue1)

        st.subheader("1. Sample ID vs Voids (%)")

        fig = px.bar(ShearFatigue1, x="Sample ID", y=['MTRD', 'Corelok BRD', 'Corelok Voids (%)'],
                     template="plotly_dark")
        st.plotly_chart(fig)

        fig = px.bar(ShearFatigue1, x="Sample ID", y=['MTRD', 'TMH1 C3 BRD', 'TMH1 C3Voids (%)'],
                     template="plotly_dark")
        st.plotly_chart(fig)




        #######################################################################################

        st.title("Dynamic Modulus")
        st.subheader("Temperature at -5\u00b0C")
        # performance = load_data_sum()
        st.table(temperature_5)



        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature_5, x='Frequency', y=['12045G1C','12045G2C','Mean','SBS mix (Mean)'],  template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature_5, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature_5, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature_5, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)
#############################################################################

        st.subheader("Temperature at 5\u00b0C")

        st.table(temperature5)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature5, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature5, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature5, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature5, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("Temperature at 20\u00b0C")

        st.table(temperature20)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature20, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature20, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature20, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature20, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

    ######################################################################################################

        st.subheader("Temperature at 40\u00b0C")

        st.table(temperature40)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")

        fig = px.line(temperature40, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature40, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature40, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature40, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        ###########################################################################################################

        st.subheader("Temperature at 55\u00b0C")

        st.table(temperature5)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature55, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature55, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature55, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature55, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        #####################################################################################################

        st.subheader("Fatique Test results at 50% initial stiffness reduction")
        st.table(FatiqueTest1)

        st.subheader("1. Sample ID vs Voids (%)")

        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Voids (%)'], template="plotly_dark")
        st.plotly_chart(fig)

        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Test Temp (o C)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Sample ID vs Siffness (Mpa)")
        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Siffness (Mpa)'], template="plotly_dark")
        st.plotly_chart(fig)

        # st.subheader("3. Sample ID vs Strain (�?)")

        # fig = px.bar(FatiqueTest1, x="Sample ID", y=["Strain (�?)"], template="plotly_dark")
        # st.plotly_chart(fig)

        st.subheader("3. Sample ID vs No.of Cycles")
        fig = px.bar(FatiqueTest1, x="Sample ID", y=["No.of Cycles"], template="plotly_dark")
        st.plotly_chart(fig)
###########################################################################################################


######## JR6242#############################################################################

    if status == 'Asphalt_JR6242':
        st.title('JR No: 6262')
        st.title('Date Reported:  1/16/2019')


        st.subheader("Hamburg Wheel Tracking Test Results")
        st.table(HamburgWheelTrackingTestn)

        st.subheader("1. Property vs Lot 1, Lot 2")

        fig = px.bar(HamburgWheelTrackingTestn, x="Property", y=['Lot 1', "Lot 2"],template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Lot 1 vs Lot 2")
        fig = px.line(HamburgWheelTrackingTestn, x='Lot 1', y='Lot 2',
                      template="plotly_dark")
        st.plotly_chart(fig)

#######################################################################################


        st.subheader("Beam Fatigue results for Lot 1 at 20\u00b0C")
        st.table(BeamFatiguen)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        fig = px.line(BeamFatiguen, x='Strain (Microstrain)', y=['Flexural stiffness (Mpa)', 'Modulus of Elasticity (Mpa)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Strain (Microstrain vs Cycles")
        fig = px.line(BeamFatiguen, x='Strain (Microstrain)', y='Cycles',template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Sample ID vs Flexural stiffness (Mpa), Modulus of Elasticity (Mpa)")
        fig = px.bar(BeamFatiguen, x="Sample ID", y=['Flexural stiffness (Mpa)', 'Modulus of Elasticity (Mpa)'],
                     template="plotly_dark")
        st.plotly_chart(fig)

####################################################################################################################


        # st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # st.table(Lot592)

        # fig = px.line(temperature_5, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        # st.plotly_chart(fig)

        st.subheader("4. Frequency vs STDEV")

        fig = px.line(temperature_5, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("5. Frequency vs CoV")

        fig = px.line(temperature_5, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)
        #############################################################################

        st.subheader("Temperature at 5\u00b0C")

        st.table(temperature5)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature5, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature5, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature5, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature5, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("Temperature at 20\u00b0C")

        st.table(temperature20)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature20, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature20, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        # st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature20, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature20, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        ######################################################################################################

        st.subheader("Temperature at 40\u00b0C")

        st.table(temperature40)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature40, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature40, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature40, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature40, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        ###########################################################################################################

        st.subheader("Temperature at 55\u00b0C")

        st.table(temperature5)

        st.subheader("1. Frequency vs 12045G1C,12045G2C, Mean,SBS mix (Mean)")
        # fig = px.bar(df, x="Campaign", y="Visits", template="plotly_dark", color='Campaign',)
        # st.plotly_chart(fig)
        # fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")
        fig = px.line(temperature55, x='Frequency', y=['12045G1C', '12045G2C', 'Mean', 'SBS mix (Mean)'],
                      template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Frequency vs STDEV, SBS mix (Mean)")
        # fig = px.bar(performance, x="Campaign", y="Profit", template="plotly_dark")
        # st.plotly_chart(fig)
        fig = px.line(temperature55, x='Frequency', y=['STDEV', 'SBS mix (Mean)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Frequency vs STDEV")

        fig = px.line(temperature55, x='Frequency', y=['STDEV'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Frequency vs CoV")

        fig = px.line(temperature55, x='Frequency', y=['CoV'], template="plotly_dark")
        st.plotly_chart(fig)

        #####################################################################################################

        st.subheader("Fatique Test results at 50% initial stiffness reduction")
        st.table(FatiqueTest1)

        st.subheader("1. Sample ID vs Voids (%)")

        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Voids (%)'], template="plotly_dark")
        st.plotly_chart(fig)

        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Test Temp (o C)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("2. Sample ID vs Siffness (Mpa)")
        fig = px.bar(FatiqueTest1, x="Sample ID", y=['Siffness (Mpa)'], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("3. Sample ID vs Strain ")

        fig = px.bar(FatiqueTest1, x="Sample ID", y=["Strain (�?)"], template="plotly_dark")
        st.plotly_chart(fig)

        st.subheader("4. Sample ID vs No.of Cycles")
        fig = px.bar(FatiqueTest1, x="Sample ID", y=["No.of Cycles"], template="plotly_dark")
        st.plotly_chart(fig)

    # status1 = st.sidebar.radio("Soils:", ["JR6034", "JR6136"])


    if status == 'Soil_JR6034':
        st.title("Post 2017 RESULTS")
        st.title('SAMPLE DESCRIPTION')


        st.subheader("Soil and gravels")
        st.table(samplen)
        st.table(sieven)
        st.table(sieve1n)
        #
        # st.subheader("1. Sample ID vs Voids (%)")
        #
        # fig = px.bar(ShearFatigue1, x="Sample ID", y=['MTRD', 'Corelok BRD', 'Corelok Voids (%)'],
        #      template="plotly_dark")
        # st.plotly_chart(fig)
        #
        # fig = px.bar(ShearFatigue1, x="Sample ID", y=['MTRD', 'TMH1 C3 BRD', 'TMH1 C3Voids (%)'],
        #      template="plotly_dark")
        # st.plotly_chart(fig)

###############################################################################
    if status == 'Soil_JR6136':
        st.title("Post 2017 RESULTS")
        st.title('SAMPLE DESCRIPTION')

        st.subheader("SIEVE ANALYSIS (%Pass)")
        # st.table(SIEVE2n)
        # st.table(sieven)
        # st.table(sieve1n)
            #
            # st.subheader("1. Sample ID vs Voids (%)")
            #
            # fig = px.bar(ShearFatigue1, x="Sample ID", y=['MTRD', 'Corelok BRD', 'Corelok Voids (%)'],
            #      template="plotly_dark")
            # st.plotly_chart(fig)
            #



if __name__ == "__main__":
    main()